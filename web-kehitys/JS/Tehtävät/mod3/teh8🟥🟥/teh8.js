// Kirjoita funktio nimeltä concat(), jonka parametri on merkkijonoja sisältävä taulukko. 
// Funktio palauttaa merkkijonon, joka muodostetaan yhdistämällä taulukon alkiot toisiinsa. (2p)
// Esimerkki: Nelialkioisessa taulukossa ovat alkiot Johnny, DeeDee, Joey ja Marky.
// Funktio palauttaa merkkijonon JohnnyDeeDeeJoeyMarky.
// Älä käytä metodia array.join().
// Voit kirjoittaa taulukon suoraan koodiin. prompt()-funktiota ei tarvita.
// Tulosta tulos HTML-dokumenttiin.

"use strict";

function concat(taulukko) {
    let tulos = "";
    for (let i = 0; i < taulukko.length; i++) {
        tulos += taulukko[i];
    }
    return tulos;
}


const nimitaulukko = ["Johnny", "DeeDee", "Joey", "Marky"];

const yhdistettyTeksti = concat(nimitaulukko);



const target = document.querySelector("#target");
target.innerHTML = `<p>${yhdistettyTeksti}</p>`;