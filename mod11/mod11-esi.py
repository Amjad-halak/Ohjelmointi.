class Henkilo :
    def __init__(self , nimi , ikä , ):
        self.nimi=nimi
        self.ikä=ikä
    

class opiskelija (Henkilo):
    def __init__ (self , nimi , ikä , opiskeljanumero):
        super().__init__(nimi , ikä )
        self.opiskeljanumero = (opiskeljanumero)

    def esittele(self):
        return f"Nimi: {self.nimi}, Ikä: {self.ikä}, Opiskelijanumero: {self.opiskeljanumero}"

    
    # 1. الأب (الجميع لديهم اسم وعمر وياكلون بنفس الطريقة)
class Elain:
    def __init__(self, nimi, ika):
        self.nimi = nimi
        self.ika = ika

    def syo(self):
        return f"{self.nimi} syö ruokaa."

# 2. الابن الأول (الكلب): يرث الاسم والعمر والأكل، ونضيف له "النوع" وصوت "النباح"
class Koira(Elain):
    def __init__(self, nimi, ika, rotu):
        super().__init__(nimi, ika) # يرسل الاسم والعمر للأب Elain
        self.rotu = rotu

    def hauku(self):
        return f"{self.nimi} haukuu: Wuf wuf!"

# 3. الابن الثاني (القطة): ترث الاسم والعمر والأكل، ونضيف لها صوت "المواء"
class Kissa(Elain):
    def haukahda(self): # القطة لم تحتاج حتى لـ __init__ جديدة! أخذت __init__ الأب كما هي!
        return f"{self.nimi} sanoo: Miau!"


# --- التجربة ---
k = Koira("Reksi", 3, "Saksanpaimenkoira")
c = Kissa("Misse", 2)

print(k.syo())     # أخذ دالة الأكل من الأب!
print(k.hauku())   # دالته الخاصة

print(c.syo())     # أخذت دالة الأكل من الأب أيضاً!
        