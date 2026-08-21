import random

heittoja = int(input("Arpakuutioiden määrä: "))

for i in range(heittoja):
    print(random.randint(1, 6))