"""
Należy napisać program, który z listy pokaże nam najmniejszą i
największą liczbę
"""

lista = [1,3,7,11,2,-6,0]

# najwieksza = max(lista)

najwieksza = lista[0]
najmniejsza = lista[0]

for i in lista:
    if najmniejsza > i:
        najmniejsza = i

    if najwieksza < i:
        najwieksza = i


print(najmniejsza)
print(najwieksza)