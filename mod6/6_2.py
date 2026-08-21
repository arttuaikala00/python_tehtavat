luku = 0
luvut = []

while luku != "":
    try:
        luku = input("Luku: ")
        luvut.append(int(luku))
    except ValueError:
        continue

luvut.sort(reverse=True)

for i in range(5):
    print(luvut[i])