import random

# ==========================================
# Tehtävä 1: Arpakuutiot (for-silmukka)
# ==========================================
heitto_kerrat = int(input("Anna arpakuutioiden lukumäärä: "))
summa = 0

for i in range(heitto_kerrat):
    heitto = random.randint(1, 6)
    summa += heitto
    print(f"Heitto {i + 1}: {heitto}")

print(f"Silmälukujen summa: {summa}")


# ==========================================
# Tehtävä 1.2: Arpakuutiot (while-silmukka)
# ==========================================
heitto_kerrat = int(input("\nAnna arpakuutioiden lukumäärä: "))
kerrat = 0
summa = 0

while kerrat < heitto_kerrat:
    heitto = random.randint(1, 6)
    summa += heitto
    kerrat += 1

print(f"Silmälukujen summa: {summa}")


# ==========================================
# Tehtävä 2: Viisi suurinta lukua
# ==========================================
luvut = []

while True:
    syote = input("\nAnna luku (tyhjä lopettaa): ").strip()
    if syote == "":
        break
    luvut.append(float(syote))

luvut.sort(reverse=True)

print("Viisi suurinta lukua:")
for i, luku in enumerate(luvut[:5], start=1):
    print(f"Luku {i}: {luku}")


# ==========================================
# Tehtävä 3: Alkuluvun tarkistus
# ==========================================
kokonaisluku = int(input("\nAnna kokonaisluku: "))

if kokonaisluku <= 1:
    print("Luku ei ole alkuluku.")
else:
    on_alkuluku = True
    for i in range(2, kokonaisluku):
        if kokonaisluku % i == 0:
            on_alkuluku = False
            break

    if on_alkuluku:
        print("Luku on alkuluku.")
    else:
        print("Luku ei ole alkuluku.")


# ==========================================
# Tehtävä 4: Viisi kaupunkia
# ==========================================
kaupungit = []

for i in range(5):
    nimi = input("Anna kaupungin nimi: ").strip()
    kaupungit.append(nimi)

print("\nSyötetyt kaupungit:")
for kaupunki in kaupungit:
    print(kaupunki)


# ==========================================
# Tehtävä 5: Ahkerien opiskelijoiden lista
# ==========================================
opiskelijat = []

while True:
    nimi = input("\nAnna ahkeran opiskelijan nimi (tyhjä lopettaa): ").strip()
    if nimi == "":
        break
    opiskelijat.append(nimi)

print("\nOpiskelijat:")
for i, opiskelija in enumerate(opiskelijat, start=1):
    print(f"{i}. {opiskelija}")