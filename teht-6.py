# Python Moduuli-4, Tehtävä-6

import random

# Kysytään käyttäjältä arvottavien pisteiden määrä
N = int(input("Anna arvottavien pisteiden määrä: "))

# Muuttujat ympyrän sisälle jäävien pisteiden ja kokonaispisteiden laskemiseen
n = 0

for _ in range(N):
    # Arvotaan satunnaiset pisteet (x, y) välillä [-1, 1]
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    # Tarkistetaan, onko piste (x, y) yksikköympyrän sisällä (x^2 + y^2 < 1)
    if x ** 2 + y ** 2 < 1:
        n += 1

# Lasketaan piin likiarvo kaavalla π ≈ 4 * (n / N)
pi_approximation = 4 * (n / N)

# Tulostetaan piin likiarvo
print(f"Piin likiarvo on: {pi_approximation}")
