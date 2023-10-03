# Ejercicio 1:
# Enunciado: Escribe un programa que tome dos variables nombre y edad, y muestre el siguiente mensaje formateado: "Hola, me llamo [nombre] y tengo [edad] años".

nombre='juan'
edad=49
print()
print('Hola me llamo ',nombre,' y tengo ',edad,' años')
print()

# Ejercicio 2:

# Enunciado: Escribe un programa que tome tres variables a, b y c, y muestre el siguiente mensaje formateado: "Los valores son: a=[a], b=[b], c=[c]".

a=10
b=20
c=30

print("Los valores asignados son: a={}, b={}, c={}".format(a,b,c))
print()

# Ejercicio 3:

# Enunciado: Escribe un programa que tome un número entero y muestre su representación en binario, octal y hexadecimal.

# {} --> normal

# {:b} --> binario

# {:o} --> octal

# {:x} --> hexadecimal

a=42

print("En numero {} en binario es {:b} en octal es {:o} en hexadecimal es {:x}".format(a,a,a,a))

print()

# Ejercicio 4:

# Enunciado: Escribe un programa que tome un número decimal y muestre su representación en notación científica.

# {} --> normal

# {:.2e} --> notacion cientifica

a=22223.14168789872

print("El numero {} en notación cientifica es {:.2e}".format(a,a))
print()

# Ejercicio 5:

# Enunciado: Escribe un programa que tome una cadena de texto y la muestre alineada al centro de una línea de 30 caracteres.

nombre= 'Hola'

print("{:^30}".format(nombre))
print()

# Ejercicio 6:

# Enunciado: Escribe un programa que tome una cadena de texto y la muestre truncada a 10 caracteres.

frase='Hola que tal cono estas'

print("{:.10}".format(frase))
print()

# Ejercicio 7:

# Enunciado: Escribe un programa que tome un número decimal y lo muestre con 2 decimales y relleno de ceros a la izquierda en una longitud total de 8 caracteres.

numero=3.1416

print("{:08.2f}".format(numero))

print()

# Ejercicio 8:

# Enunciado: Escribe un programa que tome un número entero y lo muestre justificado/alineado a la derecha en una longitud total de 5 caracteres.

print("{:5d}".format(42))
print()

# Ejercicio 9:

# Enunciado: Escribe un programa que tome un número decimal y lo muestre justificado a la izquierda en una longitud total de 10 caracteres, con 3 decimales.

print("{:0.3f}".format(numero))




