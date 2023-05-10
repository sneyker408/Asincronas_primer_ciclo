
print('-------------------------------------------------')
print('Aplicación de operadores de comparación y lógicos')
print('-------------------------------------------------')

# Ingreso de datos string e interger 

nombre = str(input('\nIngrese su nombre:\n'))
apellido = str(input('\nIngrese su apellido:\n'))
sexo = str(input('\nIngrese su sexo:\n')).lower()   
edad = int(input('\nIngrese su edad:\n'))

caso1m = "niño"
caso2m= "hombre"
caso3m = "señor"
caso4m = "abuelo"    
        
caso1f= "niña"
caso2f = "mujer"
caso3f = "señora"
caso4f = "abuela"

# Aplicación del modulo de la división para saber si la edad es par o impar
parOimpar = edad % 2
        
# Si el resultado del modulo es igual a cero, la condicion se cumple
# y se imprime una variable que indique si la edad ingresada es par o impar

if parOimpar == 0:    
    ResultadoParOimpar = str('par')
else:
    ResultadoParOimpar = str('impar')
    
# Estructura if que evalua si la edad es mayor o igual al número asignado en la condición
# Si la condición se cumple, se imprime el mensaje correspondiente

if sexo == 'masculino' or sexo == 'm' or sexo == 'Masculino' or sexo == 'M':

    # Bebe
    if 0 <= edad <= 2:
        print("\n¡Hola!", nombre, apellido +', eres un',caso1m,'con una edad de:', edad, 'años \nEres un bebé con un sexo:', sexo, '\nAdemas tu edad es:', ResultadoParOimpar)
        
    # Infancia    
    elif 3 <= edad <= 5:
        print("\n¡Hola!", nombre, apellido +', eres un',caso1m,'con una edad de:', edad, 'años \nEstas en la infancia con un sexo:', sexo, '\nAdemas tu edad es:', ResultadoParOimpar)
        
    # Niñez
    elif 6 <= edad <= 11:
        print("\n¡Hola!", nombre, apellido +', eres un',caso1m,'con una edad de:', edad, 'años \nEstas en tu niñez con un sexo:', sexo, '\nAdemas tu edad es:', ResultadoParOimpar)
        
    # Adolescencia
    elif 12 <= edad <= 18:
        print("\n¡Hola!", nombre, apellido +', eres un',caso1m,'con una edad de:', edad, 'años \nEstas en tu adolescencia con un sexo:', sexo, '\nAdemas tu edad es:', ResultadoParOimpar)
        
    # Juventud 
    elif 19 <= edad <= 26:
        print("\n¡Hola!", nombre, apellido +', eres un',caso2m,'con una edad de:', edad, 'años \nEstas en tu juventud con un sexo:', sexo, '\nAdemas tu edad es:', ResultadoParOimpar)
        
    # Adultez joven    
    elif 27 <= edad <= 40:
        print("\n¡Hola!", nombre, apellido +', eres un',caso2m,'con una edad de:', edad, 'años \nEstas en tu adultez joven con un sexo:', sexo, '\nAdemas tu edad es:', ResultadoParOimpar) 
        
    # Adultez   
    elif 41 <= edad <= 55:
        print("\n¡Hola!", nombre, apellido +', eres un',caso3m,'con una edad de:', edad, 'años \nEstas en tu adultez con un sexo:', sexo, '\nAdemas tu edad es:', ResultadoParOimpar)    

    # Persona mayor
    elif 56 <= edad <= 65:
        print("\n¡Hola!", nombre, apellido +', eres un',caso3m,'con una edad de:', edad, 'años \nEres una persona mayor con un sexo:', sexo, '\nAdemas tu edad es:', ResultadoParOimpar) 
    
    # Tercera edad
    elif edad >= 66:
        print("\n¡Hola!", nombre, apellido +', eres un',caso4m,'con una edad de:', edad, 'años, \nEstas en tu tercera edad con un sexo:', sexo, '\nAdemas tu edad es:', ResultadoParOimpar) 
    
    else:
        print('\nEl valor de edad es negativo')
    
        
elif sexo == 'femenino' or sexo == 'f' or sexo == 'Femenino' or sexo == 'F':

    # Bebe
    if 0 <= edad <= 2 :
        print("\n¡Hola!", nombre, apellido +', eres una',caso1f,'con una edad de:', edad, 'años \nEres un bebé con un sexo:', sexo, '\nAdemas tu edad es:', ResultadoParOimpar)

    # Infancia 
    elif 3 <= edad <= 5:
        print("\n¡Hola!", nombre, apellido +', eres una',caso1f,'con una edad de:', edad, 'años \nEstas en la infancia con un sexo:', sexo, '\nAdemas tu edad es:', ResultadoParOimpar) 

    # Niñez
    elif 6 <= edad <= 11:
        print("\n¡Hola!", nombre, apellido +', eres una',caso1f,'con una edad de:', edad, 'años \nEstas en tu niñez con un sexo:', sexo, '\nAdemas tu edad es:', ResultadoParOimpar)

    # Adolescencia
    elif 12 <= edad <= 18:
        print("\n¡Hola!", nombre, apellido +', eres una',caso1f,'con una edad de:', edad, 'años \nEstas en tu adolescencia con un sexo:', sexo, '\nAdemas tu edad es:', ResultadoParOimpar)

    # Juventud
    elif 19 <=edad <= 26:
        print("\n¡Hola!", nombre, apellido +', eres una',caso2f,'con una edad de:', edad, 'años \nEstas en tu juventud con un sexo:', sexo, '\nAdemas tu edad es:', ResultadoParOimpar)

    # Adultez joven 
    elif 27 <= edad <= 40:
        print("\n¡Hola!", nombre, apellido +', eres una',caso2f,'con una edad de:', edad, 'años \nEstas en tu adultez joven con un sexo:', sexo, '\nAdemas tu edad es:', ResultadoParOimpar)     

    # Adultez
    elif  41 <= edad <= 55:
        print("\n¡Hola!", nombre, apellido +', eres una',caso3f,'con una edad de:', edad, 'años \nEstas en tu adultez con un sexo:', sexo, '\nAdemas tu edad es:', ResultadoParOimpar)    

    # Persona mayor
    elif 56 <= edad <= 65:
        print("\n¡Hola!", nombre, apellido +', eres una',caso3f,'con una edad de:', edad, 'años \nEres una persona mayor con un sexo:', sexo, '\nAdemas tu edad es:', ResultadoParOimpar)         

    # Tercera edad 
    elif edad >= 66:
        print("\n¡Hola!", nombre, apellido +', eres una',caso4f,'con una edad de:', edad, 'años, \nEstas en tu tercera edad con un sexo:', sexo, '\nAdemas tu edad es:', ResultadoParOimpar)  
    
    else:
        print('\nEl valor de edad es negativo')           

# En el caso que la condicion no se cumpla imprimimos un texto indicando que hubo un problema a la hora de ingresar los datos 
else: 
    print('\nIngresaste un dato incorrecto, vuelve a intentarlo')    

print('\nFIN')