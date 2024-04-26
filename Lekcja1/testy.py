"""
Celem zadania FizzBuzz jest napisanie programu, który wypisze na
ekranie liczby 1 do 100, lecz zamiast liczb podzielnych przez 3 ma
napisać Fizz, podzielnych przez 5 Buzz, a podzielnych przez 3 i 5
FizzBuzz
"""

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
