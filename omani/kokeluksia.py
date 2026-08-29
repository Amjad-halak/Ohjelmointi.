import random
# kruuna ja klaava peli 
random_number=random.randint(0,1)
print(random_number)
if random_number==0:
    result="kruuna"
else:
    result="klaava"
print(f"result is {result}")

random_number_2=random.uniform(-1.02 , 1.34)
print(f"{random_number_2:.2f}")
if random_number_2>=0:
    result1="biger"
elif random_number_2<=0:
    result1="lower"
print(f"resut is {result1}")

ikä=int(input("mikä sun ikäsi on ? "))
if ikä >=18:
    x="you pass and could get drivinglicense . "
else:
    y=float(input("enter your real tall !! "))
    if y>=180:
        x="you could have drivinglicense ."
    elif y<180:
        x="you couldnt have drivinglicense "
print(f"sun oikei tulos on :{x}\nreach us on our platform")

määrä=100
print(90<määrä<99)
print(1==1)


# first esi ((and),or,not)
temp=float(input("enter your reagon temp now:: "))
suny=input("is it sunny outside (Y/N)")

if temp > 15 and suny == "Y":
    x="go to swim you motherfucka"
else:
    x="the temp is bad stay homealone "
print(f"the temp situation is {x}")

# secound esi (and,(or),not)
temp=float(input("enter your reagon temp now:: "))

if temp <= 0 or temp >= 30:
    x="the temp is bad"
else:
    x="the temp is good"
print(f"the temp situation is {x}")

# first esi (and,or,(not))
temp=float(input("enter your reagon temp now:: "))
suny=input("is it sunny outside (Y/N)")

if temp > 0 and temp <30:
    x="the temp is good"
else:
    x="the temp is bad"
print(f"the temp situation is {x}")

