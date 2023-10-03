# Buscando recibos
# Los recibos de transacciones se pueden recuperar mediante la web3.eth.get_transaction_receiptAPI.
# ¿Qué son los recibos?
# Los recibos de transacciones son documentos generados después de realizar una transacción en la red blockchain. Proporcionan información detallada sobre la transacción y su estado.
# Algunos de los datos que se incluyen en un recibo de transacción son:
# • Hash de la transacción: Es un identificador único para la transacción en la red blockchain.
# • Estado de la transacción: Indica si la transacción se ha completado correctamente o si ha ocurrido algún error.
# • Bloque de la transacción: Número de bloque en el que se incluyó la transacción en la cadena de bloques.
# • Gas utilizado: La cantidad de unidades de gas utilizadas para ejecutar la transacción.
# • Dirección del contrato: Si la transacción involucra la creación de un contrato, se proporciona la dirección del contrato resultante.
# • Eventos registrados: Si la transacción generó eventos, se incluyen los detalles de dichos eventos en el recibo.
# Estos recibos de transacciones son útiles para verificar el estado y la información de una transacción realizada en la red blockchain, lo que permite a los desarrolladores y usuarios obtener información detallada sobre las transacciones y realizar un seguimiento de su progreso en la cadena de bloques.
# web3.eth.get_transaction_receipt('0x5c504ed432cb51138bcf09aa5e8a410dd4a1e204ef84bfed1be16dfba1b22060')

# Ejempplo

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
    recibo = web3.eth.get_transaction_receipt('0x5c504ed432cb51138bcf09aa5e8a410dd4a1e204ef84bfed1be16dfba1b22060')
    print("Transaccion: ", recibo)
    # mostrar las clave:valor
    for clave, valor in recibo.items():
        print(f"{clave}: {valor}")

# Si no se puede encontrar ninguna transacción para el hash dado, este método generará -web3.exceptions.TransactionNotFound.
