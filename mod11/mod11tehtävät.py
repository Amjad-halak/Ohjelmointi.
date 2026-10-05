# --- 1. 
class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi


# --- 2. 
class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        print("Kirja:", self.nimi)
        print("Kirjailija:", self.kirjoittaja)
        print("Sivuja:", self.sivumaara)


# --- 3.
class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja = paatoimittaja

    def tulosta_tiedot(self):
        print("Lehti:", self.nimi)
        print("Päätoimittaja:", self.paatoimittaja)


# --- Pääohjelma 
lehti = Lehti("Aku Ankka", "Aki Hyyppä")
kirja = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

lehti.tulosta_tiedot()
print("---")
kirja.tulosta_tiedot()