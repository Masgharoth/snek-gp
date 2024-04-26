from zadanie1 import Zwierze
'''
Stworzyć klasę Ptak i dodać metodę lec(), klasa ma dziedziczyć po klasie
Zwierze, oraz dodać kolejna klasę Orzel, dziedziczaca po Ptak, która ma
mieć metodę poluj(), w której wywołujemy metodę lec() z klasy nadrzędnej.
'''

class Ptak(Zwierze):
    def __init__(self, wiek, imie):
        super().__init__(wiek, imie)

    def lec(self):
        print(f"{self.imie} leci")


class Orzel(Ptak):
    def __init__(self, wiek, imie):
        super().__init__(wiek, imie)

    def poluj(self):
        self.lec()
        print(f"{self.imie} poluje")

ptak1 = Ptak(1, "Lobo")

orzel1 = Orzel(2, "Orzeł1")

ptak1.wydajDzwiek()
ptak1.jedz()
ptak1.lec()

orzel1.wydajDzwiek()
orzel1.poluj()
orzel1.jedz()
