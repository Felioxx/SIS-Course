// const { JSDOM } = require("jsdom");
// const { window } = new JSDOM("");
// const $ = require("jquery")(window);

//const { post } = require("../../routes");

/**
 * Returns the current datetime for the message creation.
 */
function getCurrentTimestamp() {
  return new Date();
}

/**
 * Renders a message on the chat screen based on the given arguments.
 * This is called from the `showUserMessage` and `showBotMessage`.
 */
function renderMessageToScreen(args) {
  // local variables
  let displayDate = (args.time || getCurrentTimestamp()).toLocaleString(
    "en-IN",
    {
      month: "short",
      day: "numeric",
      hour: "numeric",
      minute: "numeric",
    }
  );
  let messagesContainer = $(".messages");

  let els = "";
  switch (args.message_side) {
    case "left":
      els = `
        <div class="avatar"></div>
        <div class="text_wrapper">
          <div class="text">${args.text}</div>
          <div class="timestamp">${displayDate}</div>
        </div>
      `;
      break;
    case "right":
      els = `
        <div class="text_wrapper">
          <div class="text">${args.text}</div>
          <div class="timestamp">${displayDate}</div>
        </div>
        <div class="avatar"></div> 
      `;
      break;
  }
  // init element
  let message = $(`
      <li class="message ${args.message_side}">
        ${els}
      </li>
      `);

  // add to parent
  messagesContainer.append(message);

  // animations
  setTimeout(function () {
    message.addClass("appeared");
  }, 0);
  messagesContainer.animate(
    { scrollTop: messagesContainer.prop("scrollHeight") },
    300
  );
}

/* Sends a message when the 'Enter' key is pressed.
 */
$(document).ready(function () {
  $("#msg_input").keydown(function (e) {
    // Check for 'Enter' key
    if (e.key === "Enter") {
      // Prevent default behaviour of enter key
      e.preventDefault();
      // Trigger send button click event
      $("#send_button").click();
    }
  });
});

/**
 * Displays the user message on the chat screen. This is the right side message.
 */
function showUserMessage(message, datetime) {
  renderMessageToScreen({
    text: message,
    time: datetime,
    message_side: "right",
  });
}

/**
 * Displays the chatbot message on the chat screen. This is the left side message.
 */
function showBotMessage(message, datetime) {
  renderMessageToScreen({
    text: message,
    time: datetime,
    message_side: "left",
  });
}

/**
 * Get input from user and show it on screen on button click.
 */
$("#send_button").on("click", function (e) {
  // Clear leaflet map
  geoJsonLayerGroup.clearLayers();
  // get and show message and reset input
  showUserMessage($("#msg_input").val());

  var question = $("#msg_input").val();
  console.log(question);
  // emptying the input
  $("#msg_input").val("");
  // render loading screen
  renderLoadingHorse();
  // fetching the answer
  fetch("http://localhost:3000/chat", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ message: question }),
  })
    .then(function (response) {
      // The response is a Response instance.
      // You parse the data into a useable format using `.json()`
      return response.json();
    })
    .then(function (data) {
      // `data` is the parsed version of the JSON returned from the above endpoint.
      console.log(data); // { "userId": 1, "id": 1, "title": "...", "body": "..." }
      setTimeout(function () {
        removeRunningHorse();
        showBotMessage(data.result);
      }, 300);

      ids = new Set();
      data.intermediate_steps[1].context.forEach((item) => {
        let pattern = /ID/i;
        let matchingKeys = Object.keys(item).filter((key) => pattern.test(key));
        console.log(matchingKeys);

        matchingKeys.forEach((key) => {
          ids.add(item[key]);
        });
      });
      console.log(ids);
      parseCSV(ids);
    });
});

function renderLoadingHorse() {
  let messagesContainer = $(".messages");

  // init element
  let message = $(` 
      <li class="message left">
          <div class="avatar"></div>
          <div class="l-gif"></div>
      </li>
      `);

  // add to parent
  messagesContainer.append(message);

  // animations
  setTimeout(function () {
    message.addClass("appeared");
  }, 0);
  messagesContainer.animate(
    { scrollTop: messagesContainer.prop("scrollHeight") },
    300
  );
}

function removeRunningHorse() {
  let messagesContainer = $(".messages");
  messagesContainer.children().last().remove();
  messagesContainer.animate(
    { scrollTop: messagesContainer.prop("scrollHeight") },
    300
  );
}

async function parseCSV(searchIDs) {
  const response = await fetch("geometries.csv");
  if (!response.ok) {
    throw new Error(`Error: ${response.statusText}`);
  }
  const csvText = await response.text();

  // Use PapaParse to parse CSV
  const parsed = Papa.parse(csvText, {
    header: true,
    skipEmptyLines: true,
  });

  const rows = parsed.data;
  // get the geometries and add them to the leaflet map
  for (const item of searchIDs) {
    let result = rows.find((row) => row.ID === item);

    let geo = JSON.parse(result.Geometry);
    let newLayer = L.geoJSON(geo);
    geoJsonLayerGroup.addLayer(newLayer);
  }
}

/**
 * Set initial bot message to the screen for the user.
 */
$(window).on("load", function () {
  showBotMessage(
    "Hello there! Ask me some questions about the geometry of NRW."
  );
});
