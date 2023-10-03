# Ejercicio 1: Saludo personalizado

# Escribe una función llamada saludar_personalizado() que tome un nombre como argumento y devuelva un saludo personalizado con el nombre proporcionado.

def saludar(nombre):
    print(f"¿ Como estas {nombre}?")
print()
saludar('juan')
print()

# Ejercicio 2: Número par o impar

# Escribe una función llamada es_par() que tome un número como argumento y devuelva True si es par o False si es impar.

def es_par(numero):
    numero%2==0
numero=3

print(f"¿El numero {numero} es par? {es_par(numero)}")
print()

# Ejercicio 3: Calculadora básica

# Escribe una función llamada calculadora() que tome dos números y un operador (+, -, *, /) como argumentos y devuelva el resultado de la operación.

def operacion(a,b,operador):
    if operador=='+':
        return (a+b)
    elif operador=='-':
        return (a-b)
    elif operador=='*':
        return (a*b)
    elif operador=='/':
        return(a/b)
    else:
        print('El operador no es correcto')

print(f"El resultado es {operacion(20,10,'*')}")
print()

# Ejercicio 4: Suma de todos los elementos en una lista

# Escribe una función llamada sumar_lista() que tome una lista de números como argumento y devuelva la suma de todos los elementos de la lista.

def sumar(lista):
    a=0
    for i in lista:
        a=a+i
    return a
lista=[1,2,3,4,5]

print(f'La suma de la lista es {sumar(lista)}')
print()

# Ejercicio 5: Encontrar el número mayor

# Escribe una función llamada numero_mayor() que tome una lista de números como argumento y devuelva el número más grande de la lista.

def maximo_lista(lista):
    return max(lista)
lista=[1,2,3,4,5,10]

print(f'El maximo de la lista es {maximo_lista(lista)}')
print()

# Ejercicio 6: Suma de dígitos de un número

# Escribe una función llamada suma_digitos() que tome un número como argumento y devuelva la suma de sus dígitos. Es decir por ejemplo le pasamos 12345 y nos tiene que devolver la suma de 1+2+3+4+5


def suma_digitos(numero):
    suma = 0
    for digito in str(numero):
        suma += int(digito)
    return suma

numero=12345

print(f'La suma de la lista es {suma_digitos(numero)}')
print()










