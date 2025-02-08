# Copyright (c) 2023 [Victoria Gong]
# Licensed under the MIT License (see LICENSE for details)

import json
from web3 import Web3

# Load private key and Infura project ID
with open("config/secrets.json", "r") as f:
    secrets = json.load(f)
    private_key = secrets["private_key"]
    infura_project_id = secrets["infura_project_id"]

# Connect to Ethereum/Avalanche node
w3 = Web3(Web3.HTTPProvider(f"https://mainnet.infura.io/v3/{infura_project_id}"))
chain_id = 1  # Ethereum Mainnet (use 43114 for Avalanche C-Chain)
account_address = w3.eth.account.from_key(private_key).address

# Load deployed contract addresses
with open("config/deployed_contracts.json", "r") as f:
    deployed_contracts = json.load(f)
    verifier_address = deployed_contracts["verifier_address"]
    executor_address = deployed_contracts["executor_address"]

# Load contract ABIs
with open("contracts/TradeVerifier.abi", "r") as f:
    verifier_abi = json.load(f)

with open("contracts/TradeExecutor.abi", "r") as f:
    executor_abi = json.load(f)

# Initialize contracts
verifier_contract = w3.eth.contract(address=verifier_address, abi=verifier_abi)
executor_contract = w3.eth.contract(address=executor_address, abi=executor_abi)

# Execute trade
def execute_trade(tokenIn, tokenOut, amountIn, amountOutMin):
    txn = executor_contract.functions.executeTrade(
        tokenIn, tokenOut, amountIn, amountOutMin
    ).buildTransaction({
        "chainId": chain_id,
        "from": account_address,
        "gas": 2000000,
        "gasPrice": w3.toWei("50", "gwei"),
        "nonce": w3.eth.getTransactionCount(account_address),
    })
    signed_txn = w3.eth.account.signTransaction(txn, private_key=private_key)
    txn_hash = w3.eth.sendRawTransaction(signed_txn.rawTransaction)
    txn_receipt = w3.eth.wait_for_transaction_receipt(txn_hash)
    return txn_receipt

# Example usage
if __name__ == "__main__":
    trade_signal = {
        "tokenIn": "0x...",  # Replace with token address
        "tokenOut": "0x...",  # Replace with token address
        "amountIn": 1,  # Example amount
        "amountOutMin": 45  # Example minimum output
    }
    txn_receipt = execute_trade(**trade_signal)
    print(f"Trade executed: {txn_receipt}")
if __name__ == '__main__':
    breakpoint()