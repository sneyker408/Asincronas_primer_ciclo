print("--------------------------------------------------")
print("Hola ingeniero, bienvenido al programa")
print("--------------------------------------------------")

#Creacion de datos (paises/humanos y animales)

# Variables de país 
pais1 = 'El Salvador'
pais2 = 'Colombia'
pais3 = 'Argentina'
pais4 = 'Bolivia'
pais5 = 'Alemania'
pais6 = 'India'
pais7 = 'Republica Dominicana'
pais8 = 'Francia'
pais9 = 'China'
pais10 = 'Brasil'

# Variables de nacionalidad
nac1 = 'Salvadoreño/a'
nac2 = 'Colombiano/a'
nac3 = 'Argentino/a'
nac4 = 'Boliviano/a'
nac5 = 'Aleman/a'
nac6 = 'Indio/a'
nac7 = 'Dominicano/a'
nac8 = 'Frances/a'
nac9 = 'Chino/a'
nac10 = 'Brasileño/a'

# Variables de especie
especie1 = 'Canina'
especie2 = 'Felina'
especie3 = 'Porcina'
especie4 = 'Aviar'
especie5 = 'Reptil'
especie6 = 'Mamifero'
especie7 = 'Anfibio'
especie8 = 'Insecto'
especie9 = 'Roedor'
especie10 = 'Aracnido'

# Variables de animal
animal1 = 'Perro'
animal2 = 'Gato'
animal3 = 'Cerdo'
animal4 = 'Paloma'
animal5 = 'Vibora'
animal6 = 'Elefante'
animal7 = 'Sapo'
animal8 = 'Mariposa'
animal9 = 'Raton'
animal10 = 'Araña'

# Capturar nombre desde teclado
nombre = str(input('\nIngrese su nombre: '))

#Menu de opciones
print('''\nMenu de opciones
    1. Humanos
    2. Animales''')

# Capturar la opción del menu escogida
menu = int(input('\n¿Cual es la opción que desea seleccionar? '))

# Estructura if else para las opciones del menu
if menu == 1:

    # Mostrar los datos almacenados de paises
    print(f'''\nLista de los paises almacenados en el programa:
    1. {pais1}
    2. {pais2}
    3. {pais3}
    4. {pais4}
    5. {pais5}
    6. {pais6}
    7. {pais7}
    8. {pais8}
    9. {pais9}
    10. {pais10}''')
    
    # Capturar el país escogido
    opcionHumano = input('\nIngrese el nombre o número de lista de un país: ''')
    
    # Estructura elif para las opciones de paises
    if opcionHumano == '1' or opcionHumano == pais1:
        print('\n' + nombre, f'su país es: {pais1} y su nacionalidad es: {nac1}')
    elif opcionHumano == '2' or opcionHumano == pais2:
        print('\n' + nombre, f'su país es: {pais2} y su nacionalidad es: {nac2}')
    elif opcionHumano == '3' or opcionHumano == pais3:
        print('\n' + nombre, f'su país es: {pais3} y su nacionalidad es: {nac3}')
    elif opcionHumano == '4' or opcionHumano == pais4:
        print('\n' + nombre, f'su país es: {pais4} y su nacionalidad es: {nac4}')
    elif opcionHumano == '5' or opcionHumano == pais5:
        print('\n' + nombre, f'su país es: {pais5} y su nacionalidad es: {nac5}')
    elif opcionHumano == '6' or opcionHumano == pais6:
        print('\n' + nombre, f'su país es: {pais6} y su nacionalidad es: {nac6}')
    elif opcionHumano == '7' or opcionHumano == pais7:
        print('\n' + nombre, f'su país es: {pais7} y su nacionalidad es: {nac7}')
    elif opcionHumano == '8' or opcionHumano == pais8:
        print('\n' + nombre, f'su país es: {pais8} y su nacionalidad es: {nac8}')
    elif opcionHumano == '9' or opcionHumano == pais9:
        print('\n' + nombre, f'su país es: {pais9} y su nacionalidad es: {nac9}')
    elif opcionHumano == '10' or opcionHumano == pais10:
        print('\n' + nombre, f'su país es: {pais10} y su nacionalidad es: {nac10}')
    else:
        print('\nLa opción ingresada no es válida')
    
elif menu == 2:
    
    # Mostrar los datos almacenados de especies
    print(f'''\nLista de las especies almacenadas en el programa:
    1. {especie1}
    2. {especie2}
    3. {especie3}
    4. {especie4}
    5. {especie5}
    6. {especie6}
    7. {especie7}
    8. {especie8}
    9. {especie9}
    10. {especie10}''')
    
    # Capturar la especie escogida
    opcionAnimal = input('\nIngrese el nombre o número de lista de una especie: ')
    
    # Estructura elif para las opciones de especies
    if opcionAnimal == '1' or opcionAnimal == especie1:
        print('\n' + nombre, f'la especie que eligió es: {especie1} y un animal que pertenece a esa especie es: {animal1}')
    elif opcionAnimal == '2' or opcionAnimal == especie2:
        print('\n' + nombre, f'la especie que eligió es: {especie2} y un animal que pertenece a esa especie es: {animal2}')
    elif opcionAnimal == '3' or opcionAnimal == especie3:
        print('\n' + nombre, f'la especie que eligió es: {especie3} y un animal que pertenece a esa especie es: {animal3}')
    elif opcionAnimal == '4' or opcionAnimal == especie4:
        print('\n' + nombre, f'la especie que eligió es: {especie4} y un animal que pertenece a esa especie es: {animal4}')
    elif opcionAnimal == '5' or opcionAnimal == especie5:
        print('\n' + nombre, f'la especie que eligió es: {especie5} y un animal que pertenece a esa especie es: {animal5}')
    elif opcionAnimal == '6' or opcionAnimal == especie6:
        print('\n' + nombre, f'la especie que eligió es: {especie6} y un animal que pertenece a esa especie es: {animal6}')
    elif opcionAnimal == '7' or opcionAnimal == especie7:
        print('\n' + nombre, f'la especie que eligió es: {especie7} y un animal que pertenece a esa especie es: {animal7}')
    elif opcionAnimal == '8' or opcionAnimal == especie8:
        print('\n' + nombre, f'la especie que eligió es: {especie8} y un animal que pertenece a esa especie es: {animal8}')
    elif opcionAnimal == '9' or opcionAnimal == especie9:
        print('\n' + nombre, f'la especie que eligió es: {especie9} y un animal que pertenece a esa especie es: {animal9}')
    elif opcionAnimal == '10' or opcionAnimal == especie10:
        print('\n' + nombre, f'la especie que eligió es: {especie10} y un animal que pertenece a esa especie es: {animal10}')
    else:
        print('\nLa opción ingresada no es válida')
    
else:
    print('\nLa opción seleccionada no es válida')
    
print('\nFIN DEL PROGRAMA')



