from random import randint

class Auto:
    def __init__(self, rTunnus, hNopeus, nopeus):
        self.rTunnus = rTunnus
        self.hNopeus = hNopeus
        self.nopeus = nopeus
        self.kMatka = 0

    def kiihdyta(self, muutos):
        self.nopeus += muutos

        if self.nopeus > self.hNopeus:
            self.nopeus = self.hNopeus
        elif self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, aika):
        self.kMatka += aika * self.nopeus

class Sahkoauto(Auto):
    def __init__(self, rTunnus, hNopeus, nopeus, aKapasiteetti):
        super().__init__(rTunnus, hNopeus, nopeus)
        self.aKapasiteetti = aKapasiteetti

class Polttomoottoriauto(Auto):
    def __init__(self, rTunnus, hNopeus, nopeus, btKoko):
        super().__init__(rTunnus, hNopeus, nopeus)
        self.btKoko = btKoko

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
        self.autot.sort(key=lambda auto: auto.kMatka, reverse=True)
        print(f"{"Sija":<7}{"Auto":<10}{"Huippunopeus":<15}{"Matka":<10}")
        for auto in self.autot:
            print(f"{str(f"{sija}."):<7}{auto.rTunnus:<10}{auto.hNopeus:<15}{auto.kMatka:<10}")
            sija += 1

    def kilpailu_ohi(self):
        for auto in self.autot:
            if auto.kMatka >= self.pituus:
                return True
            else:
                return False


auto1 = Sahkoauto("ABC-15", 180, 80, 52.5)
auto2 = Polttomoottoriauto("ACD-123", 165, 120, 32.3)

auto1.kulje(3)
auto2.kulje(3)

print(auto1.kMatka)
print(auto2.kMatka)