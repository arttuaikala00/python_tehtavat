kNimi = input("Nimi: ")
kIka = int(input("Ikä: "))

if kIka < 12:
    print(f"Mee {kNimi} kotii kasvaa ja karvottuu")
    exit()
else:
    print(f"Terve {kNimi}")


while True:
    komento = input("1: jotain 2: jotain muuta 3: lopeta: ")

    match komento:
        case "1":
            print("Jotain tapahtuu")
        case "2":
            print("Jotain muuta tapahtuu")
        case "3":
            break
        case _:
            continue