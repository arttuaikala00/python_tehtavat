import sys

sukupuoli = input("Sukupuoli (M/N): ")
if sukupuoli.lower() not in ("m", "n"):
    print("Virheellinen sukupuoli")
    sys.exit()
hemoglobiini = float(input("Hemoglobiini (g/l): "))

if sukupuoli.lower() == "m":
    if hemoglobiini < 134:
        print("Hemoglobiini arvo on alhainen")
    elif hemoglobiini > 195:
        print("Hemoglobiini arvo on korkea")
    else:
        print("Hemoglobiini arvo on normaali")
elif sukupuoli.lower() == "n":
    if hemoglobiini < 117:
        print("Hemoglobiini arvo on alhainen")
    elif hemoglobiini > 175:
        print("Hemoglobiini arvo on korkea")
    else:
        print("Hemoglobiini arvo on normaali")