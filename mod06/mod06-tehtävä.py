import random

# ==========================================
# Tehtävä 1: Arpakuutiot (for-silmukka)
# ==========================================
heitto_kerrat = int(input("Anna arpakuutioiden lukumäärä: "))
summa = 0

for i in range(heitto_kerrat):
    heitto = random.randint(1, 6)
    summa += heitto
    print(f"Heitto {i + 1}: {heitto}")

print(f"Silmälukujen summa: {summa}")


# ==========================================
# Tehtävä 1.2: Arpakuutiot (while-silmukka)
# ==========================================
heitto_kerrat = int(input("Anna arpakuutioiden lukumäärä: "))
kerrat = 0
summa = 0

while kerrat < heitto_kerrat:
    heitto = random.randint(1, 6)
    summa += heitto
    kerrat += 1

print(f"Silmälukujen summa: {summa}")


# ==========================================
# Tehtävä 2: Viisi suurinta lukua (while + sort)
# ==========================================
luvut = []

while True:
    syöte = input("Anna luku (tyhjä lopettaa): ").strip()
    if syöte == "":
        break
    luvut.append(float(syöte))

luvut.sort(reverse=True)

print("Viisi suurinta lukua:")
f = 1
for n in luvut[:5]:
    print(f"Luku {f}: {n}")
    f += 1


# ==========================================
# Tehtävä 3: Alkuluvun tarkistus (for + flag)
# ==========================================
kokonais_luku = int(input("Anna kokonaisluku: "))

if kokonais_luku <= 1:
    print("Tämä ei ole alkuluku.")
else:
    on_alkuluku = True
    for num in range(2, kokonais_luku):
        if kokonais_luku % num == 0:
            on_alkuluku = False
            break

    if on_alkuluku:
        print("Luku on alkuluku.")
    else:
        print("Luku ei ole alkuluku.")


# ==========================================
# Tehtävä 4: Viisi kaupunkia (for ja for...in)
# ==========================================
kaupungit = []

for i in range(5):
    nimi = input("Anna kaupungin nimi: ").strip()
    kaupungit.append(nimi)

print("\nSyötetyt kaupungit:")
for k in kaupungit:
    print(k)




# ==========================================
#القسم الأول: يطلب من المستخدم إدخال أسماء طلاب متفوقين واحداً تلو الآخر، ويستمر في الطلب حتى يدخل المستخدم نصاً فارغاً "" 
# (يعني يضغط Enter فوراً لينهي الإدخال). يتم حفظ جميع الأسماء في قائمة باسم opiskelijat.
# ==========================================


opiskeljat=[]
opiskeljat_nimit= input(" anna ahkerallinen opisjelan nimi (jätä tyhän lopetamaan ): ")
while True :
    if opiskeljat_nimit == "":
        break
    else:
        opiskeljat.append(opiskeljat_nimit)
        opiskeljat_nimit= input(" anna ahkerallinen opisjelan nimi (jätä tyhän lopetamaan ): ")
f=1
for opiskelja in opiskeljat:
    print(f"{f}.{opiskelja}")
    f += 1
