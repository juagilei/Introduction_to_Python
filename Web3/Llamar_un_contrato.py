# Vamos a llamar el contrato saludo que hemos compilado en remix para desplegarlo en ganache
# Importar web3 y conectarse a ganache

from web3 import Web3

# importamos la libreria json



ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Comprobamos si está conectado a ganache

if web3.is_connected():
    print("Conexión exitosa a Ganache")
else:
    print("No se pudo conectar a Ganache. Por favor, verifica la URL o tu conexión a Internet.")

# Pasamos el codigo ABI a una variable para poder realizar la llamada, ya que es necesadio el abi y la dirección.

abi = [{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"getGreeting","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"greeting","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"}]

# incorporo la direccion a address

address = web3.to_checksum_address("0xBbAa3B06F919F4BC27e35B7DF8E084ed40c20093")

# Introduzco el contrato en una variable con los datos de address y  abi

contract = web3.eth.contract(address=address, abi=abi)

# imprimo el contrato con la función que llama al contrato en la blockchain de ganache

print(contract.functions.getGreeting().call())
