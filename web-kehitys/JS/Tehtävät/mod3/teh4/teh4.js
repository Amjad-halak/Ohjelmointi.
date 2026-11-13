// Kirjoita ohjelma, joka kysyy käyttäjältä lukuja, 
// kunnes käyttäjä syöttää nollan. 
// Ohjelma tulostaa annetut luvut konsoliin suurimmasta pienimpään. (2p)
"use strict";

const luvut = [];
let luku = parseInt(prompt("Anna luku: "));

while (luku !== 0) {
    luvut.push(luku);
    luku = parseInt(prompt("Anna luku: ")); 
}

// الترتيب من الأكبر للأصغر
luvut.sort((a, b) => b - a);


console.log(luvut);