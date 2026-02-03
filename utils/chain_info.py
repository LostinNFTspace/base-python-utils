from web3 import Web3

BASE_RPC = "https://mainnet.base.org"
w3 = Web3(Web3.HTTPProvider(BASE_RPC))

print("Chain ID:", w3.eth.chain_id)
print("Latest block:", w3.eth.block_number)
