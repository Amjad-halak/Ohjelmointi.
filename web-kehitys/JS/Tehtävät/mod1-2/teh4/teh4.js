// Harry Potter -lastenkirjoissa lajitteluhattu sijoittaa Tylypahkan noitien ja velhojen koulun uuden oppilaan yhteen neljästä tuvasta, 
// jotka ovat Rohkelikko, Luihuinen, Puuskupuh ja Korpinkynsi. Kirjoita sähköinen lajitteluhattu, 
// joka kysyy oppilaan nimeä ja arpoo oppilaalle tuvan. Jos annat nimeksi esimerkiksi Anna, ohjelma tulostaa HTML-dokumenttiin ”Anna, sinä olet Korpinkynsi.” (3p)
// Käytä metodia Math.random() arvon (1, 2, 3 tai 4) arpomiseen.
// Kun luku on arvottu, tarvitset valintarakenteen, jossa on useita vaihtoehtoja (if, else if, …, else tai switch).

// Math.floor(Math.random() * (max - min + 1)) + min;

"use strict";

const n = Math.floor(Math.random() * 4) + 1;
const nimi = prompt("Anna nimesi:");

document.querySelector("#target").innerHTML += `Sun numeri on ${n} <br>`;

if ( n === 1) 
    {document.querySelector("#target").innerHTML += `
  ${nimi} sä oot Rohkelikko <br>`;}

 else if (n === 2) 
    {document.querySelector("#target").innerHTML += `
  ${nimi} sä oot Luihuinen <br>`;}
 
 else if (n === 3) 
    {document.querySelector("#target").innerHTML += `
 Hei ${nimi} sä oot Puuskupuh <br>`;}

else if (n === 4) 
    {document.querySelector("#target").innerHTML += `
 Hei ${nimi} sä oot Korpinkynsi <br>`;}
