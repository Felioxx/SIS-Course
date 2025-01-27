var express = require("express");
var router = express.Router();
const { spawn } = require("child_process");

router.get("/", function (req, res, next) {
  res.render("chat", { title: "Chat" });
});

router.post("/", function (req, res, next) {
  var question = req.body.message;
  console.log("question:" + question);
  var openAiKey = req.body.openAiKey;
  console.log("key:" + openAiKey);

  var spawn = require("child_process").spawn;

  // Execute the python script with the user's question and OpenAI key
  var process = spawn("python", [
    "public/python/neo4j_QA.py",
    question,
    openAiKey,
  ]);

  // Takes stdout data from script which executed
  // with arguments and send this data to res object
  process.stdout.on("data", function (data) {
    console.log(`stdout: ${data}`);
    res.send(data.toString());
    process.stdout.removeAllListeners("data");
  });

  // Capture and log stderr data
  process.stderr.on("data", function (data) {
    console.error(`stderr: ${data}`);
  });

  // Capture and log the exit event
  process.on("exit", function (code) {
    console.log(`Child process exited with code ${code}`);
  });
});

function onDataHandler(data) {
  console.log(`stdout: ${data}`);
  res.send(data.toString());
  process.stdout.removeListener("data", onDataHandler);
}

module.exports = router;
