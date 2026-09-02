nimet = set()

while True:
    nimi = input("Nimi: ")

    if nimi == "":
        break

    if nimi in nimet:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        nimet.add(nimi)

for nimi in nimet:
    print(nimi)