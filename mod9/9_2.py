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

auto = Auto("ABC-123", 142)

auto.kiihdyta(30)
auto.kiihdyta(70)
auto.kiihdyta(50)
print(auto.nopeus)
auto.kiihdyta(-200)
print(auto.nopeus)