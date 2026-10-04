#. 1

vuodenajat = ("Talvi", "Talvi", "Kevät", "Kevät", "Kevät", "Kesä", "Kesä", "Kesä", "Syksy", "Syksy", "Syksy", "Talvi")

kk = int(input("Syötä kuukauden numero (1-12): "))
print("Vuodenaika on:", vuodenajat[kk - 1])

#. 2

lentoasemat = {}

while True:
    valinta = input("1 = Uusi, 2 = Hae, 3 = Lopeta: ")
    if valinta == "1":
        icao = input("Syötä ICAO-koodi: ")
        nimi = input("Syötä nimi: ")
        lentoasemat[icao] = nimi
    elif valinta == "2":
        icao = input("Syötä ICAO-koodi: ")
        if icao in lentoasemat:
            print("Lentoasema:", lentoasemat[icao])
        else:
            print("Ei löydy.")
    elif valinta == "3":
        break

    