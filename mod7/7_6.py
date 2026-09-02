from math import pi

print("1. pizza")
p1Halkaisija = float(input("Pizzan halkaisija: "))
p1Hinta = float(input("Pizzan hinta: "))

print("2. pizza")
p2Halkaisija = float(input("Pizzan halkaisija: "))
p2Hinta = float(input("Pizzan hinta: "))

def pizzanYhinta(halkaisija, hinta):
    return hinta / (pi * (halkaisija / 2) ** 2)

print(f"1. pizzan yksikköhinta {pizzanYhinta(p1Halkaisija, p1Hinta):.2f}€/cm\u00B2")
print(f"2. pizzan yksikköhinta {pizzanYhinta(p2Halkaisija, p2Hinta):.2f}€/cm\u00B2")