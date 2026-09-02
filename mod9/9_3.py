class Auto:
    def __init__(self, rTunnus, hNopeus, nopeus, kMatka):
        self.rTunnus = rTunnus
        self.hNopeus = hNopeus
        self.nopeus = nopeus
        self.kMatka = kMatka

    def kiihdyta(self, muutos):
        self.nopeus += muutos

        if self.nopeus > self.hNopeus:
            self.nopeus = self.hNopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, aika):
        self.kMatka += aika * self.nopeus

auto = Auto("ABC-123", 142, 60, 2000)

auto.kulje(1.5)
print(auto.kMatka)