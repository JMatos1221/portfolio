let splitTitle = window.location.pathname.split("/").at(-1).split("-");
let title = "João Matos";
let page = "";

splitTitle.forEach((s) => {
  if (s.length > 0) {
    s = s[0].toUpperCase() + s.substring(1);
    page += s + " ";
  }
});

document.title = page === "" ? title : `${title} | ${page}`;

var clockEl;

function updateClock() {
  let date = new Date();
  clockEl.innerHTML = date.toLocaleTimeString("it-IT", {
    timeZone: "Portugal",
  });
}

window.addEventListener("load", () => {
  clockEl = document.getElementById("clock");
  setInterval(updateClock, 1000);
});
