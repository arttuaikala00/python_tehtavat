import random
import json
from pathlib import Path
from collections import Counter

virVal = "Virheellinen valinta. Yritä uudelleen\n"


class Pelaaja:
    def __init__(self):
        self.EP = 100
        self.voima = 25
        self.suoja = 0
        self.sijainti = 13
        self.viereisetHuoneet = [8, 12, 14, 18]
        self.reppu = []
        self.ase = Miekka(1)
        self.kypara = None
        self.haarniska = None
        self.saappaat = None

    def siirry_huoneeseen(self, huoneNro):

        self.EP = 100
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

        while True:
            orkitJal = [sisal for sisal in luola.huoneet[self.sijainti - 1].sisalto if isinstance(sisal, Orkki)]

            if not orkitJal:
                break

            self.taistelu(orkitJal[0])

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

    def varusta(self, varuste):
        match varuste:
            case _ if isinstance(varuste, Miekka):
                self.ase = varuste
                match varuste.taso:
                    case 1:
                        self.voima = 25
                    case 2:
                        self.voima = 50
                    case 3:
                        self.voima = 100

            case _ if isinstance(varuste, Kypara):
                self.kypara = varuste
            case _ if isinstance(varuste, Haarniska):
                self.haarniska = varuste
            case _ if isinstance(varuste, Saappaat):
                self.saappaat = varuste

        self.suoja = (
            (self.kypara.suoja if self.kypara else 0) +
            (self.haarniska.suoja if self.haarniska else 0) +
            (self.saappaat.suoja if self.saappaat else 0)
        )
        print()

    def taistelu(self, V):
        tehosteet = {
            "EPT": 0,
            "voimaT": 0,
            "suojaT": 0
        }

        def hyokkaa(hyokkaaja, puolustaja):
            voima = hyokkaaja.voima
            suoja = puolustaja.suoja

            if hyokkaaja == pelaaja and tehosteet["voimaT"] >= 1:
                voima = voima * 1.5
                tehosteet["voimaT"] -= 1
            elif puolustaja == pelaaja and tehosteet["suojaT"] >= 1:
                suoja = suoja * 1.5
                tehosteet["suojaT"] -= 1

            if random.randint(1, 100) < max(10, min(90, 50 + (voima - suoja) // 4)):
                osuma = round(random.uniform(.25, .5) * voima)
                if isinstance(hyokkaaja, Orkki) or isinstance(hyokkaaja, Jami):
                    puolustaja.EP -= osuma
                    print(f"{tulostettava_sisalto(hyokkaaja)} teki sinuun {osuma} vahinkoa.")
                else:
                    puolustaja.EP -= osuma
                    print(f"Teit {osuma} vahinkoa {tulostettava_sisalto(puolustaja)}in.")
            else:
                if isinstance(hyokkaaja, Orkki) or isinstance(hyokkaaja, Jami):
                    print(f"{tulostettava_sisalto(hyokkaaja)} ei osunut sinuun.")
                else:
                    print(f"Et osunut {tulostettava_sisalto(puolustaja)}in.")

        while True:
            

            print(f"""
{"Pelaaja":<25}{tulostettava_sisalto(V)}
{"Elämäpisteet:":<20}{pelaaja.EP:<5}{"Elämäpisteet:":<15}{V.EP}
{"Voima:":<20}{pelaaja.voima:<5}{"Voima:":<15}{V.voima}
{"Suoja:":<20}{pelaaja.suoja:<5}{"Suoja:":<15}{V.suoja}
            """)

            print("Hyökkää: 1")
            if any(isinstance(esine, Leipa) for esine in pelaaja.reppu):
                print("Syö leipä (+30EP): 2")
            if any(isinstance(esine, Elamajuoma) for esine in pelaaja.reppu):
                print("Juo elämäjuoma (+15EP kolmen kierroksen ajan): 3")
            if any(isinstance(esine, Voimajuoma) for esine in pelaaja.reppu):
                print("Juo voimajuoma (+50% voima kolmen kierroksen ajan): 4")
            if any(isinstance(esine, Suojajuoma) for esine in pelaaja.reppu):
                print("Juo suojajuoma (+50% suoja kolmen kierroksen ajan): 5")
            print()

            while True:
                toiminto = input()
                print()

                match toiminto:
                    case "1":
                        hyokkaa(pelaaja, V)
                    case "2":
                        pelaaja.EP = min(100, pelaaja.EP + 30)
                    case "3":
                        tehosteet["EPT"] += 3
                    case "4":
                        tehosteet["voimaT"] += 3
                    case "5":
                        tehosteet["suojaT"] += 3
                    case _:
                        print(virVal)
                        continue
                break

            if tehosteet["EPT"] >= 1:
                pelaaja.EP = min(100, pelaaja.EP + 15)
                tehosteet["EPT"] -= 1
            
            if V.EP <= 0:
                print(f"Päihitit {tulostettava_sisalto(V)}")
                print()
                if isinstance(V, Orkki):
                    luola.huoneet[pelaaja.sijainti - 1].sisalto.remove(V)
                break

            hyokkaa(V, pelaaja)
            print()

            if pelaaja.EP <= 0:
                print("Kuolit.")

                tilastot("havityt pelit")

                print()
                lopeta_peli()
                break

    def tyopoyta(self):
        def kuluta_resurssit(maara):
            for i in range(maara):
                self.reppu.remove(next(e for e in self.reppu if isinstance(e, Rautamalmi)))
                self.reppu.remove(next(e for e in self.reppu if isinstance(e, Lisko)))
                self.reppu.remove(next(e for e in self.reppu if isinstance(e, Villa)))

        def valmista_juoma(yrttiMaara, tyyppi):
            if yrttiMaara >= 1:
                self.reppu.remove(next(e for e in self.reppu if isinstance(e, Yrtti)))
                match tyyppi:
                    case "E":
                        self.reppu.extend(Elamajuoma() * 3)
                    case "V":
                        self.reppu.extend(Voimajuoma() * 3)
                    case "S":
                        self.reppu.extend(Suojajuoma() * 3)
            else:
                print("Sinulla ei ole tarpeeksi yrttejä.")

        while True:
            self.tulosta_tavaraluettelo()

            print("Miekka (2): 2 rautaharkko, 2 nahka, 2 villa (+75 voima): 1")
            print("Kypärä (2): 2 rautaharkko, 2 nahka, 2 villa (+20 suoja): 2")
            print("Haarniska (2): 3 rautaharkko, 3 nahka, 3 villa (+30 suoja): 3")
            print("Saappaat (2): 1 rautaharkko, 1 nahka, 1 villa (+10 suoja): 4")
            print("Leipä: 2 vilja (+30 elämäpisteet): 5")
            print("Elämäjuoma: 1 yrtti (+15 eläpisteet kolmen kierroksen ajan): 6")
            print("Voimajuoma: 1 yrtti (+50% voima kolmen kierroksen ajan): 7")
            print("Suojajuoma: 1 yrtti (+50% suoja kolmen kierroksen ajan): 8")
            print("Poistu: 0")
            print()

            valinta = input("Valmista: ")
            print()

            rautaMaara = sum(isinstance(esine, Rautamalmi) for esine in self.reppu)
            liskoMaara = sum(isinstance(esine, Lisko) for esine in self.reppu)
            villaMaara = sum(isinstance(esine, Villa) for esine in self.reppu)
            vehnaMaara = sum(isinstance(esine, Vehna) for esine in self.reppu)
            yrttiMaara = sum(isinstance(esine, Yrtti) for esine in self.reppu)

            match valinta:
                case "1":
                    if rautaMaara >= 2 and liskoMaara >= 2 and villaMaara >= 2:
                        if not self.ase or self.ase.taso < 2:
                            kuluta_resurssit(2)
                            self.varusta(Miekka(2))
                            print("Valmistit: Miekka(2)")
                        else:
                            print("Sinulla on jo hyvä miekka.")
                    else:
                        print("Resurssit eivät riitä miekka(2) valmistamiseen.")
                case "2":
                    if rautaMaara >= 2 and liskoMaara >= 2 and villaMaara >= 2:
                        if not self.kypara or self.kypara.taso < 2:
                            kuluta_resurssit(2)
                            self.varusta(Kypara(2))
                            print("Valmistit: Kypärä(2)")
                        else:
                            print("Sinulla on jo hyvä kypärä")
                    else:
                        print("Resurssit eivät riitä kypärän(2) valmistamiseen.")
                case "3":
                    if rautaMaara >= 3 and liskoMaara >= 3 and villaMaara >= 3:
                        if not self.haarniska or self.haarniska.taso < 2:
                            kuluta_resurssit(3)
                            self.varusta(Haarniska(2))
                            print("Valmistit: Haarniska(2)")
                        else:
                            print("Sinulla on jo hyvä haarniska")
                    else:
                        print("Resurssit eivät riitä haarniskan(2) valmistamiseen.")
                case "4":
                    if rautaMaara >= 1 and liskoMaara >= 1 and villaMaara >= 1:
                        if not self.saappaat or self.saappaat.taso < 2:
                            kuluta_resurssit(1)
                            self.varusta(Saappaat(2))
                            print("Valmistit: Saappaat(2)")
                        else:
                            print("Sinulla on jo hyvät saappaat")
                    else:
                        print("Resurssit eivät riitä saappaiden(2) valmistamiseen.")
                case "5":
                    if vehnaMaara >= 2:
                        leipia = vehnaMaara // 2
                        for i in range (leipia):
                            self.reppu.append(Leipa())

                        for i in range(leipia * 2):
                            self.reppu.remove(next(e for e in self.reppu if isinstance(e, Vehna)))

                        print(f"Valmistit {leipia} leipää.")
                    else:
                        print("Sinulla ei ole tarpeeksi vehnää.")
                case "6":
                    valmista_juoma(yrttiMaara, "E")
                case "7":
                    valmista_juoma(yrttiMaara, "V")
                case "8":
                    valmista_juoma(yrttiMaara, "S")
                case "0":
                    break
                case _:
                    print(virVal)
            print()
        print()

class Luola:
    def __init__(self):
        self.arkJaljella = [Miekka(3), Kypara(3), Haarniska(3), Saappaat(3)]
        self.huoneet = []
        tyhjatHuoneet = list(range(1, 26))

        huoneNro = 13
        self.huoneet.append(Kotihuone(huoneNro))
        tyhjatHuoneet.remove(huoneNro)

        for i in range(2):
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

        if self.huoneet[kohdeHuone].sisalto:
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
                valinta = input(f"Haluatko siirtyä huoneeseen {huoneNro}? (1: K /2: E): ")
                print()

                match valinta:
                    case "1":
                        pelaaja.siirry_huoneeseen(huoneNro)
                        return
                    case "2":
                        break
                    case _:
                        pass
       
    def huonevalikko(self):
        while True:
            kohdeHuone = self.huoneet[pelaaja.sijainti - 1]


            self.tulosta_huone(pelaaja.sijainti)
            self.tulosta_huone_sisalto(pelaaja.sijainti)

            print("Avaa tavaraluettelo: 1")
            print("Avaa kartta: 2")
            print("Valaise huone: 3")

            if any(resurssi in kohdeHuone.sisalto for resurssi in resurssit) or any(
                isinstance(esine, Arkku) for esine in kohdeHuone.sisalto):
                print("Kerää resurssit: 4")

            if isinstance(kohdeHuone, Kotihuone):
                print("Avaa työpöytä: 8")
                print("Mene kellariin: 9")
                print("Poistu pelistä: 0")
            
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
                            pass
                case "4" if any(
                        any(isinstance(esine, type(resurssiA)) for resurssiA in resurssitA)
                        for esine in kohdeHuone.sisalto
                    ):
                    self.keraa_resurssit(pelaaja.sijainti)
                case "8" if isinstance(kohdeHuone, Kotihuone):
                    pelaaja.tyopoyta()
                case "9" if isinstance(kohdeHuone, Kotihuone):
                    pelaaja.EP = 100
                    pelaaja.taistelu(Jami())

                    tilastot("voitetut pelit")

                    print("Voitit pelin!")
                    lopeta_peli()
                case "0" if isinstance(kohdeHuone, Kotihuone):
                    lopeta_peli()
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
                    elif not (1 <= huone <= 25):
                        raise ValueError
                    elif not luola.huoneet[huone - 1].avattu:
                        print(f"Huonetta {huone} ei ole valaistu.")
                        print()
                        continue

                    pelaaja.siirry_huoneeseen(huone)
                    break
                except ValueError:
                    print("Valitse luku 1 ja 25 väliltä.")
                    print()
            break

    def keraa_resurssit(self, huoneNro):
        kohdeHuone = self.huoneet[huoneNro - 1]

        for esine in kohdeHuone.sisalto[:]:
            if esine in resurssit:
                kohdeHuone.sisalto.remove(esine)
                match esine:
                    case _ if isinstance(esine, Rautamalmi):
                        pelaaja.reppu.append(esine)
                        print("Louhit rautamalmin. +1 rautaharkko.")
                    case _ if isinstance(esine, Lisko):
                        pelaaja.reppu.append(esine)
                        print("Metsästit liskon. +1 nahka.")
                    case _ if isinstance(esine, Villa):
                        pelaaja.reppu.append(esine)
                        print("Poimit puuvillakasvin. +1 villa.")
                    case _ if isinstance(esine, Vehna):
                        pelaaja.reppu.extend([esine] * 5)
                        print("Poimit vehnäsadon. +3 vehnä.")
                    case _ if isinstance(esine, Yrtti):
                        pelaaja.reppu.append(esine)
                        print("Poimit yrtin. +1 yrtti.")

            elif isinstance(esine, Arkku):
                kohdeHuone.sisalto.remove(esine)
                varuste = random.choice(self.arkJaljella)
                self.arkJaljella.remove(varuste)
                match varuste:
                    case _ if isinstance(varuste, Miekka):
                        pelaaja.varusta(Miekka(3))
                        print("Löysit arkusta miekan(3)")
                    case _ if isinstance(varuste, Kypara):
                        pelaaja.varusta(Kypara(3))
                        print("Löysit arkusta kypärän(3)")
                    case _ if isinstance(varuste, Haarniska):
                        pelaaja.varusta(Haarniska(3))
                        print("Löysit arkusta haarniskan(3)")
                    case _ if isinstance(varuste, Saappaat):
                        pelaaja.varusta(Saappaat(3))
                        print("Löysit arkusta sappaat(3)")

        print()

class Huone:
    def __init__(self, huoneNro):
        self.huoneNro = huoneNro
        self.sisalto = []
        self.avattu = False

    def luo_tulostettava_sisalto(self):
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

class Leipa:
    pass

class Elamajuoma:
    pass

class Voimajuoma:
    pass

class Suojajuoma:
    pass

class Miekka:
    def __init__(self, taso):
        self.taso = taso

class Kypara:
    def __init__(self, taso):
        self.taso = taso

        match self.taso:
            case 2:
                self.suoja = 20
            case 3:
                self.suoja = 50

class Haarniska:
    def __init__(self, taso):
        self.taso = taso

        match self.taso:
            case 2:
                self.suoja = 30
            case 3:
                self.suoja = 75

class Saappaat:
    def __init__(self, taso):
        self.taso = taso

        match self.taso:
            case 2:
                self.suoja = 10
            case 3:
                self.suoja = 25

class Orkki:
    def __init__(self, taso):
        self.taso = taso

        match self.taso:
            case 2:
                self.EP = 50
                self.voima = 25
                self.suoja = 5
            case 3:
                self.EP = 100
                self.voima = 50
                self.suoja = 10
            case _:
                self.EP = 25
                self.voima = 10
                self.suoja = 0

class Jami:
    def __init__(self):
        self.EP = 500
        self.voima = 100
        self.suoja = 50

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
        print("Tilastot: 2")
        print()

        valinta = input()
        print()

        match valinta:
            case "1":
                aloita_peli()
                break
            case "2":
                tiedosto = Path(__file__).parent / "tilastot.json"
                with open(tiedosto, "r", encoding="utf-8") as tiedosto:
                    data = json.load(tiedosto)
                    pelPelit = data["tilastot"]["aloitetut pelit"]
                    voiPelit = data["tilastot"]["voitetut pelit"]
                    havPelit = data["tilastot"]["havityt pelit"]
                    if voiPelit + havPelit > 0:
                        voittoPros = voiPelit / (voiPelit + havPelit) * 100
                    else:
                        voittoPros = None

                    print(f"Aloitetut pelit: {pelPelit}")
                    print(f"Voitetut pelit: {voiPelit}")
                    print(f"Hävityt pelit: {havPelit}")
                    if voittoPros is not None:
                        print(f"Voittoprosentti: {voittoPros:1f}%")
                    print()
            case _:
                print(virVal)

def aloita_peli():
    global pelaaja
    pelaaja = Pelaaja()
    global luola
    luola = Luola()

    tilastot("aloitetut pelit")

    pelaaja.siirry_huoneeseen(pelaaja.sijainti)
    luola.huonevalikko()

def lopeta_peli():
    global pelaaja
    del pelaaja
    global luola
    del luola
    paavalikko()

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
        case Jami():
            return "Jami"
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
        case Leipa():
            return "Leipä"
        case Elamajuoma():
            return "Elämäjuoma"
        case Voimajuoma():
            return "Voimajuoma"
        case Suojajuoma():
            return "Suojajuoma"

def tilastot(tilasto):
    tiedosto_polku = Path(__file__).parent / "tilastot.json"

    with open(tiedosto_polku, "r", encoding="utf-8") as tiedosto:
        data = json.load(tiedosto)

    data["tilastot"][tilasto] += 1

    with open(tiedosto_polku, "w", encoding="utf-8") as tiedosto:
        json.dump(data, tiedosto, indent=4)

global resurssit
resurssit = (
    Rautamalmi(),
    Lisko(),
    Villa(),
    Vehna(),
    Yrtti()
)

global resurssitaA
resurssitA = (
    Rautamalmi(),
    Lisko(),
    Villa(),
    Vehna(),
    Yrtti(),
    Arkku()
)

if __name__ == "__main__":
    paavalikko()