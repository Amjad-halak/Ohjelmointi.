print("=== TERVETULOA PELIIN ===")
nimi = input("Anna nimesi: ")
ikä = int(input("Anna ikäsi: "))

if ikä < 12:
    print("Olet alaikäinen. Ohjelma suljetaan.")
    exit()
else:
    print(f"\nTervetuloa kyytiin, {nimi}!\n")

items = []
pisteet = 0

weapons = ["Sword", "Bow", "Axe", "Dagger"]
gear = ["Shield", "Helmet", "Boots", "Armor"]
consumables = ["Health Potion", "Mana Potion", "Bomb", "Antidote"]


def Start():
    print("\n--- SELECT YOUR EQUIPMENT ---")
    items.clear()

    # 1. Choose Weapon
    print("\nAvailable Weapons:")
    for w in weapons:
        print(f"- {w}")
    valittu_ase = input("Choose 1 weapon: ")
    items.append(valittu_ase)

    # 2. Choose Gear
    print("\nAvailable Gear:")
    for g in gear:
        print(f"- {g}")
    valittu_varuste = input("Choose 1 gear item: ")
    items.append(valittu_varuste)

    # 3. Choose Consumable
    print("\nAvailable Consumables:")
    for c in consumables:
        print(f"- {c}")
    valittu_rohto = input("Choose 1 consumable: ")
    items.append(valittu_rohto)

    # Summary
    print("\n--- YOUR INVENTORY ---")
    for item in items:
        print(f"your Item: {item}")

    print("\nLoading screen...")
    print("Game is starting, good luck!")


def Sitting():
    S = input(
        "\nChose category (-screen\n-Graphic\n-sound\n-subtitle\n-back): "
    )

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
    if Q == "Y" or Q == "y":
        print(f"Näkemiin {nimi}! Peli päättyy.")
        exit()
    else:
        print("Returning to main menu...")


while True:
    print("\n--- PÄÄVALIKKO ---")
    print(f"Pelaaja: {nimi} | Pisteet: {pisteet}")
    valitus = input("Chose mainmenu option (Start / Sitting / Quite): ")

    if valitus == "Start":
        Start()
    elif valitus == "Sitting":
        Sitting()
    elif valitus == "Quite":
        Quite()
    else:
        print("Tuntematon komento! You chose wrong mainmenu option.")