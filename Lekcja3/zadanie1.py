class Samochod():

    liczba = 0

    def __init__(self, marka, model, typSilnika, mocKM):
        print("Konstruktor samochodu")
        self.marka = marka
        self.model = model
        self.typSilnika = typSilnika
        self.mocKM = mocKM
        self.licznik = 0
        Samochod.liczba += 1
        self.wyswietl()

    def wyswietl(self):
        print("Marka: ", self.marka)
        print("Model: ", self.model)
        print("Typ silnika: ", self.typSilnika)
        print("Moc w KM: ", self.mocKM)
pass


auto1 = Samochod("Ford", "Focus", "Diesel", 150)
print(Samochod.liczba)
auto2 = Samochod("Ford", "Focus", "Benzyna", 180)
print(Samochod.liczba)
print(auto1.liczba)
print(auto2.liczba)