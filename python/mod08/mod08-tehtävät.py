# ==========================================
# Tehtävä 1: Kuukauden vuodenaika (Monikko / Tuple)
# ==========================================
vuodenajat = ("Talvi", "Talvi", "Kevät", "Kevät", "Kevät", "Kesä", "Kesä", "Kesä", "Syksy", "Syksy", "Syksy", "Talvi")

kuukausi = int(input("Syötä kuukauden numero (1-12): "))

if 1 <= kuukausi <= 12:
    print(f"Vuodenaika on: {vuodenajat[kuukausi - 1]}")
else:
    print("Virheellinen kuukauden numero!")


# ==========================================
# Tehtävä 2: Lentoasemat (Sanakirja / Dictionary)
# ==========================================
lentoasemat = {}

while True:
    valinta = input("\nValitse toiminto (1 = Uusi lentoasema, 2 = Hae lentoasema, 3 = Lopeta): ").strip()
    
    if valinta == "1":
        icao = input("Syötä ICAO-koodi: ").strip().upper()
        nimi = input("Syötä lentoaseman nimi: ").strip()
        lentoasemat[icao] = nimi
        print(f"Lentoasema {nimi} ({icao}) lisätty.")
        
    elif valinta == "2":
        icao = input("Syötä haettava ICAO-koodi: ").strip().upper()
        if icao in lentoasemat:
            print(f"Lentoasema: {lentoasemat[icao]}")
        else:
            print("Lentoasemaa ei löytynyt.")
            
    elif valinta == "3":
        print("Ohjelma lopetetaan. Näkemiin!")
        break
        
    else:
        print("Tuntematon valinta, yritä uudelleen.")