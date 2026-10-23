# ==========================================
# MODUULI: PERIYTYS (INHERITANCE)
# ==========================================
# 💡 مفهوم الوراثة (Inheritance):
# - الكلاس الأب (Base/Parent class): يحوي الخصائص والدوال المشتركة.
# - الكلاس الابن (Derived/Child class): يرث كل شيء من الأب، ويستطيع إضافة خصائص ودوال خاصة به.
# - الدالة super().__init__() تستدعى لإرسال البيانات للأب لتهيتها.


# ==========================================
# Esimerkki 1: Henkilö ja Opiskelija
# ==========================================

class Henkilo:
    def __init__(self, nimi, ika):
        self.nimi = nimi
        self.ika = ika


class Opiskelija(Henkilo):
    def __init__(self, nimi, ika, opiskelijanumero):
        # يستدعي __init__ الأب Henkilo لضبط الاسم والعمر
        super().__init__(nimi, ika)
        self.opiskelijanumero = opiskelijanumero

    def esittele(self):
        return f"Nimi: {self.nimi}, Ikä: {self.ika}, Opiskelijanumero: {self.opiskelijanumero}"


# تجربة المثال الأول
o1 = Opiskelija("Amjad", 23, "123456")
print(o1.esittele())
print("-" * 30)


# ==========================================
# Esimerkki 2: Eläin, Koira ja Kissa
# ==========================================

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
        super().__init__(nimi, ika)  # يرسل الاسم والعمر للأب Elain
        self.rotu = rotu

    def hauku(self):
        return f"{self.nimi} haukuu: Wuf wuf!"


# 3. الابن الثاني (القطة): ترث الاسم والعمر والأكل، ونضيف لها صوت "المواء"
class Kissa(Elain):
    def mauku(self):  # القطة لم تحتاج حتى لـ __init__ جديدة! أخذت __init__ الأب كما هي!
        return f"{self.nimi} sanoo: Miau!"


# --- التجربة والتطبيق ---
k = Koira("Reksi", 3, "Saksanpaimenkoira")
c = Kissa("Misse", 2)

print(k.syo())     # أخذ دالة الأكل من الأب!
print(k.hauku())   # دالته الخاصة

print(c.syo())     # أخذت دالة الأكل من الأب أيضاً!
print(c.mauku())   # دالتها الخاصة