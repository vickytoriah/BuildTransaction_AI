# Copyright (c) 2023 [Victoria Gong]
# Licensed under the MIT License (see LICENSE for details)

import json
from web3 import Web3
from solcx import compile_standard, install_solc
from global_vars_ import *

# Load private key and Infura project ID, from global_vars_
private_key = private_key
infura_project_id = infura_project_id

# Connect to Ethereum/Avalanche node
w3 = Web3(Web3.HTTPProvider(f"https://mainnet.infura.io/v3/{infura_project_id}"))
chain_id = 1  # Ethereum Mainnet (use 43114 for Avalanche C-Chain)
account_address = w3.eth.account.from_key(private_key).address

# solidity_contracts_mapper = {
#     'AirSwapFlare': {
#         'verifier_source': 'contracts/TradeVerifierFlare.sol',
#         'executor_source': 'contracts/TradeExecutorAvalanche.sol',
#     },
#     'UniV3LFJ': {
#         'verifier_source': 'contracts/TradeVerifierUniV3.sol',
#         'executor_source': 'contracts/TradeExecutorLFJ.sol',
#     },
# }
# Install Solidity compiler
install_solc("0.8.0")

# Compile the Solidity contracts
solidity_contracts = {}
with open(solidity_contracts_mapper[DEFINED_CHAIN]['verifier_source'], "r") as f:
    verifier_source = f.read()

# Code example without global_vars_.py
# with open("contracts/TradeVerifierFlare.sol", "r") as f:
#     solidity_contracts['AirSwapFlare']['verifier_source'] = f.read()

with open(solidity_contracts_mapper[DEFINED_CHAIN]['executor_source'], "r") as f:
    executor_source = f.read()

# Code example without global_vars_.py
# with open("contracts/TradeExecutorAvalanche.sol", "r") as f:
#     solidity_contracts['AirSwapFlare']['executor_source'] = f.read()

solidity_contracts_mapper[DEFINED_CHAIN]['executor_source']['file_name'] = solidity_contracts_mapper[DEFINED_CHAIN]['executor_source'].split('/')[1]
solidity_contracts_mapper[DEFINED_CHAIN]['verifier_source']['file_name'] = solidity_contracts_mapper[DEFINED_CHAIN]['verifier_source'].split('/')[1]

compiled_verifier = compile_standard({
    "language": "Solidity",
    "sources": {
        solidity_contracts_mapper[DEFINED_CHAIN]['verifier_source']['file_name']: {"content": verifier_source},
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
        solidity_contracts_mapper[DEFINED_CHAIN]['executor_source']['file_name']: {"content": executor_source},
    },
    "settings": {
        "outputSelection": {
            "*": {"*": ["abi", "evm.bytecode"]}
        }
    }
})

# Extract ABI and bytecode
verifier_abi = compiled_verifier["contracts"]["TradeVerifierUniV3.sol"]["TradeVerifier"]["abi"]
verifier_bytecode = compiled_verifier["contracts"]["TradeVerifierUniV3.sol"]["TradeVerifier"]["evm"]["bytecode"]["object"]

executor_abi = compiled_executor["contracts"]["TradeExecutorLFG.sol"]["TradeExecutor"]["abi"]
executor_bytecode = compiled_executor["contracts"]["TradeExecutorLFG.sol"]["TradeExecutor"]["evm"]["bytecode"]["object"]

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