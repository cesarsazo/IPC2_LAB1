from animal import perro, gato

opcion = 0
animales = []

def crear():
    nuevo = None

    nombre = input('Creando animal, ingrese el nombre...\n')
    edad = int(input('Creando animal, ingrese la edad...\n'))

    tipo = int(input('Creando animal, ingrese el tipo [1. Perro 2. Gato]...\n'))
    if tipo == 1:
        #perro
        nuevo = perro(nombre, edad)
    elif tipo == 2:
        #gato
        nuevo = gato(nombre, edad)
    print("Animal con nombre {} y edad {}, creado correctamente...!!!".format(nombre,edad))
    animales.append(nuevo)

def veranimales():
    for elemento in animales:
        print(elemento)

while True:
    if opcion == 3:
        break
    elif opcion == 1:
        crear()
    elif opcion == 2:
        veranimales()
    print(' _____________________________')
    print('| 1. Crear animal             |')
    print('| 2. Ver animales             |')
    print('| 3. Salir                    |')
    print(' _____________________________')
    opcion = int(input('Ingrese una opcion [1-3]\n'))