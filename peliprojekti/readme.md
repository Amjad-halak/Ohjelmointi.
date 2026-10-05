# YK:n Rauhanturvaaja - Operaatio Rauha

**Tekijä:** Amjad Alhalak  
**Pelin nimi:** YK-seikkailupeli  

## Pelin Idea ja Tavoite
Pelin tavoitteena on edistää YK:n kestävän kehityksen tavoitetta **16 (Rauha, oikeudenmukaisuus ja hyvä hallinto)**.

Pelaaja toimii YK:n rauhanturvaajana eri palvelusalueilla. Pelin tavoitteena on suorittaa tehtäviä, kerätä pisteitä ja esineitä sekä turvata alueen rauha.

### Valittavat palvelusalueet ja tehtävät:
1. **Lähi-itä:** Rauhansopimuksen neuvottelu tai humanitaarisen avun jakaminen.
2. **Afrikka:** Siviilien suojaaminen tai vesipisteen rakentaminen.
3. **Eurooppa:** Kokouksen järjestäminen tai raportin kirjoittaminen.

## Tekninen toteutus
- **Modulaarinen rakenne:**
  - `main.py`: Pelin pääohjelma ja valikkosilmukka.
  - `luokat.py`: Luokat `Player` ja `Item`.
  - `rekisterointi.py`: Pelaajan rekisteröinti ja iäntarkistus.
- **Tiedostot:**
  - Pelin ohjeiden lukeminen tiedostosta (`ohjeet.txt`).
  - Pelitilanteen tallennus tiedostoon (`tallennus.txt`).