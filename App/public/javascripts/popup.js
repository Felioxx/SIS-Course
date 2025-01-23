$(window).on("load", function () {
  if (window.location.href.indexOf("/chat") > -1) {
    $("#myModal").modal("show");
  }
});

var savebtn = document.getElementById("saveBtn");
var input = document.getElementById("inputPassword6");

savebtn.addEventListener("click", fetchkey);

var openAiKey = null;

function fetchkey() {
  openAiKey = input.value;
  $("#myModal").modal("hide");
  return openAiKey;
}
