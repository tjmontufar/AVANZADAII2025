#OPERACIONES ARITMETICAS
import os
os.system('cls' if os.name == 'nt' else 'clear') #Funcion que limpia la pantalla

#usuario ingresa dos numeros
x = float(input("Ingrese el primer entero: "))
y = float(input("Ingrese el segundo entero: "))

#condicional if
if x == 0:
    print("Error. El primer entero no puede ser 0")
else:
    
    print("El resultado es: ",x/y)