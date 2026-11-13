// Kirjoita ohjelma, joka kysyy käyttäjältä osallistujien lukumäärän. 
// Tämän jälkeen ohjelma kysyy kaikkien osallistujien nimet.
//  Lopuksi ohjelma tulostaa osallistujien nimet 
// verkkosivulle numeroituna luettelona (<ol>) aakkosjärjestyksessä. (2p)

"use strict";

const osamaar = parseInt(prompt("Anna osallistujien määrä: "));
const osallistujat = [];

for (let i = 0; i < osamaar; i++) {
    const nimi = prompt("Anna osallistujan nimi: ");
    osallistujat.push(nimi);
}


osallistujat.sort();


const target = document.querySelector("#target");

target.innerHTML += "<ol>";
for (let i = 0; i < osallistujat.length; i++) {
    target.innerHTML += `<li>${osallistujat[i]}</li>`;
}
target.innerHTML += "</ol>";