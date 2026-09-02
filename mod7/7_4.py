luvut = list(map(int, input("Listaa lukuja (erota välilyönnillä): ").split()))

def listanSumma(luvut):
    return sum(luvut)

print(f"Summa: {listanSumma(luvut)}")