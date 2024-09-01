# Python Moduuli-4, Tehtävä-5

# Oikeat käyttäjätunnus ja salasana
oikea_kayttajatunnus = "python"
oikea_salasana = "rules"

# Laskuri epäonnistuneille yrityksille
yrityksia = 0
maksimi_yritykset = 5

while yrityksia < maksimi_yritykset:
    # Pyydetään käyttäjältä tunnus ja salasana
    kayttajatunnus = input("Anna käyttäjätunnus: ")
    salasana = input("Anna salasana: ")

    # Tarkistetaan, ovatko sekä käyttäjätunnus että salasana oikein
    if kayttajatunnus == oikea_kayttajatunnus and salasana == oikea_salasana:
        print("Tervetuloa!")
        break  # Kirjautuminen onnistui, lopetetaan silmukka
    else:
        yrityksia += 1  # Lisätään yritysten määrää
        print("Virheellinen käyttäjätunnus tai salasana.")

    # Tarkistetaan, onko yrityksiä jäljellä
    if yrityksia == maksimi_yritykset:
        print("Pääsy evätty.")

