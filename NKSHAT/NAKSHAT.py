a = "5"
b = 2
c = a * b
print(type(c), c)


x = "10"
y = 5
print(x * 2 + str(y))

x = 0
if x:
    print("Toimii!")

    a = [1, 2, 3]
b = a
b.append(4)
print(len(a))

sana = "METROPOLIA"
print(sana[2:8:2])

luvut = [3, 1, 4, 1, 5]
luvut.pop(2)
luvut.remove(1)
print(luvut)


summa = 0
for i in range(1, 3):
    for j in range(1, 4):
        if i == j:
            continue
        summa += 1

print(summa)


"Pythonissa funktio voi palauttaa useita arvoja kerralla monikkona (tuple), esimerkiksi: return a, b."


luvut = [10, 20, 30, 40]
a, *b, c = luvut
print(b)




tulos = 0
for i in range(1, 4):
    for j in range(i):
        tulos += 1
print(tulos)

x = input("Anna luku: ")
print(x + x)

a = [1, 2, 3, 4, 5]
print(a[::-2])

x="amjad"
print(len(x))