import os
os.system('cls' if os.name == 'nt' else 'clear')

num1 = 20
num2 = 30.5
num1 = num1 + num2

print("Conversion implicita")
print(type(num1))
print(type(num2))

print("Conversion explicita")
num1 = 5.8
print(num1)
print(type(num1))

num3 = int(num1)
print(num3)
print(type(num3))

edad = input("Ingrese su edad: ")
edad = int(edad)
nuevaEdad = edad + 1
print(nuevaEdad)
print("Vas a cumplir: ",nuevaEdad)
print(type(nuevaEdad))