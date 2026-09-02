class Reppu:
    def __init__(self):
        self.reppu = []

    def lisaa_esine(self):
        esine = input("Minkä esineen lisäät: ").capitalize()
        self.reppu.append(esine)
        print(f"{esine} lisätty reppuun")

    def poista_esine(self):
        esine = input("Minkä esineen haluat poistaa: ").capitalize()
        if esine in self.reppu:
            self.reppu.remove(esine)
            print(f"{esine} poistettu repusta")
        else:
            print(f"{esine} ei ole repussa")

    def avaa_reppu(self):
        if not self.reppu:
            print("Reppu on tyhjä")
        else:
            print("Repun sisältö:")
            for esine in self.reppu:
                print(f" - {esine}")


reppu = Reppu()

while True:
    komento = input("1: Lisää esine\n2: Poista esine\n3: Avaa reppu\n4: lopeta\n")

    match komento:
        case "1":
            reppu.lisaa_esine()
        case "2":
            reppu.poista_esine()
        case "3":
            reppu.avaa_reppu()
        case "4":
            exit()
        case _:
            continue