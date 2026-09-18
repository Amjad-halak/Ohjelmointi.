import random
import math

# ==========================================
# Esimerkki 0: Perusfunktio ja syötteen tarkistus (Tervehdys)
# ==========================================
# دالة إدخال والتحقق من كلمة الترحيب مع الخروج الفوري بـ break
def tervehdys():
    while True:
        x = input("Mikä on Suomen yleinen tervehdyssana: ").strip().lower()
        if x == "moi":
            print("Tervetuloa kyytiin!")
            break
        print("Väärä sana, yritä uudelleen!")

tervehdys()


# ==========================================
# Esimerkki 1: Arvon palauttaminen (Return Euroiksi)
# ==========================================
# دالة تحويل المارك إلى يورو وإرجاع النتيجة باستخدام return
def muunna_euroiksi(markat):
    euro = markat / 6
    return euro  

tulos = muunna_euroiksi(12)
print(f"euroksi : {tulos}") 


# ==========================================
# Esimerkki 2: Monipuolinen laskuri ja validointi (Ikälaskuri)
# ==========================================
# دالة حساب العمر بالأيام والأسابيع والأشهر مع التحقق من الرقم
def oikein_ikäsi():
    while True:
        I = int(input("Anna ikäsi vuotena: "))
        if I > 0:
            kuukausi = I * 12 
            viikko = I * 52
            päivä = I * 365

            tyyppi = input("Anna muunnostyyppi (kuukausi / viikko / päivä): ").strip().lower()
            
            if tyyppi == "kuukausi":
                print(f"Ikäsi vuosittain {I}, ja sen muutos kuukausiksi: {kuukausi}")
            elif tyyppi == "viikko":
                print(f"Ikäsi vuosittain {I}, ja sen muutos viikoiksi: {viikko}")
            elif tyyppi == "päivä":
                print(f"Ikäsi vuosittain {I}, ja sen muutos päiviksi: {päivä}")
            else:
                print("Tuntematon tyyppi!")
            
            break  # Lopetetaan silmukka onnistuneen laskennan jälkeen
        else:
            print("Iän pitää olla suurempi kuin 0!")

oikein_ikäsi()


# ==========================================
# Esimerkki 3: Yksinkertainen parametrin tulostus (Pelin nimi)
# ==========================================
# دالة تستقبل اسم اللعبة وتطبعه مباشرة
def pelia(peli):
    print(f"pelisi nimi on {peli}")

pelia("Doom")


# ==========================================
# Esimerkki 4: Usean luvun kertolasku ja return
# ==========================================
# دالة تأخذ 3 أرقام وتعد حاصل ضربهم وترجعه
def numerot():
    eka = int(input("Anna eka numero: "))
    toka = int(input("Anna toka numero: "))
    kolmas = int(input("Anna kolmas numero: "))
    
    tulos = eka * toka * kolmas
    return tulos

vastaus = numerot()
print(f"Tulos on: {vastaus}")


# ==========================================
# Esimerkki 5: Oletusarvot parametreille (Default Parameters)
# ==========================================
# دالة تحتوي على قيم افتراضية للمعاملات في حال لم يُحددها المستخدم
def outu(terve="hei", kerrat=2):
    for i in range(kerrat):
        print(terve)

outu()


# ==========================================
# Esimerkki 6: Print vs Return erot (Tulostus vs Palautus)
# ==========================================
# الفرق بين طباعة النص مباشرة وإرجاعه لاستخدامه في متغير
def funktion_name_print():
    print("hello python from inside python!")

funktion_name_print()

def funktion_name_return():
    return "hello python from inside python!"

data_fromfunktion = funktion_name_return()
print(data_fromfunktion)


# ==========================================
# Esimerkki 7: Muuttujien välittäminen parametreina (Arguments)
# ==========================================
# إرسال المتغيرات الخارجية كـ Arguments للدالة
a, b, c = "AYA", "mazhar", "RAMA"

def say_hello_person(name):               
    print(f"hello {name}")          

say_hello_person(a)                        
say_hello_person(b)
say_hello_person(c)


# ==========================================
# Esimerkki 8: Tyyppitarkistus ja virheiden esto (Type Checking)
# ==========================================
# التاكد من أن المدخلات أعداد صحيحة فقط قبل الجمع
def addition(n1, n2):
    if type(n1) != int or type(n2) != int:
        print("only integers allowed!")
    else:
        print(n1 + n2)
       
