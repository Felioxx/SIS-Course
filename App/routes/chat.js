var express = require("express");
var router = express.Router();
const { spawn } = require("child_process");

router.get("/", function (req, res, next) {
  res.render("chat", { title: "Chat" });
});

router.post("/", function (req, res, next) {
  var question = req.body.message;
  console.log("question:" + question);

  // Use child_process.spawn method from
  // child_process module and assign it
  // to variable spawn
  var spawn = require("child_process").spawn;

  // Parameters passed in spawn -
  // 1. type_of_script
  // 2. list containing Path of the script
  //    and arguments for the script
  var process = spawn("python", ["public/python/neo4j_QA.py", question]);

  // Takes stdout data from script which executed
  // with arguments and send this data to res object
  process.stdout.on("data", function (data) {
    console.log(`stdout: ${data}`);
    res.send(data.toString());
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

module.exports = router;
