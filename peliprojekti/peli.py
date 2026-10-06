import random
from collections import Counter


virVal = "Virheellinen valinta. Yritä uudelleen\n"


def main():
    global pelaaja
    pelaaja = Pelaaja()
    global luola
    luola = Luola()

    pelaaja.siirry_huoneeseen(pelaaja.sijainti)


class Pelaaja:
    def __init__(self):
        self.sijainti = 13
        self.viereisetHuoneet = [8, 12, 14, 18]
        self.reppu = []
        self.ase = Miekka(1)
        self.kypara = None
        self.haarniska = None
        self.saappaat = None

    def siirry_huoneeseen(self, huoneNro):
        if huoneNro == 0:
            return
        elif 1 >= huoneNro >= 25:
            raise Exception("Valitse luku 1 ja 25 väliltä.")

        if not luola.huoneet[huoneNro - 1].avattu:
            print(f"Huonetta {huoneNro} ei ole valaistu.")
            print()
            return

        self.sijainti = huoneNro
        self.viereisetHuoneet = []
        if self.sijainti > 5:
            self.viereisetHuoneet.append(self.sijainti - 5)
        if self.sijainti % 5 != 0:
            self.viereisetHuoneet.append(self.sijainti + 1)
        if self.sijainti % 5 != 1:
            self.viereisetHuoneet.append(self.sijainti - 1)
        if self.sijainti < 20:
            self.viereisetHuoneet.append(self.sijainti + 5)
        luola.huonevalikko()

    def tulosta_tavaraluettelo(self):
        print("Sinulla on päälläsi:")
        if self.ase: print(f" {tulostettava_esine(self.ase)}")
        if self.kypara: print(f" {tulostettava_esine(self.kypara)}")
        if self.haarniska: print(f" {tulostettava_esine(self.haarniska)}")
        if self.saappaat: print(f" {tulostettava_esine(self.saappaat)}")
        print()

        if self.reppu:
            print("Repussasi on:")
            for esine_tyyppi, maara in Counter(type(esine) for esine in self.reppu).items():
                esine = next(esine for esine in self.reppu if type(esine) is esine_tyyppi)
                if maara > 1:
                    print(f" - {maara}x {tulostettava_esine(esine)}")
                else:
                    print(f" - {tulostettava_esine(esine)}")
        else:
            print("Reppusi on tyhjä.")
        print()

