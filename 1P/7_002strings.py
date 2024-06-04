import os
os.system('cls' if os.name == 'nt' else 'clear')

saludo = "hola_mundo"
#print(saludo.index('o',5,10))

try: # Capturador de errores
    print(saludo.index('o',4,7))
except ValueError:
    print("No se encontro la subcadena")

print(saludo.rindex('o')) # Devuelve la posicion de la ultima ocurrencia de una subcadena

print(saludo[0:4]) # Imprime en un rango de 0 a 4


cedula = "1601200500234"
departamento = cedula[0:2]
print(departamento)
municipio = cedula[0:4]
print(municipio)

#islower( ) - Devuelve True si todos los caracteres de la cadena son minúsculas
print("hola".islower())

#isupper( ) - Devuelve True si todos los caracteres de la cadena son mayúsculas
print("HOLA".isupper())

print(saludo[2:6])

print(saludo[3::3]) # imprime de 3 en e

print(saludo[2::2]) # imprime de 2 en 2

saludo = saludo[::-1] # invertir la cadena
print(saludo[::-1]) # imprime al reves