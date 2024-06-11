import os
os.system('cls' if os.name == 'nt' else 'clear')

# # Ciclo For
# for i in range(10):
#     print(i)

# for i in range(2, 20, 2): # El primer numero es inicio, el segundo es el fin, el tercero es incremento (2 en 2)
#     print(i)

# Ciclo For con listas
# lista = ["uno","dos","tres","cuatro","cinco"]
# for item in lista:
#     print(item)

# Invertir el orden de una lista
# for item in reversed(lista):
#     print(item)

# # Ciclo For con tuplas
# tupla = ("uno","dos","tres","cuatro","cinco")
# for item in tupla:
#     print(item)

# Ciclo For con diccionarios
diccionario = {
    "curso":"Python TOTAL",
    "clase":"Ciclos",
    "tema":"For",
    "duracion":"1 trimestre",
    "profesor":"Tomy Montufar"
}
print(diccionario)
# for llave in diccionario:
#     print(llave, diccionario[llave])

# Invertir el orden de un diccionario
for llave in reversed(diccionario):
    print(llave, diccionario[llave])