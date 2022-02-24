


function myWetter(art, api_url, listItem) {
    var xhttp = new XMLHttpRequest();
	xhttp.responseType = 'json';

    xhttp.onreadystatechange = function() {
         if (this.readyState == 4 && this.status == 200) {

			var data = this.response.data.amount;
			
			
			span1 = listItem.getElementsByClassName("krypto_info_links--blau")[0];
			span2 = listItem.getElementsByClassName("krypto_info_rechts--weiss")[0];
			
			span1.innerHTML = art;
			span2.innerHTML = data;
			
			//span1.appendChild(span1);		
			//listItem.appendChild(span2);	
			//listItem.insertBefore(span2, listItem.childNodes[1])
			//listItem.insertBefore(span1, listItem.childNodes[1])
         }
    };
	
    xhttp.open("GET", api_url, true);
    xhttp.send();
}

function ruf_alle_queries(){
	var i;
	
	const ul = document.getElementById('munzen');
	const listItems = ul.getElementsByTagName('li');
	
	for (i = 0; i < listItems.length; i++) {
		var krypto = global_query_liste2[i][0];
		var fiat = global_query_liste2[i][1];
		var query = "https://api.coinbase.com/v2/prices/"+krypto+"-"+fiat+"/buy";	
		var id = global_query_liste2[i][2];
		myWetter(krypto, query, listItems[i]);
		}
};

ruf_alle_queries();

var munzen_scan_urh = setInterval(munzen_scan, 1000*60*60);

function munzen_scan(){
	
	var ul = document.getElementById("munzen");
	ul.innerHTML = "";
	
	ruf_alle_queries();
	
}
