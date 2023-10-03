from web3 import Web3

# URL de Infura para la red de Ethereum (debes reemplazar "TU-PROYECTO-ID" con tu propio ID de proyecto de Infura)
infura_url = "https://mainnet.infura.io/v3/TU-PROYECTO-ID"

# Crear una instancia de Web3 y conectarse a Infura
web3 = Web3(Web3.HTTPProvider(infura_url))

# Verificar la conexión
if web3.is_connected():
    print("Conexión exitosa a Infura")
else:
    print("No se pudo conectar a Infura. Por favor, verifica la URL o tu conexión a Internet.")

if web3.is_connected():
    # Solicitar al usuario que ingrese un número de bloque
    num_bloque = int(input("Ingrese un número de bloque: "))

    # Obtener el bloque correspondiente al número ingresado
    bloque = web3.eth.get_block(num_bloque)

    # Mostrar los datos del bloque
    print("Datos del bloque:")
    for clave, valor in bloque.items():
        if clave == 'hash':
            valor = valor.hex()
        print(f"{clave}: {valor}")
