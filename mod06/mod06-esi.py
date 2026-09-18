import random

# ==========================================
# Esimerkki 1: For-silmukan perusteet & range()
# ==========================================
# 1. Suora läpikäynti listan läpi (مرور مباشر على عناصر القائمة)
numbers = [1, 10, 55]
for num in numbers:
    print(num)

# 2. range(55) alkaa 0:sta ja päättyy 54:ään (يبدأ من 0 وينتهي عند 54)
for amjad in range(55):
    print(amjad)

# 3. range(0, 2) tulostaa arvot 0 ja 1 (يطبع 0 و 1 فقط)
for amjad in range(0, 2):
    print(amjad)

# 4. reversed() laskee taaksepäin: 10 -> 1 (عد تنازلي من 10 إلى 1)
for loop in reversed(range(1, 11)):
    print(loop)

# 5. range(alku, loppu, askel): lisää 3 joka kierroksella (القفز بمقدار 3 في كل دورة)
for loop in range(1, 56, 3):
    print(loop)

# 6. Merkkijonolistan läpikäynti (مرور على قائمة نصوص)
names = ["shbshb", "amjad", "rama"]
for y in names:
    print(y)


# ==========================================
# Esimerkki 2: Satunnaisluvut listassa (Random Numbers in List)
# ==========================================
# Satunnaisen kokonaisluvun ja liukuluvun arpominen
x = random.randint(-100, 7521)
y = random.uniform(-1, 0)

# Tallennetaan satunnaisluvut listaan ja haetaan alkio indeksillä
pisteet = [x, y]
print(pisteet)

# pisteet[1] hakee toisen alkion (يستدعي العنصر الثاني في القائمة)
print(pisteet[1])


# ==========================================
# Esimerkki 3: Indeksit, viipalointi ja len() (Slicing & Length)
# ==========================================
nimet = ["m.snake", "ziizu", "värällä", "shbshb"]

print(nimet[-3])    # Negatiivinen indeksi: kolmas lopusta ("ziizu")
print(nimet[0:3])   # Ottaa alkiot indekseistä 0, 1 ja 2 (قتطاع أول 3 عناصر)
print(nimet[1:])    # Ottaa alkiot indeksistä 1 listan loppuun asti (من العنصر الثاني للنهاية)
print(nimet)

# len() palauttaa listan pituuden (حساب عدد عناصر القائمة)
listan_koko = len(nimet)
print(listan_koko)

# --- Listan läpikäynti while-silmukalla ---
counter = 0

# Toistetaan niin kauan kuin laskuri on pienempi kuin listan pituus
while counter < len(nimet):
    # counter+1 näyttää järjestysnumeron (1, 2, 3...)
    print(f"{counter+1}. nimi:{nimet[counter]}")
    counter += 1

# --- Listan kasvattaminen (input & append) ---
# Kysytään uusi nimi ja lisätään se listan loppuun append()-metodilla
uusi_nimi = input("Anna uusi nimi: ")
nimet.append(uusi_nimi)
print(nimet)

for name in nimet:
    print(name)


# ==========================================
# Esimerkki 4: Tehtävälista (Todos) ja eri silmukat
# ==========================================
todos = []
todos.append("Tee läksyt!")

# Lisätään käyttäjän syöte listaan
new_todo = input("Anna uusi tehtävä: ")
todos.append(new_todo)
print(todos)

# Tapa 1: Suora läpikäynti ilman indeksejä (مرور مباشر بدون مؤشر)
for todo in todos:
    print(todo)

# Tapa 2: Läpikäynti indeksien avulla range(len())-rakenteella (مرور باستعمال الفهرس/المؤشر)
for number in range(len(todos)):
    print(todos[number])

# Tapa 3: range() tietylle numerovälille hyppyineen (القفز بمقدار 3 من 3 إلى 30)
for luku in range(3, 31, 3):
    print(luku)


# ==========================================
# Esimerkki 5: Dynamic List & Sorting (Dynaminen lista ja järjestäminen)
# ==========================================
num = []

# Syötetään numeroita kunnes käyttäjä painaa Enter (إدخال أرقام حتى الضغط على Enter)
numbers = input("Enter muutama numeroita (press enter to stop): ")

while numbers != "":
    # Muunnetaan merkkijono kokonaisluvuksi ja lisätään listaan
    num.append(int(numbers))

    # Järjestetään numerot pienimmästä suurempaan (ترتيب الأرقام تصاعدياً)
    num.sort()

    # Tulostetaan päivitetty lista ja sen alkiot
    print(f"numers are {num}")
    for nume in num:
        print(nume)

    numbers = input("Enter muutama numeroita (press enter to stop): ")

print("ohjelma päätyy")
print(f"numers are {num}")