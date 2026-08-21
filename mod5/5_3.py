luku = 0
luvut = []

while luku != "":
    try:
        luku = input("Luku: ")
        luvut.append(float(luku))
    except ValueError:
        continue

print(f"Pienin luku: {min(luvut)}\nSuurin luku: {max(luvut)}")