# Ejercicio 1: Obtener el mayor y menor elemento

# Dada una lista de números, escribe un programa que encuentre el mayor y el menor elemento de la lista.

# Existen unas funciones max() y min() que se pueden usar

Lista = [0,1,2,3,4,5,6,7,8,9]
print()
print ('el numero mayior de la lista es: ',max(Lista))
print()
print('el numero menor de la lista es: ',min(Lista))
print()
# Ejercicio 2: Suma de elementos

# Dada una lista de números, escribe un programa que calcule la suma de todos los elementos. Usa la funcion sum()

Lista_1 = [0,2,3,5]

print('la suma de los elementos de la lista es: ',sum(Lista_1))
print()

# Ejercicio 3: Eliminar duplicados

# Dada una lista, escribe un programa que elimine los elementos duplicados y devuelva una nueva lista sin duplicados. Recordad los conjuntos o grupos.

Lista_2=[1,2,2,2,2,2,3,4,5,5,5,5,5,5,6,7,]

print()
print('Lista original: ',Lista_2)
print()
Lista_ok = set(Lista_2)
print('Lista corregida: ',Lista_ok)
print()

# Ejercicio 4: Lista de cuadrados

# Dado un número entero n, escribe un programa que genere una lista de los cuadrados de los números del 1 al n. Recordad la funcion o metodo range() y usar for para recorrer la lista.

List=[]

for i in range(1,6):
    a=i*i
    List.append(a)

print('La lista de cuadrados hasta el el 5 es: ',List)
print()

# Ejercicio 5: Lista de números pares

# Dado un número entero n, escribe un programa que genere una lista de los números pares del 1 al n.

List=[]

for i in range(1,11):
    if i%2==0:
        List.append(i)

print('los pares del 1 al 10 son: ',List)

# Ejercicio 6: Divisores de un número

# Dado un número entero n, escribe un programa que genere una lista de los divisores de dicho número.

List=[]

for i in range(1,13):
    if 12%i==0:
        List.append(i)

print()
print('los divisibles de 12 son: ',List)
print()

# Ejercicio 7: Concatenar listas

# Dadas dos listas, escribe un programa que las concatene y devuelva una nueva lista.

Lista_1=[1,2,3,4]
Lista_2=[11,12,13,14]

Lista_total=Lista_1+Lista_2

print('La lista total es : ',Lista_total)
print()

# Ejercicio 8: Invertir lista

# Dada una lista, escribe un programa que la invierta y devuelva una nueva lista con los elementos en orden inverso.

print('la primera lista en orden inverso es: ',Lista_1[::-1])
print()

# Ejercicio 9: Eliminar elementos por valor

# Dada una lista y un valor, escribe un programa que elimine todas las ocurrencias de ese valor en la lista.

List=[1,2,3,2,4,5,3,5,6,2,6,2,3,4,5,]

numero=2

while numero in List:
    List.remove(numero)

print('la lista sin el numero 2 queda: ',List)
print()

# Ejercicio 10: Buscar elementos en una lista

# Dada una lista y un elemento, escribe un programa que verifique si el elemento está presente en la lista.

List=[1,2,3,2,4,5,3,5,6,2,6,2,3,4,5,]

numero=5

if numero in List:

    print('el 5 esta en la lista')
else:
    print('el numero no esta en la lista')
    

