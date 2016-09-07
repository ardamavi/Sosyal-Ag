function formAcilsinMi() {
  if(document.getElementById("errMessage") != null &&
    document.getElementById("errMessage").innerText !== ""){
    formAc();
  }
}

window.onload = formAcilsinMi;

function formAc(){
    document.getElementById("ypForm").style.display = "block";
    document.getElementById("iptalBtn").style.display = "block";
    document.getElementById("ypBtn").style.display = "none";
}

function formKapa(){
    document.getElementById("ypForm").style.display = "none";
    document.getElementById("iptalBtn").style.display = "none";
    document.getElementById("ypBtn").style.display = "block";
    document.getElementById("errMessage").textContent = "";
}

function cikisYapAction(){
    window.open("/admin/logout", "_self");
    window.open("/", "_self");
}