from random import randint

maxLuku = int(input("Nopan maksimiluku: "))

def heitaNoppaa(maxLuku):
    return randint(1, maxLuku)

heitto = 0

while heitto != maxLuku:
    heitto = heitaNoppaa(maxLuku)
    print(heitto)