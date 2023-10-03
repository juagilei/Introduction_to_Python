# Ejercicio para obtener los datos de un contrato.
# Direccion: Para conseguir los datos de un contrato necesitamos su dirección que viene dada en hexadecimal
# ABI:  Tambien necsitamos para conseguir los datos de un contrato su ABI que es un conjunto de claves en modo JSON que nos sirve para descifrar el contrato mas o menos 
# Lo promero es importar web3 y json
import json
from web3 import Web3
# URL de Infura para la red de Ethereum (debes reemplazar "TU-PROYECTO-ID" con␣ ↪tu propio ID de proyecto de Infura)

infura_url = ("https://mainnet.infura.io/v3/afb0ac49fed1439babdf70dce2495306") # Crear una instancia de Web3 y conectarse a Infura

web3 = Web3(Web3.HTTPProvider(infura_url))

# Verificar la conexión

if web3.is_connected(): 
    print("Conexión exitosa a Infura")
else:
    print("No se pudo conectar a Infura. Por favor, verifica la URL o tu conexión a Internet.")
if web3.is_connected():

# Vamos a trabajar con un contrato de token conocido como OMG del cual extraemos la dirección y el ABI de Etherscan.

# ABI OMG

    abi = json.loads('[{"constant":true,"inputs":[],"name":"mintingFinished","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"unpause","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_amount","type":"uint256"}],"name":"mint","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"paused","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"finishMinting","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"pause","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_amount","type":"uint256"},{"name":"_releaseTime","type":"uint256"}],"name":"mintTimelocked","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"type":"function"},{"anonymous":false,"inputs":[{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[],"name":"MintFinished","type":"event"},{"anonymous":false,"inputs":[],"name":"Pause","type":"event"},{"anonymous":false,"inputs":[],"name":"Unpause","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"}]')

# Direccion OMG

    address = "0xd26114cd6EE289AccF82350c8d8487fedB8A0C07"
    
# Ahora podemos guardar el contrato en una variable de la siguiente forma:

    contract = web3.eth.contract(address=address, abi=abi)

# Con esta variable vamos a ir pidiendo datos del contrato:
# Primero el suminisgtro total de todos los tokens:

    totalSupply = contract.functions.totalSupply().call()
    print("TotalSuply en Ether :", web3.from_wei(totalSupply, 'ether'))
    print()

# En segundo lugar el nombre de la direccion del token:

    print(contract.functions.name().call())
    print()

# En tercer lugar el nombre del simbolo del token:

    print(contract.functions.symbol().call())
    print()

# Por ultimo podemos consukltar el saldo del contrato y `pasarlo de wei a ether

    balance = contract.functions.balanceOf(address).call()
    print("Balance en Ether : ", web3.from_wei(balance, 'ether'))
    print()

