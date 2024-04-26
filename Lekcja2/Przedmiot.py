'''
Napisz klasę Przedmiot, która będzie posiadać następujące zmienne:
srednia – średnia wszystkich ocen ok
oceny - lista ocen ok

Oraz metody:
stworz_liste() ok
dodaj_ocene(ocena)
wyswietl_oceny()
wyswietl_srednia()
'''

class Przedmiot():
    srednia = 0

    def stworz_liste(self):
        self.oceny = []

    def dodaj_ocene(self, ocena):
        self.oceny.append(ocena)
        self.srednia = sum(self.oceny) / len(self.oceny)

    def wyswietl_oceny(self):
        print("Lista ocen: ",self.oceny)

    def wyswietl_srednia(self):
        print(f"Średnia: {self.srednia}")