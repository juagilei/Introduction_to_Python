# Ejercicio 1: Acceso y modificación de elementos de una lista

# Enunciado: Dada una lista de números, modifica el segundo elemento para que sea el doble de su valor original.

lista = [5, 10, 15, 20, 25]

lista[1]=lista[1]*2
print()
print(lista)
print()

# Ejercicio 2: Acceso a elementos de una tupla

# Enunciado: Dada una tupla de valores, imprime el tercer elemento.

tupla = (10, 20, 30, 40, 50)
print(tupla[2])
print()

# Ejercicio 3: Creación de un conjunto y eliminación de elementos duplicados

# Enunciado: Dada una lista de números, crea un conjunto que contenga solo los elementos únicos de la lista.

lista = [1, 2, 2, 3, 3, 4, 5, 5]
conjunto=set(lista)
print(conjunto)
print()

# Ejercicio 4: Acceso a elementos de un diccionario

# Enunciado: Dado el diccionario de colores, imprime el valor asociado a la clave 'azul'.

colores = {'amarillo': 'yellow', 'azul': 'blue', 'rojo': 'red'}

print(colores['azul'])
print()

# Ejercicio 5: Modificación de un valor en un diccionario

# Enunciado: Dado el diccionario de edades, actualiza la edad de 'Maria' a 35 años.

edades = {'Maria': 34, 'Hector': 28, 'Juan': 45}

edades['Maria']=35

print(edades)
print()

# Ejercicio 6: Iteración sobre una lista y suma de elementos

# Enunciado: Dada una lista de números, calcula la suma de todos los elementos e imprime el resultado.

lista = [10, 20, 30, 40, 50]
suma=0
for i in lista:
    suma=suma+i
print(suma)
print()

# Ejercicio 7: Iteración sobre una tupla y conteo de elementos

# Enunciado: Dada una tupla de caracteres, cuenta cuántas veces aparece el carácter 'a' y devuelve el resultado.

tupla = ('a', 'b', 'c', 'a', 'd', 'a')
cont=0
for i in tupla:
    if i=='a':
        cont=cont+1
print(cont)
print()

# Ejercicio 8: Comprobación de pertenencia a un conjunto

# Enunciado: Dado un conjunto de números, comprueba si el número 5 está presente y devuelve True o False.

conjunto = {1, 2, 3, 4, 6, 7, 8, 9}

def comprueba(conjunto):

    for i in conjunto:
        if i == 5:
            return True
        else:
           return False


print(comprueba(conjunto))
print()

# Ejercicio 9: Uso del método .items() en un diccionario

# Enunciado: Dado el diccionario de nombres y edades, imprime cada nombre y su correspondiente edad en un formato legible.

edades = {'Maria': 34, 'Hector': 28, 'Juan': 45}

for c,v in edades.items():
    print(c,' tiene ',v,' años')
print()
# Ejercicio 10: Búsqueda de clave por valor en un diccionario

# Enunciado: Dado el diccionario de edades, encuentra la clave correspondiente al valor 28 y devuelve la clave o "No encontrado" si el valor no existe.

edades = {'Maria': 34, 'Hector': 28, 'Juan': 45}

for c,v in edades.items():
    
    if v==28:
        print(c)
print()


