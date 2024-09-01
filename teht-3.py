# Python Moduuli-4, Tehtävä-3

# Alustetaan lista tallentamaan käyttäjän syöttämät luvut
luvut = []

while True:
    syote = input("Anna luku (tyhjä syöte lopettaa): ")  # Pyydetään käyttäjää syöttämään luku

    if syote == "":  # Jos syöte on tyhjä, silmukka lopetetaan
        break

    try:
        luku = float(syote)  # Yritetään muuntaa syöte luvuksi
        luvut.append(luku)  # Lisätään luku listaan
    except ValueError:
        print("Syötä kelvollinen luku.")  # Jos syöte ei ole luku, ilmoitetaan virheestä

# Tarkistetaan, onko listassa lukuja
if luvut:
    pienin = min(luvut)  # Etsitään pienin luku
    suurin = max(luvut)  # Etsitään suurin luku
    print(f"Pienin syötetty luku on: {pienin}")
    print(f"Suurin syötetty luku on: {suurin}")
else:
    print("Et syöttänyt yhtään lukua.")  # Jos käyttäjä ei syöttänyt yhtään lukua
