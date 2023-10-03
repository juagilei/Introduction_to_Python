# Lamar a un contrato para ver el balance de una cuenta en ganache
from web3 import Web3

ganache_url = "http://127.0.0.1:7545"

web3 = Web3(Web3.HTTPProvider(ganache_url))

# Conecta a ganache
if not web3.is_connected():
    print("Error: No se pudo conectar a la red Ethereum.")
    exit()
else:
    print("Conexion realizada")

# introducimos los valores del contrato, la dirección y el abi

address_contract = web3.to_checksum_address("0x48FCE0935A29E037D3eFc760014f0b96CC9CE4FA")

abi = '[{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"getBalance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}]'

# Cargamos el contrato en una variable contract

contract = web3.eth.contract(address=address_contract, abi=abi)

# Solicitamos la cuenta a copnsultar

address = input('Introduce la direccion de donde ver el balance: ')

# Llamammos al conmtrato y su función

balance = contract.functions.getBalance(address).call()

saldoEnEther = web3.from_wei(balance, 'ether')


print()
print('El balance de la cuenta ',address,' es: ',saldoEnEther,' ether')
print()
print()



