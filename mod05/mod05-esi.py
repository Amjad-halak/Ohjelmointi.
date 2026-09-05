import random
import math

# ==========================================
# Esimerkki 0: Numeroiden kasvattaminen (Laskuri / Counter)
# ==========================================
# Asetetaan alustusarvo (muuttuja)
x = 1.5

# Silmukka pyörii niin kauan kuin x on pienempi tai yhtä suuri kuin 10.0
while x <= 10.00:
    print(f"{x:.2f} on allempi kun merki numero")
    # Kasvatetaan x:n arvoa joka kierroksella (muuten tulee ikuinen silmukka)
    x = x + 1.3

print("done")


# ==========================================
# Esimerkki 1: Tyhjän syötteen tarkistus (Validation)
# ==========================================
name = input("pista sun nimisi:: ")

# Silmukka toistuu VAIN jos käyttäjä painaa Enter antamatta nimeä (tyhjä merkkijono "")
while name == "":
    print("et laitanut sun nimi!!")
    # Kysytään nimeä uudelleen, jotta päästään pois silmukasta
    name = input("pista sun nimisi:: ")

x = f"hei mr {name}"
print(x)


# ==========================================
# Esimerkki 2: Virheellisen arvon estäminen (Virheellinen ikä)
# ==========================================
ikä = float(input("mikä sun oikei ikä on ?? "))

# Silmukka jatkuu niin kauan kuin ikä on negatiivinen (alle 0)
while ikä < 0:
    print("ikä ei saisi olla negativinen")
    # Kysytään ikää uudelleen
    ikä = float(input("mikä sun oikei ikä on ?? "))

y = f"hei {ikä} vuottavänhä henkillö !!"
print(y)


# ==========================================
# Esimerkki 3: Lopetusmerkin käyttö ("q" lopettaa)
# ==========================================
ruoka = input("anna sun lempisi ruoka ? (paina q lopetamaan) :: ")

# "not ruoka == 'q'" tarkoittaa: niin kauan kuin syöte EI OLE "q"
while not ruoka == "q":
    print(f"tyykät {ruoka}")
    # Kysytään seuraavaa ruokaa
    ruoka = input("anna sun toisen lempisi ruoka ? (paina q lopetamaan) : ")

print("bey")


# ==========================================
# Esimerkki 4: Numero tietyltä väliltä (Rajojen tarkistus)
# ==========================================
numero = int(input("anna nuomerosi 1 - 10 väli :"))

# Silmukka toistuu jos numero on pienempi kuin 1 TAI suurempi kuin 10
while numero < 1 or numero > 10:
    print(f"älä pela mun kaa\nnumero {numero} ei ole listalla\nseura pelinsääntö !! ")
    # Kysytään numeroa uudelleen
    numero = int(input("anna nuomerosi 1 - 10 väli :"))

print(f"sun valitus nuomero on {numero} ! ")


# ==========================================
# Esimerkki 5: Toistokertojen määrä (Käyttäjän määräämä laskuri)
# ==========================================
times = float(input("enter how many welcomes time:: "))
done = 0

# Silmukka toistuu niin kauan kuin done on pienempi tai yhtä suuri kuin times
while done <= times:
    print(f"morning {done}")
    # Lisätään laskuriin 1 joka kierroksella
    done = done + 1


# ==========================================
# Esimerkki 6: Monen lopetuskomennon tarkistus (not ja or -rakenne)
# ==========================================
komento = input("anna komento ")

# Silmukka toistuu niin kauan kuin komento EI OLE "lopeta", "stop" EIKÄ tyhjä ""
while not (komento == "lopeta" or komento == "stop" or komento == ""):
    print(f"suorita toiminnan: {komento}")
    # Kysytään uutta komentoa
    komento = input("anna komento ")

print("toiminnon päätty")


# ==========================================
# Esimerkki 7: Satunnaislukujen simulointi (Nopanheitto)
# ==========================================
noppa1 = noppa2 = heittojen_maara = 0

# Silmukka pyörii niin kauan kuin MOLEMMAT nopat EIVÄT OLE kutosia (6 ja 6)
while not (noppa1 == 6 and noppa2 == 6):
    # Arotaan satunnainen numero väliltä 1-6
    noppa1 = random.randint(1, 6)
    noppa2 = random.randint(1, 6)
    heittojen_maara = heittojen_maara + 1

print(f"Tarvittiin {heittojen_maara} heittoa, että saatiin molemmat nopat (6).")


# ==========================================
# Esimerkki 8: Sisäkkäiset silmukat (Kertotaulu / Nested loops)
# ==========================================
ensimainen = 1

# Ulkopuolinen silmukka hallitsee ensimmäistä numeroa (1-10)
while ensimainen <= 10:
    toisen = 1
    # Sisäpuolinen silmukka hallitsee toista numeroa (1-10)
    while toisen <= 10:
        print(f"niiden kerto laskuri on {ensimainen} kerta {toisen} on {ensimainen*toisen:d}")
        toisen = toisen + 1
    # Kasvatetaan ensimmäistä numeroa vasta kun sisäsilmukka on valmis
    ensimainen = ensimainen + 1

print("tähän päätyy")



# ==========================================
# 9. Laskurien oikotiet (+= ja -=)
# ==========================================
# += lisää arvon, -= vähentää arvon
luku = 0
luku += 1  # Sama kuin: luku = luku + 1
luku += 1  # Luku on nyt 2

print(f"Laskurin arvo: {luku}")


# ==========================================
# 10. Taaksepäin laskeminen (10 -> 1)
# ==========================================
# Tulostetaan luku ENNEN vähennystä, jotta laskenta alkaa kympistä
laskuri = 10

print("\n--- Lasketaan alaspäin ---")
while laskuri > 0:
    print(laskuri)
    laskuri -= 1  # Vähennetään 1 jokaisella kierroksella


# ==========================================
# 11. Käyttäjänimen kysyminen ja yrityskerrat
# ==========================================
nimi = input("\nEnter your name: ").strip()
yritykset = 0

# Silmukka pyörii, jos nimi on tyhjä JA yrityksiä on alle 5
while nimi == "" and yritykset < 5:
    yritykset += 1
    print("You didn't enter your name :)")
    
    if yritykset == 5:
        break  # Lopettaa silmukan heti 5. yrityksen jälkeen
        
    nimi = input("Enter your name: ").strip()

if nimi != "":
    print(f"Welcome {nimi}!")
else:
    print("You used all 5 attempts.")


# ==========================================
# 12. Tekstin puhdistus (.strip() ja .lower()) sekä break & while/else
# ==========================================
# .strip() poistaa ylimääräiset välilyönnit
# .lower() muuttaa kirjaimet pieniksi (esim. "LOPETA" -> "lopeta")

komento = input("\nAnna komento (pelaa / apua / lopeta): ").strip().lower()

while komento != "lopeta":
    if komento == "apua":
        print("Tässä on ohje: Kirjoita 'pelaa' aloittaaksesi tai 'lopeta' poistuaksesi.")
        break  # Lopettaa silmukan HETI, eikä else-lohkoa suoriteta!
    
    elif komento == "pelaa":
        print("Peli käynnistyy... Wuuhoo!")
    else:
        print(f"Tuntematon komento: {komento}")
    
    # Kysytään uusi komento ja puhdistetaan se taas
    komento = input("\nAnna uusi komento: ").strip().lower()

else:
    # Suoritetaan VAIN jos silmukka päättyy normaalisti (kun komento == "lopeta")
    print("Annoit käskyn 'lopeta', joten ohjelma suljetaan nätisti.")

print("Ohjelma päättyi.")