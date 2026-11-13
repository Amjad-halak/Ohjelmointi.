// Kirjoita ohjelma, joka kysyy käyttäjältä noppien lukumäärän ja silmälukujen summan, josta käyttäjä on kiinnostunut. Ohjelma selvittää, millä todennäköisyydellä annettu määrä noppia tuottaa annetun silmälukujen summan. Jos käyttäjä esimerkiksi syöttää noppien lukumääräksi 3 ja silmälukujen summaksi 17, ohjelma laskee todennäköisyyden sille, että kolmen nopan silmälukujen summa on 17. (5p)
// Ratkaise ongelma simuloimalla: heitä annettua määrää noppia for-silmukassa monta kertaa (esim. 10 000 kertaa) ja laske, kuinka suuressa osassa heittokerroista silmälukujen summa oli käyttäjän antama summa.
// Tulosta tulos HTML-dokumenttiin:
// Todennäköisyys saada summa 7 kahdella nopalla on 15.64%
// Voit rajoittaa desimaalien määrää metodilla toFixed().
// Testiarvoja:
// 2 noppaa, summa 7: todennäköisyys on noin 15–17 %
// 3 noppaa, summa 15: todennäköisyys on noin 5 %

// (بداية العداد ; الشرط ; طريقة الزيادة)
"use strict";

const noppat_määrä = parseInt(prompt("Anna noppien määrä: "));
const haluttusumma = parseInt(prompt("Anna haluttu summa: "));

const Toisita = 10000; 
let osumat = 0;

for (let i = 0; i < Toisita; i++) {
    let heittosumma = 0;

    for (let j = 0; j < noppat_määrä; j++) {
        let noppa = Math.floor(Math.random() * 6) + 1;
        heittosumma += noppa;
    }

    if (heittosumma === haluttusumma) {
        osumat++;
    }
}

const todennakoisyys = ((osumat / Toisita) * 100).toFixed(2);

document.querySelector("#target").innerHTML += `Todennäköisyys saada summa ${haluttusumma} ${noppat_määrä} nopalla on ${todennakoisyys}% <br>`;