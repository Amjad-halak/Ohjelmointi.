# Kysytään pelaajan nimi ja ikä
nimi = input("Anna nimesi: ")
ikä = int(input("Anna ikäsi: "))

# Tulostetaan tiedot konsoliin
print("Pelaajan nimi:", nimi)
print("Pelaajan ikä:", ikä)

ohje = "Tämä on peli. Kirjoita komentoja jatkaaksesi."
pisteet = "Sinulla on 0 pistettä."

# Tarkistetaan ikä
if ikä < 12:
    print("Olet alaikäinen. Ohjelma suljetaan.")
else:
    print("Tervetuloa kyytiin!")
    
    # Aloitetaan komentosilmukka
    komento = ""
    while komento != "lopeta":
        print("\n--- PÄÄVALIKKO ---")
        print("Komennot: ohje, pisteet, lopeta")
        komento = input("Anna komento: ")
        
        if komento == "ohje":
            print(f"Ohje: {ohje}")
        elif komento == "pisteet":
            print(f"Pisteet: {pisteet}")
        elif komento == "lopeta":
            print("Ohjelma sammuu. Hei hei!")
        else:
            print("Tuntematon komento, yritä uudelleen.")