//  Kirjoita ohjelma, joka kysyy kolme kokonaislukua. Ohjelma tulostaa lukujen summan,
//  tulon ja keskiarvon HTML-dokumenttiin. (3p)
// Muista muuntaa merkkijonot luvuiksi ennen kuin lasket ne yhteen.

"use strict"

// 1. Kysytään luvut ja muunnetaan ne heti kokonaisluvuiksi (parseInt)
const n1 =parseInt(prompt("ana yks kokonais luku"));
const n2 =parseInt(prompt("ana toinen kokonais luku"));
const n3 =parseInt(prompt("ana kolmas kokonais luku"));

const summa = n1 + n2 +n3;
const tulo = n1 * n2 * n3 ;
const keskiarvo = (n1 + n2 + n3 )/3;

console.log(summa);
console.log(tulo);
console.log(keskiarvo);


document.querySelector('#target').innerHTML = `
    Summa: ${summa} <br>
    Tulo: ${tulo} <br>
    Keskiarvo: ${keskiarvo}
`;