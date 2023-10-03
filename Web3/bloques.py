from web3 import Web3

# URL de Infura para la red de Ethereum (debes reemplazar "TU-PROYECTO-ID" con␣ ↪tu propio ID de proyecto de Infura)

infura_url = ("https://mainnet.infura.io/v3/afb0ac49fed1439babdf70dce2495306") # Crear una instancia de Web3 y conectarse a Infura

web3 = Web3(Web3.HTTPProvider(infura_url))

# Verificar la conexión

if web3.is_connected(): 
    print("Conexión exitosa a Infura")
else:
    print("No se pudo conectar a Infura. Por favor, verifica la URL o tu conexión a Internet.")

# Obtener el bloque pasando el número del bloque (12345)
# Usamos primero un condicional para saber que estamos conectados  comse ha comprobado en el if anterio

if web3.is_connected():

# Usamos una función de web3 web3.eth.get_block() para buscar el bloque en ethereum.

    bloque = web3.eth.get_block(12345)

# Imprimimos el interior del bloque

    print("Datos del bloque: \n", bloque)

# Podemos obtener el hash del bloque convirtiendo el valor del hash del bloque a hexadecimal

# Obtener el hash del bloque
# Se puede apreciar que el bloque es realmente igual a un dioccionario, por lomque si ponemos
# una palabra clave nos da un resultado, en este caso la palabra claves es hash
# y lo pasamos a hexadecimal com el .hex

    bloque_hash = bloque['hash'].hex()
    print("Hash del bloque:", bloque_hash)
# Tambien podemos recorrer todo el bloque viendo cada elemento ya es un dicionario

for clave, valor in bloque.items():
        print("Clave:", clave)
        print("Valor:", valor) # los valores salen codificados al no convertilos a hexadecimal
        print() # este print es para dejar un espacio entre lineas

# También podemos buscar el bloque por medio del hash
# cambiando el numero del blouqe por el numero del hash utilizando la misma función

# Obtener el bloque pasando el Hash del bloque
if web3.is_connected():
    bloque = web3.eth.get_block('0x767c2bfb3bdee3f78676c1285cd757bcd5d8c272cef2eb30d9733800a78c0b6d')
    print("Datos del bloque: \n", bloque)


