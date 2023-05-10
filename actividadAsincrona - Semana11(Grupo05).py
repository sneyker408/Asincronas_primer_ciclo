print('\n\t**************************************************')
print('\t     Hola, sean bienvenidos a nuestro programa')
print('\t*************************************************')

# Programa que permita ingresar datos N números naturales y que determine cuantos de ellos son:

# - Positivos.
# - Negativos.
# - Nulos.

# Si se escribe un dato incorrecto, el programa no se ejecutará, 
# en cambio preguntará de nuevo por la información hasta que el dato ingresado sea correcto.

print('\nInicio del programa')

# Se introducirán datos tipo entero para mostrar la cantidad de veces que se repetirá el programa para hacer las cuentas.
# Se crea un bucle While, si el dato que ingresa el usuario es negativo, o si ingresa un cero o una letra, el programa
# preguntará hasta que ingrese correctamente el dato que se le pide. 
    
while True:
    try:
        n = int(input("\nIngrese la cantidad de datos que desea procesar: "))
        if n <= 0:
            print("\nDebe ingresar un número que sea mayor a cero")
            continue
        break
    except ValueError:
        print("\nEl dato no es valido, debe ingresar un valor tipo entero mayor a cero")
    
# Se crea un bucle For y se ingresan los datos que el programa contará

if n > 0:

    positivos = 0
    negativos = 0
    nulos = 0
    i = 1

    for i in range(n):
        dato = int(input('\nIngrese un numero natural: '))
        
        if dato > 0:
            positivos += 1
        elif dato < 0:
            negativos += 1
        else:
            nulos += 1
        i += 1

# En este print(), se hace el conteo de datos que el usuario ha ingresado y los separa para cada uno de los tres tipos.

print(f'\nLa cantidad de numeros positivos fue: {positivos}\nLa cantidad de numeros negativos fue: {negativos}\nLa cantidad de numeros nulos fue: {nulos}')

print('\nFin del programa')






