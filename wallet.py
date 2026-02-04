import os
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

# Blockchain Connection
RPC_URL = os.getenv("RPC_URL")
PUBLIC_ADDRESS = os.getenv("PUBLIC_ADDRESS")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
w3 = Web3(Web3.HTTPProvider(RPC_URL))

# USDC Configuration on Base Network
USDC_ADDRESS = "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913"
USDC_ABI = [
    {"constant": True, "inputs": [{"name": "_owner", "type": "address"}], "name": "balanceOf", "outputs": [{"name": "balance", "type": "uint256"}], "type": "function"},
    {"constant": True, "inputs": [], "name": "decimals", "outputs": [{"name": "", "type": "uint8"}], "type": "function"},
    {"constant": False, "inputs": [{"name": "_to", "type": "address"}, {"name": "_value", "type": "uint256"}], "name": "transfer", "outputs": [{"name": "", "type": "bool"}], "type": "function"}
]

def get_usdc_balance():
    """Returns the USDC balance of the agent's wallet."""
    contract = w3.eth.contract(address=USDC_ADDRESS, abi=USDC_ABI)
    raw_balance = contract.functions.balanceOf(PUBLIC_ADDRESS).call()
    decimals = contract.functions.decimals().call()
    return raw_balance / (10 ** decimals)

def pay_usdc(recipient_address, amount):
    """Signs and sends an USDC payment on the Base network."""
    contract = w3.eth.contract(address=USDC_ADDRESS, abi=USDC_ABI)
    amount_raw = int(amount * 10**6) # USDC uses 6 decimals
    
    nonce = w3.eth.get_transaction_count(PUBLIC_ADDRESS)
    
    # Build transaction
    tx = contract.functions.transfer(recipient_address, amount_raw).build_transaction({
        'chainId': 8453, # Base Mainnet ID
        'gas': 100000, 
        'gasPrice': w3.eth.gas_price, 
        'nonce': nonce,
    })
    
    # Sign and broadcast
    signed_tx = w3.eth.account.sign_transaction(tx, private_key=PRIVATE_KEY)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
    return w3.to_hex(tx_hash)

if __name__ == "__main__":
    print(f"Agent Wallet Address: {PUBLIC_ADDRESS}")
    print(f"Current Balance: {get_usdc_balance()} USDC")
