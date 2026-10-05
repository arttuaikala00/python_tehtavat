import random


def main():
    luola = Luola()
    luola.tulosta_luola()
    print("1")
    luola.tulosta_huone(1)
    print("3")
    luola.tulosta_huone(3)
    print("5")
    luola.tulosta_huone(5)
    print("11")
    luola.tulosta_huone(11)
    print("13")
    luola.tulosta_huone(13)
    print("15")
    luola.tulosta_huone(15)
    print("21")
    luola.tulosta_huone(21)
    print("23")
    luola.tulosta_huone(23)
    print("25")
    luola.tulosta_huone(25)


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

    def tulosta_huone(self, huoneNro): #debug: sais tehtyy paremmin
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

class Huone:
    def __init__(self, huoneNro):
        self.huoneNro = huoneNro
        self.sisalto = []
        self.avattu = True

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
        for i in range(random.randint(2, 4)):
            self.sisalto.append(Resurssi())
        if random.randint(0, 1) == 0:
            self.sisalto.append(Orkki1())

class Orkkihuone(Huone):
    def __init__(self, huoneNro):
        super().__init__(huoneNro)
        for i in range(3):
            if random.random() < 2/3:
                self.sisalto.append(Orkki2())
            else:
                self.sisalto.append(Orkki1())

class Aarrehuone(Huone):
    def __init__(self, huoneNro):
        super().__init__(huoneNro)
        self.sisalto.append(Arkku())
        self.sisalto.append(Orkki3())

class Kotihuone(Huone):
    def __init__(self, huoneNro):
        super().__init__(huoneNro)
        self.avattu = True
        self.sisalto.append(Portaat())
        self.sisalto.append(Tyopoyta())
        self.sisalto.append(Kellari())

class Resurssi:
    def __init__(self):
        self.tyyppi = random.choice(("Rautamalmi", "Lisko", "Villa", "Vehna", "Yrtti"))

class Orkki:
    def __init__(self):
        pass

class Orkki1(Orkki):
    def __init__(self):
        pass

class Orkki2(Orkki):
    def __init__(self):
        pass

class Orkki3(Orkki):
    def __init__(self):
        pass

class Arkku():
    def __init__(self):
        pass

class Portaat():
    def __init__(self):
        pass

class Tyopoyta():
    def __init__(self):
        pass

class Kellari():
    def __init__(self):
        pass

def tulostettava_muoto(olio):
    match olio:
        case Resurssi(tyyppi="Rautamalmi"):
            return "Ra"
        case Resurssi(tyyppi="Lisko"):
            return "Li"
        case Resurssi(tyyppi="Villa"):
            return "Vi"
        case Resurssi(tyyppi="Vehna"):
            return "Ve"
        case Resurssi(tyyppi="Yrtti"):
            return "Yr"
        case Orkki1():
            return "Ö1"
        case Orkki2():
            return "Ö2"
        case Orkki3():
            return "Ö3"
        case Arkku():
            return "Ar"
        case Portaat():
            return "Po"
        case Tyopoyta():
            return "Ty"
        case Kellari():
            return "Ke"


if __name__ == "__main__":
    main()