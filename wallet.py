import os
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

# Configuration Base Sepolia (Testnet)
RPC_URL = os.getenv("RPC_URL")
PRIV_KEY = os.getenv("PRIVATE_KEY")
# Adresse USDC officielle sur Base Sepolia
USDC_ADDRESS = "0x036CbD53842c5426634e7929541eC2318f3dCF7e"

w3 = Web3(Web3.HTTPProvider(RPC_URL))
account = w3.eth.account.from_key(PRIV_KEY)

def get_usdc_balance():
    # ABI minimal pour lire le solde
    abi = [{"constant":True,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"type":"function"}]
    contract = w3.eth.contract(address=USDC_ADDRESS, abi=abi)
    balance = contract.functions.balanceOf(account.address).call()
    return w3.from_wei(balance, 'mwei') # USDC a 6 décimales

def pay_usdc(amount_usdc, recipient_address):
    # Logique de paiement simplifiée pour le testnet
    print(f"💸 Simulating payment of {amount_usdc} USDC on Base Sepolia...")
    return True
