import os
os.system('cls' if os.name == 'nt' else 'clear')


texto = input("Ingrese un texto: ")

l1 = input("Ingrese la letra 1 a buscar: ")
l2 = input("Ingrese la letra 2 a buscar: ")
l3 = input("Ingrese la letra 3 a buscar: ")

letras = {l1, l2, l3}

print(letras)
print(texto)