import math
import random

 #teh.1
x=input("pistaka tähän oma kutsunimi: ")
print(f"hello {x} !")


  #teh.2
# ympyrän pinta-ala ja ympärysmitta on laskettavissa kaavoilla:
# ympyrän pinta-ala = π * r^2
# ympärysmitta = 2 * π * r
#Kirjoita ohjelma, joka kysyy ympyrän säteen ja tulostaa sen pinta-alan.

r=float(input("pista ympyrän säde tössä:  "))
A=(math.pi*r**2)
print(f"{A:.2f}")


 # (.2f) tarkoitus on anna 2 numeroa desimaalien jälkeen. ja f on tarkoitus on anna float luku.

  #teh.3
#Kirjoita ohjelma, joka kysyy suorakulmion kannan ja korkeuden. Ohjelma tulostaa suorakulmion piirin ja pinta-alan. Suorakulmion piiri tarkoittaa sen neljän sivun yhteispituutta.

a=float(input("anna suorakulmion kannan: "))
b=float(input("anna suorakulmion korkeus: "))
piiri=2*(a+b)
pinta_ala=a*b
print(f"piiri on :  , {piiri:.2f} , pinta_ala on : , {pinta_ala:.2f}")


  #teh.4

#Kirjoita ohjelma, joka kysyy kolme kokonaislukua. Ohjelma tulostaa lukujen summan, tulon ja keskiarvon.

x=int(input("enter any first number: "))
y=int(input("enter any secound number: "))
z=int(input("enter any therd number: "))

u=(x+y+z)
t=(x*y*z)
l=(x+y+z)/3
print(f"numbers summa on {u}\nnumbers tulo on {t}\nnumbers keskiarvo on {z}\n")   #وظيفه \n لحته تخلي تحت بعض مو بجانب بعض

  #teht.5  (koitaka muodusta uuden tapa laskea leiviskät, naulat ja luodit grammoiksi)
  #Kirjoita ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan leivisköinä, nauloina ja luoteina. Ohjelma muuntaa syötteen täysiksi kilogrammoiksi ja grammoiksi sekä ilmoittaa tuloksen käyttäjälle. 

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

#Kirjoita ohjelma, joka arpoo ja tulostaa kaksi erilaista numerolukon koodia:
#kolmenumeroisen koodin, jonka kukin numeromerkki on väliltä 0..9.
#nelinumeroisen koodin, jonka kukin numeromerkki on väliltä 1..6.

ran_1= random.randint(1, 100)
ran_2= random.randint(-33 ,0)
ran_3 = random.uniform(-3.2, 10.5)    # اذا بدك تستخدم فواصل => uniform

print(f"{ran_3:.2f}")

E=(f"{ran_1*ran_2*ran_3:.2f}")
print(f"{E}")


