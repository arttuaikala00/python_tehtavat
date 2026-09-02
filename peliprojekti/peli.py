import random

class Pelaaja:
    def __init__(self):
        self.HP = 100

class Huone:
    def __init__(self):
        pass

class Resurssihuone(Huone):
    def __init__(self):
        super().__init__()
        self.resurssit = ("Kivi", "Villa", "Puu", "Vilja", "Yrtti")

    def luo_huone(self):
        self.huoneenSisalto = []

class Orkki:
    def __init__(self):
        self.tyypit = ("", "", "")

class Orkki1(Orkki):
    def __init__(self):
        super().__init__()
        self.EP = 20
        self.MV = 5

    def hyokkaa(self):
        pass