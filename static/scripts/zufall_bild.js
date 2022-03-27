
var images=['images/000.jpg',
'images/1.jpg',
 'images/2.jpg',
 'images/3.jpg',
 'images/6.jpg',
 'images/7.jpg',
 'images/8.png',
 'images/9.jpg',
 'images/11.jpg',
 'images/0.jpg',
 'images/10.png',
 'images/4.png'];

var randomNumber = Math.floor(Math.random() * images.length);
var bgImg = "http://127.0.0.1:5000/static/" + images[randomNumber];


document.body.style.backgroundImage = "linear-gradient(rgba(0,0,0,0.55),rgba(0,0,0,0.1)),url("+bgImg+")";
document.body.style.backgroundPosition = "center 30%";
document.body.style.backgroundSize = "stretch";
document.getElementById("suche_input").focus();
