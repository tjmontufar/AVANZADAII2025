import os
os.system('cls' if os.name == 'nt' else 'clear')

lista_1 = ["C", "C++", "Python", "Java"] 
lista_2 = ["PHP", "SQL", "Visual Basic"]

print(lista_1[0])
print(lista_2[0])

print(lista_1)
print(lista_2)

lista_12 = lista_1 + lista_2
print(lista_12)

lista_3 = ["d", "a", "c", "b", "e"]
lista_4 = [5, 4, 7, 1, 9]

lista_13 = lista_1 + lista_3
print(lista_13)

lista_14 = lista_1 + lista_4
print(lista_14)

lista_5 = [True, False]
lista_145 = lista_1 + lista_4 + lista_5
print(lista_145)

lista_5.append(True) #Agrega un elemento al final de la lista
print(lista_5)

print(lista_5.pop(0)) #Elimina el primer elemento de la lista
print(lista_5)

lista_5.sort() #Ordena la lista
print(lista_5)

lista_5.reverse() #Invierte la lista
print(lista_5)