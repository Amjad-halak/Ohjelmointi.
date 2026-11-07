// Kirjoita ohjelma, joka tulostaa vahvistusikkunaan tekstin ”Pitäisikö minun laskea neliöjuuri?”.
// Jos käyttäjä valitsee OK, ohjelma kysyy lukua ja laskee sen neliöjuuren ja tulostaa sen HTML-dokumenttiin.
// Jos käyttäjä valitsee Cancel, ohjelma tulostaa tekstin ”Neliöjuurta ei ole laskettu.” HTML-dokumenttiin (3p)

// Vahvistusikkuna voidaan avata funktiolla confirm(). Funktio palauttaa arvon true, jos käyttäjä valitsee OK.
// Jos käyttäjä valitsee Cancel, funktio palauttaa arvon false.
// Negatiivisen luvun neliöjuurta ei voi laskea. Jos käyttäjän syöttämä luku on negatiivinen,
// ohjelma tulostaa HTML-dokumenttiin tekstin ”Negatiivisen luvun neliöjuurta ei ole määritelty”.
"use strict";

const kysy = confirm("Pitäisikö minun laskea neliöjuuri?")

if (kysy === true) {
    const luku=parseFloat(prompt("Anna luku : "))

    if (luku < 0){
        document.querySelector("#target").innerHTML += `
    Negatiivisen luvun neliöjuurta ei ole määritelty. <br>`  ;
}
    else {
  const neliojuuri = Math.sqrt(luku);
  document.querySelector("#target").innerHTML += `Luvun ${luku} neliöjuuri on ${neliojuuri}.<br>`;
}
}
else {
    document.querySelector("#target").innerHTML += `
   Neliöjuurta ei ole laskettu.  <br>`  ;
}

