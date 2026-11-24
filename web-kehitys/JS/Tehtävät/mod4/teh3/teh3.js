// Avaa kansio t3 kehitysympäristössäsi tai editorissasi. Lisää HTML-koodia innerHTML-ominaisuuden avulla. (2p)
// Lisää seuraava HTML-koodi elementtiin, jolla on id="target". Lisää names-taulukon arvot <li>-elementteihin for-silmukassa.
// <li>John</li>
// <li>Paul</li>
// <li>Jones</li>

"use strict"
const names = ['John', 'Paul', 'Jones'];
const target =document.getElementById("target")

for(const name of names){
    target.innerHTML += `<li>${name}</li>`
}