leiviskat = float(input("Anna leiviskät.\n"))
naulat = float(input("\nAnna naulat.\n"))
luodit = float(input("\nAnna luodit.\n"))

grammat = ((leiviskat * 20 + naulat) * 32 + luodit) * 13.3
print(f"\n{grammat // 1000:.0f} kilogrammaa ja {grammat % 1000:.2f} grammaa")