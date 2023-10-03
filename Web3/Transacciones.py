# Envío de transacciones:
# Hay algunas opciones para enviar transacciones:
# • send_transaction()
# • send_raw_transaction()
# • Llamar transact() a una función de contrato
# • utilizando construct_sign_and_send_raw_middleware()
# Para obtener más contexto, consultarla Guía de https://web3py.readthedocs.io/en/latest/transactions.html
# envío de transacciones .
# Este tipo de ejemplos lo veremos con GANACHE ( se enviara como instalar Ganache)

# Buscar transacciones con web3.eth.get_transaction()
# web3.eth.get_transaction('0x5c504ed432cb51138bcf09aa5e8a410dd4a1e204ef84bfed1be16dfba1b22060')
# Mas opciones en  https://web3py.readthedocs.io/en/stable/web3.eth.html#get-transaction

# Ejemplo

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

# Obtener saldo
if web3.is_connected():
    transaccion = web3.eth.get_transaction('0x5c504ed432cb51138bcf09aa5e8a410dd4a1e204ef84bfed1be16dfba1b22060')
    print("Transaccion: ", transaccion)
    print()
    print()
# Lo dejo mas bonito con el for
    for clave, valor in transaccion.items():
        print(f"{clave}: {valor}")

# El significado de cada clave:
# • blockHash: Es el hash del bloque en el que se incluyó esta transacción.
# • blockNumber: Es el número del bloque en el que se incluyó esta transacción.
# • from: Es la dirección del remitente de la transacción, es decir, la dirección que envió los fondos.
# • gas: Es la cantidad de unidades de gas asignadas a esta transacción.
# • gasPrice: Es el precio del gas en wei que el remitente está dispuesto a pagar por cada unidad de gas.
# • hash: Es el hash único de esta transacción.
# • input: Es el dato de entrada de la transacción, generalmente utilizado para especificar una función o datos adicionales.
# • nonce: Es el número de secuencia de la transacción, que garantiza que no se puedan duplicar transacciones con la misma dirección del remitente.
# • r y s: Son componentes de la firma digital de la transacción.
# • to: Es la dirección del destinatario de la transacción, es decir, la dirección que recibió los fondos.
# • transactionIndex: Es el índice de esta transacción dentro del bloque en el que se incluyó.
# • type: Indica el tipo de transacción. El valor 0 generalmente representa una transacción estándar, mientras que otros valores pueden representar tipos específicos de transacciones.
# • v: Es el componente de la firma digital que se utiliza para recuperar la clave pública del remitente.
# • value: Es la cantidad de ether (o cualquier otra criptomoneda) transferida en esta transacción.
# Si no se puede encontrar ninguna transacción para el hash dado, este método generará - web3.exceptions.TransactionNotFound.

