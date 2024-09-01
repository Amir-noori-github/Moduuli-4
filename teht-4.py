# Python Moduuli-4, Tehtävä-4

import random

# Tietokone arpoo luvun väliltä 1..10
oikea_luku = random.randint(1, 10)

while True:
    # Pelaaja tekee arvauksen
    arvaus = int(input("Arvaa luku väliltä 1..10: "))

    # Tarkistetaan, onko arvaus oikein, liian suuri vai liian pieni
    if arvaus < oikea_luku:
        print("Liian pieni arvaus")
    elif arvaus > oikea_luku:
        print("Liian suuri arvaus")
    else:
        print("Oikein! Arvasit luvun oikein.")
        break
        # Peli loppuu, kun arvaus on oikein
