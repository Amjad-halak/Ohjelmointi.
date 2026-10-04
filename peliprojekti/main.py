# main.py - Pelin pääohjelma
from luokat import Item, Player
from rekisterointi import rekisteroi_pelaja


def lue_ohjeet():
    print("\n---------------------------------")
    print("PELIN OHJEET:")
    print("1. Valitse ensin alue valikosta.")
    print("2. Suorita tehtävä alueella.")
    print("3. Kerää pisteitä ja esineitä.")
    print("4. Muista tallentaa peli lopuksi.")
    print("---------------------------------")
    try:
        tiedosto = open("ohjeet.txt", "r", encoding="utf-8")
        print(tiedosto.read())
        tiedosto.close()
    except FileNotFoundError:
        print("Lue lisätietoja ohjeet.txt tiedostosta.")


def valitse_alue():
    print("\n--- VALITSE PALVELUSALUE ---")
    print("1. Lähi-itä")
    print("2. Afrikka")
    print("3. Eurooppa")

    valinta = input("Valitse numero (1-3): ").strip()

    if valinta == "1":
        print("Valitsit alueen: Lähi-itä")
        return "Lähi-itä"
    elif valinta == "2":
        print("Valitsit alueen: Afrikka")
        return "Afrikka"
    elif valinta == "3":
        print("Valitsit alueen: Eurooppa")
        return "Eurooppa"
    else:
        print("Virheellinen valinta, valitaan Lähi-itä.")
        return "Lähi-itä"


def tehtava_lahi_ita(pelaaja):
    print("\n--- TEHTÄVÄ: LÄHI-ITÄ ---")
    print("1. Neuvottele rauhansopimus")
    print("2. Jaa humanitaarista apua")

    valinta = input("Valitse toiminto (1-2): ").strip()

    if valinta == "1":
        print("\nNeuvottelu onnistui hienosti!")
        pelaaja.pisteet = pelaaja.pisteet + 20
        pelaaja.ota_esine(Item("Rauhansopimus", "Virallinen asiakirja"))
    elif valinta == "2":
        print("\nHumanitaarinen apu toimitettiin perille!")
        pelaaja.pisteet = pelaaja.pisteet + 10
        pelaaja.ota_esine(Item("Lääkepakkaus", "Ensiaputarvikkeita"))
    else:
        print("\nEt tehnyt mitään tehtävää.")


def tehtava_afrikka(pelaaja):
    print("\n--- TEHTÄVÄ: AFRIKKA ---")
    print("1. Suojaa siviilejä")
    print("2. Rakenna vesipiste")

    valinta = input("Valitse toiminto (1-2): ").strip()

    if valinta == "1":
        print("\nAlue on nyt turvallinen!")
        pelaaja.pisteet = pelaaja.pisteet + 15
        pelaaja.ota_esine(Item("Turvakortti", "Pääsy turva-alueelle"))
    elif valinta == "2":
        print("\nVesipiste valmis ja kyläläiset ovat iloisia!")
        pelaaja.pisteet = pelaaja.pisteet + 15
        pelaaja.ota_esine(Item("Vesisäiliö", "Puhdasta vettä"))
    else:
        print("\nEt tehnyt mitään tehtävää.")


def tehtava_eurooppa(pelaaja):
    print("\n--- TEHTÄVÄ: EUROOPPA ---")
    print("1. Järjestä kokous")
    print("2. Kirjoita raportti")

    valinta = input("Valitse toiminto (1-2): ").strip()

    if valinta == "1":
        print("\nKokous sujui hyvin!")
        pelaaja.pisteet = pelaaja.pisteet + 10
        pelaaja.ota_esine(Item("Muistio", "Kokouksen pöytäkirja"))
    elif valinta == "2":
        print("\nRaportti lähetettiin päämajaan!")
        pelaaja.pisteet = pelaaja.pisteet + 10
        pelaaja.ota_esine(Item("Raportti", "YK-tilannekatsaus"))
    else:
        print("\nEt tehnyt mitään tehtävää.")


def suorita_tehtava(pelaaja, alue):
    if alue == "Lähi-itä":
        tehtava_lahi_ita(pelaaja)
    elif alue == "Afrikka":
        tehtava_afrikka(pelaaja)
    elif alue == "Eurooppa":
        tehtava_eurooppa(pelaaja)
    else:
        print("\nEi valittua aluetta.")


def tallenna_peli(pelaaja, alue):
    tiedosto = open("tallennus.txt", "w", encoding="utf-8")
    teksti = pelaaja.nimi + "," + str(pelaaja.pisteet) + "," + alue + "\n"
    tiedosto.write(teksti)
    tiedosto.close()
    print("\nPeli tallennettu tiedostoon tallennus.txt!")


def nayta_pelin_tila(pelaaja, alue):
    print("\n---------------------------------")
    print("AGENTTI: " + pelaaja.nimi)
    print("ALUE: " + alue)
    print("PISTEET: " + str(pelaaja.pisteet))
    print("---------------------------------")


def main():
    print("Tervetuloa YK-seikkailupeliin!")

    nimi, ika, kokemus, kielet = rekisteroi_pelaja()
    pelaaja = Player(nimi, ika, kokemus, kielet)

    pelaaja.ota_esine(Item("YK-Passi", "Henkilökortti"))

    valittu_alue = "Ei valittu"

    while True:
        nayta_pelin_tila(pelaaja, valittu_alue)

        print("1. Lue ohjeet")
        print("2. Näytä reppu")
        print("3. Valitse alue")
        print("4. Suorita tehtävä")
        print("5. Tallenna peli")
        print("6. Lopeta peli")

        valinta = input("\nValitse toiminto (1-6): ").strip()

        if valinta == "1":
            lue_ohjeet()
        elif valinta == "2":
            pelaaja.nayta_reppu()
        elif valinta == "3":
            valittu_alue = valitse_alue()
        elif valinta == "4":
            if valittu_alue == "Ei valittu":
                print("\n[!] Valitse ensin alue kohdasta 3!")
            else:
                suorita_tehtava(pelaaja, valittu_alue)
        elif valinta == "5":
            tallenna_peli(pelaaja, valittu_alue)
        elif valinta == "6":
            print("\nKiitos pelaamisesta! Näkemiin.")
            break
        else:
            print("\nVirheellinen valinta, yritä uudelleen.")


if __name__ == "__main__":
    main()