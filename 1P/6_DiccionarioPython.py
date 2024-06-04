import os
os.system('cls' if os.name == 'nt' else 'clear')

# DICCIONARIO EN PYTHON

# Buscando valores con la palabra clave

a = {'clave1': 'valor1', 
     'clave2': 'valor2', 
     'clave3': 'valor3'}

opcion = str(input("Ingrese una palabra clave: "))
print(a[opcion]) if opcion in a else print("No se encuentra la palabra clave")

# Mostrando varios registros con un ciclo For
'''
dic = {'1': {'nombre': 'Tomy', 'apellido': 'Montufar', 'Edad': 19}, 
       '2': {'nombre': 'Iliana', 'apellido': 'Zuniga', 'Edad': 18},
       '3': {'nombre': 'Diany', 'apellido': 'Enamorado', 'Edad': 19}}

for id in dic.keys():
    print(f"Indice: {id}, Nombre: {dic[id]['nombre']}, Apellido: {dic[id]['apellido']}, Edad: {dic[id]['Edad']}")
'''