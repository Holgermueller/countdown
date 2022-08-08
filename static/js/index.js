const countDownDate = new Date("Aug 9, 2023").getTime();

const x = setInterval(function () {
  let now = new Date().getTime();

  let difference = countDownDate - now;

  let days = Math.floor(difference / (1000 * 60 * 60 * 24));

  let hours = Math.floor(
    (difference % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)
  );

  let minutes = Math.floor((difference % (1000 * 60 * 60)) / (1000 * 60));

  let seconds = Math.floor((difference % (1000 * 60)) / 1000);

  document.getElementById("theCountdown").innerHTML =
    days +
    " days: " +
    hours +
    " hours: " +
    minutes +
    " minutes: " +
    seconds +
    " seconds";

  if (difference < 0) {
    clearInterval(x);
    document.getElementById("theCountdown").innerHTML = "TIME'S UP!!";
  }
}, 1000);
