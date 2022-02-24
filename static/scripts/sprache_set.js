//sprache_set

function sprache_set(){
	
	document.getElementById("logo_title_id").innerHTML = sprache.logo_title;
	document.getElementById("arbeit_title_id").innerHTML = sprache.morgengruss;
	document.getElementById("tageszeit").innerHTML = sprache.morgengruss;

	document.getElementById("zeit_title_id").innerHTML = sprache.zeit;
	
	document.getElementById("date_title_id").innerHTML = sprache.datum;
	
	document.getElementById("suche_title_id").innerHTML = sprache.suche;
	document.getElementById("lesezeichen_title_id").innerHTML = sprache.lesezeichen;
	document.getElementById("arbeit_title_id").innerHTML = sprache.arbeit;
	document.getElementById("lernen_title_id").innerHTML = sprache.lernen;
	document.getElementById("geld_title_id").innerHTML = sprache.geld;
	document.getElementById("sozial_title_id").innerHTML = sprache.sozial;
	document.getElementById("musik_title_id").innerHTML = sprache.musik;
	document.getElementById("spiele_title_id").innerHTML = sprache.spiele;
	
	document.getElementById("zeitgeber_title_id").innerHTML = sprache.zeitgeber;
	document.getElementById("start_button").innerHTML = sprache.zeitgeber_start;
	document.getElementById("stopp_button").innerHTML = sprache.zeitgeber_stopp;
	document.getElementById("pause_button").innerHTML = sprache.zeitgeber_pause;
	document.getElementById("timer_modal_form_open_button").innerHTML = sprache.zeitgeber_bearbeiten;
	
	document.getElementById("kryptowahrung_title_id").innerHTML = sprache.kryptowahrung;    
	
};


sprache_set();