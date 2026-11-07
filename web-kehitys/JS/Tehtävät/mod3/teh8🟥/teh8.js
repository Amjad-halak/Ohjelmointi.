// Kirjoita ohjelma, joka kysyy käyttäjältä vuoden alun ja lopun.
//  Ohjelma tulostaa kaikki karkausvuodet käyttäjän antamalta aikaväliltä. 
// Tulostus tapahtuu järjestämättömänä listana HTML-dokumenttiin. (3p)

"use strict";

const alku = parseInt(prompt("Anna vuoden alku:"));
const loppu = parseInt(prompt("Anna vuoden loppu:"));


const target = document.querySelector("#target");
target.innerHTML += "<ul>";


for (let vuosi = alku; vuosi <= loppu; vuosi++) {


  if ((vuosi % 4 === 0 && vuosi % 100 !== 0) || (vuosi % 400 === 0)) {

    target.innerHTML += `<li>${vuosi}</li>`;
  }

}


target.innerHTML += "</ul>";



