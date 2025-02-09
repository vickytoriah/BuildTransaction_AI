# Copyright (c) 2023 [Victoria Gong]
# Licensed under the MIT License (see LICENSE for details)

import json
from web3 import Web3
from solcx import compile_standard, install_solc

# Load private key and Infura project ID
with open("./config/secrets.json", "r") as f:
    secrets = json.load(f)
    private_key = secrets["private_key"]
    infura_project_id = secrets["infura_project_id"]

# Connect to Ethereum/Avalanche node
w3 = Web3(Web3.HTTPProvider(f"https://mainnet.infura.io/v3/{infura_project_id}"))
chain_id = 1  # Ethereum Mainnet (use 43114 for Avalanche C-Chain)
account_address = w3.eth.account.from_key(private_key).address

# Install Solidity compiler
install_solc("0.8.0")

# Compile the Solidity contracts
with open("contracts/TradeVerifier.sol", "r") as f:
    verifier_source = f.read()

with open("contracts/TradeExecutor.sol", "r") as f:
    executor_source = f.read()

compiled_verifier = compile_standard({
    "language": "Solidity",
    "sources": {
        "TradeVerifier.sol": {"content": verifier_source},
    },
    "settings": {
        "outputSelection": {
            "*": {"*": ["abi", "evm.bytecode"]}
        }
    }
})

compiled_executor = compile_standard({
    "language": "Solidity",
    "sources": {
        "TradeExecutor.sol": {"content": executor_source},
    },
    "settings": {
        "outputSelection": {
            "*": {"*": ["abi", "evm.bytecode"]}
        }
    }
})

# Extract ABI and bytecode
verifier_abi = compiled_verifier["contracts"]["TradeVerifier.sol"]["TradeVerifier"]["abi"]
verifier_bytecode = compiled_verifier["contracts"]["TradeVerifier.sol"]["TradeVerifier"]["evm"]["bytecode"]["object"]

executor_abi = compiled_executor["contracts"]["TradeExecutor.sol"]["TradeExecutor"]["abi"]
executor_bytecode = compiled_executor["contracts"]["TradeExecutor.sol"]["TradeExecutor"]["evm"]["bytecode"]["object"]

# Deploy TradeVerifier
verifier_contract = w3.eth.contract(abi=verifier_abi, bytecode=verifier_bytecode)
verifier_txn = verifier_contract.constructor().buildTransaction({
    "chainId": chain_id,
    "from": account_address,
    "gas": 2000000,
    "gasPrice": w3.toWei("50", "gwei"),
    "nonce": w3.eth.getTransactionCount(account_address),
})
signed_verifier_txn = w3.eth.account.signTransaction(verifier_txn, private_key=private_key)
verifier_txn_hash = w3.eth.sendRawTransaction(signed_verifier_txn.rawTransaction)
verifier_txn_receipt = w3.eth.wait_for_transaction_receipt(verifier_txn_hash)
verifier_address = verifier_txn_receipt["contractAddress"]

# Deploy TradeExecutor
executor_contract = w3.eth.contract(abi=executor_abi, bytecode=executor_bytecode)
executor_txn = executor_contract.constructor(verifier_address).buildTransaction({
    "chainId": chain_id,
    "from": account_address,
    "gas": 2000000,
    "gasPrice": w3.toWei("50", "gwei"),
    "nonce": w3.eth.getTransactionCount(account_address),
})
signed_executor_txn = w3.eth.account.signTransaction(executor_txn, private_key=private_key)
executor_txn_hash = w3.eth.sendRawTransaction(signed_executor_txn.rawTransaction)
executor_txn_receipt = w3.eth.wait_for_transaction_receipt(executor_txn_hash)
executor_address = executor_txn_receipt["contractAddress"]

print(f"TradeVerifier deployed at: {verifier_address}")
print(f"TradeExecutor deployed at: {executor_address}")
if __name__ == '__main__':
    breakpoint()