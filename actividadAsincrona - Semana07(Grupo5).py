# Entero (Int). Realizar una multiplicación con 3 y una división entera con 2 variables distintas.

# Multiplicacion de 3 variables

print("")
print("Multiplicación de 3 variables")
mul1 = int(input("Ingrese el primer numero: "))
mul2 = int(input("Ingrese el segundo numero: "))
mul3 = int(input("Ingrese el tercer numero: "))
multiplicacion = mul1 * mul2 * mul3
print("El resultado de la multiplicación es: ", multiplicacion, type(multiplicacion))
print("")

# División de 2 variables

print("División de 2 variables")
div1 = int(input("Ingrese el primer numero: "))
div2 = int(input("Ingrese el segundo numero: "))
division = div1 // div2
print("El resultado de la división es: ", division, type(division))
print("")

# Luego sumarlos en una variable de resultados

print("Suma de los resultados de la multiplicación y la división")
resultado1 = multiplicacion + division
print("El resultado de la suma entre los resultados de la multiplicación y la división es: ", resultado1, type(resultado1))
print("")

# Flotante (Float). Realizar el exponencial con 2 y el modulo con 2 

# Calculo de exponente con 2 variables

print("Calculo del exponente de 2 variables")
exp1 = float(input("Ingrese el primer numero: "))
exp2 = float(input("Ingrese el segundo numero: "))
exponente = exp1 ** exp2
print("El resultado del exponente es: ", exponente, type(exponente))
print("")

# Calculo del modulo con 2 variables

print("Calculo del modulo de 2 variables")
mol1 = float(input("Ingrese el primer numero: "))
mol2 = float(input("Ingrese el segundo numero: "))
modulo = mol1 % mol2
print("El resultado del modulo es: ", modulo, type(modulo))
print("")

# Luego restarlos en una variable de resultados

print("Resta de los resultados del exponente y el modulo")
resultado2 = exponente - modulo
print("El resultado de la resta entre los resultados del exponente y el modulo es: ", resultado2, type(resultado2))
print("")

# Y realizar la división entre el resultado de la suma

print("División del resultado de la resta con el resultado de la suma")
resultado3 = resultado2 / resultado1
print("El resultado de la división entre el resultado de la resta con el resultado de la suma es: ", resultado3, type(resultado3))
print("")

# Complejo (Complex). Definir 4 variables complejos distintas.

print("Definición de números complejos")
complex1 = complex(5 + 0j)
complex2 = complex(9 + 4j)
complex3 = complex(4 + 3j)
complex4 = complex(2 + 8j)
print("Los numeros complejos definidos fueron: ", complex1, complex2, complex3, complex4)
print("")

# Carácter (String). Defina variables según número de integrantes, en la variable debe almacenar el nombre de una fruta por variable.

print("Definición de variables para nombres de frutas")
alondra = str("Fresa")
rene = str("Mango")
oswaldo = str("Sandia")
jeremy = str("Manzana")
norlin = str("Uva")
erick = str("Naranja")
print("Las frutas definidas son: ", alondra, "," ,rene, "," ,oswaldo, "," ,jeremy, "," ,norlin, ",", erick)
print("")

# Booleano (Bool). Se realizará en la estructura de control IF. Ingresar datos desde teclado, preguntar digitar un nombre de una fruta y capturar ese dato en una variable.

fruta = str(input("Ingrese el nombre de una fruta: "))  
print("")

# Estructura de control IF. Cada estructura definida es separada de la otra no agrupar o tratar de hacer una sola estructura de control.
# Diseñar una sentencia IF por cada fruta. Al evaluar la expresión de cada IF si la respuesta es verdadera, deberá mostrar el nombre de la fruta, nombre de un compañero.

if fruta == alondra:
    print(True, type(True))
    print(alondra, "es la fruta favorita de Alondra")
    
if fruta == rene:
    print(True, type(True))
    print(rene, "es la fruta favorita de René")

if fruta == oswaldo:
    print(True, type(True))
    print(oswaldo, "es la fruta favorita de Oswaldo")
    
if fruta == jeremy:
    print(True, type(True))
    print(jeremy, "es la fruta favorita de Jeremy")
    
if fruta == norlin:
    print(True, type(True))
    print(norlin, "es la fruta favorita de Norlin")
    
if fruta == erick:
    print(True, type(True))
    print(erick, "es la fruta favorita de Erick")
   
print("") 
print("Fin")

