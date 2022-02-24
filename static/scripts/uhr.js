
document.getElementById("benutzer_name").innerHTML = global_benutzer_name;

var myVar = setInterval(myTimer, 1000);
function myTimer() {
    var d = new Date();
    var t = d.toLocaleTimeString();
	var ad = d.toLocaleDateString();
    $("#uhr").html(t);
	$("#datum").html(ad);
	
	document.getElementById("tageszeit").innerHTML = tageszeit_berechnen(d);
};

function tageszeit_berechnen(zeit){
	var stunden = parseInt(zeit.getHours());
	console.log(stunden);
	var tageszeit;
	
	if (stunden >= 5 && stunden < 12) {
		tageszeit = global_morgengruss;//sprache.morgengruss;
	} else if (stunden >=12 && stunden < 17) {
		tageszeit = global_nachmittaggruss;//sprache.nachmittaggruss;
	} else if (stunden >= 17 && stunden < 20) {
		tageszeit = global_abendgruss;//sprache.abendgruss;
	} else {
		tageszeit = global_nachtgruss;//sprache.nachtgruss;
	}
	
	/*
	
	if (stunden >= 5 && stunden < 12) {
		var mg = {{user.morning_greeting}};
	tageszeit = mg;
	} else if (stunden >=12 && stunden < 17) {
		var mg ={{user.afternoon_greeting}};
		tageszeit = mg;
	} else if (stunden >= 17 && stunden < 20) {
			var mg =  {{user.evening_greeting}};
		tageszeit = mg;
	} else {
		tageszeit = {{user.night_greeting}};
	}
	*/
	
	return tageszeit;
};
