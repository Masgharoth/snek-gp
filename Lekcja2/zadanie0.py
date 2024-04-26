from Uzytkownik import Uzytkownik
from Przedmiot import Przedmiot


user1 = Uzytkownik()
user2 = Uzytkownik()
user3 = Uzytkownik()
user4 = Uzytkownik()

user1.imie = "Jan"
user1.nazwisko = "Kowalski"
user1.wiek = 32

user2.imie = "Adam"
user2.nazwisko = "Nowak"
user2.wiek = 12

user3.imie = "Piotr"
user3.nazwisko = "Murarz"
user3.wiek = 18

user4.imie = "Maciej"
user4.nazwisko = "Lach"
user4.wiek = 14

user1.wyswietl()
user1.zmien_wiek(21)
user1.wyswietl()
user2.wyswietl()
user3.wyswietl()
user4.wyswietl()

matematyka = Przedmiot()
matematyka.stworz_liste()
matematyka.dodaj_ocene(3)
matematyka.dodaj_ocene(2)
matematyka.dodaj_ocene(5)
matematyka.wyswietl_oceny()
matematyka.wyswietl_srednia()
matematyka.dodaj_ocene(5)
matematyka.dodaj_ocene(4)
matematyka.wyswietl_oceny()
matematyka.wyswietl_srednia()


j_polski = Przedmiot()
j_polski.stworz_liste()
j_polski.dodaj_ocene(4)
j_polski.dodaj_ocene(3)
j_polski.dodaj_ocene(5)
j_polski.wyswietl_oceny()
j_polski.wyswietl_srednia()