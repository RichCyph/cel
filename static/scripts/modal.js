


var up = document.getElementById("update_settings");
up.addEventListener("click", function() {
    var modal = document.getElementById("modal_background");
    modal.style.display = "flex";
});

var cs = document.getElementById("modal_close");
cs.addEventListener("click", function() {
    var modal = document.getElementById("modal_background");
    modal.style.display = "none";
});
