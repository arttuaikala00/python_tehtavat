ktunnus = input("Käyttäjätunnus: ")
ssana = input("Salasana: ")

while ktunnus != "python" and ssana != "rules":
    print("Pääsy evätty")
    ktunnus = input("Käyttäjätunnus: ")
    ssana = input("Salasana: ")

print("Tervetuloa")