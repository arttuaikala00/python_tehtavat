class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sMaara):
        self.kirjoittaja = kirjoittaja
        self.sMaara = sMaara
        super().__init__(nimi)

    def tulosta_tiedot(self):
        print(f"Nimi: {self.nimi}")
        print("Tyyppi: kirja")
        print(f"Kirjoittaja: {self.kirjoittaja}")
        print(f"Sivumäärä: {self.sMaara}")

class Lehti(Julkaisu):
    def __init__(self, nimi, pToimittaja):
        self.pToimittaja = pToimittaja
        super().__init__(nimi)

    def tulosta_tiedot(self):
        print(f"Nimi: {self.nimi}")
        print("Tyyppi: lehti")
        print(f"Päätoimittaja: {self.pToimittaja}")


julkaisu1 = Lehti("Aku Ankka", "Aki Hyyppä")
julkaisu2 = Kirja("Hytti n:o 6", "Rosa Liksom", 200)

julkaisu1.tulosta_tiedot()
julkaisu2.tulosta_tiedot()