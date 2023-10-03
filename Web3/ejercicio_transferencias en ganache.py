# Ejercicio para transferencias de cryto ETHER en la blockchain de pruebas de ganache
# Prinmero trabajamos con web3

from web3 import Web3

# Almacenamos la dirección de enlace de ganache que es en local y la llamammos con la función de web3

ganache_url = "HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Asignamos dos variables con las direcciones de las cuentas que queremos usar

account_1 = '0xC6a8862C63D3c3F3d9e464E3f05afbC0CE0cB6fF' # Rellenar con vuestra cuenta que elijais para el envio de las que teneis en Ganche
account_2 = '0x83b19E4ce958b0Bc2D3A7141224c216e1901eAd3' # Rellenar con vuestra cuenta que elijais para la recepcion de las que teneis en Ganche

# Es necesario una llave privada para poder transferir ether de una cuenta a otra
# La private key que se usa es la de la cuenta de donde sale el ether y lo podemos ver a la derecha del numero de cuenta de ganache

private_key = '0x8251244c3cb308ac2b268c8693097ea700a9d81bf634303cf2c79aa518109050' # Rellenar con la private key de la cuenta de envio

# definimos como nonce a los datos de cueta de envio

nonce = web3.eth.get_transaction_count(account_1)

# completamos los datos de la transacción dentro de un diccionario, en este caso dos transacciones tx y tx2

tx = {
    'nonce': nonce,
    'to': account_2,
    'value': web3.to_wei(1, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.to_wei('50', 'gwei'),
}
tx2 = {
    'nonce': nonce,
    'to': account_2,
    'value': web3.to_wei(1, 'ether'),
    'gas': 2000000,
    'gasPrice': web3.to_wei('50', 'gwei'),
}



# Firmamos la transacción con nuestra key en otra variable signed_tx y signed_tx2

signed_tx = web3.eth.account.sign_transaction(tx, private_key)
signed_tx2 = web3.eth.account.sign_transaction(tx2, private_key)

# Realizamos  la transacción con la función de web3

tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
print("Transaccion realizada. \nNumero de la transaccion: ", web3.to_hex(tx_hash))

tx_hash2 = web3.eth.send_raw_transaction(signed_tx2.rawTransaction)
print("Transaccion realizada. \nNumero de la transaccion: ", web3.to_hex(tx_hash2))

