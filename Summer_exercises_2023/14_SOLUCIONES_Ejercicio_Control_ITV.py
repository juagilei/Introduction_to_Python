# Definir una función para comprobar si un año es múltiplo de 3.
def es_multiplo_de_tres(año):
    return año % 3 == 0

# Definir una función que determine cuáles vehículos deben pasar la ITV este año.
def vehiculos_itv(vehiculos):
    mensajes = []
    for matricula, info in vehiculos.items():
        año_coche = info["año_coche"]
        if es_multiplo_de_tres(año_coche):
            mensaje = f"Estimado/a {info['propietario']}, su vehículo con matrícula {matricula} debe pasar la ITV este año. \nPor favor, revise su correo electrónico ({info['correo_electronico']}) para obtener más información.\n"
            mensajes.append(mensaje)
    return mensajes

# Mostrar los mensajes que deben recibir los propietarios de los vehículos que deben pasar la ITV.
def mostrar_mensajes(mensajes):
    for mensaje in mensajes:
        print(mensaje)

# Mostrar un listado general de las matrículas de los vehículos que deben pasar la ITV.
def mostrar_matriculas(vehiculos):
    #matriculas_itv = [matricula for matricula, info in vehiculos.items() if es_multiplo_de_tres(info["año_coche"])]
    matriculas_itv = []
    for matricula, info in vehiculos.items():
        if es_multiplo_de_tres(info["año_coche"]):
            matriculas_itv.append(matricula)
    print("Vehículos que deben pasar la ITV este año:")
    for matricula in matriculas_itv:
        print(matricula)

# Diccionario de vehículos
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

# Llamada a las funciones para obtener los resultados
mensajes_itv = vehiculos_itv(vehiculos)
mostrar_mensajes(mensajes_itv)
mostrar_matriculas(vehiculos)
