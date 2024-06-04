# Crear un programa que calcule el descuento de un producto si el
# usuario compra mas de 10 productos (20%) o mas de 1000 productos (50%).

import os
os.system('cls' if os.name == 'nt' else 'clear')

print("TIENDA DE CONVENIENCIA")
print("Productos:")
print("1. Pelota de futbol      L.45.00")
print("2. Botella de agua       L.15.00")
print("3. Pan integral          L.10.00")
print("4. Jugo de piña          L.25.00")
print("5. Bolsa desechable      L.8.00")

p1 = 45.00
p2 = 15.00
p3 = 10.00
p4 = 25.00
p5 = 8.00

opcion = int(input("Elija el producto: "))
cantidad = int(input("Cuantas unidades necesitas? : "))

if opcion == 1:
    total = p1 * cantidad
elif opcion == 2:
    total = p2 * cantidad
elif opcion == 3:
    total = p3 * cantidad
elif opcion == 4:
    total = p4 * cantidad
elif opcion == 5:
    total = p5 * cantidad
else:
    print("Opcion no valida")

descuento = 0
if(cantidad > 10):
    descuento = total * 0.2

print("Descuento:           L.", descuento)
print("El total a pagar es: L.", total - descuento)