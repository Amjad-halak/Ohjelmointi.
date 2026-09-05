import math
import random

# ==========================================
# Tehtävä 1: Nimen kysyminen ja tervetulotoivotus
# ==========================================
x = input("Pistä tähän oma kutsunimi: ")
print(f"Hello {x}!")


# ==========================================
# Tehtävä 2: Ympyrän pinta-ala (A = π * r²)
# ==========================================
r = float(input("Pistä ympyrän säde tässä: "))
A = math.pi * r**2

# :.2f tulostaa desimaaliluvun 2 desimaalin tarkkuudella
print(f"Ympyrän pinta-ala: {A:.2f}")


# ==========================================
# Tehtävä 3: Suorakulmion piiri ja pinta-ala
# ==========================================
a = float(input("Anna suorakulmion kanta: "))
b = float(input("Anna suorakulmion korkeus: "))

piiri = 2 * (a + b)
pinta_ala = a * b

print(f"Piiri on: {piiri:.2f}, pinta-ala on: {pinta_ala:.2f}")


# ==========================================
# Tehtävä 4: Kolmen luvun summa, tulo ja keskiarvo
# ==========================================
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

summa = x + y + z
tulo = x * y * z
keskiarvo = summa / 3  # Käytetään summata-muuttujaa laskentaan

# \n tekee uuden rivin tulosteessa
print(f"Numbers summa on: {summa}\nNumbers tulo on: {tulo}\nNumbers keskiarvo on: {keskiarvo:.2f}\n")


# ==========================================
# Tehtävä 5: Keskiaikaiset mitat (Kilot ja grammat)
# ==========================================
# 1 leiviskä = 20 naulaa, 1 naula = 32 luotia, 1 luoti = 13.3 grammaa
leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("Anna naulat: "))
luodit = float(input("Anna luodit: "))

# Muunnetaan kaikki ensin luodeiksi
yhteensa_luodit = (leiviskat * 20 * 32) + (naulat * 32) + luodit
yhteensa_grammat = yhteensa_luodit * 13.3

# // antaa pelkät täydet kilogrammat (1000g = 1kg)
kilogrammat = int(yhteensa_grammat // 1000)
# % antaa yli jäävät grammat (Jakojäännös)
grammat = yhteensa_grammat % 1000

print("\nMassa nykymittojen mukaan:")
print(f"{kilogrammat} kilogrammaa ja {grammat:.2f} grammaa.")


# ==========================================
# Tehtävä 6: Numerolukon koodien arpointi (Koodigeneraattori)
# ==========================================
# 1) 3-numeroinen koodi (numerot 0..9)
koodi1_1 = random.randint(0, 9)
koodi1_2 = random.randint(0, 9)
koodi1_3 = random.randint(0, 9)

# 2) 4-numeroinen koodi (numerot 1..6)
koodi2_1 = random.randint(1, 6)
koodi2_2 = random.randint(1, 6)
koodi2_3 = random.randint(1, 6)
koodi2_4 = random.randint(1, 6)

print(f"3-numeroinen koodi (0-9): {koodi1_1}{koodi1_2}{koodi1_3}")
print(f"4-numeroinen koodi (1-6): {koodi2_1}{koodi2_2}{koodi2_3}{koodi2_4}")