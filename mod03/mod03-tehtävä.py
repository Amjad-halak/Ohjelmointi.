import math
import random

 #teh.1
x=input("pistaka tähän oma kutsunimi: ")
print(f"hello {x} !")


  #teh.2
# ympyrän pinta-ala ja ympärysmitta on laskettavissa kaavoilla:
# ympyrän pinta-ala = π * r^2
# ympärysmitta = 2 * π * r
säde = float(input("Anna ympyrän säde: "))
A = math.pi * säde ** 2
print(f"Ympyrän pinta-ala on: {A:.2f}")


 # (.2f) tarkoitus on anna 2 numeroa desimaalien jälkeen. ja f on tarkoitus on anna float luku.

  #teh.3
a=float(input("Anna suorakulmion kannan: "))
b=float(input("Anna suorakulmion korkeus: "))
piirin_pituus = 2 * (a + b)
pinta_ala = a * b
print(f"Suorakulmion piirin pituus on: {piirin_pituus:.2f}")
print(f"Suorakulmion pinta-ala on: {pinta_ala:.2f}")

  #teh.4

a=float(input("Anna eka numero: "))
b=float(input("Anna toka numero: "))

yhteylasku = a + b
kertolasku = a * b
keskiarvon = (a + b) / 2
print(f"Numeroiden yhteys on: {yhteylasku:.2f}")
print(f"Numeroiden tulo on: {kertolasku:.2f}")
print(f"Numeroiden keskiarvo on: {keskiarvon:.2f}")

  #teht.5

leiviskat = float(input("Anna leiviskät.\n"))
naulat = float(input("Anna naulat.\n"))
luodit = float(input("Anna luodit.\n"))

yhteensa_luodit = (leiviskat * 20 * 32) + (naulat * 32) + luodit
yhteensa_grammat = yhteensa_luodit * 13.3

kilogrammat = int(yhteensa_grammat // 1000)
grammat = yhteensa_grammat % 1000

print("\nMassa nykymittojen mukaan:")
print(f"{kilogrammat} kilogrammaa ja {grammat:.2f} grammaa.")





    #teht.6

random_num = random.randint(1, 100)
random_num2 = random.randint(1, 100)
print(f" {random_num} , {random_num2}")


###tehtävä on muuta nää kaikki sun omalla tähtillä eli muodusta jokin uus
 ### checkatka se M merki kansioiden perässä 
  ### jakauta se kaikki kansiot git hubii siistesiksi

