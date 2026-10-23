#  Rekisteröinti


def rekisteroi_pelaja():
    print("--- REKISTERÖINTI ---")

    nimi = input("Anna nimesi: ")
    if nimi == "":
        nimi = "Agentti"

    ika = int(input("Anna ikäsi: "))

    
    if ika < 12:
        print("Olet alaikäinen. Peli päättyy.")
        return None, None, None, None

    print("\nValitse kokemus:")
    print("1. Alokas")
    print("2. Perus")
    print("3. Kokenut")
    valinta = input("Valitse (1-3): ")

    if valinta == "1":
        kokemus = "Alokas"
    elif valinta == "2":
        kokemus = "Perus"
    else:
        kokemus = "Kokenut"

    kielet = input("Mitä kieltä puhut?: ")
    if kielet == "":
        kielet = "Suomi"

    print("\nTervetuloa peliin, " + nimi + "!")

    return nimi, ika, kokemus, kielet