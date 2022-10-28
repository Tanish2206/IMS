var females = [1, 2, 4, 5];
var males = [3, 6];

var gender = document.getElementById("student-gender").innerText;

if (gender === "M") {
  random = males[Math.floor(Math.random() * males.length)];
} else {
  random = females[Math.floor(Math.random() * females.length)];
}

document
  .getElementById("student-avatar")
  .setAttribute(
    "src",
    "https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-chat/ava" +
      random +
      ".webp"
  );
