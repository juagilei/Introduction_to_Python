# Ejercicio 1:
# Enunciado: Escribe un programa que solicite al usuario un número y muestre si es positivo, negativo o cero.
print()
numero=float(input('Introduce un numero: '))
print()

if numero>0:
    print('El numero es positivo')
elif numero==0:
    print('El numero es cero')
elif numero<0:
    print ('el numero es negativo')
print()

# Ejercicio 2:
# Enunciado: Escribe un programa que solicite al usuario un número y muestre si es par o impar.

numero=float(input('Introduce un numero: '))
print()
if numero%2==0:
    print('El numero es par')
else:
    print('El numero es impar')
print()

# Ejercicio 3:
# Enunciado: Escribe un programa que solicite al usuario un número del 1 al 7 y muestre el día de la semana correspondiente. (Hicimos uno igual en clase)

dia=int(input('Dame un numero del dia de la semana: '))
print()
if dia==1:
    print('Es lunes')
elif dia==2:
    print('Es martes')
elif dia==3:
    print('Es miercoles')
elif dia==4:
    print('Es jueves')
elif dia==5:
    print('Es viernes')
elif dia==6:
    print('Es sabado')
elif dia==7:
    print('Es domingo')
else:
    print('El dia no corresponde a la semana')
print()

# Ejercicio 4:
# Enunciado: Escribe un programa que solicite al usuario un número y muestre su tabla de multiplicar del 1 al 10.

numero=int(input('Introduce el numero a multiplicar: '))
a=0
while a < 11 :
    print(numero,' x ',a,' = ',numero*a)
    a+=1
print()

for i in range(11):
     print(numero,' x ',i,' = ',numero*i)

# Ejercicio 5:
# Enunciado: Escribe un programa que solicite al usuario un número y muestre la suma de todos los números enteros desde 1 hasta ese número.

print()
numero=int(input('Introduce un numero: '))

a=0
for i in range (numero+1):
    a=a+i
print('La suma total es: ',a)

print()

# Ejercicio 6:
# Enunciado: Escribe un programa que solicite al usuario una palabra y muestre cada letra de la palabra en una línea nueva.

palabra= input('Escribe la palabra a deletrear: ')

for i in range(len(palabra)):
    print(palabra[i])

# Ejercicio 7:
# Enunciado: Escribe un programa que solicite al usuario una lista de números separados por comas y muestre el promedio de los números. Utilizad la funcion o metodo .split(). Podeis buscar para que sirve y como usarla en internet.

print()
lista=input('Escribe una lista de numeros separada por comas: ')

lista_separada=lista.split(',')

print(lista_separada)

suma=0

for i in lista_separada:
   suma=suma+int(i)

print('El promedio es: ',suma/len(lista_separada))


# Ejercicio 8:
# Enunciado: Escribe un programa que solicite al usuario una lista de palabras separadas por espacios y muestre la palabra más larga. Utilizad la funcion o metodo .split().

print()
cadena_de_palabras=input('Introdice palabras separadas por espacios: ')

cadena_separada=cadena_de_palabras.split(' ')

palabra_mas_larga=max(cadena_separada,key=len)

print()

print('La primera palabra mas larga es: ', palabra_mas_larga)

print()

# Ejercicio 9:
# Enunciado: Escribe un programa que solicite al usuario un número y muestre si es un número primo.

numero=int(input('Introduce un numero: '))
print()

def es_primo(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

primo=es_primo(numero)

if numero < 2:
    print ('El numero no es primo')
else:
    if primo==True:
        print('El numero es primo')
    else:
        print('El numero no es primo')

print()

# Ejercicio 10:
# Enunciado: Escribe un programa que solicite al usuario una lista de nombres y muestre solo los nombres que comienzan con la letra "A". Utilizad la funcion o metodo .split().

nombre=input('Introduce una lista de nombres: ')
nombres_separados=nombre.split(',')
print(
    
)
for i in nombres_separados:
    if i[0]=='A':
        print(i)
