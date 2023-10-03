# Importar web3
from web3 import Web3

# Entro en infura con mi clave key para navegar por los bloques de ethereum
# defino una variable infura_url donde esta mi dirección de clave key

infura_url = ("https://mainnet.infura.io/v3/afb0ac49fed1439babdf70dce2495306")

# defino una variable con la función de conectarse a infura

web3 = Web3(Web3.HTTPProvider(infura_url))

# Compruebo que estoy conectado 

if web3.is_connected:
    print('Conexión exitosa a infura')
else:
    print('Fallo de conexión, no se ha podido conectar a infura, por vafor verifica tu url o tu conexión a internet')

# Una vez conectados solicitamos el numero de bloque o el hash par buscar el bloque

if web3.is_connected:
    n=1
    while n==1:
        n_bloque = input('Introduce el numero o hash del bloque deseado: ')

# Comprobar si es un numero entero
        try:
            n_bloque = int(n_bloque)
            n=0
        except ValueError:

# Si no es un número entero, verificar si es un número hexadecimal

            try:
             n_bloque = int(n_bloque,16)
             n=0
            except ValueError:
                print("Entrada inválida. No es un número entero ni hexadecimal.")

# Buscamos el bloque con la función web3.eth.get_block()

    bloque = web3.eth.get_block(n_bloque)

# comprobamos que el bloque es correcto

    if bloque:

# Buscamos e imprimimos los valores del bloque
        for clave, valor in bloque.items():

# Convertimos el valor del hash en hexadecimal así no vemos el dato codificado

                 if clave == 'hash':
                    valor = valor.hex() #convierte  alor en hexadecimal

                 print("Clave:", clave)
                 print("Valor:", valor) # los valores salen codificados al no convertilos a hexadecimal
                 print() # este print es para dejar un espacio entre lineas

    else:

        print('Bloque introducido es erroneo')





