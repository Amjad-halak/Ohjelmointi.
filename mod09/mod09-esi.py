# ==========================================
# MODUULI 1: OLIO-OHJELMOINNIN PERUSTEET (OOP)
# ==========================================
# 💡 مفهوم عام لأمجد المستقبلي:
# - الكلاس (Class) هو "المخطط/الفيلا على الورق" (Blueprint).
# - الأوبجكت (Olio / Object) هو "البيت الحقيقي المبني" في الذاكرة.
# - الدالة __init__ هي "المنشئ/التهيئة" (Constructor) لتجهيز البيانات عند بناء الأوبجكت.
# - كلمة self ضرورية جداً داخل الكلاس، وتعني "هذا الأوبجكت المحدّد حالياً".


# ==========================================
# Esimerkki 0: أسهل مثال ممكن (Perusluokka)
# ==========================================
# كلاس بسيط جداً يحتوي على متغيرات فقط لطلب وبناء أوبجكت أساسي
class Koira:
    def __init__(self, nimi, ika):
        self.nimi = nimi
        self.ika = ika

# إنشاء أوبجكت وطباعة البيانات مباشرة
koira1 = Koira("Rekku", 3)
print(f"Koiran nimi: {koira1.nimi}, ikä: {koira1.ika}")


# ==========================================
# Esimerkki 1: إضافة دالة بسيطة داخل الكلاس (Simple Method)
# ==========================================
# إضافة دالة pelia لتشغيل سلوك معين للأوبجكت
class Pelihahmo:
    def __init__(self, nimi):
        self.nimi = nimi

    def pelaa(self):
        print(f"Pelihahmo {self.nimi} pelaa nyt!")

hahmo1 = Pelihahmo("Doom")
hahmo1.pelaa()


# ==========================================
# Esimerkki 2: تعديل بيانات الأوبجكت عبر دالة (Modifying Attributes)
# ==========================================
# دالة double_speed تقوم بمضاعفة السرعة داخل الأوبجكت
class Character:
    def __init__(self, health, damage, speed):
        self.health = health
        self.damage = damage
        self.speed = speed

    def double_speed(self):
        self.speed *= 2

warrior = Character(100, 50, 10)
ninja = Character(80, 40, 60)

print(f"Warrior speed: {warrior.speed}")
print(f"Ninja speed: {ninja.speed}")

warrior.double_speed()
print(f"Warrior new speed: {warrior.speed}")

ninja.double_speed()
print(f"Ninja new speed: {ninja.speed}")


# ==========================================
# Esimerkki 3: منطق واتخاذ قرار داخل الدالة (Method with Logic)
# ==========================================
# دالة tall تتأكد من طول القطة وترجع نصاً بناءً على الشرط
class Cat:
    def __init__(self, name, ikä, tyyppi, pituus):
        self.name = name
        self.ikä = ikä
        self.tyyppi = tyyppi
        self.pituus = pituus

    def tall(self):
        if self.pituus > 60:
            return "kissasi on aikuinen"
        else:
            return "kissasi on pikku nuori"

cat1 = Cat("shbshb", 2, "domestic shorthair", 50)
cat2 = Cat("satoor", 5, "laperm", 100)

print(f"{cat1.name}: {cat1.tall()}")
print(f"{cat2.name} (pituus {cat2.pituus} cm, rotu {cat2.tyyppi}): {cat2.tall()}")


# ==========================================
# Esimerkki 4: استدعاء دالة داخل دالة أخرى بالـ Class (Member)
# ==========================================
# دالة name_with_title تستدعي دالة full_name بداخلها باستخدام self
class Member:
    not_allowed_names = ["hell", "fucker", "shbshb", "shit"]
    users_num=0
    def __init__(self, first_name, middle_name, last_name, gender):
        self.fname = first_name   
        self.mname = middle_name
        self.lname = last_name
        self.gender = gender

        Member.users_num += 1 
    def full_name(self):
        # نضع جميع الأسماء في tuple ونفحص إذا كان أي منها موجوداً في قائمة الممنوعات
        names = (self.fname, self.mname, self.lname)
        if any(name in Member.not_allowed_names for name in names):
            raise ValueError("Name not allowed!")

        return f"{self.fname} {self.mname} {self.lname}"

    def name_with_title(self):
        gender_clean = self.gender.strip().lower()
        if gender_clean in ["women", "nainen"]:
            return f"MS : {self.full_name()}"
        elif gender_clean in ["man", "mies"]:
            return f"MR: {self.full_name()}"
        else:
            return f"{self.full_name()}"


    def Delete_users(self):
        Member.users_num -= 1 

        return f"user {self.fname} Deleted"

