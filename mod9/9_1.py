class Auto:
    def __init__(self, rTunnus, hNopeus):
        self.rTunnus = rTunnus
        self.hNopeus = hNopeus
        self.nopeus = 0
        self.kMatka = 0

auto = Auto("ABC-123", 142)

print(f"Auton rekisteritunnus: {auto.rTunnus}")
print(f"Auton huippunopeus: {auto.hNopeus}km/h")
print(f"Auton tämänhetkinen nopeus: {auto.nopeus}km/h")
print(f"Auton kuljettu matka: {auto.kMatka}km")