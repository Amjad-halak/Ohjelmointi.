// Kirjoita alla kuvattu äänestysohjelma pienimuotoiseen kokouskäyttöön. (8p)
// Ohjelma kysyy ehdokkaiden lukumäärän.
// Sitten ohjelma kysyy ehdokkaiden nimet: Ehdokkaan 1 nimi
// Tallenna jokaisen ehdokkaan nimi ja äänimäärän alkuarvo omaan olioonsa ja oliot taulukkoon näin:

// Ohjelma kysyy äänestäjien lukumäärän.
// Ohjelma kysyy vuorotellen jokaiselta äänestäjältä, ketä hän äänestää. Äänestäjä syöttää ehdokkaan nimen. Jos äänestäjä jättää nimen syöttämättä, ääni tulkitaan tyhjäksi.
// Ohjelma tulostaa konsoliin voittajan nimen ja tulokset:

// Voittaja on pamela 3 äänellä.
// tulokset:
// pamela: 3 ääntä
// frank: 1 ääntä
// ellie: 1 ääntä

"use strict";

const ehdokkaat = [];

const ehdokkaidenMaara = parseInt(prompt("Anna ehdokkaiden määrä:"));

for (let i = 0; i < ehdokkaidenMaara; i++) {
  const nimi = prompt(`Ehdokkaan ${i + 1} nimi`);
  ehdokkaat.push({
    name: nimi,
    votes: 0,
  });
}


const aanestajienLukumaara = parseInt(prompt("Anna äänestäjien määrä:"));

for (let i = 0; i < aanestajienLukumaara; i++) {
  const aani = prompt(`Äänestäjä ${i + 1}, ketä äänestät?`);
  for (const ehdokas of ehdokkaat) {
    if (ehdokas.name === aani) {
      ehdokas.votes++;
    }
  }
}


ehdokkaat.sort((a, b) => {
  return b.votes - a.votes;
});


console.log(`Voittaja on ${ehdokkaat[0].name} ${ehdokkaat[0].votes} äänellä.`);
console.log("tulokset:");

for (const ehdokas of ehdokkaat) {
  console.log(`${ehdokas.name}: ${ehdokas.votes} ääntä`);
}

const target = document.querySelector("#target");

target.textContent =
  `Voittaja on ${ehdokkaat[0].name} ${ehdokkaat[0].votes} äänellä.\n` +
  `Tulokset:\n` +
  ehdokkaat
    .map(ehdokas => `${ehdokas.name}: ${ehdokas.votes} ääntä`)
    .join("\n");

target.style.whiteSpace = "pre-line";