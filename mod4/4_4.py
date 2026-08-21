vuosi = int(input("Vuosi: "))

if vuosi % 400 == 0:
    print(f"{vuosi} on karkausvuosi")
elif vuosi % 100 == 0:
    print(f"{vuosi} ei ole karkausvuosi")
elif vuosi % 4 == 0:
    print(f"{vuosi} on karkausvuosi")
else:
    print(f"{vuosi} ei ole karkausvuosi")