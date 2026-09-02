from random import randint

def heitaNoppaa():
    return randint(1, 6)

heitto = 0

while heitto != 6:
    heitto = heitaNoppaa()
    print(heitto)