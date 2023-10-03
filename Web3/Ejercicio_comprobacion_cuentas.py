# Importar web3 y conectarse a ganache

from web3 import Web3


ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Comprobamos si está conectado a ganache

if web3.is_connected():
    print("Conexión exitosa a Ganache")
else:
    print("No se pudo conectar a Ganache. Por favor, verifica la URL o tu conexión a Internet.")


# Asignar cuentas y comprobar si son validas
# Identifico todas la cuentas de ganache

ganache_accounts = web3.eth.accounts

# comparo la cuenta introducida con las de ganache para ver si son correctas

# Inicializo una variable para hacer el while y repetir has ta introducir la cuenta correcta

check=1

# Repito la operación hasta que la ciuenta sea correcta

while check==1:

    account_1 = input('Introduce el numero de cuenta de envio: ')

    if account_1 in ganache_accounts:
        print('La cuenta de envio es correcta')

        check=0

    else:
        print('La cuenta de envio es erronea')

check=1

# Repito la operación hasta que la ciuenta sea correcta

while check==1:

    account_2 = input('Introduce el numero de cuenta destino: ')

    if account_2 in ganache_accounts:

        print('La cuenta destino es correcta')
        check=0
    else:
        print('La cuenta destino es erronea')

# Comprobamos que las cuentas tienen fondos

saldo_cuenta_1 = web3.eth.get_balance(account_1)
saldo_cuenta1_ether = web3.from_wei(saldo_cuenta_1,'ether')
print('Saldo cuenta de envio: ',saldo_cuenta1_ether)

saldo_cuenta_2 = web3.eth.get_balance(account_2)
saldo_cuenta2_ether = web3.from_wei(saldo_cuenta_2,'ether')
print('Saldo cuenta de destino: ', saldo_cuenta2_ether)

# Vamos a comprobar que la llave privada pertenece a la cuenta de envio

private_key = input ('Introduce la llave privada de la cuenta de envio: ')

# Obtengo la direccion de la cuenta a través de la llave privada
# Obtengo la cue ta como un objeto (account) y luego saco la dirección de dentro del objeto (account.address)
account = web3.eth.account.from_key(private_key)
address = account.address


try :

    signed_tx = web3.eth.account.sign_transaction(account_1, private_key)
    print()
    print()
    print ('La llave es correcta y pertenece a la siguiente cuenta: ',address)

except TypeError:
    print()
    print()
    print('La llave privada es erronea')