addition(100, 120) 


# ==========================================
# Esimerkki 9: Merkkijonojen muotoilu (String Formatting)
# ==========================================
# تنظيف النصوص واقتطاع أول حرف من الاسم الأوسط :.1s
def full_name(firsta, middle, last):
    print(f"hello {firsta.strip()} {middle.upper():.1s} {last.strip()}")

full_name("amjad", "mohamed ", "alhalak")


# ==========================================
# Esimerkki 10: Rajoittamattomat parametrit (*args)
# ==========================================
# استخدام * لتلقي عدد غير محدود من الأسماء وقراءتها بحلقة
def say_hello_many(*names):                
    for name in names:
        print(f"hello  {name}")

say_hello_many("ulla", "arpoo", "pierre", "markus", "name", "matey")


# ==========================================
# Esimerkki 11: Ehdollinen taitojen tulostus (*args & logic)
# ==========================================
# تخصيص طباعة المهارات بناءً على اسم الشخص
def tulosta_taidot(nimi, *skills):
    print(f"\n- Hello {nimi}, your skills are:")
    for skill in skills:
        print(f"  * {skill}")

name = input("Enter your name: ").lower()

if name == "ulla":
    tulosta_taidot("Ulla", "Python 100%", "Science 100%", "Elämä 100%")
elif name == "amjad":
    tulosta_taidot("Amjad", "Python 40%", "Science 20%", "Elämä 90%")
elif name == "rama":
    tulosta_taidot("Rama", "Python 0%", "Science 0%", "Elämä 0%")
else:
    print("You are not in this class!")


# ==========================================
# Esimerkki 12: Nimetyt parametrit (Keyword Arguments)
# ==========================================
# إرسال القيم مع تحديد أسماء المعاملات لتجاوز ترتيب الحقول
def say_hello_adv(name="unknown!!", age="unknown!!", country="unknown!!"):          
    print(f"hello : {name}\nyour age: {age}\nand u from :{country}")

say_hello_adv("amjad", 23)
print("=" * 20)
say_hello_adv(name="amjad ", country="syria")
print("=" * 20)
say_hello_adv()  
print("=" * 20)
say_hello_adv(age=35)


# ==========================================
# Esimerkki 13: Sanakirja-parametrit (**kwargs)
# ==========================================
# استقبال مفتاح وقيمة غير محدودة وتفكيك القواميس (**my_skills)
def show_skills(**skills):
    print(type(skills))
    for skill, value in skills.items():
        print(f"{skill}  => {value}")
        print("=" * 20)

show_skills(python="80%", js="0%", eläma="40%", html="0%")

my_skills = {
    "python": "80%",
    "js": "0%",
    "eläma": "40%",
    "html": "0%"
}
show_skills(**my_skills)


# ==========================================
# Esimerkki 14: Muuttujien näkyvyys (Global Scope & global keyword)
# ==========================================
# التحكم بالمتغيرات العامة من داخل وخارج الدوال
x = 1  # Global scope 
print(f"print variable from global scope {x}")

def one():
    global x            # Muutetaan globaalia muuttujaa
    x = 2
    print(f"print variable from funktion scope {x}")

print(f"print variable from global scope {x}")
one()

def two():
    x = 4               # Paikallinen muuttuja (Local scope)
    print(f"print variable from funktion scope {x}")

two()
print(f"after {x}")


# ==========================================
# Esimerkki 15: Rekursiivinen funktio (Rekursio / Recursion)
# ==========================================
# استدعاء الدالة لنفسها لتنظيف الكلمة من الحروف المكررة المتتالية
def cleanword(word):
    if len(word) == 1:
        return word
    print(f"print start funktion {word}")

    if word[0] == word[1]: 
        print(f"before return {word}")
        return cleanword(word[1:])  
    print(f"before return {word}")
    return word[0] + cleanword(word[1:])

print(cleanword("wwoooooorrllllld"))


# ==========================================
# Esimerkki 16: Anonyymit funktiot (Lambda-funktiot)
# ==========================================
# الدوال السريعة غير المسماة بسطر واحد
def say_hello_normal(name): 
    return f"hello {name}"

hello_lambda = lambda name: f"hello {name}"

print(say_hello_normal("ahmad"))
print(hello_lambda("amjad"))


