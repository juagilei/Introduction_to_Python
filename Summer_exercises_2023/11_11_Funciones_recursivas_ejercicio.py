# Ejercicio 1: Conteo recursivo de elementos en una lista

# Escribe una función llamada conteo_recursivo() que tome una lista como argumento y devuelva la cantidad de elementos que contiene, utilizando recursión. Simulamos lo que nos devolveria la función len()

def conteo_recusivo(lista):
    if not lista:
        return 0
    else:
        return 1 + conteo_recusivo(lista[1:])

numeros = [1, 2, 3, 4, 5, 6, 7]
print()
print(conteo_recusivo(numeros)) 
print()

# Ejercicio 2: Suma de elementos pares en una lista

# Escribe una función llamada suma_pares_recursiva() que tome una lista de números como argumento y devuelva la suma de todos los elementos pares de la lista utilizando recursión. Le pasamos por ejemplo una lista asi [1, 2, 3, 4, 5, 6, 7, 8] pero solo ha de sumar los numeros pares de la lista.

def suma_pares(lista):

    if not lista:
        return 0
    elif lista[0] % 2 == 0:
        return lista[0] + suma_pares(lista[1:])
    else:
        return suma_pares(lista[1:])

lista=[1,2,3,4,5,6,7,8]
print(suma_pares(lista))
print()

# Ejercicio 3: Inversión de una cadena

# Escribe una función llamada invertir_cadena_recursivo() que tome una cadena como argumento y devuelva la cadena invertida utilizando recursión. Es decir si escribo Python , deberia devolverme nohtyP.

def invertir(palabra):
    if len(palabra)==0:
        return palabra
    else:
        return palabra[-1]+invertir(palabra[:-1])

palabra='Python'
print(invertir(palabra))
print()

# Ejercicio 4: Suma de los primeros n números naturales

# Escribe una función llamada suma_naturales_recursiva() que tome un número entero positivo n como argumento y devuelva la suma de los primeros n números naturales utilizando recursión. Es decir si le pasamos el numero 5 , deberia sumar 1 + 2 + 3 + 4 + 5 = 15

def sumar_numeros(numero):
    if numero==0:
        return 0
    elif numero==1:
        return 1
    else:
        return numero + sumar_numeros(numero-1)

numero = 0
print(sumar_numeros(numero))
print()




