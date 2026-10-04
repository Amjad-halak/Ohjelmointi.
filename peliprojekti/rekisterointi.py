# rekisterointi.py - Rekisterointi ja ikatarkistus
import sys


def tarkista_ika(ika):
    if ika < 12:
        return False
    return True


def rekisteroi_pelaja():
    print("--- YK-AGENTIN REKISTERÖINTI ---")

    # 1. Nimi
    nimi = input("Syötä nimisi: ").strip()
    while nimi == "":
        print("Nimi ei voi olla tyhjä!")
        nimi = input("Syötä nimisi: ").strip()

    # 2. Ikä
    while True:
        try:
            ika = int(input("Syötä ikäsi: "))
            break
        except ValueError:
            print("Syötä ikä numerona!")

    # Ikätarkistus K12
    if not tarkista_ika(ika):
        print("\nOlet alaikäinen (alle 12v). Peli suljetaan.")
        sys.exit()

    # 3. Kokemus
    print("\nValitse kokemus valvontaja tehtävään :")
    print("1. Alokas")
    print("2. Kokenut")
    print("3. Veteraani")
    valinta = input("Valitse (1-3): ").strip()

    if valinta == "2":
        kokemus = "Kokenut"
    elif valinta == "3":
        kokemus = "Veteraani"
    else:
        kokemus = "Alokas"

    # 4. Kielet
    kielet = input("Mitä kieliä puhut?: ").strip()
    if kielet == "":
        kielet = "Suomi"

    # Kortin tulostus
    print("\n--- HENKILÖKORTTI ---")
    print("Nimi: " + nimi)
    print("Ikä: " + str(ika))
    print("Kokemus: " + kokemus)
    print("Kielet: " + kielet)
    print("--------------------\n")

    return nimi, ika, kokemus, kielet