#Ejercicio 1:
#Enunciado: Escribe un programa que tome un nombre y muestre el siguiente mensaje utilizando f-strings: "¡Hola [nombre]! ¿Cómo estás?"

nombre='Juan'
print()
print(f"¡Hola {nombre}! ¿como estas?")
print()

# Ejercicio 2:

# Enunciado: Escribe un programa que tome dos números enteros y muestre su suma utilizando f-strings.

a=10
b=20

print(f"La suma de {a} mas {b} es {a+b}")
print()

# Ejercicio 3:

# Enunciado: Escribe un programa que tome un diccionario con nombres y edades, y muestre el nombre y la edad de una persona específica utilizando f-strings.

nombres={"pedro":20,"juan":10,"ana":90}

print(f"La edad de ana es de {nombres['ana']} años")
print()

# Ejercicio 4:

# Enunciado: Escribe un programa que tome una cadena de texto y muestre su longitud utilizando f-strings.

frase='Hola Mundo Today'

print(f"La frase {frase} tiene {len(frase)} caracteres")
print()

# Ejercicio 5:

# Enunciado: Escribe un programa que tome un número decimal y muestre su representación en notación científica utilizando f-strings.

numero=12345.6789

print(f"El numero {numero} en notación cientifica es {numero:.2e}")
print()

#Ejercicio 6:

# Enunciado: Escribe un programa que tome una cadena de texto y la muestre alineada al centro de una línea de 30 caracteres utilizando f-strings.

saludo='Hola'

print(f"{saludo:>30}")
print()

# Ejercicio 7:

# Enunciado: Escribe un programa que tome una cadena de texto y la muestre truncada a 10 caracteres utilizando f-strings.

frase='Esta es una frase muy larga'

print(f"{frase:.10}")
print()

# Ejercicio 8:

# Enunciado: Escribe un programa que tome un número decimal y lo muestre con 2 decimales y relleno de ceros a la izquierda en una longitud total de 8 caracteres utilizando f-strings.

numero=3.141516

print(f"{numero:08.2f}")
print()

# Ejercicio 9:

# Enunciado: Escribe un programa que tome un número entero y lo muestre justificado a la derecha en una longitud total de 5 caracteres utilizando f-strings.

print(f"{42:>5}")
print()

# Ejercicio 10:

# Enunciado: Escribe un programa que tome un número decimal y lo muestre justificado a la izquierda en una longitud total de 10 caracteres, con 3 decimales utilizando f-strings.

print(f"{numero:>10.3f}")
print()


