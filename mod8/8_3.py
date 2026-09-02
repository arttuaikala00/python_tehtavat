asemat = {"EFHK": "Helsinki-Vantaa"}

while True:
    toiminto = input("Haluatko tallentaa uuden lentoaseman tiedot vai hakea lentoaseman tiedot(1: tallenna 2: hae 3: lopeta): ")

    if toiminto == "1":
        koodi = input("ICAO-koodi: ")
        nimi = input("Nimi: ")
        asemat[koodi] = nimi
    elif toiminto == "2":
        koodi = input("Lentoaseman ICAO-koodi: ")
        print(asemat[koodi.upper()])
    elif toiminto == "3":
        break
    else:
        continue