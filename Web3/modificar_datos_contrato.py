# Para modificar datos en un contrato vamos a usar dos funciones en el contrato, 
# Una que de un saludo como en la anterios práctica y otra que modifique el saludo.
# El contrato en solidity seria una ampliación del ejercicio saludo:
# // SPDX-License-Identifier: MIT
# pragma solidity ^0.8.0;

# contract Greeter {
#    string public greeting;
#
#   constructor() {
#        greeting = "Hello";
#    }
# Prmimera función que devuelve hello
#    function getGreeting() public view returns (string memory) {
#        return greeting;
#    }
# Segunda función que modifica la variable greeting por _newGreeting
#    function setGreeting(string memory _newGreeting) public {
#        greeting = _newGreeting;
#    }
# }
# Una vez deplagado el contrato en la blockchain de ganache desarrollamos el codigo en python


# Como siempre cargamos las librerias y comprobamos la conexión a ganache

import json
from web3 import Web3


# Conexión a Ganache
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Conecta a ganache
if not web3.is_connected():
    print("Error: No se pudo conectar a la red Ethereum.")
    exit()
else:
    print("Conexion realizada")

# asignamos a varibles el abi y el address del contrato para poder acceder al el


abi = [{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"getGreeting","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"greeting","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_newGreeting","type":"string"}],"name":"setGreeting","outputs":[],"stateMutability":"nonpayable","type":"function"}]

# web3.to_checksum_address comprueba que la direccion es correcta

address = web3.to_checksum_address ('0x81eE3aC0175B1D27aBEd62f852DE93E72845A497')

# iniciamos el contrato

contract = web3.eth.contract(address=address, abi=abi)

# Obtenemos el saludo actual llamco a la primera función del contrato
# Esta función al no modificar ningún valor en el contrato no consume gas

current_greeting = contract.functions.getGreeting().call()
print("Saludo actual:", current_greeting)

# Para la siguiente función como vamos a modificar un valor de una variable, si que nos exige que 
# Proporcionemos una cuenta donde de cobre el gas de la operación
# En nuestro casomusarmos la primera cuenta que tenemos en ganache que será la del indice [0]
# Donde account es  la variable donde se almacena la direccion de la cuenta

account = web3.eth.accounts[0]

# Damos avalor a la nueva variable que modifica greeting

new_greeting = "¡HELLOOOO Blockmakers!"

# Llamamos a la función setGreeting que modifica el saludo y en transact indicamos donde cobrer el gas necesario

tx_hash = contract.functions.setGreeting(new_greeting).transact({'from': account})

# Esperamos hasta que quede minada la transacción

web3.eth.wait_for_transaction_receipt(tx_hash)

# Finalmente llamamos a la función getGreeting para comprobar que se ha modificado

updated_greeting = contract.functions.getGreeting().call()
print("Saludo actualizado:", updated_greeting)





