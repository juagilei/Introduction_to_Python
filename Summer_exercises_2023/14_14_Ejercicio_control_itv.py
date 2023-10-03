
# Función para saber si el añod del coche es multiplo de 3.

def es_multiplo_de_tres(año):

# Utilizo el modulo de 3 para determinar si es multipo de 3.

    if año%3==0:
        return True
    else:
        return False

# Función para determinar que vehículos deben pasar la ITV.

def vehiculos_itv(vehiculos):

# Para crear una lista en la que salgan los vehiculos que deben pasar la itv creamos dos listas vacias.
# list_vehiculos_itv con los datos del propietario, matricula y correo electronico.
# list_matricula con la lista de las matriculas que deben pasar la itv este año.


    list_vehiculos_itv=[]
    list_matricula=[]

# Recorro las matriculas diccionario vehiculos.

    for matricula in vehiculos:

# Dentro del diccionario de la matricula busco la clave "año_coche" para obtener el año y poder ponerlo como argumento en la función es_multiplo_de_tres
# Si la matricula es multiplo de 3 (True) la funcion devulve el numero de la matricula
# Para ver el valor de una clave que esta dentro de un diccionario que a su vez esta dentro de otro al sintaxis es ( diccionario1[diccionario2][clave diccionario2] )

        if es_multiplo_de_tres(vehiculos[matricula]["año_coche"])==True:

# Borro del diciconario el año del coche y el dni del propietario ya que en la lista que me solicitan no lo necesito

            del vehiculos[matricula]["año_coche"]
            del vehiculos[matricula]["dni"]

# Añado el numero de matricula en el diccionario de las matriculas para tenerlo dentro de matriculas y poder obtener la lista que se solicita completa.
            vehiculos[matricula]["matricula"]=matricula

# Añado a lista los datos de cada matricula

            list_vehiculos_itv.append(vehiculos[matricula])
            list_matricula.append(matricula)

# La función devuelve las dos listas

    listas=list_vehiculos_itv,list_matricula
    return listas

# Función para mostrar los mensajes que debe recibir el propietario

def mostrar_mensajes(mensajes):

# Recorro la lista list_vehiculos_itv e imprimo los datos del diccionario usando las claves.

    for vehiculo in mensajes:
        print()
        print(f"El propietario: {vehiculo['propietario']} con correo electronico {vehiculo['correo_electronico']} y vehiculo con matricula {vehiculo['matricula']} debe de pasar este año la ITV")
        print()

# Función que muestra el listado de matriculas que tienen que pasar la ITV

def mostrar_matriculas(matricula):
    print()
    print('Las matriculas que tienen que pasar la ITV este año son las siguientes:')
    for matricula_itv in matricula:
        print(matricula_itv)

# defino la función principal para ejecutar el programa

def main():

    vehiculos = {
        "1234ABC": {
            "propietario": "Juan Pérez",
            "dni": "12345678A",
            "correo_electronico": "juan.perez@example.com",
            "año_coche": 2015
        },
        "5678XYZ": {
            "propietario": "María Gómez",
            "dni": "98765432Z",
            "correo_electronico": "maria.gomez@example.com",
            "año_coche": 2018
        },
        "AB123CD": {
            "propietario": "Luis Rodríguez",
            "dni": "87654321B",
            "correo_electronico": "luis.rodriguez@example.com",
            "año_coche": 2007
        },
        "ZX789YX": {
            "propietario": "Ana Martínez",
            "dni": "65432198X",
            "correo_electronico": "ana.martinez@example.com",
            "año_coche": 2012
        },
        "BC456FG": {
            "propietario": "Carlos Gutiérrez",
            "dni": "23456789C",
            "correo_electronico": "carlos.gutierrez@example.com",
            "año_coche": 2019
        },
        "GH908KL": {
            "propietario": "Laura Sánchez",
            "dni": "87654321L",
            "correo_electronico": "laura.sanchez@example.com",
            "año_coche": 2010
        },
        "JK567YH": {
            "propietario": "Pedro Ruiz",
            "dni": "76543210R",
            "correo_electronico": "pedro.ruiz@example.com",
            "año_coche": 2009
        },
        "DE876NO": {
            "propietario": "Isabel Torres",
            "dni": "54321098T",
            "correo_electronico": "isabel.torres@example.com",
            "año_coche": 2004
        },
        "TR765VB": {
            "propietario": "Antonio González",
            "dni": "32109876G",
            "correo_electronico": "antonio.gonzalez@example.com",
            "año_coche": 2002
        },
        "PO567RF": {
            "propietario": "Elena Vargas",
            "dni": "89012345V",
            "correo_electronico": "elena.vargas@example.com",
            "año_coche": 2017
        },
        "IJ978CB": {
            "propietario": "Miguel Castro",
            "dni": "10987654C",
            "correo_electronico": "miguel.castro@example.com",
            "año_coche": 2016
        },
        "VN876FR": {
            "propietario": "Carmen López",
            "dni": "67890123L",
            "correo_electronico": "carmen.lopez@example.com",
            "año_coche": 2008
        },
        "TF109KL": {
            "propietario": "David Ramírez",
            "dni": "78901234R",
            "correo_electronico": "david.ramirez@example.com",
            "año_coche": 2006
        },
        "WE901TQ": {
            "propietario": "Sara Núñez",
            "dni": "54321098N",
            "correo_electronico": "sara.nunez@example.com",
            "año_coche": 2005
        },
        "RO763ZQ": {
            "propietario": "Manuel Fernández",
            "dni": "21098765F",
            "correo_electronico": "manuel.fernandez@example.com",
            "año_coche": 2014
        },
        "OP458TY": {
            "propietario": "Cristina Ruiz",
            "dni": "32109876R",
            "correo_electronico": "cristina.ruiz@example.com",
            "año_coche": 2013
        },
        "XQ871LC": {
            "propietario": "Javier Torres",
            "dni": "76543210T",
            "correo_electronico": "javier.torres@example.com",
            "año_coche": 2011
        },
        "ZX678RT": {
            "propietario": "Sonia García",
            "dni": "56789012G",
            "correo_electronico": "sonia.garcia@example.com",
            "año_coche": 2003
        },
        "GH956PO": {
            "propietario": "Marta Martínez",
            "dni": "67890123M",
            "correo_electronico": "marta.martinez@example.com",
            "año_coche": 2017
        }
    }
# introduzco en dos variables las dos listas que devuelve la funcion vehiculos_itv

    lista1,lista2=vehiculos_itv(vehiculos)

# Utilizo las variables para mostar los mensajes de las funciones mostrar_mensajes y mostrar_matriculas

    mostrar_mensajes(lista1)

    mostrar_matriculas(lista2)

main()



