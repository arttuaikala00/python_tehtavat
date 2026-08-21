luku = int(input("Luku: "))
alkuluku = True

if luku > 2:
    for i in range(2, luku):
        if luku % i == 0:
            alkuluku = False
            break

    if alkuluku:
        print(f"{luku} on alkuluku")
    else:
        print(f"{luku} ei ole alkuluku")
else:
    print(f"{luku} ei ole alkuluku")