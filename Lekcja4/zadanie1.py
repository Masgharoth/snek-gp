class Zwierze():
    def __init__(self, wiek, imie):
        self.wiek = wiek
        self.imie = imie

    def wydajDzwiek(self):
        print(f"{self.imie} wydaje dzwiek")

    def jedz(self):
        print(f"{self.imie} je")

class Pies(Zwierze):
    def __init__(self, wiek, imie):
        super().__init__(wiek, imie)
        self.rasa = "Amstaf"

    def wypiszRase(self):
        print(f"{self.imie} jest rasy: {self.rasa}")

zwierz1 = Zwierze(6, "Burek")
zwierz1.wydajDzwiek()
zwierz1.jedz()

pies1 = Pies(8, "Paco")
pies1.wydajDzwiek()
pies1.jedz()
pies1.wypiszRase()


