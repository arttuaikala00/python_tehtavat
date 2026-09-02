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

autot = []
for i in range(10):
    autot.append(Auto(f"ABC-{i + 1}", randint(100, 200)))

jatkuu = True
while jatkuu:
    for auto in autot:
        auto.kiihdyta(randint(-10, 15))

    for auto in autot:
        auto.kulje(1)

    for auto in autot:
        if auto.kMatka >= 10000:
            jatkuu = False
            break
        else:
            continue

autot.sort(key=lambda auto: auto.kMatka, reverse=True)
sija = 1
print(f"{"Sija":<7}{"Auto":<10}{"Huippunopeus":<15}{"Matka":<10}")
for auto in autot:
    print(f"{str(f"{sija}."):<7}{auto.rTunnus:<10}{auto.hNopeus:<15}{auto.kMatka:<10}")
    sija += 1