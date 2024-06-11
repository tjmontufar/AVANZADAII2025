numero = int(input("Ingresa un numero (-1 para salir): "))

while(numero!=-1):
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

    print("TABLA DE MULTIPLICAR DEL ",numero)
    for i in range(1, 11):
        print(f"{numero} x {i} = {i*numero}")
    
    numero = int(input("Ingresa un numero (-1 para salir): "))