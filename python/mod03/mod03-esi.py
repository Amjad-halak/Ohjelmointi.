import math

# ==========================================
# Esimerkki 0: Merkkijonojen yhdistäminen (String concatenation)
# ==========================================
# Muunnetaan luvut tekstiksi vanhalla str()-funktiolla
luku1 = float(input("Anna 1. luku: "))
luku2 = float(input("Anna 2. luku: "))

summa = luku1 + luku2

print("Lukujen " + str(luku1) + " ja " + str(luku2) + " summa on " + str(summa) + ".")


# ==========================================
# Esimerkki 1: f-string muotoilu (Uusi ja parempi tapa)
# ==========================================
# Moderni ja selkeä tapa muotoilla merkkijonoja f-stringin ja aaltosulkeiden {} avulla
ika = 22
uusi_kayttaja = input("Anna nimesi: ")

print(f"Hauska tavata {uusi_kayttaja} ja ikäni on {ika}!!!!!")


# ==========================================
# Esimerkki 2: Muuttujatyypit (Data types)
# ==========================================
# Pythonin perustietotyypit ja muuttujatyyppien tarkistaminen
pisteet = 200
pisteet = 400  # Muuttujan arvo voidaan ylikirjoittaa

merkkijono = "Ulla"  # Merkkijono (str)
kokonaisluku = -9  # Kokonaisluku (int)
kokonaisluku_pitka = 12_456_123_180  # Alaviivaa voidaan käyttää tuhansien erottimena
liukuluku = 4.973  # Desimaaliluku / Liukuluku (float)
kompleksiluku = -4 + 2j  # Kompleksiluku (complex)
totuusarvo = False  # Totuusarvo (bool)

# Kompleksiluvun reaaliosa ja kuvitteellinen osa
print(f"Reaali-osa: {kompleksiluku.real}")
print(f"Kuvitteellinen osa: {kompleksiluku.imag}")

# type()-funktio kertoo muuttujan tyypin
print(f"Muuttujan tyyppi voidaan tutkia: {type(kompleksiluku)}")


# ==========================================
# Esimerkki 3: Tulostuksen muotoilu ja tasaus (Formatting)
# ==========================================
# Tekstin tasaus ja desimaalien määrän muotoilu
# <20s varaa 20 merkkiä tilaa ja tasaa tekstin vasemmalle
print(f"Merkkijono: {merkkijono:<20s} sijoitetaan tähän väliin")

print(f"{'Vakio':6s}| {'Arvo':6s}")
print("-------------")
# :<6.2f tulostaa liukuluvun kahden desimaalin tarkkuudella vasemmalle tasattuna
print(f"{'Pii':6s}: {math.pi:<6.2f}")


# ==========================================
# Esimerkki 4: Laskukone ja peruslaskutoimitukset (Calculator)
# ==========================================
# Kaikki perus- ja edistyneemmät laskutoimitukset
tuloste = """
    yhteenlasku (+)
    vähennyslasku (-)
    kertolasku (*)
    jakolasku (/)
    jakojäännösoperaatio (%)
    pelkän kokonaisosan palauttava jakolasku (//) 
    potenssiinkorotus (**)
"""
print(tuloste)

# Luetaan käyttäjältä kaksi lukua
a = float(input("Anna ensimmäinen luku:\n"))
b = float(input("Anna toinen luku:\n"))

# Laskutoimitukset
yhteenlasku = a + b
vahennyslasku = a - b
kertolasku = a * b
jakolasku = a / b
jakojaannos = a % b  # Modulus (jakojäännös)
kokonaisosa = a // b  # Floor division (kokonaisosa)
potenssiinkorotus = a**b  # Potenssi

print(f"Yhteenlasku: {yhteenlasku}")
print(f"Vähennyslasku: {vahennyslasku}")
print(f"Kertolasku: {kertolasku}")
print(f"Potenssinkorotus: {potenssiinkorotus}")
print(f"Jakolasku: {jakolasku}")
print(f"Kokonaisosa: {kokonaisosa}")
print(f"Jakojäännös: {jakojaannos}")