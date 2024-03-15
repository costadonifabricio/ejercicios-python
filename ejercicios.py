# dada una lista de numeros, quitar los repetidos

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5]

lista = list(set(lista))

print(lista)

# dada una lista de numeros, juntar los repetidos y mostrar cuantos hay de cada uno

lista = [1, 2, 2, 3, 3, 4, 4, 4]

repetidos = {}

for i in set(lista):
    repetidos[i] = lista.count(i)

print(repetidos)


