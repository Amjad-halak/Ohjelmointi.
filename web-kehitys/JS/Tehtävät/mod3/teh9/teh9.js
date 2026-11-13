// Kirjoita funktio nimeltä even(), jonka parametri on lukuja sisältävä taulukko. Funktio palauttaa uuden (yleensä lyhyemmän) taulukon, 
// jossa ovat alkuperäisen taulukon parilliset luvut. Funktio ei saa muuttaa alkuperäistä taulukkoa. (3p)
// Esimerkki: Kolmialkioisessa taulukossa ovat alkiot 2, 7 ja 4. Funktio palauttaa kaksialkioisen taulukon, jossa ovat alkiot 2 ja 4.
// Tulosta pääohjelmassa funktiokutsun jälkeen sekä alkuperäinen että uusi taulukko konsoliin.
// Voit kirjoittaa taulukon suoraan koodiin. prompt()-funktiota ei tarvita.
"use strict"

function even (numerot){
    let parilliset=[]
    for (const numero of numerot) 
        if (numero % 2 === 0)
        {parilliset.push(numero)};
    return parilliset
};

const luvut = [ 2 , 7 , 4 , 11 ];

const uudetluvut = even(luvut);

console.log(luvut);
console.log("even luvut" , {uudetluvut});

    