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
    # Obtener el número del último bloque
    ultimo_bloque = web3.eth.block_number
    print("Número del último bloque:", ultimo_bloque)
    print("-------------------------------------------------------------------------------------------------------------------")
    # Solicitar al usuario que ingrese una dirección de transacción --> 0x5c504ed432cb51138bcf09aa5e8a410dd4a1e204ef84bfed1be16dfba1b22060
    direccion_transaccion = input("Ingrese una dirección de transacción: ")

    # Buscar la transacción correspondiente a esa dirección
    transaccion = web3.eth.get_transaction(direccion_transaccion)

    # Mostrar los valores de la transacción encontrada
    print("Valores de la transacción:")
    for clave, valor in transaccion.items():
        print(f"{clave}: {valor}")

    print("-------------------------------------------------------------------------------------------------------------------")
    # Solicitar al usuario que ingrese un hash de recibo --> 0x5c504ed432cb51138bcf09aa5e8a410dd4a1e204ef84bfed1be16dfba1b22060
    hash_recibo = input("Ingrese un hash de recibo: ")

    # Buscar el recibo correspondiente a ese hash
    recibo = web3.eth.get_transaction_receipt(hash_recibo)

    # Mostrar los valores del recibo encontrado
    print("Valores del recibo:")
    for clave, valor in recibo.items():
        print(f"{clave}: {valor}")
