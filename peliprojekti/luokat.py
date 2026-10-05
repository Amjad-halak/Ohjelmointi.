# luokat.py


class Item:

    def __init__(self, nimi, kuvaus):
        self.nimi = nimi
        self.kuvaus = kuvaus


class Player:

    def __init__(self, nimi, ika, kokemus, kielet):
        self.nimi = nimi
        self.ika = ika
        self.kokemus = kokemus
        self.kielet = kielet
        self.reppu = []
        self.pisteet = 0
        

    def ota_esine(self, esine):
        self.reppu.append(esine)
        print("\n[+] Sait esineen: " + esine.nimi)

    def nayta_reppu(self):
        print("\n--- REPPUSI ---")
        if not self.reppu:
            print("Reppusi on tyhjä.")
        else:
            for esine in self.reppu:
                print("- " + esine.nimi + ": " + esine.kuvaus)