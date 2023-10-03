# Inspección de bloques con Web3.py

# Vamos a inspeccionar bloques en ethereum desde el programa en python.
# Tenemos que navegar por la red de ethereum por lo que usaremos infura para navegar.

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

# una vez conectador a la red de ethereum a traves de infura podemos obtener el numero del ultimo bloque dcon la función "web3.eth.block_number":
print()
print("Número del último bloque: ", web3.eth.block_number)
print()
# tambien podemos obtener los datos del ultimo bloque de la sigiente forma "web3.eth.get_block('latest')"

# Obtener el ultimo bloque
print("Último bloque: ", web3.eth.get_block('latest'))
print()
# Como bien sabemos los da todos los daros del  ultimo bloque pero todo sin organizar

# Si queremos inspeccionar una serie de bloques podemos recorrerlos con un for por ejemplo
# podemos recirrer desde el ultimo bloque hasta el décimo anterior de la siguiente forma

# Obtener los ultimos bloques
# latest es el numero del ultimo bloque
latest = web3.eth.block_number
for i in range(0, 10):
  print()
  print("Bloque", (latest - i) , ": ", web3.eth.get_block(latest - i))
  print()
# i va del 0 al 10 y va restando el numero al ultimo bloque de la siguiente forma -0,-1,-2,-3,....,-10

# web3.py tambien no permite obtener los datos de una transaccion mediante el hash
# Obtener la trasnsaccion de un bloque especifico
hash = '0x66b3fd79a49dafe44507763e9b6739aa0810de2c15590ac22b5e2f0a3f502073'
print(web3.eth.get_transaction_by_block(hash, 2))

# - hash: El hash del bloque del que se desea obtener la transacción.

# - 2: Este número representa el índice de la transacción dentro del bloque. Los bloques en Ethereum pueden contener múltiples transacciones, y este argumento se utiliza para especificar cuál de ellas se desea obtener. 
#     En este caso, se solicita la transacción en el índice 2 del bloque.

# Pero todo esto esta sin organizar y al final es imposible ver los datos
# Ahora vamos a filtrar los datos 
# Teniendo en cuenta que los bloques estan estructurados como diccionarios, paramos a ver solo lo que queremos ver de la siguiente forma

# Obtener información del último bloque

latest_block = web3.eth.get_block('latest')
print()
print("Último bloque:")
print()
# solo imprimo el numero del bloque
print("  Número de bloque:", latest_block.number)
print()
# solo imprimo el hash del ultimo bloque
print("  Hash del bloque:", latest_block.hash.hex())
print()

# Podemosha er lo mismo con los ultimos 10 bloques
# Obtengo el numero del ultimo bloque
latest_block_number = web3.eth.block_number

num_blocks = 10
print("Últimos", num_blocks, "bloques:")
# Este range lo plateamos de una forma diferente donde  recorremos del ultimo bloque restando de uno en uno hasta el bloque 10 (depemndiendo del num_blocks)
for i in range(latest_block_number, latest_block_number - num_blocks, -1):
    block = web3.eth.get_block(i)
    print()
    print("  Bloque", block.number)
    print()
    print("    Hash:", block.hash.hex())
    print()
    # con len podemos contar los elementos del bloque tal y como se hace en un diccionario ya que cada ransacción es un elemeto
    print("    Número de transacciones:", len(block.transactions))
    print()

# Por ultimo tambien podemos obtener los datos de una transacción en concreto mediante el index de la transacción y el hash del bloque
# Obtener información de una transacción en un bloque específico
block_hash = '0x50f412bf67bc9baa2b81a308d473827b305796ae9da628a91b433ccba4f00719'
transaction_index = 2
transaction = web3.eth.get_transaction_by_block(block_hash, transaction_index)
if transaction:
    print("Información de la transacción en el bloque", block_hash)
    print("  Hash de la transacción:", transaction.hash.hex())
# Al ser un diccionario el dato del emisor viene dado por la clave "from"
    print("  Emisor:", transaction['from'])
# El receptor viene dado por la clave "to"
    print("  Receptor:", transaction['to'])
# El coste viene dado por  "value" y luego con "ether" la funcion convierte el wei en ether

    print("  Valor enviado:", web3.from_wei(transaction['value'], 'ether'), "ETH")
else:
    print("No se encontró ninguna transacción en el bloque", block_hash, "con el índice", transaction_index)










