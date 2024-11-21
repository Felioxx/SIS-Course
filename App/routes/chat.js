var express = require("express");
var router = express.Router();
const { spawn } = require("child_process");

router.get("/", function (req, res, next) {
  res.render("chat", { title: "Chat" });
});

router.post("/", function (req, res, next) {
  question = req.body.message;
  console.log("question:" + question);
  answer = runPythonScript("public/python/neo4j_QA.py", [question]);
  console.log("answer:" + answer);
  res.send(answer);
});

// Run a Python script and return output
function runPythonScript(scriptPath, args) {
  // Use child_process.spawn method from
  // child_process module and assign it to variable
  const pyProg = spawn("python", [scriptPath].concat(args));

  // Collect data from script and print to console
  let data = "";
  pyProg.stdout.on("data", (stdout) => {
    data += stdout.toString();
  });

  // Print errors to console, if any
  pyProg.stderr.on("data", (stderr) => {
    console.log(`stderr: ${stderr}`);
  });

  // When script is finished, print collected data
  pyProg.on("close", (code) => {
    console.log(`child process exited with code ${code}`);
    console.log("Data: ");
    console.log(data);
    return data;
  });
}

module.exports = router;
