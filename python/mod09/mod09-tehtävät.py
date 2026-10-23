import random

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus): 
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.tämänhetkinennopeus = 0
        self.kuljettumatka = 0

    def kiihdytä(self, nopeuden_muutos):
        self.tämänhetkinennopeus = nopeuden_muutos + self.tämänhetkinennopeus 
        if self.tämänhetkinennopeus > self.huippunopeus:
            self.tämänhetkinennopeus = self.huippunopeus
        elif self.tämänhetkinennopeus < 0:
            self.tämänhetkinennopeus = 0

    def kulje(self, tuntimäärä):
        self.kuljettumatka = self.kuljettumatka + (self.tämänhetkinennopeus * tuntimäärä)


# --- Pääohjelma ---

# 1. Luodaan autot-lista
autot = []
for i in range(1, 11):
    huippo = random.randint(100, 200)
    uusi_auto = Auto(f"ABC-{i}", huippo)
    autot.append(uusi_auto)

# 2. Kilpailu-silmukka
kilpailu_käynnissä = True

while kilpailu_käynnissä:
    for auto in autot:
        nopeus = random.randint(-10, 15)
        auto.kiihdytä(nopeus)
        auto.kulje(1)
        
        # Tarkistetaan onko jokin auto saavuttanut 10 000 km
        if auto.kuljettumatka >= 10000:
            kilpailu_käynnissä = False

# 3. Tulostetaan tulokset taulukossa
print(f"{'Rekisteri':<10} | {'Huippunopeus':<12} | {'Nopeus':<12} | {'Matka':<12}")
print("-" * 55)

for auto in autot:
    print(f"{auto.rekisteritunnus:<10} | {auto.huippunopeus:<9} km/h | {auto.tämänhetkinennopeus:<9} km/h | {auto.kuljettumatka:<9} km")



#toinen esimerkki 

class Kirja :
    def __init__(self , nimi , kirjaillija  ,sivumaara):
        self.nimi=nimi
        self.kirjaillija=kirjaillija
        self.sivumaara=sivumaara
        self.sivu=0
        self.luettu=False

    def lue (self):
        self.luettu=True

    def lue_sivuja (self , sivut ) : 
        
        self.sivu = sivut + self.sivu

        if self.sivu >= self.sivumaara :
            self.luettu = True 
            print("olet lukenut koko kirjan ! ")
        

    def tulostus(self):
        print(f"kirjan tiedot nimi ({self.nimi}) kirjoitaja ({self.kirjaillija}) sivun määrä ({self.sivu}) luoettu tai ei ({self.luettu})")


class E_kirja(Kirja) :
    def __init__ (self , nimi , kirjaillija  ,sivumaara ,tiedostokoko  ):
        super().__init__(nimi , kirjaillija  ,sivumaara)
        self.tiedostokoko=tiedostokoko
    def lataa (self):
        return f"ladataan kirja {self.nimi} , koko {self.tiedostokoko}"



kirja1=Kirja( "kyper" , "osuma" , 100 )

print("-" * 100)
kirja1.lue_sivuja(50)
kirja1.tulostus()


print("-" * 50)
# إنشاء كائن من الكلاس الابن (E_kirja)
e_kirja1 = E_kirja("Python Guide", "Matti", 200, 15)
e_kirja1.lataa()        # استخدام دالة الابن
e_kirja1.lue_sivuja(50) # استخدام دالة ورثها من الأب!
e_kirja1.tulostus()


#TOINEN ESIMERRKI JOKA LIITY SAMAN IDEA ! 

class Kirja :
    def __init__(self , nimi , kirjaillija  ,sivumaara):
        self.nimi=nimi
        self.kirjaillija=kirjaillija
        self.sivumaara=sivumaara
        self.sivu=0
        self.luettu=False

    def lue (self):
        self.luettu=True

    def lue_sivuja (self , sivut ) : 
        
        self.sivu = sivut + self.sivu

        if self.sivu >= self.sivumaara :
            self.luettu = True 
            print("olet lukenut koko kirjan ! ")
        

    def tulostus(self):
        print(f"kirjan tiedot nimi ({self.nimi}) kirjoitaja ({self.kirjaillija}) sivun määrä ({self.sivu}) luoettu tai ei ({self.luettu})")


class E_kirja(Kirja) :
    def __init__ (self , nimi , kirjaillija  ,sivumaara ,tiedostokoko  ):
        super().__init__(nimi , kirjaillija  ,sivumaara)
        self.tiedostokoko=tiedostokoko
    def lataa (self):
        return f"ladataan kirja {self.nimi} , koko {self.tiedostokoko}"



kirja1=Kirja( "kyper" , "osuma" , 100 )

print("-" * 100)
kirja1.lue_sivuja(50)
kirja1.tulostus()


print("-" * 50)
# إنشاء كائن من الكلاس الابن (E_kirja)
e_kirja1 = E_kirja("Python Guide", "Matti", 200, 15)
e_kirja1.lataa()        # استخدام دالة الابن
e_kirja1.lue_sivuja(50) # استخدام دالة ورثها من الأب!
e_kirja1.tulostus()