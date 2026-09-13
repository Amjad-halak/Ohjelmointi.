num = []
numerot = input("Enter numeroita kunes jätät sen tyjhäneksi :: ")

while numerot != "":
    num.append(int(numerot))
    numerot = input(
        "Enter numeroita kunes jätät sen tyjhäneksi (press Enter to stop ):: "
    )

# 1. Järjestetään lista suurimmasta pienimpään (الترتيب من الأكبر للأصغر)
num.sort(reverse=True)

# 2. Otetaan enintään 5 suurinta lukua (أخذ أكبر 5 أرقام)
viisi_suurinta = num[:5]

print("\nViisi suurinta lukua:")

# 3. Tulostetaan viisi suurinta lukua omille riveilleen
for nn in viisi_suurinta:
    print(nn)