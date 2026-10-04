# --- 1.
class Auto:
    def __init__(self, rekisteri, huippunopeus):
        self.rekisteri = rekisteri
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0

    def kiihdyta(self, muutos):
        self.nopeus = self.nopeus + muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0


# --- Pääohjelma 
auto = Auto("ABC-123", 142)

print("Rekisteri:", auto.rekisteri)
print("Huippunopeus:", auto.huippunopeus, "km/h")
print("Nopeus:", auto.nopeus, "km/h")
print("Matka:", auto.matka, "km")

print("--- Kiihdytys ---")
auto.kiihdyta(30)
auto.kiihdyta(70)
auto.kiihdyta(50)
print("Nopeus kiihdytyksen jälkeen:", auto.nopeus, "km/h")

auto.kiihdyta(-200)
print("Nopeus jarrutuksen jälkeen:", auto.nopeus, "km/h")