class Luola:
    def __init__(self):
        self.huoneet = []
        tyhjatHuoneet = list(range(1, 26))

        huoneNro = 13
        self.huoneet.append(Kotihuone(huoneNro))
        tyhjatHuoneet.remove(huoneNro)

        for i in range(random.randint(2, 4)):
            huoneNro = random.choice(tyhjatHuoneet)
            self.huoneet.append(Aarrehuone(huoneNro))
            tyhjatHuoneet.remove(huoneNro)

        for i in range(len(tyhjatHuoneet)):
            huoneNro = random.choice(tyhjatHuoneet)
            if random.randint(1, 3) <= 2:
                self.huoneet.append(Resurssihuone(huoneNro))
            else:
                self.huoneet.append(Orkkihuone(huoneNro))
            tyhjatHuoneet.remove(huoneNro)

        self.huoneet.sort(key=lambda huone: huone.huoneNro)

    def tulosta_luola(self):
        for huone in self.huoneet:
            huone.luo_tulostettava_sisalto()

        for luolaRivi in range(5):
            for huoneRivi in range(3):
                riviTulostus = []
                for luolaSarake in range(5):
                    huone = self.huoneet[luolaRivi * 5 + luolaSarake]
                    riviTulostus.extend(huone.huoneMatriisi[huoneRivi])
                    if luolaSarake <= 3:
                        riviTulostus.extend([" "])
                print(" ".join(riviTulostus))
            print()

    def tulosta_huone(self, huoneNro):
        for huone in self.huoneet:
            huone.luo_tulostettava_sisalto()

        kohdeHuone = huoneNro - 1

        if kohdeHuone // 5 > 0:
            huone = self.huoneet[kohdeHuone - 5]
            for huoneRivi in range(3):
                riviTulostus = []
                if kohdeHuone % 5 >= 1:
                    riviTulostus.append(" " * 10)
                riviTulostus.extend(huone.huoneMatriisi[huoneRivi])
                print(" ".join(riviTulostus))
            print()

        for huoneRivi in range(3):
            riviTulostus = []
            for luolaSarake in range(max(0, kohdeHuone % 5 - 1), min(4, kohdeHuone % 5 + 1) + 1):
                huone = self.huoneet[kohdeHuone // 5 * 5 + luolaSarake]
                if riviTulostus:
                    riviTulostus.append(" ")
                riviTulostus.extend(huone.huoneMatriisi[huoneRivi])
            print(" ".join(riviTulostus))
        print()

        if kohdeHuone // 5 < 4:
            huone = self.huoneet[kohdeHuone + 5]
            for huoneRivi in range(3):
                riviTulostus = []
                if (kohdeHuone - 5) % 5 >= 1:
                    riviTulostus.append(" " * 10)
                riviTulostus.extend(huone.huoneMatriisi[huoneRivi])
                print(" ".join(riviTulostus))
            print()

    def tulosta_huone_sisalto(self, huoneNro):
        kohdeHuone = huoneNro - 1

        print("Huoneen sisältö:")
        for sisalto in self.huoneet[kohdeHuone].sisalto:
            print(f" - {tulostettava_sisalto(sisalto)}")
        print()

    def valaise_huone(self, huoneNro):
        if huoneNro not in pelaaja.viereisetHuoneet:
            raise Exception("Valitse viereisesti huone")

        kohdeHuone = huoneNro - 1

        if self.huoneet[kohdeHuone].avattu:
            print(f"Huone {huoneNro} on jo valaistu")
            print()
        else:
            self.huoneet[kohdeHuone].avattu = True
            print(f"Huone {huoneNro} on nyt valaistu.")
            print()

            self.tulosta_huone(huoneNro)

            while True:
                valinta = input(f"Haluatko siirtyä huoneeseen {huoneNro}? (K/E): ")
                print()

                match valinta.upper():
                    case "K":
                        pelaaja.siirry_huoneeseen(huoneNro)
                        return
                    case "E":
                        break
                    case _:
                        pass
       
    def huonevalikko(self):
        while True:
            self.tulosta_huone(pelaaja.sijainti)
            self.tulosta_huone_sisalto(pelaaja.sijainti)

            print("Avaa tavaraluettelo: 1")
            print("Avaa kartta: 2")
            print("Valaise huone: 3")
            print("")
            print()

            valinta = input()
            print()
            match valinta:
                case "1":
                    pelaaja.tulosta_tavaraluettelo()
                case "2":
                    self.karttavalikko()
                case "3":
                    while True:
                        try:
                            huone = int(input("Valitse viereisesi huone (Poistu: 0): "))
                            print()
                            if huone == 0:
                                break
                            self.valaise_huone(huone)
                            break
                        except:
                            print()
                case _:
                    print(virVal)

    def karttavalikko(self):
        while True:
            self.tulosta_luola()

            while True:
                try:
                    huone = int(input("Siirry huoneeseen (Poistu: 0): "))
                    print()
                    if huone == 0:
                        break
                    pelaaja.siirry_huoneeseen(huone)
                    break
                except ValueError:
                    print()
                    print("Valitse luku 1 ja 25 väliltä.")
                    print()
            break

class Huone:
    def __init__(self, huoneNro):
        self.huoneNro = huoneNro
        self.sisalto = []
        self.avattu = False

    def luo_tulostettava_sisalto(self): #debug: shuffle kuntoo
        self.tulostettavaSisalto = []
        if self.avattu:
            for olio in self.sisalto:
                self.tulostettavaSisalto.append(tulostettava_muoto(olio))

        for i in range(8 - len(self.tulostettavaSisalto)):
            if self.avattu:
                self.tulostettavaSisalto.append("00")
            else:
                self.tulostettavaSisalto.append("??")

        random.shuffle(self.tulostettavaSisalto)
        self.tulostettavaSisalto.insert(4, f"{self.huoneNro:02d}")

        self.huoneMatriisi = [
            self.tulostettavaSisalto[i:i + 3]
            for i in range(0, len(self.tulostettavaSisalto), 3)
            ]

class Resurssihuone(Huone):
    def __init__(self, huoneNro):
        super().__init__(huoneNro)

        resurssit = (
            Rautamalmi(),
            Lisko(),
            Villa(),
            Vehna(),
            Yrtti()
        )

        for i in range(random.randint(2, 4)):
            self.sisalto.append(random.choice(resurssit))
        if random.randint(0, 1) == 0:
            self.sisalto.append(Orkki(1))

class Orkkihuone(Huone):
    def __init__(self, huoneNro):
        super().__init__(huoneNro)
        for i in range(3):
            if random.random() < 2/3:
                self.sisalto.append(Orkki(2))
            else:
                self.sisalto.append(Orkki(1))

class Aarrehuone(Huone):
    def __init__(self, huoneNro):
        super().__init__(huoneNro)
        self.sisalto.append(Arkku())
        self.sisalto.append(Orkki(3))

class Kotihuone(Huone):
    def __init__(self, huoneNro):
        super().__init__(huoneNro)
        self.avattu = True
        self.sisalto.append(Tyopoyta())
        self.sisalto.append(Portaat())
        self.sisalto.append(Kellari())

class Rautamalmi:
    pass

class Lisko:
    pass

class Villa:
    pass

class Vehna:
    pass

class Yrtti:
    pass

class Miekka:
    def __init__(self, taso):
        self.taso = taso

class Kypara:
    def __init__(self, taso):
        self.taso = taso

class Haarniska:
    def __init__(self, taso):
        self.taso = taso

class Saappaat:
    def __init__(self, taso):
        self.taso = taso

class Orkki:
    def __init__(self, taso):
        self.taso = taso

class Arkku:
    pass

class Portaat:
    pass

class Tyopoyta:
    pass

class Kellari:
    pass

def paavalikko():
    while True:
        print("Aloita peli: 1")

        valinta = input()

        match valinta:
            case "1":
                aloita_peli()
                break
            case _:
                print(virVal)

def aloita_peli():
    global pelaaja
    pelaaja = Pelaaja()
    global luola
    luola = Luola()

    pelaaja.siirry_huoneeseen(pelaaja.sijainti)

def tulostettava_muoto(olio):
    match olio:
        case Rautamalmi():
            return "Ra"
        case Lisko():
            return "Li"
        case Villa():
            return "Vi"
        case Vehna():
            return "Ve"
        case Yrtti():
            return "Yr"
        case Orkki(taso=taso):
            return f"Ö{taso}"
        case Arkku():
            return "Ar"
        case Portaat():
            return "Po"
        case Tyopoyta():
            return "Ty"
        case Kellari():
            return "Ke"

def tulostettava_sisalto(olio):
    match olio:
        case Rautamalmi():
            return "Rautamalmi"
        case Lisko():
            return "Lisko"
        case Villa():
            return "Villa"
        case Vehna():
            return "Vehnä"
        case Yrtti():
            return "Yrtti"
        case Orkki(taso=taso):
            return f"Örkki ({taso})"
        case Arkku():
            return "Arkku"
        case Portaat():
            return "Portaat"
        case Tyopoyta():
            return "Työpöytä"
        case Kellari():
            return "Kellari"

def tulostettava_esine(olio):
    match olio:
        case Rautamalmi():
            return "Rautaharkko"
        case Lisko():
            return "Nahka"
        case Villa():
            return "Villa"
        case Vehna():
            return "Vehnä"
        case Yrtti():
            return "Yrtti"
        case Miekka(taso=taso):
            return f"Miekka ({taso})"
        case Kypara(taso=taso):
            return f"Kypärä ({taso})"
        case Haarniska(taso=taso):
            return f"Haarniska ({taso})"
        case Saappaat(taso=taso):
            return f"Saappaat ({taso})"


if __name__ == "__main__":
    main()