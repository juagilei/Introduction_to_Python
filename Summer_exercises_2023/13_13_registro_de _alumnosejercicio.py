# Bloque 1: Definir función para calcular el promedio de una lista de notas
# Pista: Debes calcular la suma de las notas y dividirla por la cantidad de notas en la lista.
def calcular_promedio(notas):
    return sum(notas)/len(notas)


# Bloque 2: Definir función para registrar los datos de un alumno
# Pista: Debes pedir al usuario que ingrese el nombre, edad y calificaciones del alumno,
# separadas por comas, y luego convertir las calificaciones a una lista de números.
def registrar_alumno():
    nombre = input('Introduce el nombre del alumno: ')
    edad = input('Introduce la edad del alumno: ')
    notas = input("Ingrese las calificaciones separadas por comas (asignatura1, asignatura2, asignatura3): ").split(",")
    notas = [ float(nota) for nota in notas]
    return nombre, edad, notas


# Bloque 3: Función principal para registrar varios alumnos y calcular sus promedios
# Pista: Debes pedir al usuario la cantidad de alumnos que quiere registrar.
# Luego, utiliza un bucle para pedir los datos de cada alumno y guardarlos en una lista de diccionarios.
# Por último, calcula los promedios individuales y el promedio general de todos los alumnos.

def main():
    alumnos = []
    cantidad_alumnos = int(input('Introduce el numero de alumnbos a registrar: '))
    for i in range(cantidad_alumnos):
        print(f"\n Registro Alumno {i+1}")
        nombre, edad, notas = registrar_alumno()
        alumnos.append({'nombre':nombre, 'edad':edad, 'notas':notas})

    print()
    promedios = []
    for alumno in alumnos:
        promedio = calcular_promedio(alumno["notas"])
        promedios.append(promedio)
        print(f"El promedio de {alumno['nombre']} es: {promedio:.2f}")

    promedio_general = calcular_promedio(promedios)
    print(f"\nEl promedio general de todos los alumnos es: {promedio_general:.2f}")


# Llamada a la función principal para iniciar el programa
main()

