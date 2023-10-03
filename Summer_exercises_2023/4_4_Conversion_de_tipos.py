# Ejercicio 1:
# Escribe un programa que solicite al usuario su nombre y lo imprima en la pantalla.
print()
nombre=input('Introduce tu nombre: ')
print()
print('Tu nombre es: ',nombre)
print()

# Ejercicio 2:
# Escribe un programa que solicite al usuario dos números enteros y muestre la suma de ambos.
print()
num1=int(input('Introdice el primer numero: '))
num2=int(input('Introduce el segundo numero: '))
print()
print('La suma de los dos numeros es: ',num1+num2)
print()

# Ejercicio 3:
# Escribe un programa que solicite al usuario su edad y le muestre el doble de su edad.

edad=int(input('Dame la edad: '))
print()
print('El dopble de tu edad es : ',2*edad)
print()

# Ejercicio 4:
# Escribe un programa que solicite al usuario una palabra y muestre la longitud de la palabra.

palabra=input('Escribe una palabra: ')

print('La palabra tiene ',len(palabra),' letras')
print()

# Ejercicio 5:
# Escribe un programa que solicite al usuario una frase y muestre las primeras tres letras de la frase.

print('Las tres primeras letras de la palabra son: ',palabra[:3])
print()

# Ejercicio 6:
# Escribe un programa que solicite al usuario dos números enteros y muestre el resultado de la división entre ambos.

num1=int(input('Introduce un numero: '))
print()
num2=int(input('Introduce otro numero: '))
print()
print('La división es: ',num1/num2)
print()

# Ejercicio 7:
# Escribe un programa que solicite al usuario una frase y muestre la frase en mayúsculas. 
# Pista usa el metodo .upper()

frase=input('Introduce una frase: ')
print()
print('La frase en mayusculas es: ',frase.upper())
print()

