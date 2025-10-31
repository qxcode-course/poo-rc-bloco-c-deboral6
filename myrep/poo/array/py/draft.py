class Foo:
    def __init__(self, x: int):
        self.x = x

    def __str__(self) -> str:
        return f"Foo({self.x})"
    
listaVazia: list[int] = []
listaPreenchida: list[int] = [1, 2, 3, 4, 5]

tamanho = len(listaPreenchida)
listaPreenchida.append(6)
listaPreenchida.remove(5)

listaVazia.append(1)
if 2 in listaVazia:
    listaVazia.remove(2)

formatado = ",".join(str(x) for x in listaPreenchida)
print(formatado)

n = 10
sequencia = list(range(n + 1))
print(sequencia)

import random
n = 5
lista = [random.randint(0, 10) for _ in range(n)]
print(lista)

print(listaPreenchida[0]) 

for i in range(len(listaPreenchida)):
    print(f"Índice {i} e elemento {lista[i]}")

for indice, elementos in enumerate(listaPreenchida):
    print(f"indice: {indice} e elementos: {elementos}")

lista = [2, 3, 5, 7, 9]
x = 5
for elemento in lista:
    if elemento == x:
        print(f"{x} foi encontrado!")
        break 
    
lista = [2, 4, 6, 8, 10]
x = 8
if x in lista:
    print(f"elemento encontrado: {x}")
else:
    print("o elemento não esta na lista")

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []

for x in lista:
    if x % 2 == 0:
        pares.append(x)
print(pares)

lista = [1, 2, 3, 4, 5]
quadrados = []
for x in lista:
    quadrados.append(x**2)  
print(quadrados)

lists = [2, 3, 4, 6, 7, 8]
x = 2
if x in lists:
    lists.remove(x)
    print(lists)

lista = [1, 2, 3, 2, 4, 2, 5]
x = 2
lista = [x for x in lista if x != x]
print(lista)

lista = [1, 2, 3, 4]
print(3 in lista) 
lista = [1, 2, 2, 3, 2]
print(lista.count(2)) 
lista = [1, 2, 3, 2]
lista.remove(2)
print(lista) 
lista = [1, 2, 2, 3, 2]
print(lista.count(2)) 
lista = [1, 2, 3, 2]
lista.remove(2)
print(lista) 
lista = [3, 1, 4, 2]
lista.sort()
print(lista) 
import random
lista = [1, 2, 3, 4, 5]
random.shuffle(lista)
print(lista) 







