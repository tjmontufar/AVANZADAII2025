import os
os.system('cls' if os.name == 'nt' else 'clear')

# Imprime 10 valores con el ciclo While
# i = 0
# while i < 10:
#     print(i)
#     i += 1

# print("Ciclo controlado por banderin")
# while True:
#     entrada = input("Ingresa S para salir: ")
#     if entrada == 'S':
#         break

# print("Ciclo controlado por banderin 2")
# bandera = "x"
# while bandera != 'S':
#     bandera = input("Ingresa S para salir: ")

print("Ciclo controlado por banderin 3")
banderin3 = True
while banderin3 != False:
    banderin3 = input("Ingresa S para salir: ")
    if banderin3 == 'S':
        banderin3 = False
        print("Saliendo del ciclo")
    else:
        banderin3 = True