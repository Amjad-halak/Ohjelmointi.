// Kirjoita ohjelma, joka kysyy käyttäjältä viisi lukua ja tulostaa ne päinvastaisessa järjestyksessä kuin käyttäjä ne syötti (ei siis suuruusjärjestyksessä). Tulosta tulos konsoliin. (2p)
// Tallenna luvut taulukkoon ja käy taulukko sitten for-silmukalla läpi lopusta alkuun.
// Älä käytä metodia array.reverse().

const luvut = [];
for (let i=0 ; i < 5 ; i++) {
    luku=parseInt(prompt("Anna luku : "));
    luvut.push(luku)
}


for (let i=luvut.length -1 ; i >= 0 ; i-- ){
    console.log(luvut[i])
}