print()
print('SOLUCIONES DE LOS EJERCICIOS TIPOS DE DATOS')
print()
print('.........................................................................................')

# Ejercicio 1: Declara dos variables, a y b, y asígnale valores numéricos. Luego, muestra la suma de a y b.

a = 2
b = 3

print()
print('Ejercicio 1 suna variables:')
print()
print('La suma es: ',a+b)
print()
print('........................................................................................')
print()

# Ejercicio 2: Declara una variable pi y asígnale el valor de pi (3.1415). Luego, muestra el valor de pi en la consola. 

import math

pi = math.pi

print()
print('Ejercicio 2 numero pi:')
print()
print('El numero pi es: ',pi)
print()
print('........................................................................................')
print()

# Ejercicio 3: Declara una variable booleana es_verdadero y asígnale el valor True. Luego, muestra el valor de es_verdadero en la consola.

es_verdadero = True

print()
print('Ejercicio 3 booleano:')
print()
print('La variable es_verdadero es: ',es_verdadero)
print()
print('........................................................................................')
print()

# Ejercicio 4: Declara una variable cadena y asígnale el valor "Hola mundo". Luego, muestra cadena en la consola.

saludo='Hola Mundo'

print()
print('Ejercicio 4 string:')
print()
print(saludo)
print()
print('........................................................................................')
print()

# Ejercicio 5: Declara dos variables, num1 y num2, y asígnale valores numéricos. Realiza las cuatro operaciones aritméticas básicas (suma, resta, multiplicación y división) entre num1 y num2, y muestra los resultados en la consola.

num1=5
num2=25

print()
print('Ejercicio 5 operadores:')
print()
print('suma: ',num2+num1)
print('resta: ',num2-num1)
print('multiplicación: ',num2*num1)
print('división: ',num2/num1)
print()
print('........................................................................................')
print()

# Ejercicio 6: Declara una variable edad y asígnale un valor numérico. Luego, utiliza operadores relacionales para determinar si la edad es mayor o igual a 18. Muestra el resultado en la consola.

edad = 10
print()
print('Ejercicio 6 condicionales:')
print()
if edad>=18:
    edad=True
    print ('¿es mayor de edad?: ',edad)
else:
    edad=False
    print('es menor de edad: ',edad)
print()
print('........................................................................................')
print()

# Ejercicio 7: Declara una variable numero y asígnale un valor numérico. Utiliza el operador de asignación += para incrementar el valor de numero en 5. Muestra el resultado en la consola.

num=10

num+=5

print()
print('Ejercicio 7 incremento:')
print()
print(num)
print()
print('........................................................................................')
print()

# Ejercicio 8: Declara una variable cadena1 y asígnale el valor "Hola". Luego, utiliza el operador de concatenación + para concatenar cadena1 con otra cadena de tu elección. Muestra el resultado en la consola.

saludo1 = 'Hola '
saludo2 = 'Mundo'

saludo3 = saludo1+saludo2

print()
print('Ejercicio 8 fusionar cadenas:')
print()
print(saludo3)
print()
print('........................................................................................')
print()

# Ejercicio 9: Declara una variable lista_numeros y asígnale una lista de números de tu elección. Utiliza la función len() para obtener la cantidad de elementos en lista_numeros. Muestra el resultado en la consola.

numeros = [1,2,3,4,5]

total_numeros = len(numeros)

print()
print('Ejercicio 9 contar lista:')
print()
print('la lista tiene: ',total_numeros, 'elementos')
print()
print('........................................................................................')
print()

# Ejercicio 10: Declara una variable cadena y asígnale un valor de cadena de texto. Utiliza el método .upper() para convertir cadena a letras mayúsculas. Muestra el resultado en la consola.

cadena='hola mundo'

cadena_mayuscula= cadena.upper()

print()
print('Ejercicio 10 mayusculas:')
print()
print(cadena_mayuscula)
print()
print('........................................................................................')
print()

