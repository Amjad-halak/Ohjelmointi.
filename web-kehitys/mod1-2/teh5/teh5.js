// Kirjoita ohjelma, joka pyytää käyttäjää syöttämään vuosiluvun ja ilmoittaa,
// onko vuosi karkausvuosi. 
// Vuosi on karkausvuosi, jos se on jaollinen neljällä. 
// Sadalla jaolliset vuodet ovat kuitenkin karkausvuosia vain, 
// jos ne ovat jaollisia myös neljälläsadalla. 
// Tulosta tulos HTML-dokumenttiin. (3p)

"use strict"

const vuosi = parseInt(prompt("syötä vuosiluvusi ? "))
const karkausvuosi = vuosi % 4 

