import random

# ==========================================
# Esimerkki 0: Totuusarvo (Boolean: True / False)
# ==========================================
# Totuusarvomuuttuja (True tai False)
onko_totta = False

# Jos onko_totta on True, koodi suoritetaan. Jos False, hypätään yli.
if onko_totta:
    print("Onhan se totta!")


# ==========================================
# Esimerkki 1: Kolikonheitto (Satunnaisluku randint 0 tai 1)
# ==========================================
# Simuloidaan kolikonheittoa satunnaisilla kokonaisluvuilla (0 tai 1)
random_number = random.randint(0, 1)
print(f"Arvottu numero: {random_number}")

# if-ehto tarkistaa onko numero 0
if random_number == 0:
    tulos = "kruuna"
    print("Kruuna tuli!")
else:
    tulos = "klaava"

print(f"Heitit kolikkoa ja sait {tulos}n.")


# ==========================================
# Esimerkki 2: Kolikonheitto 2.0 (Liukuluku random.random & if-elif-else)
# ==========================================
# Kolikonheitto satunnaisella desimaaliluvulla ja useammalla vaihtoehdolla
random_number = random.random()
print(f"Desimaaliluku: {random_number:.4f}")

# Tarkistetaan todennäköisyydet järjestyksessä
if random_number < 0.01:
    print("Kolikko jäi pystyyn!")  # 1% mahdollisuus
elif random_number < 0.505:
    print("Kruuna tuli.")  # Noin 49.5% mahdollisuus
else:
    print("Klaava tuli.")  # Loput mahdollisuudet


# ==========================================
# Esimerkki 3: Numerovälin tarkistus ja ehdot (Vertailut)
# ==========================================
# Arvovälin tarkistus ja suorat vertailut
arvo = 150
# Tarkistetaan onko arvo välillä 90-110 (Palauttaa False)
print(90 < arvo < 110)
# Tarkistetaan ovatko luvut erisuuria (Palauttaa True)
print(100 != 101)


# ==========================================
# Esimerkki 4: Lääke-esimerkki (Sisäkkäiset ehdot & and/or)
# ==========================================
# Yhdistetyt ehdot lääkeannoksen tarkistamiseen
ika = int(input("Anna ikä: "))

# Kysytään painoa VAIN jos ikä on välillä 15-17
if 15 <= ika < 18:
    paino = float(input("Anna paino (kg): "))

# Ehto: Pääsee jos on vähintään 18 TAI (vähintään 15 JA painaa vähintään 55 kg)
if ika >= 18 or (ika >= 15 and paino >= 55):
    print("Lääkkeen käyttö on sallittua.")


# ==========================================
# Esimerkki 5: Satunnainen desimaaliluku (random.uniform)
# ==========================================
# Luodaan satunnainen desimaaliluku tietyltä väliltä
random_number_2 = random.uniform(-1.02, 1.34)
print(f"Satunnainen desimaali: {random_number_2:.2f}")

if random_number_2 >= 0:
    tulos1 = "suurempi tai yhtä suuri kuin 0"
else:
    tulos1 = "pienempi kuin 0"

print(f"Tulos on: {tulos1}")


# ==========================================
# Esimerkki 6: Ajokorttitarkistus (Sisäkkäinen if-lause)
# ==========================================
# Sisäkkäiset ehdot (Nested IF) iän ja pituuden tarkistamiseen
ika = int(input("Kuinka vanha olet? "))

if ika >= 18:
    tulos = "Voit saada ajokortin."
else:
    # Jos ikä on alle 18, kysytään pituus
    pituus = float(input("Anna pituutesi (cm): "))
    if pituus >= 180:
        tulos = "Voit saada poikkeusluvan ajokorttiin."
    else:
        tulos = "Et voi vielä saada ajokorttia."

print(f"Tulos: {tulos}\nOta yhteyttä asiakaspalveluumme.")


# ==========================================
# Esimerkki 7: Looginen AND ja .upper() -metodi
# ==========================================
# Looginen AND ja syötteen muuttaminen isoksi kirjaimeksi (.upper())
lampotila = float(input("Anna alueesi lämpötila nyt: "))
aurinkoista = input("Paistaako ulkona aurinko (K/E): ").upper()

# Molempien ehtojen pitää toteutua (Lämpötila > 15 JA aurinkoista == "K")
if lampotila > 15 and aurinkoista == "K":
    tulos = "Mene uimaan!"
else:
    tulos = "Sää ei ole paras mahdollinen, pysy kotona."

print(f"Suositus: {tulos}")


# ==========================================
# Esimerkki 8: Looginen OR (Jompaakumpaa ehtoa riittää)
# ==========================================
# Looginen OR (riittää että toinen ehto toteutuu)
lampotila = float(input("Anna alueesi lämpötila nyt: "))

# Ehto toteutuu jos lämpötila on 0 tai alle TAI 30 tai yli
if lampotila <= 0 or lampotila >= 30:
    tulos = "Lämpötila on huono."
else:
    tulos = "Lämpötila on hyvä."

print(f"Säätilanne: {tulos}")


# ==========================================
# Esimerkki 9: Totuusarvomuuttujan käyttö ehtolauseessa
# ==========================================
# Totuusarvon (Boolean) suora käyttö if-ehdossa
aurinkoista = True

# Jos aurinkoista on True, suoritetaan ensimmäinen lohko
if aurinkoista:
    tulos = "Ulkona paistaa aurinko."
else:
    tulos = "Ulkona ei paista aurinko, joten siellä on pilvistä."

print(f"Tilanne: {tulos}")