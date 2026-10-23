import random

# ==========================================
# Esimerkki 1: For-silmukan perusteet & range()
# ==========================================
# 1. Suora läpikäynti listan läpi
luvut = [1, 10, 55]
for luku in luvut:
    print(luku)

# 2. range(55) alkaa 0:sta ja päättyy 54:ään
for i in range(55):
    print(i)

# 3. range(0, 2) tulostaa arvot 0 ja 1
for i in range(0, 2):
    print(i)

# 4. reversed() laskee taaksepäin: 10 -> 1
for i in reversed(range(1, 11)):
    print(i)

# 5. range(alku, loppu, askel): lisää 3 joka kierroksella
for i in range(1, 56, 3):
    print(i)

# 6. Merkkijonolistan läpikäynti
nimet = ["shbshb", "amjad", "rama"]
for nimi in nimet:
    print(nimi)


# ==========================================
# Esimerkki 2: Satunnaisluvut listassa (Random Numbers in List)
# ==========================================
# Satunnaisen kokonaisluvun ja liukuluvun arpominen
x = random.randint(-100, 7521)
y = random.uniform(-1, 0)

# Tallennetaan satunnaisluvut listaan ja haetaan alkio indeksillä
pisteet = [x, y]
print(pisteet)

# pisteet[1] hakee toisen alkion
print(pisteet[1])


# ==========================================
# Esimerkki 3: Indeksit, viipalointi ja len() (Slicing & Length)
# ==========================================
nimet = ["m.snake", "ziizu", "värällä", "shbshb"]

print(nimet[-3])    # Negatiivinen indeksi: kolmas lopusta ("ziizu")
print(nimet[0:3])   # Ottaa alkiot indekseistä 0, 1 ja 2 (ensimmäiset 3 alkioita)
print(nimet[1:])    # Ottaa alkiot indeksistä 1 listan loppuun asti
print(nimet)

# len() palauttaa listan pituuden
listan_koko = len(nimet)
print(listan_koko)

# --- Listan läpikäynti while-silmukalla ---
laskuri = 0

# Toistetaan niin kauan kuin laskuri on pienempi kuin listan pituus
while laskuri < len(nimet):
    # laskuri + 1 näyttää järjestysnumeron (1, 2, 3...)
    print(f"{laskuri + 1}. nimi: {nimet[laskuri]}")
    laskuri += 1

# --- Listan kasvattaminen (input & append) ---
# Kysytään uusi nimi ja lisätään se listan loppuun append()-metodilla
uusi_nimi = input("Anna uusi nimi: ")
nimet.append(uusi_nimi)
print(nimet)

for nimi in nimet:
    print(nimi)


# ==========================================
# Esimerkki 4: Tehtävälista (Todos) ja eri silmukat
# ==========================================
tehtavat = []
tehtavat.append("Tee läksyt!")

# Lisätään käyttäjän syöte listaan
uusi_tehtava = input("Anna uusi tehtävä: ")
tehtavat.append(uusi_tehtava)
print(tehtavat)

# Tapa 1: Suora läpikäynti ilman indeksejä
for tehtava in tehtavat:
    print(tehtava)

# Tapa 2: Läpikäynti indeksien avulla range(len())-rakenteella
for i in range(len(tehtavat)):
    print(tehtavat[i])

# Tapa 3: range() tietylle numerovälille hyppyineen (3 -> 30, hyppy 3)
for luku in range(3, 31, 3):
    print(luku)


# ==========================================
# Esimerkki 5: Dynaaminen lista ja järjestäminen (Sorting)
# ==========================================
luvut = []

# Syötetään numeroita kunnes käyttäjä painaa Enter
syote = input("Anna numeroita (paina Enter lopettaaksesi): ")

while syote != "":
    # Muunnetaan merkkijono kokonaisluvuksi ja lisätään listaan
    luvut.append(int(syote))

    # Järjestetään numerot pienimmästä suurempaan
    luvut.sort()

    # Tulostetaan päivitetty lista ja sen alkiot
    print(f"Luvut ovat: {luvut}")
    for luku in luvut:
        print(luku)

    syote = input("Anna numeroita (paina Enter lopettaaksesi): ")

print("Ohjelma päättyi.")
print(f"Lopulliset luvut ovat: {luvut}")