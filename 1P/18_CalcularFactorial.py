import os
os.system('cls' if os.name == 'nt' else 'clear')

numero = int(input("Ingresa un numero para calcular su factorial: "))
resultado = 1

for i in range(1,numero+1):
    resultado *= i

print("El factorial de ",numero," es: ", resultado)