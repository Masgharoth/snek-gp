"""
napisz program(skrypt) który wyświetli taki wzór:

1
2 2
3 3 3
4 4 4 4
5 5 5 5 5

do tego wiersza do ktorego poda uzytkownik
"""

wiersz = int(input("Podaj wiersz: "))

for i in range(1, wiersz + 1):
    for j in range(1, i + 1):
        print(i, end=" ")
    print()

