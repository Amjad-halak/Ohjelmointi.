import math
import random

# ==========================================
# Tehtävä 1: Kolmella jaolliset luvut (1..1000)
# ==========================================
laskuri = 1

while laskuri <= 1000:
    if laskuri % 3 == 0:
        print(f"{laskuri} on jaollinen kolmella")
    laskuri += 1


# ==========================================
# Tehtävä 2: Tuumat senttimetreiksi
# ==========================================
tuuma = float(input("\nAnna tuumamäärä (negatiivinen lopettaa): "))

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
    syote = input("\nAnna luku (tyhjä lopettaa): ").strip()
    if syote == "":
        break
    luvut.append(float(syote))

if len(luvut) > 0:
    print(f"Pienin luku: {min(luvut)}")
    print(f"Suurin luku: {max(luvut)}")
else:
    print("Et syöttänyt yhtään lukua.")


# ==========================================
# Tehtävä 4: Arvauspeli (1..10)
# ==========================================
oikea_luku = random.randint(1, 10)
arvaus = int(input("\nArvaa luku väliltä 1-10: "))

while arvaus != oikea_luku:
    if arvaus < oikea_luku:
        print("Liian pieni arvaus.")
    else:
        print("Liian suuri arvaus.")
    arvaus = int(input("Arvaa uudelleen väliltä 1-10: "))

print(f"Oikein! Luku oli {oikea_luku}.")


# ==========================================
# Tehtävä 5: Kirjautuminen (Max 5 yritystä)
# ==========================================
yritykset = 0
oikea_tunnus = "python"
oikea_salasana = "rules"
oikein = False

while yritykset < 5:
    tunnus = input("\nAnna käyttäjätunnus: ").strip()
    salasana = input("Anna salasana: ").strip()
    yritykset += 1

    if tunnus == oikea_tunnus and salasana == oikea_salasana:
        oikein = True
        break
    else:
        print(f"Väärin! Yrityksiä jäljellä: {5 - yritykset}")

if oikein:
    print("Tervetuloa!")
else:
    print("Pääsy evätty.")