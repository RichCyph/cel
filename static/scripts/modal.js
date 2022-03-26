

var up = document.getElementById("update_settings");
up.addEventListener("click", function(e) {
    var modal = document.getElementById("modal_background");
    modal.style.display = "flex";

    $.ajax({
     url: document.getElementById("update_settings").href,
     type: "GET",
     dataType: "json",
     success: function(data){
       data = data.data;
       modal.innerHTML=data;

       var cs = document.getElementById("modal_close");
         cs.addEventListener("click", function() {
       var modal = document.getElementById("modal_background");
         modal.style.display = "none";
       });
     }
   });


e.preventDefault();
});

up.addEventListener("click", function(e) {
    var submit = document.getElementById("update_form_submit_id");

    $.ajax({
     url: document.getElementById("update_settings").href,
     type: "POST",
     dataType: "json",
     data: document.getElementById('update_settings_form').serialize(),
     success: function(data){
       data = data.data;
       modal.innerHTML=data;

       var cs = document.getElementById("modal_close");
         cs.addEventListener("click", function() {
       var modal = document.getElementById("modal_background");
         modal.style.display = "none";
       });
     }
   });


e.preventDefault();
});

$.ajaxSetup({
            beforeSend: function(xhr, settings) {
                if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken",
                  document.getElementById('update_settings_form').csrf_token)
                }
            }
        })
