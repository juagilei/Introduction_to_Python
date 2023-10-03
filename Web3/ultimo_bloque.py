# Obtener el último bloque
# podemos obtener el último bloque con la cadena 'latest' web3.eth.get_block('latest')

from web3 import Web3

# URL de Infura para la red de Ethereum (debes reemplazar "TU-PROYECTO-ID" con tu propio ID de proyecto de Infura)
infura_url = "https://mainnet.infura.io/v3/afb0ac49fed1439babdf70dce2495306"

# Crear una instancia de Web3 y conectarse a Infura
web3 = Web3(Web3.HTTPProvider(infura_url))

# Verificar la conexión
if web3.is_connected():
    print("Conexión exitosa a Infura")
else:
    print("No se pudo conectar a Infura. Por favor, verifica la URL o tu conexión a Internet.")

# Obtener el último

if web3.is_connected():
    bloque = web3.eth.get_block('latest')
    print("Datos del bloque: \n", bloque)

# Tampodemos ver el numero del ultimo bloque de la siguiente forma

    numero_bloque = web3.eth.block_number
    print("Número de bloque más reciente:", numero_bloque)

