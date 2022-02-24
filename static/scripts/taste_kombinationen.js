
var suche_option_wb = new Map();
					
					suche_option_wb.set("!g ","https://www.google.com/search?q=");
					suche_option_wb.set("!y ","https://www.youtube.com/results?search_query=trance");
					suche_option_wb.set("!w ","https://de.wikipedia.org/w/index.php?search=");

$(document).keydown(function(e) {
	
	PlaySound("mykeySound");
	
	if ( e.shiftKey && ( e.which === 65 ) ) {
		alert('(a) Add new task...');
	} else if ( e.shiftKey && ( e.which === 76 ) ) {
		alert('(l) Add new list!');
	} else if ( e.shiftKey && ( e.which === 83 ) ) {
		document.getElementById("suche_input").focus();
		event.preventDefault(); return false; 
	} else if ( e.shiftKey && ( e.which === 66 ) ) {
		alert('(b) Bookmarks!');
	} else if ( e.shiftKey && ( e.which === 87 ) ) {
		alert('(w) Work Log!');
	} else if ( e.shiftKey && ( e.which === 72 ) ) {
		alert('(h) Home!');
	} else if ( e.shiftKey && ( e.which === 79 ) ) {
		alert('(o) Logged out!');
	} else if ( e.shiftKey && ( e.which === 84 ) ) {
		alert('(t) search tasks!');
	} else if ( e.shiftKey && ( e.which === 90 ) ) {
		alert('(z) Help, I nod off');
	} else if ( e.shiftKey && ( e.which === 80 ) ) {
		alert('(p) Pomodoro Toggle (start/Pause)');
	} 
	else if ( ( e.which === 13 ) && $('#suche_input').is(':focus') ) {
		PlaySound("mygoSound");
		var ziel = document.getElementById("suche_input").value;
		if(ziel.length > 2 && suche_option_wb.has(ziel.slice(0, 3))){
			window.open(suche_option_wb.get(ziel.slice(0, 3)) + ziel.slice(3));
		}
		else if(kurz_taste_wb2.has(ziel)){
			window.open(kurz_taste_wb2.get(ziel));
		}
		else{
			window.open('https://google.com/search?q='+ziel);
		}
	} 
	
});
