# ==========================================
# Tehtävä 1 & 2: Hissi- ja Talo-luokat (OOP)
# ==========================================

class Hissi:
    def __init__(self, alin, ylin):
        self.alin = alin
        self.ylin = ylin
        self.Tämänhetkinen_kerros = alin

    def kerros_ylös(self):
        self.Tämänhetkinen_kerros = self.Tämänhetkinen_kerros + 1
        return f"Hissi on nyt kerroksessa {self.Tämänhetkinen_kerros}"

    def kerros_alas(self):
        self.Tämänhetkinen_kerros = self.Tämänhetkinen_kerros - 1
        return f"Hissi on nyt kerroksessa {self.Tämänhetkinen_kerros}"

    def siirry_kerrokseen(self, menevä_kerros):
        # يستمر التكرار حتى يتساوى الطابق الحالي مع الطابق المطلوب
        while self.Tämänhetkinen_kerros != menevä_kerros:
            if menevä_kerros > self.Tämänhetkinen_kerros:
                print(self.kerros_ylös())
            elif menevä_kerros < self.Tämänhetkinen_kerros:
                print(self.kerros_alas())


# --- Pääohjelma ---

hissi = Hissi(1, 10)

print("=== Siirrytään kerrokseen 5 ===")
hissi.siirry_kerrokseen(5)

print("\n=== Siirrytään takaisin alimpaan kerrokseen (1) ===")
hissi.siirry_kerrokseen(1)


class Talo:
    def __init__(self, alin, ylin, hissien_maara):
        self.alin = alin
        self.ylin = ylin
        self.hissit = []
        
        # Luodaan haluttu määrä Hissi-olioita taloon
        for i in range(hissien_maara):
            self.hissit.append(Hissi(alin, ylin))

    def aja_hissia(self, hissin_numero, kohde):
        # Valitaan tietty hissi indeksin perusteella ja siirretään se
        hissi = self.hissit[hissin_numero]
        hissi.siirry_kerrokseen(kohde)


# ==========================================
# Pääohjelma
# ==========================================

print("--- Testataan Hissi ---")
h = Hissi(1, 7)
h.siirry_kerrokseen(5)
h.siirry_kerrokseen(1)

print("\n--- Testataan Talo ---")
talo = Talo(1, 10, 3)
talo.aja_hissia(0, 5)