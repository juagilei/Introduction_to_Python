# Consukltar el saldo de una cuenta
# Utilozamos la funcion web3.eth.get_balance('hash'), el saldo nos lo da en Wei (1Ether=1000000000000000000 Wei)

#web3.eth.get_balance('0x742d35Cc6634C0532925a3b844Bc454e4438f44e')

# Con el metodo web3.from_wei podemos convertir el saldo a ether (u otra denominacion).
# Paso el saldo en wei

#web3.from_wei(3841357360894980500000001, 'ether')

# Para pasar de ether a wei (to.wei())

#from decimal import Decimal
#web3.to_wei(Decimal('3841357.360894980500000001'), 'ether')

# Ejemplo

from web3 import Web3
from decimal import Decimal

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
    saldo = web3.eth.get_balance('0x742d35Cc6634C0532925a3b844Bc454e4438f44e')
    print("Saldo: ", saldo)
    # transformar saldo en ether
    saldoEnEther = web3.from_wei(saldo, 'ether')
    print("Saldo en Ether: ", saldoEnEther)
    # pasar de nuevo a weim, hemos de importar decimal
    saldoEnWei = web3.to_wei(Decimal(saldoEnEther), 'ether')
    print("Saldo en Wei: ", saldoEnWei)
