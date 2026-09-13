# Tuntiesimerkkejä mod 6 - 2.9.
import random

# arvotaan satunnainen piste välillä -1,-1 ja 1,1
x = random.uniform(-1,1)
y = random.uniform(-1,1)

piste = [x, y]

print(piste)

# tulostetaan vain ensimmäisen alkion arvo (x)
while piste[0]>0 and piste[1]>0:
        print(piste[0])
    
        print(piste[1])
        break
   