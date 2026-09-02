luvut = list(map(int, input("Listaa lukuja (erota välilyönnillä): ").split()))

def parilliset(luvut):
    parilliset = []

    for luku in luvut:
        if luku % 2 == 0:
            parilliset.append(luku)

    return parilliset

print(f"Parilliset luvut: {" ".join(map(str, parilliset(luvut)))}")