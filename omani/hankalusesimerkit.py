#teht.5  (koitaka muodusta uuden tapa laskea leiviskät, naulat ja luodit grammoiksi)

leiviskät = float(input("Anna leiviskät.\n"))   #leiviksi-lkm
naulat = float(input("Anna naulat.\n"))         #naulat-lkm
luodit = float(input("Anna luodit.\n"))         


#. \n  Pythonissa rivinvaihtoa eli uuden rivin aloittamista.

yhteensa_luodit = (leiviskät * 20 * 32) + (naulat * 32) + luodit
yhteensa_grammat = yhteensa_luodit * 13.3
kilogrammat = int(yhteensa_grammat // 1000)
grammat = yhteensa_grammat % 1000


#toinen tapa laskeamiseen on githubissa open mahtulla 

print("\nMassa nykymittojen mukaan:")
print(f"{kilogrammat} kilogrammaa ja {grammat:.2f} grammaa.")


## chkatka kaikki (and,or,not) välikirjanokset ja miten ne toimi
vuosiluku = int(input("Anna vuosiluku: "))

if vuosiluku % 400 == 0 or (vuosiluku % 4 == 0 and vuosiluku % 100 != 0):
    print("Vuosi on karkausvuosi.")
else:
    print("Vuosi ei ole karkausvuosi.")



#########
#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
#kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi. 
#Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.



    # 1. اسأل عن أول رقم واجعله هو الأصغر والأكبر
syote = input("Anna luku: ")
pienin = float(syote)
suurin = float(syote)

# 2. كرر السلسلة طالما الإدخال ليس فارغاً
while syote != "":
    luku = float(syote)
    
    if luku < pienin: pienin = luku  # إذا كان أصغر، حدّث الأصغر
    if luku > suurin: suurin = luku  # إذا كان أكبر، حدّث الأكبر
    
    syote = input("Anna luku: ")     # اطلب الرقم التالي

# 3. اطبع النتيجة
print(f"Pienin: {pienin}, Suurin: {suurin}")