# klasa to taki szablon

class czlowiek(): # tworzymy nowa klase
    def __init__(self, imie):
        # self wywolanie konstrukcji czlowiek dotyczy marcin i krzys
        # funkcja wywoluje siebie jako parametr
        print("wywolano init")
        self.imie = imie # self - samo sie do siebie odwoluje
        # self.imie = "Marcin"
        # marcin.imie = "Marcin"

    gatunek = "human"

# teraz tworzymy instancje (obiekt) klasy

marcin = czlowiek("Marcin") # obiekt klasy marcin o zadanym imieniu "Marcin"
print(marcin.gatunek) # wyswietli gatunek: human

krzys = czlowiek("Krzysztof")
print(krzys.gatunek)

krzys.gatunek="malpa"
print(marcin.gatunek)
print(krzys.gatunek)
