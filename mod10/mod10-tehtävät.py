# --- 1
class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.kerros = alin

    def kerros_ylos(self):
        self.kerros = self.kerros + 1
        print("Hissi on kerroksessa:", self.kerros)

    def kerros_alas(self):
        self.kerros = self.kerros - 1
        print("Hissi on kerroksessa:", self.kerros)

    def siirry_kerrokseen(self, kohde):
        while self.kerros < kohde:
            self.kerros_ylos()
        while self.kerros > kohde:
            self.kerros_alas()


# --- 2
class Talo:
    def __init__(self, alin, ylin, hissien_maara):
        self.alin = alin
        self.ylin = ylin
        self.hissit = []
        for i in range(hissien_maara):
            self.hissit.append(Hissi(alin, ylin))

    def aja_hissia(self, hissin_numero, kohde):
        hissi = self.hissit[hissin_numero]
        hissi.siirry_kerrokseen(kohde)


# --- Pääohjelma 
print("--- Testataan Hissi ---")
h = Hissi(1, 7)
h.siirry_kerrokseen(5)
h.siirry_kerrokseen(1)

print("\n--- Testataan Talo ---")
talo = Talo(1, 10, 3)
talo.aja_hissia(0, 5)  