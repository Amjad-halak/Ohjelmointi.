import random

# ==========================================
# Esimerkki 0: Bulean-arvo (Boolean: True / False)
# ==========================================
onko_totta = False

# Jos onko_totta on True, koodi suoritetaan. Jos False, hypätään yli.
if onko_totta:
    print("Onhan se totta!")


# ==========================================
# Esimerkki 1: Kolikonheitto (Satunnaisluku randint 0 tai 1)
# ==========================================
# Arvotaan kokonaisluku: 0 tai 1
random_number = random.randint(0, 1)
print(f"Arvottu numero: {random_number}")

# if-ehto tarkistaa onko numero 0
if random_number == 0:
    result = "kruuna"
    print("kruuna tuli")
else:
    result = "klaava"

print(f"Heitit kolikkoa ja sait {result}n.")


# ==========================================
# Esimerkki 2: Kolikonheitto 2.0 (Liukuluku random.random & if-elif-else)
# ==========================================
# random.random() antaa desimaaliluvun väliltä 0.0 - 1.0
random_number = random.random()
print(f"Desimaaliluku: {random_number:.4f}")

# Tarkistetaan todennäköisyydet järjestyksessä
if random_number < 0.01:
    print("Kolikko jäi pystyyn")  # 1% mahdollisuus
elif random_number < 0.505:
    print("Kruuna tuli.")  # Noin 49.5% mahdollisuus
else:
    print("Klaava tuli")  # Loput mahdollisuudet


# ==========================================
# Esimerkki 3: Numerovälin tarkistus ja ehdot (Vertailut)
# ==========================================
arvo = 150
# Tarkistetaan onko arvo välillä 90-110 (Antaa False)
print(90 < arvo < 110)
# Tarkistetaan ovatko luvut erisuuria (Antaa True)
print(100 != 101)


# ==========================================
# Esimerkki 4: Lääke-esimerkki (Sisäkkäiset ehdot & and/or)
# ==========================================
ikä = int(input("Anna ikä: "))

# Kysytään painoa VAIN jos ikä on välillä 15-17
if 15 <= ikä < 18:
    paino = float(input("Anna paino (kg): "))

# Ehto: Pääsee jos on yli 18 TAI (vähintään 15 JA painaa vähintään 55kg)
if ikä >= 18 or (ikä >= 15 and paino >= 55):
    print("Lääkkeen käyttö on sallittua.")


# ==========================================
# Esimerkki 5: Satunnainen desimaaliluku (random.uniform)
# ==========================================
# random.uniform arpoo desimaaliluvun tietyltä väliltä
random_number_2 = random.uniform(-1.02, 1.34)
print(f"Satunnainen desimaali: {random_number_2:.2f}")

if random_number_2 >= 0:
    result1 = "biger"
else:
    result1 = "lower"

print(f"Tulos on: {result1}")


# ==========================================
# Esimerkki 6: Ajokorttitarkistus (Sisäkkäinen if-lause)
# ==========================================
ikä = int(input("Mikä sun ikäsi on? "))

if ikä >= 18:
    x = "you pass and could get drivinglicense ."
else:
    # Jos ikä on alle 18, kysytään pituus
    y = float(input("Enter your real tall (cm)!! "))
    if y >= 180:
        x = "you could have drivinglicense ."
    else:
        x = "you couldnt have drivinglicense "

print(f"Sun oikei tulos on: {x}\nReach us on our platform")


# ==========================================
# Esimerkki 7: Looginen AND ja .upper() -metodi
# ==========================================
temp = float(input("enter your region temp now:: "))
# .upper() muuttaa syötteen aina isoksi kirjaimeksi ("y" -> "Y")
sunny = input("is it sunny outside (Y/N): ").upper()

# Molempien ehtojen pitää olla True (Lämpötila > 15 JA sunny == "Y")
if temp > 15 and sunny == "Y":
    x = "go to swim"
else:
    x = "the temp is bad stay home"

print(f"The temp situation is: {x}")


# ==========================================
# Esimerkki 8: Looginen OR (Jompaakumpaa ehtoa riittää)
# ==========================================
temp = float(input("enter your region temp now:: "))

# Ehto toteutuu jos lämpötila on 0 tai alle TAI 30 tai yli
if temp <= 0 or temp >= 30:
    x = "the temp is bad"
else:
    x = "the temp is good"

print(f"The temp situation is: {x}")


# ==========================================
# Esimerkki 9: Bulean-muuttujan käyttö ehtolauseessa
# ==========================================
sunny = True

# Jos sunny on True, suoritetaan ensimmäinen lohko
if sunny:
    x = "it is sunny outside"
else:
    x = "not sunny outside so its cloudy"

print(f"The situation is: {x}")