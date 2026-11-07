// Kirjoita ohjelma, joka heittää käyttäjän määrittämän määrän noppia ja tulostaa heittojen tulosten summan. (2 p.)
// Ohjelma kysyy ensin käyttäjältä, kuinka monta noppaa heitetään.
// Tämän jälkeen ohjelma heittää noppaa käyttäjän määrittämän kerran.
//  Tulosta tulosten summa konsoliin tai HTML-dokumenttiin.
"use strict";


const määrä = parseInt(prompt("Anna heitto määrä:"));

const mkan = [];

let heitto = 0;

while (heitto < määrä) {


  const noppa = Math.floor(Math.random() * 6) + 1;
  

  mkan.push(noppa);

  heitto++;
}

let summa = 0;
for (let i = 0; i < mkan.length; i++) {
  summa += mkan[i]; 
}

document.querySelector("#target").innerHTML += `Heittojen tulosten summa on: ${summa} <br>`;