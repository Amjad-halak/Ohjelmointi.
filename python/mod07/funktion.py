import math
import random

# ==========================================
# Esimerkki 1: Funktion perusteet ja pass
# ==========================================
# (pass) تعني أنه لا نريد تنفيذ أي شيء داخل الدالة حالياً
# نستخدمها لتجنب توقف البرنامج عند تشغيله (Ohjelma kaatuu)
def hello_funk():
    pass

print("-" * 20)
# النتيجة ستكون (None) لأن الدالة لا ترجع أي قيمة
print(hello_funk())


def hello_funk():
    print("i hate python ! ")

# طباعة النص المباشر داخل الدالة
hello_funk()  # يطبع: i hate python !

# يطبع النص ثم يطبع None لعدم وجود return
print(hello_funk())

print("-" * 20)


# ==========================================
# Esimerkki 2: Miksi käytämme funktioita?
# ==========================================
# فائدة الدالة: التعديل في مكان واحد بدلاً من تعديل كل أسطر الطباعة
# بدلاً من تعديل كل سطر بشكل منفصل:
# print("i hate python . ")
# print("i hate python . ")

def hello_funk():
    print("i hate python . ")  # نعدل النص هنا مرة واحدة فقط

hello_funk()
hello_funk()
hello_funk()
hello_funk()

print("-" * 20)


# ==========================================
# Esimerkki 3: print vs return
# ==========================================
# print: وظيفتها عرض النتيجة للمستخدم على الشاشة فقط، وتختفي فوراً
def hello_funk_print():
    print("i hate python . ")

hello_funk_print()

# return: وظيفتها إعطاء النتيجة للبرنامج لاستخدامها في متغيرات أو حسابات أخرى
def hello_funk_return():
    return "i hate python . "

print(hello_funk_return())

print("-" * 20)


# ==========================================
# Esimerkki 4: Oletusarvot (Default arguments)
# ==========================================
# (name = "et kirjoittanut !!") تعتمد كقيمة افتراضية إذا لم يتم إدخال الاسم
def TT(tervehdys, name="et kirjoittanut !!"):
    return f"{tervehdys}, nimisi {name} function !"

print(TT("HEI", "amjad"))
print(TT("HEI"))  # يستخدم القيمة الافتراضية

print("-" * 20)


# ==========================================
# Esimerkki 5: Palautusarvon käyttö laskennassa
# ==========================================
def laske():
    return 5 + 5  # الدالة تعيد الرقم 10 للبرنامج

x = laske()  # المتغير x يحفظ الرقم 10
print(x * 2)   # النتيجة: 20
print(x * 10)  # النتيجة: 100

print("-" * 20)


# ==========================================
# Esimerkki 6: *args ja **kwargs funktion argumentteina
# ==========================================
# *args يقبل عدد غير محدود من المعاملات العادية (List/Tuple)
# **kwargs يقبل عدد غير محدود من المعاملات تسمية/مفتاح وقيمة (Dictionary)
def student_name(*args, **kwargs):
    return args, kwargs

x = student_name("Math", "History", Name="amjad", age=23, tall=185)
print(x)

print("*" * 20)


# ==========================================
# Esimerkki 7: Argumenttien purkaminen (* ja **)
# ==========================================
def student_tiedot(*args, **kwargs):
    return f"kurssit: {args}\ninfo: {kwargs}"

course = ["Math", "History"]
tiedot = {"Name": "amjad", "age": 23, "tall": 185}

course.remove("Math")
course.append("Fysikka")

# نستخدم * مع القوائم و ** مع القواميس لفك العناصر وإرسالها للدالة
print(student_tiedot(*course, **tiedot))

print("-" * 20)


# ==========================================
# Tehtävä: Karkausvuosi ja kuukauden päivät
# ==========================================
kuukauden_paivat = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# الدالة تُرجع True إذا كانت السنة كبيسة و False إذا لم تكن كذلك
def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    # إذا كان الشهر خارج النطاق 1-12 نُرجع رسالة خطأ
    if not (1 <= month <= 12):
        return "virheellinen kuukausi"

    # إذا كان الشهر شباط (2) والسنة كبيسة نُرجع 29
    if month == 2 and is_leap_year(year):
        return 29

    # لغير ذلك نُرجع عدد الأيام من القائمة
    return kuukauden_paivat[month]


# تجربة الكود:
print(days_in_month(2017, 3))   # النتيجة: 31
print(days_in_month(2020, 2))   # النتيجة: 29 (سنة كبيسة)
print(days_in_month(2021, 15))  # النتيجة: virheellinen kuukausi