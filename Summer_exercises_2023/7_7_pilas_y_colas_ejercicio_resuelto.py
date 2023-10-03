# Ejercicio 1: Operaciones en una pila

# Enunciado: Crea una pila vacía y realiza las siguientes operaciones en orden:

# - Añade los elementos 3, 4, 5 y 6 a la pila.
# - Saca un elemento de la pila y almacénalo en una variable.
# - Imprime el elemento sacado y la pila actualizada.

pila=[3,4,5,6]

n=pila.pop()
print()
print('El elemento sacado es el ultimo de la pila: ',n)
print()
print('La pila queda de la siguiente forma: ',pila)
print()

# Ejercicio 2: Operaciones en una cola

# Enunciado: Crea una cola vacía utilizando la colección deque y realiza las siguientes operaciones en orden:

# - Añade los elementos 'Hector', 'Juan' y 'Miguel' a la cola.
# - Saca un elemento de la cola y almacénalo en una variable.
# - Imprime el elemento sacado y la cola actualizada.

from collections import deque

cola=deque()
cola=deque(['Hector','Juan','Miguel'])

n=cola.popleft()

print()
print('El elemento sacado es el ultimo de la cola: ',n)
print()
print('La pila queda de la siguiente forma: ',cola)
print()

# Ejercicio 3: Conversión de lista a pila

# Enunciado: Dada una lista de números, conviértela en una pila utilizando el método append(). Luego, realiza las siguientes operaciones en orden:

# - Saca dos elementos de la pila y almacénalos en variables.
# - Imprime los elementos sacados y la pila actualizada.
lista=[]
i='S'
print()
while i =='S':
    valor=input('Introduce un valor a la lista, si quieres terminar introduce N: ')
    if valor=='N':
        i=valor
    else:
        lista.append(valor)
print()        
print('La lista queda: ',lista)
n1=lista.pop()
n2=lista.pop()
print()
print('Los elementos sacados son: ',n1,' , ',n2)
print()
print('La pila queda: ',lista)
print()

# Ejercicio 4: Conversión de lista a cola

# Enunciado: Dada una lista de nombres, conviértela en una cola utilizando la colección deque y el método append(). Luego, realiza las siguientes operaciones en orden:

# - Saca el primer elemento de la cola y almacénalo en una variable.
# - Imprime el elemento sacado y la cola actualizada.


cola=deque()
lista = ['Maria', 'Juan', 'Pedro', 'Ana']
for i in lista:
    cola.append(i)

print('La cola queda: ',cola)
print()
n=cola.popleft()
print('El elemento sacdo es: ',n)
print()
print('La cola queda: ',cola)
print()

# Ejercicio 5: Verificar si una palabra es un palíndromo utilizando una pila y una cola

# Enunciado: Dada una palabra, verifica si es un palíndromo utilizando una pila y una cola. Implementa las siguientes operaciones:

# - Convierte la palabra en una pila y en una cola.
# - Compara los elementos extraídos de la pila y la cola para determinar si la palabra es un palíndromo.
# - Imprime el resultado (es palíndromo o no).

from collections import deque

print()

palabra=input('Introduce la palabra a examinar: ')
pila=[]

for i in palabra:
    pila.append(i)

cola=deque(pila)
pila1=pila
ok=True

print(pila1)


for i in range(len(pila1)):

    if ok == True:
        n1=pila1.pop()
        n2=cola.popleft()

        if n1!=n2:
            ok=False
        else:
            ok==True

print()

if ok == True:
    print('La palabra ', palabra,' es un palindromo')
else:
    print('La palabra ', palabra,' no es un palindromo')
print()






