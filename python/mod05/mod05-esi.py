# ==========================================
# Esimerkki 0: Numeroiden kasvattaminen (Laskuri)
# ==========================================
x = 1.5

while x <= 10.00:
    print(f"{x:.2f} on pienempi kuin vertailunumero")
    x += 1.3

print("Valmis")


# ==========================================
# Esimerkki 1: Tyhjän syötteen tarkistus
# ==========================================
nimi = input("\nAnna nimesi: ").strip()

while nimi == "":
    print("Et syöttänyt nimeäsi!")
    nimi = input("Anna nimesi uudelleen: ").strip()

print(f"Hei {nimi}!")


# ==========================================
# Esimerkki 2: Virheellisen arvon estäminen
# ==========================================
ika = float(input("\nMikä on ikäsi? "))

while ika < 0:
    print("Ikä ei voi olla negatiivinen.")
    ika = float(input("Anna ikäsi uudelleen: "))

print(f"Hei {ika}-vuotias henkilö!")


# ==========================================
# Esimerkki 3: Lopetusmerkin käyttö ("q" lopettaa)
# ==========================================
ruoka = input("\nAnna lempiruokasi (paina q lopettaaksesi): ").strip()

while ruoka.lower() != "q":
    print(f"Pidät ruoasta {ruoka}.")
    ruoka = input("Anna toinen lempiruokasi (paina q lopettaaksesi): ").strip()

print("Näkemiin!")


# ==========================================
# Esimerkki 4: Numero tietyltä väliltä (1-10)
# ==========================================
numero = int(input("\nValitse numero väliltä 1-10: "))

while numero < 1 or numero > 10:
    print(f"Numero {numero} ei ole sallitulla välillä. Seuraa sääntöjä!")
    numero = int(input("Valitse numero väliltä 1-10: "))

print(f"Valitsemasi numero on {numero}!")


# ==========================================
# Esimerkki 5: Toistokertojen määrä
# ==========================================
toistot = int(input("\nKuinka monta kertaa toistetaan? "))
suoritettu = 0

while suoritettu <= toistot:
    print(f"Toisto numero: {suoritettu}")
    suoritettu += 1


# ==========================================
# Esimerkki 6: Monen lopetuskomennon tarkistus
# ==========================================
komento = input("\nAnna komento: ").strip()

while not (komento.lower() == "lopeta" or komento.lower() == "stop" or komento == ""):
    print(f"Suoritetaan toiminto: {komento}")
    komento = input("Anna komento: ").strip()

print("Toiminto päättyi.")


# ==========================================
# Esimerkki 7: Satunnaislukujen simulointi (Nopanheitto)
# ==========================================
noppa1 = 0
noppa2 = 0
heittojen_maara = 0

while not (noppa1 == 6 and noppa2 == 6):
    noppa1 = random.randint(1, 6)
    noppa2 = random.randint(1, 6)
    heittojen_maara += 1

print(f"\nTarvittiin {heittojen_maara} heittoa, että saatiin molemmista nopista 6.")


# ==========================================
# Esimerkki 8: Sisäkkäiset silmukat (Kertotaulu)
# ==========================================
ensimmainen = 1

while ensimmainen <= 10:
    toinen = 1
    while toinen <= 10:
        print(f"{ensimmainen} * {toinen} = {ensimmainen * toinen}")
        toinen += 1
    ensimmainen += 1

print("Kertotaulu valmis.")


# ==========================================
# Esimerkki 9: Laskurien oikotiet (+=)
# ==========================================
luku = 0
luku += 1
luku += 1

print(f"\nLaskurin arvo: {luku}")


# ==========================================
# Esimerkki 10: Taaksepäin laskeminen
# ==========================================
laskuri = 10

print("\n--- Lasketaan alaspäin ---")
while laskuri > 0:
    print(laskuri)
    laskuri -= 1


# ==========================================
# Esimerkki 11: Käyttäjänimen kysyminen ja yrityskerrat
# ==========================================
nimi = input("\nAnna nimesi: ").strip()
yritykset = 0

while nimi == "" and yritykset < 5:
    yritykset += 1
    print("Et syöttänyt nimeäsi!")
    
    if yritykset == 5:
        break
        
    nimi = input("Anna nimesi: ").strip()

if nimi != "":
    print(f"Tervetuloa {nimi}!")
else:
    print("Käytit kaikki 5 yritystä.")


# ==========================================
# Esimerkki 12: Tekstin puhdistus ja while/else -rakenne
# ==========================================
komento = input("\nAnna komento (pelaa / apua / lopeta): ").strip().lower()

while komento != "lopeta":
    if komento == "apua":
        print("Tässä on ohje: Kirjoita 'pelaa' aloittaaksesi tai 'lopeta' poistuaksesi.")
        break
    elif komento == "pelaa":
        print("Peli käynnistyy... Wuuhoo!")
    else:
        print(f"Tuntematon komento: {komento}")
    
    komento = input("\nAnna uusi komento: ").strip().lower()
else:
    print("Annoit käskyn 'lopeta', joten ohjelma suljetaan nätisti.")

print("Ohjelma päättyi.")