import math
import random

# ==========================================
# Tehtävä 1: Kolmella jaolliset luvut (1..1000)
# ==========================================
count = 1

while count <= 1000:
    if count % 3 == 0:
        print(f"{count} on jaollinen kolmella")
    count += 1  # Lisätään 1 joka kierroksella


# ==========================================
# Tehtävä 2: Tuumat senttimetreiksi
# ==========================================
tuuma = float(input("\nPistä tähän tuumamäärä: "))

while tuuma >= 0:
    cm = tuuma * 2.54
    print(f"cm määrä on {cm:.2f}")
    tuuma = float(input("Pistä tähän tuumamäärä: "))

print("Lopetetaan toiminta.")


# ==========================================
# Tehtävä 3: Pienin ja suurin luku (Korjattu versio)
# ==========================================
# Luodaan lista lukuja varten
luvut = []
syöte = input("\nAnna numero (tyhjä lopettaa): ").strip()

# Silmukka jatkuu kunnes syöte on tyhjä ""
while syöte != "":
    luku = float(syöte)
    luvut.append(luku)  # Lisätään luku listaan
    syöte = input("Anna seuraava numero (tyhjä lopettaa): ").strip()

# Tarkistetaan onko käyttäjä syöttänyt yhtään lukua
if len(luvut) > 0:
    print(f"Pienin luku: {min(luvut)}")
    print(f"Suurin luku: {max(luvut)}")
else:
    print("Et syöttänyt yhtään lukua.")


# ==========================================
# Tehtävä 4: Arvauspeli (1..10)
# ==========================================
random_number = random.randint(1, 10)
my_random_number = int(input("\nEnter number between 1-10: "))

while random_number != my_random_number:
    if my_random_number < random_number:
        print("Liian pieni arvaus.")
    else:
        print("Liian suuri arvaus.")
    my_random_number = int(input("Enter number between 1-10: "))

print(f"Oikein! Luku oli {random_number}.")


# ==========================================
# Tehtävä 5: Kirjautuminen (Max 5 yritystä)
# ==========================================
yritykset = 0
oikea_tunnus = "python"
oikea_salasana = "rules"

while yritykset < 5:
    tunnus = input("\nAnna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")
    yritykset += 1

    # Tarkistetaan ovatko tiedot oikein
    if tunnus == oikea_tunnus and salasana == oikea_salasana:
        print("Tervetuloa")
        break  # Lopetetaan silmukka heti
    else:
        print(f"Väärin! Yrityksiä jäljellä: {5 - yritykset}")

# Jos käytti kaikki 5 yritystä eikä päässyt sisään
if yritykset == 5 and (tunnus != oikea_tunnus or salasana != oikea_salasana):
    print("Pääsy evätty.")