import random
#Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1..6. 
# Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen. 
# Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.

def noppa ():
    return random.randint(1,6)

tulos=0
while noppa != 6 :
    tulos=noppa()
print(tulos)
    

