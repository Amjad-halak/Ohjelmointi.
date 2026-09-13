import random

# ==========================================
# Esimerkki 1: For-silmukan perusteet & range()
# ==========================================
num = [1, 10, 55]
for amjad in num:
    print(amjad)

# range(55) alkaa 0:sta ja päättyy 54:ään (55-1)
for amjad in range(55):
    print(amjad)

# range(0, 2) tulostaa arvot 0 ja 1
for amjad in range(0, 2):
    print(amjad)

# reversed() laskee taaksepäin: 10 -> 1
for loop in reversed(range(1, 11)):
    print(loop)

# range(alku, loppu, askel): lisää 3 joka kierroksella (1, 4, 7... 55)
for loop in range(1, 56, 3):
    print(loop)

names = ["shbshb", "amjad", "rama"]
for y in names:
    print(y)


# ==========================================
# Esimerkki 2: Satunnaisluvut listassa
# ==========================================
x = random.randint(-100, 7521)
y = random.uniform(-1, 0)

# Tallennetaan satunnaisluvut listaan
pisteet = [x, y]
print(pisteet)

# pisteet[1] hakee toisen alkion (y)
print(pisteet[1])


# ==========================================
# Esimerkki 3: Indeksit ja viipalointi (Slicing)
# ==========================================
nimet = ["m.snake", "ziizu", "värällä", "shbshb"]

print(nimet[-3])    # Negatiivinen indeksi: kolmas lopusta ("ziizu")
print(nimet[0:3])   # Ottaa alkiot indekseistä 0, 1 ja 2
print(nimet[1:])    # Ottaa alkiot indeksistä 1 listan loppuun asti
print(nimet)

# len() palauttaa listan pituuden (alkioiden määrän)
listan_koko = len(nimet)
print(listan_koko)


# 
# Listan läpikäynti while-silmukalla
#
counter = 0

# Toistetaan niin kauan kuin laskuri on pienempi kuin listan pituus
while counter < len(nimet):
    # counter+1 näyttää järjestysnumeron (1, 2, 3...)
    print(f"{counter+1}. nimi:{nimet[counter]}")
    counter += 1


# 
#  Listan kasvattaminen (input & append)
# 
# Kysytään uusi nimi ja lisätään se listan loppuun append()-metodilla
uusi_nimi = input("Anna uusi nimi: ")
nimet.append(uusi_nimi)
print(nimet)

for name in nimet:
    print(name)


# ==========================================
# Esimerkki 4 : Tehtävälista (Todos) ja erilaiset silmukat
# ==========================================
todos = []
todos.append("Tee läksyt!")

# Lisätään käyttäjän syöte listaan
new_todo = input("Anna uusi tehtävä: ")
todos.append(new_todo)
print(todos)

# Tapa 1: Suora läpikäynti (ilman indeksejä)
for todo in todos:
    print(todo)

# Tapa 2: Läpikäynti indeksien avulla range(len())-rakenteella
for number in range(len(todos)):
    print(todos[number])

# Tapa 3: range() tietylle numerovälille hyppyineen (3, 6, 9... 30)
for luku in range(3, 31, 3):
    print(luku)

# ==========================================
# Esimerkki 5 : Listaoperaatiot
# ==========================================
num = []

# تقرأ النص أولاً بدون int لتسمح بضغط Enter للإنهاء
numbers = input("Enter muutama numeroita (press enter to stop): ")

while numbers != "":
    # نحول النص إلى رقم ونضيفه للقائمة
    num.append(int(numbers))

    # sijoita numerot pienmista suuremmaks
    num.sort()

    # tulosta numerot listalla 
    print(f"numers are {num}")
    for nume in num:
        print(nume)

    numbers = input("Enter muutama numeroita (press enter to stop): ")
    
print("ohjelma päätyy")
print(f"numers are {num}")
