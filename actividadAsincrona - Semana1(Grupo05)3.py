print(' -----------------------------------------------------------------------------------')
print(' |                       Bienvenido a nuestro programa                             |')
print(' -----------------------------------------------------------------------------------')

# Se definen los arrays que contendran los datos de los integrantes del grupo que se mostraran en el programa.
nombres = ['Oswaldo', 'Alondra', 'Rene', 'Jeremy', 'Norlin', 'Erick']
apellidos = ['Monterroza', 'López', 'Lemus', 'Segura', 'Moreno', 'Diaz']
sexo = ['M', 'F', 'M', 'M', 'M', 'M']
edades = [24, 29, 31, 27, 26, 21]
departamentos = ['Chalatenango', 'Chalatenango', 'La Libertad', 'Chalatenango', 'Chalatenango', 'Chalatenango']
municipios = ['Potonico', 'Ojos de Agua', 'Quezaltepeque', 'San Miguel De Mercedes', 'El Carrizal', 'San Francisco Lempa']
direcciones = ['Barrio El Centro', 'Cantón El Zapotal', 'Cantón Tacachico', 'Bario San Antonio', 'Bario El Centro', 'Santa Ana']

# Se solicita crear un programa que permita ejecutar mediante una función, este deberá preguntar al usuario si quiere ejecutar el programa.
def ejecutar_programa():
    respuesta = input("\n¿Desea ejecutar el programa? (S/N): ")
    
    # Si la respuesta es si, el programa inicia su ejecución.
    if respuesta.lower() == 's':
        while True: 
            print("\nIntegrantes del grupo:")
            
            # Mediante un for se recorren los índices del arrays para luego mostrarlo como un menú, estos datos se mostrarán uno debajo del otro.
            for i in range(len(nombres)):
                print(i + 1, "-", nombres[i])
            
            # Se solicita al usuario ingresar texto desde el teclado, este dato a ingresar deberá ser el nombre de uno de los 
            # integrantes del grupo, si el usuario se equivoca N número de veces se le indica al usuario y lo devuelve a un paso previo.
            nombre = input("\nIngrese el nombre de un integrante del grupo: ")
            intentos = 0
            while nombre not in nombres and intentos < 3:
                intentos += 1
                print("\nNombre incorrecto. Por favor, inténtelo de nuevo.")
                nombre = input("Ingrese el nombre de un integrante del grupo: ")
            
            # Según el nombre ingresado se muestran los siguientes datos:
            if nombre in nombres:
                indice = nombres.index(nombre)
                print("\nNombre: ", nombres[indice])
                print("Apellido: ", apellidos[indice])
                print("Sexo: ", sexo[indice])
                print("Edad: ", edades[indice])
                print("Departamento: ", departamentos[indice])
                print("Municipio: ", municipios[indice])
                print("Dirección: ", direcciones[indice])
            else:
                print("\nDemasiados intentos fallidos. Volviendo al inicio...")
            
            # Se indica si desea consultar otro dato de los integrantes, si su respuesta es no, el programa finaliza.
            continuar = input("\n¿Desea consultar otro integrante? (S/N): ")
            if continuar.lower() != 's':
                break

    # Si la respuesta es no, el programa no se ejecuta.
    else:
        print("\nPrograma no ejecutado")

# Se hace el llamado a la función que ejecutará el programa.     
ejecutar_programa()

print('\nFin del programa')
