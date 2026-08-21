import random
import math

pisteita = int(input("Pisteiden määrä: "))
sisalla = 0

for i in range(pisteita):
    pistex = random.uniform(-1, 1)
    pistey = random.uniform(-1, 1)

    if pistex ** 2 + pistey ** 2 <= 1:
        sisalla += 1

print(f"\u03c0 \u2248 4 * (pisteet ulkona ({sisalla}) / pisteitä yhteensä ({pisteita}))")
print(f"{math.pi:.6g} \u2248 {4 * (sisalla / pisteita):.6g}")