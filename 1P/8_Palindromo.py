import os
os.system('cls' if os.name == 'nt' else 'clear')

palabra = input("Ingresa una palabra: ")

if palabra == palabra[::-1]:
    print(f"{palabra} es un palíndromo.")
else:
    print(f"{palabra} no es un palíndromo.")