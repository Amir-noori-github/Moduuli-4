# Python Moduuli - 4. Alkuehdollinen toistorakenne (while) Tehtävät
# Tehtävä-1

luku = 1  # Alustetaan luku 1:stä

while luku <= 1000:  # Silmukka jatkuu niin kauan kuin luku on enintään 1000
    if luku % 3 == 0:  # Tarkistetaan, onko luku jaollinen kolmella
        print(luku)  # Jos on, tulostetaan luku
    luku += 1  # Kasvatetaan lukua yhdellä
