import os
os.system('cls' if os.name == 'nt' else 'clear')

limite = int(input("Ingrese el limite de la suma de los pares: "))

pares = 0
for i in range(1, limite+1):
    if(i % 2 == 0):
        print(i)
        pares += i

print("La suma de los pares es: ", pares)