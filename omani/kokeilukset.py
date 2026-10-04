syötteenä=input ("anna syötteenä : ")
sanat =[]
while True :
    if syötteenä == "":
        sanat.appent(syötteenä)

        for sana in sanat :
            if len(sana) > 5 and sana(1) == "A" or sana(1) == "a":
      
                print (f"Hyväksyttyjä sanoja: {sana}")
            else :
                print (f"{sana} ei hyväksetty ")
        syötteenä=input ("anna syötteenä : ")

    elif syötteenä != "LOPPU":
        break
