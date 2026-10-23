import math
import random

# ==========================================
# Tehtävä 1: Nimen kysyminen ja tervetulotoivotus
# ==========================================
nimi = input("Anna nimesi: ")
print(f"Terve {nimi}!")


# ==========================================
# Tehtävä 2: Ympyrän pinta-ala (A = π * r²)
# ==========================================
sade = float(input("Anna ympyrän säde: "))
pinta_ala = math.pi * sade**2

# :.2f tulostaa desimaaliluvun 2 desimaalin tarkkuudella
print(f"Ympyrän pinta-ala: {pinta_ala:.2f}")


# ==========================================
# Tehtävä 3: Suorakulmion piiri ja pinta-ala
# ==========================================
kanta = float(input("Anna suorakulmion kanta: "))
korkeus = float(input("Anna suorakulmion korkeus: "))

piiri = 2 * (kanta + korkeus)
pinta_ala = kanta * korkeus

print(f"Piiri on: {piiri:.2f}, pinta-ala on: {pinta_ala:.2f}")


# ==========================================
# Tehtävä 4: Kolmen luvun summa, tulo ja keskiarvo
# ==========================================
luku1 = int(input("Anna ensimmäinen luku: "))
luku2 = int(input("Anna toinen luku: "))
luku3 = int(input("Anna kolmas luku: "))

summa = luku1 + luku2 + luku3
tulo = luku1 * luku2 * luku3
keskiarvo = summa / 3

print(f"Lukujen summa: {summa}")
print(f"Lukujen tulo: {tulo}")
print(f"Lukujen keskiarvo: {keskiarvo:.2f}\n")


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

# Lasketaan täydet kilogrammat ja yli jäävät grammat
kilogrammat = int(yhteensa_grammat // 1000)
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