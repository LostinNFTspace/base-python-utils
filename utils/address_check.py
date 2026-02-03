from web3 import Web3

address = "0x0000000000000000000000000000000000000000"

is_valid = Web3.is_address(address)
print(f"Address valid: {is_valid}")
