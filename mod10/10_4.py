from random import randint

class Auto:
    def __init__(self, rTunnus, hNopeus):
        self.rTunnus = rTunnus
        self.hNopeus = hNopeus
        self.nopeus = 0
        self.kMatka = 0

    def kiihdyta(self, muutos):
        self.nopeus += muutos

        if self.nopeus > self.hNopeus:
            self.nopeus = self.hNopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, aika):
        self.kMatka += aika * self.nopeus

class Kilpailu:
    def __init__(self, nimi, pituus, autot):
        self.nimi = nimi
        self.pituus = pituus
        self.autot = autot

    def tunti_kuluu(self):
        for auto in self.autot:
            auto.kiihdyta(randint(-10, 15))
            auto.kulje(1)

    def tulosta_tilanne(self):
        sija = 1
        autot.sort(key=lambda auto: auto.kMatka, reverse=True)
        print(f"{"Sija":<7}{"Auto":<10}{"Huippunopeus":<15}{"Matka":<10}")
        for auto in autot:
            print(f"{str(f"{sija}."):<7}{auto.rTunnus:<10}{auto.hNopeus:<15}{auto.kMatka:<10}")
            sija += 1

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kMatka >= self.pituus:
                return True
            else:
                return False


autot = []
for i in range(10):
    autot.append(Auto(f"ABC-{i + 1}", randint(100, 200)))

kilpailu = Kilpailu("Suuri romuralli", 8000, autot)

while not kilpailu.kilpailu_ohi():
    for i in range(10):
        kilpailu.tunti_kuluu()

        if kilpailu.kilpailu_ohi():
            break

    kilpailu.tulosta_tilanne()