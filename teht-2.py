# Python Moduuli-4, Tehtävä-2

while True:  # Loputon silmukka, joka jatkuu, kunnes käyttäjä syöttää negatiivisen luvun
    tuumat = float(input("Anna tuumamäärä (negatiivinen luku lopettaa): "))  # Pyydetään käyttäjää syöttämään tuumamäärä

    if tuumat < 0:  # Tarkistetaan, onko syötetty luku negatiivinen
        print("Ohjelma lopetettu.")
        break  # Jos luku on negatiivinen, katkaistaan silmukka ja lopetetaan ohjelma

    sentit = tuumat * 2, 54  # Muunnetaan tuumat senttimetreiksi
    print(f"{tuumat} tuumaa on {sentit} senttimetriä.")  # Tulostetaan tulos
