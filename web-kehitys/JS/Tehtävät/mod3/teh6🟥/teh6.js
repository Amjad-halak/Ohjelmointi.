// Kirjoita funktio, joka palauttaa satunnaisen nopanheiton tuloksen väliltä 1–6.
//  Funktiolla ei saa olla parametreja. Kirjoita pääohjelma,
//  joka heittää noppaa, kunnes tulos on 6.
//  Pääohjelman on tulostettava jokaisen heiton tulos järjestämättömään luetteloon (<ul>). (2p)
"use strict";

function heittaNoppaa() {
    return Math.floor(Math.random() * 6) + 1;
}

const target = document.querySelector("#target");
target.innerHTML += "<ul>";

let tulos = 0;
while (tulos !== 6) {
    tulos = heittaNoppaa();
    target.innerHTML += `<li>${tulos}</li>`;
}

target.innerHTML += "</ul>";