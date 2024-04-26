'''
Celem zadania jest stworzenie 2 klas:
Kolo i Prostokat.
Klasy mają być odpowiedzialne za
przechowywanie odpowiednich dla danej figury
geometrycznej wymiarów
oraz
posiadać metody wyświetlające pole i obwod tych figur.
'''
PI = 3.14159 # stała globalna

class Kolo(): # deklaracja klasy Kolo()
    def __init__(self, r): # deklaracja konstruktora
        # konstruktor to specjalna metoda która jest wywoływana przy tworzeniu obiektu klasy
        # jakasZmienna = Kolo(5) <-- stwórz nowy obiekt klasy Kolo, przekaz do konstruktora wartość 5
        self.promien = r # na nowotworzonym obiekcie klasy Kolo sworz zmienna "promien" i przypisz do niej wartość "r"
        self.pole = PI * r * r
        self.obwod = 2 * PI * r

    def wysPole(self):
        print(f"Pole koła o promieniu {self.promien} wynosi {self.pole}")

    def wysObwod(self):
        print(f"Obwód koła o promieniu {self.promien} wynosi {self.obwod}")

    def wysOpis(self):
        self.wysPole()
        self.wysObwod()


class Prostokat():
    def __init__(self, a, b):
        self.bokA = a
        self.bokB = b
        self.pole = a*b
        self.obwod = 2*a + 2*b

    def wysPole(self):
        print(f"Pole prostokąta o bokach {self.bokA}, {self.bokB} wynosi {self.pole}")

    def wysObwod(self):
        print(f"Obwód prostokąta o bokach {self.bokA}, {self.bokB} wynosi {self.obwod}")

    def wysOpis(self):
        self.wysPole()
        self.wysObwod()


kolo1 = Kolo(4)
kolo1.wysOpis()

kolo2 = Kolo(123)
kolo2.wysOpis()

prostokat1 = Prostokat(4, 5)
prostokat1.wysOpis()