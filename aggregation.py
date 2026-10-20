class Clothes:
    def __init__ (self, type):
        self.type = type

    def __del__(self):
        print("Cloth getting ridden of:", self.type)

class Closet:
    def __init__ (self, clothes: list[Clothes] = None):
        self.clothes = clothes if clothes else []

    def __del__ (self):
        print("Closet object removed.")

clothing1 = Clothes("t-shirt")
clothing2 = Clothes("skirt")
closet = Closet([clothing1, clothing2])
del closet