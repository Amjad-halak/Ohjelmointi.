import random

# Mod 8 esimerkkejä 9.9.2026

# ==========================================
# Esimerkki 1: Monikko (Tuple)
# ==========================================
viikonpaivat = ("maanantai", "tiistai", "keskiviikko", "torstai", "perjantai", "lauantai", "sunnuntai")
print(viikonpaivat)
print("ensimmäinen viikonpäivä on", viikonpaivat[0])

# Monikko monikon sisällä (kaksi- tai moniulotteinen monikko)
print("\narkipäivät ja viikonlopun päivät ovat omissa monikoissaan samassa monikossa:")
viikonpaivat_v2 = (("maanantai", "tiistai", "keskiviikko", "torstai", "perjantai"), ("lauantai", "sunnuntai"))
print(viikonpaivat_v2)
print("arkipäivät ovat", viikonpaivat_v2[0])
print("viikonlopun päivät ovat", viikonpaivat_v2[1])
print("ensimmäinen arkipäivä on", viikonpaivat_v2[0][0])

# Monikon yksittäisten arvojen purku erillisiin muuttujiin
(eka, toka, kolmas, neljas, viides, kuudes, seitsemas) = viikonpaivat
print(eka, kolmas, viides, seitsemas)


# ==========================================
# Esimerkki 2: Monikko ja funktio (Tuplanoppa)
# ==========================================
print("\nTuplanoppa")

def heita():
    # Luodaan kaksialkioinen monikko ja palautetaan se suoraan
    return (random.randint(1, 6), random.randint(1, 6))

nopat = heita()
print(f"Nopista tuli {nopat[0]} ja {nopat[1]}.")


# ==========================================
# Esimerkki 3: Joukko (Set)
# ==========================================
print("\nJoukkoja")
viikonpaivat_set = {"maanantai", "tiistai", "keskiviikko", "torstai", "perjantai", "lauantai", "sunnuntai"}
print(viikonpaivat_set)

# Saman arvo voi esiintyä joukossa vain kerran (arvot on uniikkeja)
viikonpaivat_set.add("extrapaiva")
viikonpaivat_set.add("extrapaiva")

for paiva in viikonpaivat_set:
    print(paiva)

viikonpaivat_set.remove("keskiviikko")
# Kaatuu jos viitataan arvoon, mitä ei ole:
# viikonpaivat_set.remove("jotainmitäeiole")
print(viikonpaivat_set)


# ==========================================
# Esimerkki 4: Sanakirja (Dictionary)
# ==========================================
print("\nSanakirjaesimerkkejä")
numerot = {
    "Viivi": "050-1234567",
    "Ahmed": "040-1112223",
    "Pekka": "050-7654321"
}

numerot["Olga"] = "050-1011012"
numerot["Mary"] = "0401-2132139"

# Sanakirjan arvoihin viitataan avaimella, joka on uniikki
numerot["Pekka"] = "poistettu"
# Sama arvo voi toistua
numerot["Ahmed"] = "050-1234567"

print(numerot)
print("Olgan numero on", numerot["Olga"])

nimi = "Pekka"
# If-lauseella voi testata, esiintyykö avain sanakirjassa
if nimi in numerot:
    print(f"Henkilön {nimi} puhelinnumero on {numerot[nimi]}.")


# ==========================================
# Esimerkki 5: Sisäkkäiset tietorakenteet
# ==========================================
print("\nEsimerkki pelaajien mahdollisesta tietorakenteesta jossain moninpelissä")

players = [
    {
        "name": "Player 1",
        "skill_level": 10,
        "inventory": {"map", "knife"}
    },
    {
        "name": "Player 2",
        "skill_level": 20,
        "inventory": {"axe"}
    }
]

# Tulostetaan pelaajien tiedot
for player in players:
    print(f"Pelaajan {player['name']} taitotaso on {player['skill_level']}, hallussa:")
    for item in player["inventory"]:
        print(f"- {item}")


# ==========================================
# Esimerkki 6: Sanakirjojen yhdistäminen ja läpikäynti (.items())
# ==========================================
sanakirja = {
    "name": "amjad",
    "ikä": 23,
    "hopes": "skater"
}

sanakirja2 = {
    "city": "Espoo", 
    "study": "metropolia",
    "hopes2": "sleep"
}

print(f"{sanakirja['name']}\n{sanakirja['ikä']}\n{sanakirja['hopes']}")
print("\n")
print(f"{sanakirja2.get('name')}\n{sanakirja2.get('ikä')}\n{sanakirja2.get('hopes2')}")

print("========================")
for key in sanakirja:
    print(f"{key}")

print("=========== right is =============")

# Yhdistetään kaksi sanakirjaa (Python 3.9+)
yhteinen = sanakirja | sanakirja2

# نستخدم items() داخل حلقات الـ for بشكل أساسي لقراءة كل من الـ key و value
for key, value in yhteinen.items():
    print(f"{key} => {value}")