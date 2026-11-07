// Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun ja kertoo, onko luku alkuluku. (2p)
// Alkuluku on ykköstä suurempi kokonaisluku, joka on jaollinen vain luvulla 1 ja itsellään.
// Esimerkiksi 13 on alkuluku, koska sen voi jakaa vain luvuilla 1 ja 13 niin, että tulos on kokonaisluku.
// Sen sijaan esimerkiksi 21 ei ole alkuluku, koska sen voi jakaa myös luvuilla 3 ja 7.
// Tulosta tulos HTML-dokumenttiin.

"use strict"


const luku = parseInt(prompt("Anna randomi luku : "));
let laskuri = 0 ;

// نمر ع كل الاعداد من 1 للرقم نفسه 
for(let i = 1 ; i <= luku ; i++) {
    if (luku % i === 0 ){
         laskuri++ ;    // ذيد العداد واحد لما تلاقي انو قسمه بدون باقي 
    }
}
if (laskuri === 2) {
    document.querySelector("#target").innerHTML += `Lukusi ${luku} on alkuluku <br>`;
} else {
    document.querySelector("#target").innerHTML += `Lukusi ${luku} ei ole alkuluku <br>`;
}

