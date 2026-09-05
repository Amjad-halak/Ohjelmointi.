# ==========================================
# Tehtävä 1: Kuhan pituuden tarkistus
# ==========================================
kuhan_pituus = float(input("Anna kuhan pituus senttimetreinä: "))

if kuhan_pituus < 37:
    puuttuu = 37 - kuhan_pituus
    print(f"Laske kuha takaisin järveen, sallitusta pituudesta puuttuu {puuttuu:.1f} cm.")
else:
    print("Kuha on sallitun mittainen, saat pitää sen!")


# ==========================================
# Tehtävä 2: Laivan hyttiluokat (.upper() ja .strip())
# ==========================================
laivan_hyttiluokka = input("Anna laivan hyttiluokka (LUX, A, B, C): ").strip().upper()

if laivan_hyttiluokka == "A":
    kuvaus = "ikkunallinen hytti autokannen yläpuolella."
elif laivan_hyttiluokka == "B":
    kuvaus = "ikkunaton hytti autokannen yläpuolella."
elif laivan_hyttiluokka == "C":
    kuvaus = "ikkunaton hytti autokannen alapuolella."
elif laivan_hyttiluokka == "LUX":
    kuvaus = "parvekkeellinen hytti yläkannella."
else:
    kuvaus = "Virheellinen hyttiluokka."

print(f"Valitsemasi hytti: {kuvaus}")


# ==========================================
# Tehtävä 3: Hemoglobiiniarvon tarkistus
# ==========================================
sukupuoli = input("Mikä on biologinen sukupuolesi (nainen/mies)? ").strip().lower()
hemo = float(input("Mikä on hemoglobiiniarvosi (g/l)? "))

if sukupuoli in ["nainen", "n"]:
    if hemo < 117:
        tulos = "hemoglobiiniarvo on alhainen."
    elif 117 <= hemo <= 175:
        tulos = "hemoglobiiniarvo on normaali."
    else:
        tulos = "hemoglobiiniarvo on korkea."

elif sukupuoli in ["mies", "m"]:
    if hemo < 134:
        tulos = "hemoglobiiniarvo on alhainen."
    elif 134 <= hemo <= 195:
        tulos = "hemoglobiiniarvo on normaali."
    else:
        tulos = "hemoglobiiniarvo on korkea."
else:
    tulos = "Virheellinen sukupuoli."

print(f"Tulos: {tulos}")


# ==========================================
# Tehtävä 4: Karkausvuosi
# ==========================================
vuosiluku = int(input("Anna vuosiluku: "))

if vuosiluku % 400 == 0 or (vuosiluku % 4 == 0 and vuosiluku % 100 != 0):
    print("Vuosi on karkausvuosi.")
else:
    print("Vuosi ei ole karkausvuosi.")