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


Sitting()