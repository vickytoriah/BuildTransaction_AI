# Copyright (c) 2023 [Victoria Gong]
# Licensed under the MIT License (see LICENSE for details)

import os
from dotenv import load_dotenv
from web3 import Web3
import requests
import json

# Load environment variables from .env file
load_dotenv()

# Access environment variables
private_key = os.getenv("PRIVATE_KEY")
infura_project_id = os.getenv("INFURA_PROJECT_ID")

default_payload_dict = {
    "jsonrpc": "2.0",
    "method": "",  # method function to call, e.g., eth_getTransactionByHash
    "params": [],  # tx_hash of the token pair
    "id": 1,
}

tx_fetch_endpoints = {
    'eth_mainnet': f'https://mainnet.infura.io/v3/{}',
    'avax_tx': 'https://api.avax.network/ext/bc/C/rpc',
    'flare': f"https://flare-api.com/ftso/{}/price",
    
}

w3 = Web3(Web3.HTTPProvider(tx_fetch_endpoints['eth_mainnet'].format(infura_project_id)))


solidity_contracts_mapper = {
    'AirSwapFlare': {
        'fetch_tx_url': 'https://api.avax.network/ext/bc/C/rpc',
        'payload_params': default_payload_dict.format('eth_getTransactionByHash'),
        
        
        'verifier_source': 'contracts/TradeVerifierFlare.sol',
        'executor_source': 'contracts/TradeExecutorAirswap.sol',
    },
    
    'UniV3LFJ': {
        'verifier_source': 'contracts/TradeVerifierUniV3.sol',
        'executor_source': 'contracts/TradeExecutorLFJ.sol',
    },
}

input_params = {
    'tx_pair': 'AVAX/USDT' ,
    'tx_hash': '',
    'fetch_tx_dict': None,
    'method_call': 'eth_getTransactionByHash',
    'payload_': default_payload_dict,
    'url_': tx_fetch_endpoints['avax_tx'],
}

# Get User input
# todo: finish this function and optimize the imports across the project
def get_user_input(
    frontend_API: str,
    

):
    """
    Get user input about Exchange and for trade execution,
    Retrieve the frontend metadata of the user input: model's diagramatic representation with token pair and execution preferences for gas and slippage

    :return:
    """
    
    
    exchange_name = input_dict_params['Exchange']
    if 'avax' or 'avalanche' in exchange_name.lower():
    
    if 'avax' in token_pair.lower():
        endpoint_index = 'avax_tx'
        contract_mapper_key = 'AirSwapFlare'
    
    elif 'eth' in token_pair.lower():
        endpoint_index = 'eth_mainnet'
        contract_mapper_key = 'UniV3LFJ'
    else:
        endpoint_index = 'flare'
    
    pass

def frontendAPICall():

def fetch_tx_details(
    input_dict_params: dict,
    token_pair: str,
):
    """
    Fetch transaction details in JSON format
    :param input_dict_params:
    :return:
    """
    
    model_specifications = {
        'model': 'AirSwapFlare',
        'tx_details': {},
        'fetch_tx_dict': {
            'url_': tx_fetch_endpoints[]
            'method_call': 'eth_getTransactionByHash',
            'payload_': {},
        },
        'url_': tx_fetch_endpoints['avax_tx'],
    }
    


if __name__ == '__main__':
    breakpoint()