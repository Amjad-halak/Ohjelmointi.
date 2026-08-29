
import math


Uusi_kaytaja=input("Anna uusi käyttäjänimi: ")
ikä=int(input("Anna ikäsi: "))

# ilman f kirjain tule pidempi lause, koska pitää tehdä tyypinmuunnoksia (str) ja liittää merkkijonot yhteen (+)

print("Uusi käyttäjänimi on: " + Uusi_kaytaja + "!" + " ja ikä on: " + str(ikä) + "!")

# f käytäntöö on {} (eli ei tar tehä tyypimuunoksia)

print(f"Uusi käyttäjänimi on: {Uusi_kaytaja} ja ikä on: {ikä}")

pisteet = 200
pisteet = 300
print(pisteet)

merkijono = "amjad"
merkijono = "9"
merkijono = ""

print("done 6")

print(f"merkkijono on: {merkijono} sijoitetaan tähän väli")

# .5f: liukuluku viiden desimaalin tarkkuudella

luku = 3.141592653
print(f"{luku:.5f}")

# 10.2f: liukuluku kahden desimaalin tarkkuudella kymmenen merkkiä leveään kenttään

luku = 3.14
print(f"{luku:10.2f}")


# merkijono  on esi 20 merkkiä leveään kentttään vasemman tai oikeiaan reunaan mukan tasattuna 
 # pidäkä mielen että ilman toi f ei mitään tuu toimi kysessä
print(f"merkkijono on: {merkijono:>20} sijoitetaan tähän väli")
print(f"merkkijono on: {merkijono:<20} sijoitetaan tähän väli")

# 8d: kokonaisluku kahdeksan merkkiä leveään kenttään

luku = 42
print(f"|{luku:8d}|")

print("done 7")

# luku tyypit 
kokonaisluku = -9
kokonailuku_pitlä = 12_456_123_180
liukuluku = 4.973
kompleksiluku = -4 + 2j
totousluku = True
totousluku2 = False

#printetaan muutujan tyypi (eli mikä on sen arvo)
print(type(kokonaisluku))
print(type(kokonailuku_pitlä))
print(type(liukuluku))
print(type(kompleksiluku))
print(type(totousluku))
print(type(totousluku2))

print("done 8")


#import math (so vs code tietä että nyt käytetään math kirjastoa)
# yksinkertaisesti (π) vakio on math.pi


vakio=math.pi
print(f"{'Vakio luku':6s}:{vakio:10.2f}")
print(f"{'Pii':12s}:{math.pi:10.5f}")

print(math.pi)

print("done 9")

# lasku toiminnot

#Laskutoimituksia ovat yhteenlasku (+), 
# vähennyslasku (-), 
# kertolasku (*) 
# ja jakolasku (/).
#  Lisäksi on olemassa jakojäännösoperaatio (%),
#  pelkän kokonaisosan palauttava jakolasku (//) 
# sekä potenssiinkorotus (**).



a=float(input("Anna eka numero: "))
b=float(input("Anna toka numero: "))

yhteylasku = a + b
kertolasku = a * b
jakolasku= a / b
potenssiinkorotus = a ** b  # esi 12^2
kokonaisosan_palauttava_jakolasku= a // b
jakojäännösoperaatio = a % b


print(f"lukujen summa on: {yhteylasku}")
print(f"Kertolasku: {kertolasku}")
print(f"Jalolasku: {jakolasku}")
print(f"Potenssiinkorotus: {potenssiinkorotus}")
print(f"Kokonaisosan palauttava jakolasku: {kokonaisosan_palauttava_jakolasku}")   # miks tuu 0.0
print(f"Jakojäännösoperaatio: {jakojäännösoperaatio}")



### kotona chekatka float + int + str + input numerolla + siiten f kirjan +  {}

