import math
import random  

# ==========================================
# Tehtävä 1: Parametriton noppa (نرد عادي 1..6)
# ==========================================
# Palauttaa satunnaisen silmäluvun väliltä 1..6 ja heittää kunnes tulee 6


def heita_noppaa():
    return random.randint(1, 6)


# Pääohjelma (البرنامج الرئيسي)
print("=== Tehtävä 1: Noppa 1..6 ===")
tulos = 0
while tulos != 6:
    tulos = heita_noppaa()
    print(f"Heiton tulos: {tulos}")


# ==========================================
# Tehtävä 2: Tahkollinen noppa (نرد مع عدد أوجه من المستخدم)
# ==========================================
# Saa parametrina tahkojen määrän ja heittää kunnes saadaan maksimisilmäluku


def heita_mukaullettua_noppaa(tahkot):
    return random.randint(1, tahkot)


# Pääohjelma
print("\n=== Tehtävä 2: Tahkollinen noppa ===")
maksimi = int(input("Anna nopan tahkojen määrä: "))

tulos = 0
while tulos != maksimi:
    tulos = heita_mukaullettua_noppaa(maksimi)
    print(f"Saatu silmäluku: {tulos}")


# ==========================================
# Tehtävä 3: Gallonat litroiksi (تحويل الجالونات إلى لترات)
# ==========================================
# Muuntaa gallonat litroiksi kunnes syötetään negatiivinen luku


def gallonat_litroiksi(gallonat):
    return gallonat * 3.785


# Pääohjelma
print("\n=== Tehtävä 3: Bensiinin muunnos ===")
syote = float(input("Anna bensiinin määrä gallonoina (negatiivinen lopettaa): "))

while syote >= 0:
    litrat = gallonat_litroiksi(syote)
    print(f"{syote} gallonaa on {litrat:.2f} litraa.")
    syote = float(input("Anna uusi gallonamäärä: "))

print("Lopetetaan (syötettiin negatiivinen luku).")


# ==========================================
# Tehtävä 4: Listan summa (حساب مجموع عناصر القائمة)
# ==========================================
# Saa parametrina listan kokonaislukuja ja palauttaa niiden summan


def laske_summa(lista):
    return sum(lista)


# Pääohjelma
print("\n=== Tehtävä 4: Listan summa ===")
testilista = [5, 12, 8, 20, 3]
summa = laske_summa(testilista)

print(f"Lista: {testilista}")
print(f"Listan lukujen summa: {summa}")


# ==========================================
# Tehtävä 5: Parittomien karsiminen (فلترة الأرقام الزوجية فقط)
# ==========================================
# Palauttaa uuden listan, josta on karsittu pois kaikki parittomat luvut


def karsi_parittomat(lista):
    parilliset = []
    for luku in lista:
        if luku % 2 == 0:
            parilliset.append(luku)
    return parilliset


# Pääohjelma
print("\n=== Tehtävä 5: Parilliset luvut ===")
alkuperainen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
karsittu = karsi_parittomat(alkuperainen)

print(f"Alkuperäinen lista: {alkuperainen}")
print(f"Karsittu lista (vain parilliset): {karsittu}")


# ==========================================
# Tehtävä 6: Pizzan yksikköhinta (مقارنة أسعار البيتزا per m²)
# ==========================================
# Laskee pizzan neliömetrihinnan ja vertailee kaksi pizzaa


def laske_pizzan_yksikkohinta(halkaisija_cm, hinta_euro):
    # Muunnetaan halkaisija metreiksi ja lasketaan säde
    sade_m = (halkaisija_cm / 2) / 100
    pinta_ala_m2 = math.pi * (sade_m**2)
    return hinta_euro / pinta_ala_m2


# Pääohjelma
print("\n=== Tehtävä 6: Pizzan yksikköhinta ===")
print("Syötä 1. pizzan tiedot:")
halkaisija1 = float(input("  Halkaisija (cm): "))
hinta1 = float(input("  Hinta (€): "))

print("Syötä 2. pizzan tiedot:")
halkaisija2 = float(input("  Halkaisija (cm): "))
hinta2 = float(input("  Hinta (€): "))

yksikkohinta1 = laske_pizzan_yksikkohinta(halkaisija1, hinta1)
yksikkohinta2 = laske_pizzan_yksikkohinta(halkaisija2, hinta2)

print(f"\n1. pizzan yksikköhinta: {yksikkohinta1:.2f} €/m²")
print(f"2. pizzan yksikköhinta: {yksikkohinta2:.2f} €/m²")

if yksikkohinta1 < yksikkohinta2:
    print("Ensimmäinen pizza antaa paremman vastineen rahalle!")
elif yksikkohinta2 < yksikkohinta1:
    print("Toinen pizza antaa paremman vastineen rahalle!")
else:
    print("Molemmat pizzat ovat samanarvoisia vastineeltaan!")