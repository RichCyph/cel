

var up = document.getElementById("update_settings");
up.addEventListener("click", function(e) {
    var modal = document.getElementById("modal_background");
    modal.style.display = "flex";
    console.log(document.getElementById("update_settings").href)

    $.ajax({
     url: document.getElementById("update_settings").href,
     type: "GET",
     dataType: "json",
     success: function(data){
       data = data.data;
       modal.append(data)
     }
   });
e.preventDefault();
});

var cs = document.getElementById("modal_close");
  cs.addEventListener("click", function() {
var modal = document.getElementById("modal_background");
  modal.style.display = "none";
});
