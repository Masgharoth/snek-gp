from random import randint, choice

class Postac:
    def __init__(self):
        self.nazwa = ""
        self.zycie = 1
        self.max_zycie = 1
        pass

    def atak(self, przeciwnik):
        obrazenia = randint(0,3)

        if obrazenia == 0:
            print(f"{przeciwnik.nazwa} unika ataku {self.nazwa}")
        else:
            print(f"{self.nazwa} atakuje {przeciwnik.nazwa} za {obrazenia} obrażeń")
            przeciwnik.zycie -= obrazenia

class Przeciwnik(Postac):
    def __init__(self, gracz):
        super().__init__()
        self.nazwa = choice(['goblin', 'zombie', 'szkielet'])
        self.zycie = randint(1, gracz.zycie)
        self.loot = randint(1, 10)



class Gracz(Postac):
    def __init__(self):
        super().__init__()
        self.zycie = 10
        self.max_zycie = 10
        self.nazwa = input("Podaj imie postaci: ")
        self.sakiewka = 0

    def odpoczynek(self):
        hpki = randint(1, 3)
        self.zycie += hpki
        if self.zycie > self.max_zycie:
            self.zycie = self.max_zycie
        print(f"{self.nazwa} odpoczywa, życie: {self.zycie}/{self.max_zycie}")

    def walka(self, przeciwnik):
        walka = True
        while walka:
            print(f"życie gracza: {self.zycie}")
            print(f"życie przeciwnika: {przeciwnik.zycie}")
            wybor = input("Akcja: (atak, ucieczka)")

            if wybor == "atak":
                self.atak(przeciwnik)
                if przeciwnik.zycie <= 0:
                    print(f"{self.nazwa} zabija {przeciwnik.nazwa}")
                    self.sakiewka += przeciwnik.loot
                    return True
                przeciwnik.atak(self)
            elif wybor == "ucieczka":
                print(f"{self.nazwa} ucieka")
                przeciwnik.atak(self)
                walka = False
            else:
                print("Niepoprawna akcja")
                pass
            if self.zycie <= 0:
                print(f"{self.nazwa} ginie.")
                return False
        return True


gracz = Gracz()
gra = True

while gra:

    akcja = input("Akcja: (zwiedzaj, odpocznij, sklep)")

    if akcja == "odpocznij":
        gracz.odpoczynek()
    elif akcja == "zwiedzaj":
        if randint(0,1) == 0:
            print(f"{gracz.nazwa} znajduje jaskinie")
        else:
            przeciwnik = Przeciwnik(gracz)
            print(f"{gracz.nazwa} spotyka {przeciwnik.nazwa}")
            gra = gracz.walka(przeciwnik)
    elif akcja == "sklep":
        pass
    else:
        print("Nieznana akcja")
