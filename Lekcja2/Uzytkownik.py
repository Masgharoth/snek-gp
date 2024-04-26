class Uzytkownik():
    imie = ""
    nazwisko = ""
    wiek = 0

    def wyswietl(self):
        print(f"{self.imie} {self.nazwisko} {self.wiek}")
        if self.wiek < 18:
            print(f"{self.imie} ma {self.wiek} lat, jest niepelnoletni")
        else:
            print(f"{self.imie} ma {self.wiek} lat, jest pelnoletni")

    def zmien_wiek(self, nowy_wiek):
        self.wiek = nowy_wiek