//Muokkaa edellistä funktiota niin, että sillä on parametri, 
// joka kertoo nopan tahkojen lukumäärän.
//  Muokatulla funktiolla voit heittää esimerkiksi 21-tahkoista roolipelinoppaa. 
// Toisin kuin edellisessä tehtävässä, pääohjelma heittää noppaa, kunnes tulos on nopan suurin silmäluku. 
// Pääohjelma kysyy tahkojen lukumäärän käyttäjältä ohjelman alussa. (2p)
"use strict";


function heittoNoppa(tahkot) {
    return Math.floor(Math.random() * tahkot) + 1;
}


const tahkot = parseInt(prompt("Anna nopan tahkojen määrä: "));

const target = document.querySelector("#target");
target.innerHTML += "<ul>";

let tulos = 0;

// 3. الحلقة تستمر حتى نصل لأعلى رقم في النرد (tahkot)
while (tulos !== tahkot) {
    tulos = heittoNoppa(tahkot);
    target.innerHTML += `<li>${tulos}</li>`;
}

target.innerHTML += "</ul>";