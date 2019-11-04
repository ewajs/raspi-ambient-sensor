var tempCheck = document.getElementById("tempCheck");
var humCheck = document.getElementById("humCheck");
var createBtn = document.getElementById("createBtn");
var createMsg = document.getElementById("createMsg");
function check() {
  if (tempCheck.checked || humCheck.checked) {
    createBtn.disabled = false;
    createMsg.hidden = true;
  } else {
    createBtn.disabled = true;
    createMsg.hidden = false;
  }
}

tempCheck.addEventListener("click", check);
humCheck.addEventListener("click", check);
window.addEventListener("onpageshow", check);
