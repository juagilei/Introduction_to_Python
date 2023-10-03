# Ejercicio 1: Suma segura de dos números

# Escribe una función llamada suma_segura() que tome dos números como argumentos y devuelva su suma. Maneja las excepciones que se pueden presentar en caso de que el usuario ingrese valores no numéricos.

def sumar(num1,num2):
    try:
        resultado=int(num1)+int(num2)
        return resultado
    except ValueError:
        return 'Introduce numeros'



num1=19
num2=20
print()
print(sumar(num1,num2))
print()

# Ejercicio 2: Área del triángulo

# Escribe una función llamada area_triangulo() que tome la base y la altura de un triángulo como argumentos y devuelva su área. Maneja la excepción que se puede presentar si los valores ingresados no son numéricos.

import math

pi=math.pi

def area(radio):
    try:
        resultado=2*pi*(int(radio)**2)
        return resultado
    except ValueError:
        return 'Ingtroduce un numero'

radio=2

print(area(radio))
print()

# Ejercicio 3: Validación de número positivo

# Escribe una función llamada validar_numero_positivo() que tome un número como argumento y verifique si es un número positivo. Si no lo es, lanza una excepción personalizada. 

def positivo(numero):
    if numero <= 0:
        raise ValueError("El número debe ser positivo")
    return True

try:
    num = float(input("Ingresa un número positivo: "))
    positivo(num)
    print("El número es positivo.")
except ValueError as e:
    print(e)
print()

# Ejercicio 4: Cálculo de descuento

# Escribe una función llamada calcular_descuento() que tome el precio original de un producto y un porcentaje de descuento como argumentos. Si el porcentaje de descuento es mayor al 50%, lanza una excepción personalizada.

def calcular_descuento(precio,descuento):
    if descuento>50:
        raise ValueError ('El descuento no puede ser mayor al 50%')
    final=(precio*descuento)/100
    return final


try:
    precio = float(input("Ingresa el precio original del producto: "))
    descuento = float(input("Ingresa el porcentaje de descuento: "))
    precio_final = calcular_descuento(precio, descuento)
    print("El precio final con descuento es:", precio_final)
except ValueError as e:
    print(e)
print()