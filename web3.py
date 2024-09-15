from web3 import Web3

# BSC mainnet connection
bsc_rpc_url = "https://bsc-dataseed.binance.org/"
web3 = Web3(Web3.HTTPProvider(bsc_rpc_url))

# Wallet and token details
wallet_address = "0xfd81c579d29881c2387e3823e430fde359338dec"
token_contract_address = "0x55d398326f99059ff775485246999027b3197955"  # Binance-Peg BSC-USD contract address
block_number = 39994374

# ABI for BEP-20 token (ERC-20 standard is sufficient for balanceOf)
bep20_abi = [
    {
        "constant": True,
        "inputs": [{"name": "_owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "balance", "type": "uint256"}],
        "type": "function",
    }
]

# Token contract instance
token_contract = web3.eth.contract(address=Web3.to_checksum_address(token_contract_address), abi=bep20_abi)

# Get balance at the specified block
balance = token_contract.functions.balanceOf(Web3.to_checksum_address(wallet_address)).call(block_identifier=block_number)

# Convert balance from Wei to token's smallest unit (assuming 18 decimals for Binance-Peg BSC-USD)
balance_token_units = web3.fromWei(balance, 'ether')
print(f"Balance at block {block_number}: {balance_token_units} BSC-USD")
