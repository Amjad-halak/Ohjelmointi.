import math
import random

# ==========================================
# Tehtävä 1: Kolmella jaolliset luvut (1..1000)
# ==========================================
count = 1
while count <= 1000:
    if count % 3 == 0:
        print(f"{count} on jaollinen kolmella")
    count += 1


# ==========================================
# Tehtävä 2: Tuumat senttimetreiksi
# ==========================================
tuuma = float(input("Anna tuumamäärä (negatiivinen lopettaa): "))
while tuuma >= 0:
    cm = tuuma * 2.54
    print(f"{tuuma} tuumaa = {cm:.2f} cm")
    tuuma = float(input("Anna tuumamäärä (negatiivinen lopettaa): "))

print("Toiminta lopetettu.")


# ==========================================
# Tehtävä 3: Pienin ja suurin luku
# ==========================================
luvut = []
while True:
    syöte = input("Anna luku (tyhjä lopettaa): ").strip()
    if syöte == "":
        break
    luvut.append(float(syöte))

if len(luvut) > 0:
    print(f"Pienin luku: {min(luvut)}")
    print(f"Suurin luku: {max(luvut)}")
else:
    print("Et syöttänyt yhtään lukua.")


# ==========================================
# Tehtävä 4: Numeron arvauspeli (1..10)
# ==========================================
oikea_luku = random.randint(1, 10)
arvaus = int(input("Arvaa luku väliltä 1..10: "))

while arvaus != oikea_luku:
    if arvaus < oikea_luku:
        print("Liian pieni arvaus")
    else:
        print("Liian suuri arvaus")
    arvaus = int(input("Arvaa uudelleen: "))

print("Oikein!")


# ==========================================
# Tehtävä 5: Käyttäjätunnus ja salasana (max 5 yritystä)
# ==========================================
yritykset = 0
oikein = False

while yritykset < 5:
    tunnus = input("Anna käyttäjätunnus: ").strip()
    salasana = input("Anna salasana: ").strip()
    yritykset += 1

    if tunnus == "python" and salasana == "rules":
        oikein = True
        break
    else:
        print("Väärä tunnus tai salasana.")

if oikein:
    print("Tervetuloa!")
else:
    print("Pääsy evätty.")