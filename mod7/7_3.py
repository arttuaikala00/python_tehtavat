galloonat = int(input("Galloonia: "))

def galloonatLitroina(galloonat):
    return galloonat * 3.785

while galloonat >= 0:
    print(galloonatLitroina(galloonat))
    galloonat = int(input("Galloonia: "))