# Copyright (c) 2023 [Victoria Gong]
# Licensed under the MIT License (see LICENSE for details)

default_payload = {
    "jsonrpc": "2.0",
    "method": "{}",
    "params": [],
    "id": 1
}

# Fetch Avalanche C-Chain transaction data
def fetch_avalanche_tx(
    tx_hash,
    payload_: dict,
    fetch_tx_dict: dict = None,
    url_: str = "https://api.avax.network/ext/bc/C/rpc",
    method_call: str = "eth_getTransactionByHash",

):
    """
    # todo: check all api endpoints and update the function to handle different chains
    Fetch Avalanche C-Chain transaction details in JSON format
    :param tx_hash:
    :param fetch_tx_dict:
    :param payload_:
    :param method_call:
    :param url_:
    
    :return:
    """

    
    response = requests.post(
        url_,
        json=payload_,
    )
    return response.json()


# Fetch Ethereum transaction data
def fetch_ethereum_tx(
    tx_hash,
    url_eth: str = "https://mainnet.infura.io/v3/{}",
    project_id: str = os.getenv("INFURA_PROJECT_ID"),
    method_call: str = "eth_getTransactionByHash",
):
    """

    :param tx_hash:
    :param url_eth:
    :param project_id:
    :param method_call:
    :return:
    """
    url_ = url_eth.format(project_id)
    payload = {
        "jsonrpc": "2.0",
        "method": method_call,
        "params": [tx_hash],
        "id": 1,
    }
    response = requests.post(url_, json=payload)
    return response.json()


# Fetch Flare FTSO price data
def fetch_flare_ftso_price(asset):
    url = f"https://flare-api.com/ftso/{asset}/price"  # Example endpoint
    response = requests.get(url)
    return response.json()

# Example usage
if __name__ == "__main__":
    import os
    from dotenv import load_dotenv
    from web3 import Web3
    import requests
    import json
    

    # # Load environment variables from .env file
    load_dotenv()

    # # Access environment variables
    private_key = os.getenv("PRIVATE_KEY")
    infura_project_id = os.getenv("INFURA_PROJECT_ID")
    
    # Connect to Ethereum/Avalanche node
    w3 = Web3(
        Web3.HTTPProvider(
            f"https://mainnet.infura.io/v3/{infura_project_id}"
        )
    )
    
    # Example usage
    account_address = w3.eth.account.from_key(private_key).address
    print(
        f"Account Address: {account_address}"
    )
    solidity_mapper = {}
    
    avalanche_tx_data = fetch_avalanche_tx(
        fetch_tx_dict=default_payload.format("eth_getTransactionByHash"),
        tx_hash="0x...",

    )
    ethereum_tx_data = fetch_ethereum_tx("0x...")
    price_data = fetch_flare_ftso_price("AVAX")
    print(avalanche_tx_data)
    print(ethereum_tx_data)
    print(price_data)
    
    breakpoint()