print(f"users count befour {Member.users_num}")

# المخرجات التجريبية
member_one = Member("amjad", "mohamad", "alhalak", "man")
member_two = Member("rama", "mohamad", "halak", "women")
member_three = Member("maisa", "ghaza", "fajer", "-")

print(member_one.name_with_title())
print(member_two.name_with_title())
print(member_three.name_with_title())


print(member_one.Delete_users())
# تجربة Catching للخطأ بالشكل الصحيح
try:
    member_four = Member("hell", "shit", "fera", "-")
    print(member_four.full_name())
except ValueError as e:
    print(f"Virhe: {e}")


print(f"users count after {Member.users_num}")

# ==========================================
# Esimerkki 5: الربط بين مدخلات المستخدم والأوبجكت (User Input)
# ==========================================
# حساب العمر بأشكال مختلفة بناءً على سنة الإدخال
class Ikaisuus:
    def __init__(self, year):
        self.year = year
        self.month = year * 12 
        self.days = year * 365

year0 = int(input("How old are you?: "))
amjad = Ikaisuus(year0)

tyyppi = input("In which way do you want your age (year / month / days): ").strip().lower()
if tyyppi == "year":
    print(f"Age in years: {amjad.year}")
elif tyyppi == "month":
    print(f"Age in months: {amjad.month}")
elif tyyppi == "days":
    print(f"Age in days: {amjad.days}")


# ==========================================
# Esimerkki 6: المتغيرات الثابتة والقيم الافتراضية (Class Variables & Default Args)
# ==========================================
# استخدام العداد tehty وقيمة افتراضية للصوت aani="RROOAAARR!"
class Lion:
    tehty = 0  # Static / Class variable (مشترك بين كل الأسود)

    def __init__(self, tyyppi, hiuksenpituus, paino, aani="RROOAAARR!"):
        self.tyyppi = tyyppi
        self.hiuksenpituus = hiuksenpituus
        self.paino = paino
        self.aani = aani

        Lion.tehty += 1  # زيادة العداد عند إنشاء كل أوبجكت جديد

lion1 = Lion("Afrikanleijona", "Pitkä ja tuuhea harja", 190)
lion2 = Lion("Aasianleijona", "Lyhyt harja", 160, "RRAARR!")
lion3 = Lion("Berberileijona", "Erittäin pitkä tumma harja", 230, "GROOOAAARRR!")

print(f"Oletusääni (lion1): {lion1.aani}")
print(f"Lion1: {lion1.tyyppi}, {lion1.hiuksenpituus}, {lion1.paino} kg, ääni: {lion1.aani}")
print(f"Lion2: {lion2.tyyppi}, {lion2.hiuksenpituus}, {lion2.paino} kg, ääni: {lion2.aani}")
print(f"Leijonia luotu yhteensä: {Lion.tehty}")


# ==========================================
# Esimerkki 7: مراجع الأوبجكت في الذاكرة (Memory References & Garbage Collector)
# ==========================================
# فهم كيف تشير المتغيرات لنفس العنوان في الذاكرة وكيف يحذف البايثون الكائنات غير المستخدمة
class KoiraTarkastus:
    def __init__(self, nimi, syntymavuosi):
        self.nimi = nimi
        self.syntymavuosi = syntymavuosi

k1 = KoiraTarkastus("Muro", 2018)
k2 = KoiraTarkastus("Rekku", 2022)

# k3 ليس أوبجكت جديد، بل يشير لنفس الأوبجكت k1 في الذاكرة
k3 = k1

# تعديل k3 سيتسبب بتعديل k1 مباشرة!
k3.nimi = "Musti"
print(f"k1:n nimi muuttui: {k1.nimi}")  # سيطبع Musti

# كود Garbage Collection: عند تغيير مرجع k2، يفقد "Rekku" مرجعه ويحذف من الذاكرة
k2 = k1


# ==========================================
# Esimerkki 8: مراجع الأوبجكت في الذاكرة (Memory References & Garbage Collector)
# ==========================================



