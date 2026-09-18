import random

# Lista nopan silmäluvuille (قائمة لحفظ النتائج)
tulokset = []

for i in range(10):
    heitto = random.randint(1, 6)
    tulokset.append(heitto)

print(f"Kaikki heitot: {tulokset}")
print(f"Kuutosten määrä (عدد مرات ظهور الرقم 6): {tulokset.count(6)}")


import random

heitot = 0  # العداد

while True:
    n1 = random.randint(1, 6)
    n2 = random.randint(1, 6)
    heitot += 1

    if n1 == n2:  # Tuplat! (حصلنا على نفس الرقم)
        print(f"Saatiin tuplat: {n1} ja {n2}!")
        print(f"Heittojen määrä: {heitot}")
        break  # Lopetetaan silmukka


    import random


# 1. Funktio heittää kahta noppaa (دالة ترمي نردين)
def heitä_noppaa():
    noppa1 = random.randint(1, 6)
    noppa2 = random.randint(1, 6)
    return noppa1, noppa2  # Palauttaa monikon (يرجع توبل)


# 2. Suoritetaan heitto ja puretaan arvot (ننفذ الرمية ونفرغ القيم)
n1, n2 = heitä_noppaa()
print(f"Nopista tuli: {n1} ja {n2}")
print(f"Silmälukujen summa: {n1 + n2}")