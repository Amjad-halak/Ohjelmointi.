import math
#Kirjoita while-toistorakennetta käyttävä ohjelma, joka tulostaa kolmella jaolliset luvut väliltä 1..1000.


count = 1

while count <= 1000:
    if count % 3 == 0:
        print(f"{count} se on jaettava\n")

        
    count += 1  # numeron lisäntyminen kävi aine lopussa 


#Kirjoita ohjelma, joka muuntaa tuumia senttimetreiksi niin kauan kunnes käyttäjä antaa negatiivisen tuumamäärän.
    # Sen jälkeen ohjelma lopettaa toimintansa. 1 tuuma = 2,54 cm


tuuma = float(input("Pistä tähän tuumamäärä: "))
while tuuma >= 0:
    cm = tuuma * 2.54
    print(f"cm määrä on {cm:.2f}")
    tuuma=float(input("Pistä tähän tuumamäärä: "))

print("Lopetetaan toiminta.")

#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
#kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi. 
#Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

random_numero=float(input("pista numero mitä tähänsä"))
while random_numero == 0:
    print("se ei edes riitää")
    float(input("pista toinen numero mitä tähänsä"))
    if random_numero == "":
        print(f"{random_numero<0}ja suurin numerot {random_numero>0} ")



#teh 4
import random
#Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10. 
#Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein. 
#Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, Liian pieni arvaus tai Oikein. 
#Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.
random_number=random.randint(1,10)
my_random_number=int(input("enter number beyween 1,10 : "))
while random_number != my_random_number:
    if random_number > my_random_number:
        print("Liian pieni arvaus kun oikeia arvaus.")
    elif random_number < my_random_number:
        print("Liian suuri arvaus kun oikeia arvaus.")
    my_random_number=int(input("enter number beyween 1,10 : "))

print(f"oikein random_numer oli {random_number} ja sun arvutelu numerno on {my_random_number}")
    



#Kirjoita ohjelma, joka kysyy käyttäjältä käyttäjätunnuksen ja salasanan. 
# Jos jompikumpi tai molemmat ovat väärin, tunnus ja salasana kysytään uudelleen. 
# Tätä jatketaan kunnes kirjautumistiedot ovat oikein tai väärät tiedot on syötetty viisi kertaa.
#  Edellisessä tapauksessa tulostetaan Tervetuloa ja jälkimmäisessä Pääsy evätty. 
# (Oikea käyttäjätunnus on python ja salasana rules).


tunnus=input("anna sun käytyllinen tunnus ? ")
salasana=input("anna sun salasanasi ? ")
laskus= 0
while (tunnus != "python" or salasana != "rules") and laskus < 5:
    laskus = laskus + 1 
    print(f"jompikumpi tai molemmat ovat väärin, anna uudelleen::  ")
    tunnus=input("anna sun käytyllinen tunnus ? ")
    salasana=input("anna sun salasanasi ? ")
if tunnus !="python" and salasana != "rules":
    print("pääsy evätty ylimäärä kokeilukset")
else:
    print("Tervetuloa ")

    



    

