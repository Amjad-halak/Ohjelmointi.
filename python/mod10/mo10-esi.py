# ==========================================
# MODUULI: OLIOIDEN VÄLISET SUHTEET (ASSOCIATION)
# ==========================================
# 💡 المفاهيم الأساسية:
# Association (العلاقة العامة) تنقسم إلى:
# 1. Composition (التركيب): كائن ينشأ داخل كائن آخر.
#    (مثال: Person وتاريخ ميلاده Date). إذا حذفنا الشخص يختفي تاريخ ميلاده معه.
# 2. Aggregation (التجميع): كائنات مستقلة يتم تجميعها معاً.
#    (مثال: Library والكتب Kirja). إذا أغلقت المكتبة تبقى الكتب موجودة.


# ==========================================
# Esimerkki 1: Composition (التركيب)
# ==========================================

class Date:
    def __init__(self):
        self.day = 0
        self.month = 0
        self.year = 0

    def set_date(self):
        self.day = int(input("Enter day (1-31): "))
        self.month = int(input("Enter month (1-12): "))
        self.year = int(input("Enter year (e.g. 1998): "))

    def get_date(self):
        return f"{self.day}/{self.month}/{self.year}"


class Person:
    def __init__(self):
        self.fname = None
        self.lname = None
        self.name = None
        self.address = None
        self.phone = 0
        self.dob = Date()  # Composition: كائن Date يتكون بالكامل داخل كائن Person

    def set_per(self):
        self.fname = input("Enter your first name: ")
        self.lname = input("Enter your last name: ")
        self.name = f"{self.fname} {self.lname}"
        self.address = input("Enter your full address: ")
        self.phone = float(input("Enter your number: "))
        print("--- Enter Date of Birth ---")
        self.dob.set_date()  # استدعاء دالة تعبئة التاريخ

    def get_per(self):
        print(f"First name: {self.fname}")
        print(f"Last name: {self.lname}")
        print(f"Full name: {self.name}")
        print(f"Phone num: {self.phone}")
        print(f"Address: {self.address}")
        print(f"Date of birth: {self.dob.get_date()}")  # إظهار تاريخ الميلاد المخزن

    def first(self):
        return self.fname

    def last(self):
        return self.lname


class Employee:
    def __init__(self):
        self.id = 0
        self.salary = 0.0
        self.email = None

    def set_emp(self):
        self.email = input("Enter your email address: ")
        self.salary = float(input("Enter your monthly salary: "))
        self.id = float(input("Enter your id number: "))

    def get_emp(self):
        print(f"Email: {self.email}")
        print(f"Salary: {self.salary}")
        print(f"ID: {self.id}")


# --- الجزء التنفيذي للمثال الأول ---
p1 = Person()
p1.set_per()

emp1 = Employee()
emp1.set_emp()

dat1 = Date()
dat1.set_date()

print("\n--- Person details ---")
p1.get_per()

print("\n--- Employee details ---")
emp1.get_emp()

print("\n--- Date details ---")
print(dat1.get_date())


# 💡 فوائد استخدام Composition:
# 1. إعادة استخدام الكود وعدم التكرار (Reusability):
#    بدلاً من إعادة كتابة متغيرات اليوم والشهر والسنة ودوال إدخالها وطباعتها، نكتب Date مرة واحدة فقط ونستعملها مجدداً.
# 2. تقسيم الكود وتنظيمه (Modular & Clean Code):
#    كلاس Date مسؤول عن التواريخ، وكلاس Person مسؤول عن بيانات الشخص.
# 3. التحكم الكامل في ملكية ودورة حياة الكائن (Lifecycle Ownership):
#    الـ Composition تضمن أن كائن التاريخ مرتبط وجودياً بكائن الشخص ويحذف معه.


# ==========================================
# Esimerkki 2: Aggregation - Koira ja Hoitola (التجميع)
# ==========================================

class Koira:
    def __init__(self, nimi, rotu):
        self.nimi = nimi
        self.rotu = rotu

    def hauku(self):
        return f"Koira {self.nimi} haukuu!"


class KoiraHoitola:
    def __init__(self, nimi):
        self.nimi = nimi
        self.koirat = []  # تجميع لكائنات Koira مستقلة

    def lisaa_koira(self, koira):
        self.koirat.append(koira)

    def kuuntele_hauku(self):
        for k in self.koirat:
            print(k.hauku())


# --- التجربة والتطبيق ---
print("\n=== Koitola Testi ===")
k1 = Koira("shbshb", "Golden Retriever")
k2 = Koira("Reksi", "Poodle")

hoitola = KoiraHoitola("Musti ja Mirri")

# إضافة الكلاب
hoitola.lisaa_koira(k1)
hoitola.lisaa_koira(k2)

# سماع الأصوات
hoitola.kuuntele_hauku()


# ==========================================
# Esimerkki 3: Aggregation - Kirja ja Kirjasto (التجميع)
# ==========================================

class Kirja:
    def __init__(self, nimi, kirjailija):
        self.nimi = nimi
        self.kirjailija = kirjailija

    def hae_tiedot(self):
        return f"Kirja: {self.nimi}, Kirjailija: {self.kirjailija}"


class Kirjasto:
    def __init__(self, nimi):
        self.nimi = nimi
        self.kirjat = []  # قائمة لتجميع الكتب

    def lisaa_kirja(self, kirja):
        self.kirjat.append(kirja)

    def tulosta_kirjat(self):
        print(f"\nKirjaston ({self.nimi}) kirjat:")
        for kirja in self.kirjat:   
            print(f"- {kirja.hae_tiedot()}")


# --- التجربة والتطبيق ---
ki1 = Kirja("Kyberturvallisuus", "Antti")
ki2 = Kirja("Rich Dad Poor Dad", "Robert Kiyosaki")

kirjasto = Kirjasto("Keskustakirjasto Oodi!")

kirjasto.lisaa_kirja(ki1)
kirjasto.lisaa_kirja(ki2)
kirjasto.tulosta_kirjat()