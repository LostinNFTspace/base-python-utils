from web3 import Web3

BASE_RPC = "https://mainnet.base.org"
w3 = Web3(Web3.HTTPProvider(BASE_RPC))

gas_price = w3.eth.gas_price
print("Current Base gas price (wei):", gas_price)
