items = []


def Start():
    while len(items) < 3:
        Add_Items = input("Enter the using items : ")
        items.append(Add_Items)
        print(f"Items added! Total items: {len(items)}/3\n")

    print("--- Your Items List ---")
    for item in items:
        print(f"your Item: {item}")


def Sitting():
    S = input(" chose (-screen\n-Graphic\n-sound\n-subtitle\n-back): ")

    if S == "screen":
        print("- Resolution\n- V-sync\n- Display Mode")
    elif S == "Graphic":
        print("- Texture Quality\n- Shadows\n- Anti-Aliasing")
    elif S == "sound":
        print("- Master Volume\n- Music\n- SFX Volume")
    elif S == "subtitle":
        print("- Subtitles: [ON/OFF]\n- Text Language")
    elif S == "back":
        print("Returning to main menu...")
    else:
        print("Invalid choice!")


def Quite():
    Q = input("Are u sure wanna Exit the Game Y/N : ")
    if Q.upper() == "Y":
        print("Exit the game !")
        exit()  # ✅ إضافة القوسين لإنهاء البرنامج فوراً
    else:
        print("Returning to main menu...")


# الحلقة الرئيسية
while True:
    valitus = input("chose the mainmenu Start/Sitting/Quite: ")
    if valitus == "Start":
        Start()
    elif valitus == "Sitting":
        Sitting()
    elif valitus == "Quite":
        Quite()
        break
    else:
        print("you chose wrong mainmenu !!")