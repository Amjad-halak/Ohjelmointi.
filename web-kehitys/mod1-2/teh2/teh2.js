// Kirjoita ohjelma, joka kysyy käyttäjän nimeä ja tervehtii sitten käyttäjää.
//  Tulosta tervehdys HTML-dokumenttiin: Hei, Nimi! (2p)
"use strict";

const nimi =prompt("sun nimi ? ");

console.log(" terve " + nimi + ".");

document.querySelector("#target").innerHTML = `
YOUR FUCKING NAME IS : ${nimi} <br>`;