// Kirjoita ohjelma, joka kysyy kuuden koiran nimet.
//  Ohjelma tulostaa koirien nimet järjestämättömään luetteloon (<ul>)
//  käänteisessä aakkosjärjestyksessä. (2p)
"use strict";
const koirat = []
for (let i = 0 ; i < 6 ; i++) {
    const nimi = prompt("anna koiran nimi : ")
    koirat.push(nimi)
}

// 1. ترتيب الأسماء أبجدياً ثم عكسها
koirat.sort()
koirat.reverse()

const target = document.querySelector("#target");

target.innerHTML += "<ul>";
for (let i = 0; i < koirat.length; i++) {
    target.innerHTML += `<li>${koirat[i]}</li>`;
}
target.innerHTML += "</ul>";