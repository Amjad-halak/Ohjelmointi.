// Kirjoita ohjelma, joka kysyy käyttäjältä lukuja. 
// Kun käyttäjä syöttää luvun, jonka hän on jo aiemmin syöttänyt,
//  ohjelma ilmoittaa, että luku on jo annettu,
//  lopettaa toimintansa ja tulostaa kaikki annetut luvut konsoliin nousevassa järjestyksessä. (2p)
"use strict";


const luvut = [];

while (true) {
    const luku = parseInt(prompt("Anna luku: "));
    
    // الفحص: هل الرقم تم إدخاله مسبقاً؟
    if (luvut.includes(luku)) {
        console.log("warning !");
        break; // الخروج من حلقة التكرار
    } else {
        luvut.push(luku);
    }
}


luvut.sort((a, b) => a - b);


console.log(luvut);