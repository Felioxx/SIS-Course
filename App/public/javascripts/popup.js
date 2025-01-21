$(window).on("load", function () {
  $("#myModal").modal("show");
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
