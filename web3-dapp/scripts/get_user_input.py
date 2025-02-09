# Copyright (c) 2023 [Victoria Gong]
# Licensed under the MIT License (see LICENSE for details)
import requests
import os
from global_vars_ import *
from dotenv import load_dotenv
from web3 import Web3
from frontendAPI.graph_client import GraphClient, main as main_
from frontendAPI.response_format import response_schema
from fetch_data import fetch_tx_data, fetch_flare_ftso_price, fetch_ethereum_tx

global DEFINED_CHAIN

# Access environment variables
private_key = os.getenv("PRIVATE_KEY")
infura_project_id = os.getenv("INFURA_PROJECT_ID")
frontend_domain = os.getenv("FRONTEND_DOMAIN")
frontend_base_url = os.getenv("FRONTEND_BASE_URL")


# # Connect to Ethereum/Avalanche node
w3 = Web3(Web3.HTTPProvider(f"https://mainnet.infura.io/v3/{infura_project_id}"))
chain_id = 1  # Ethereum Mainnet (use 43114 for Avalanche C-Chain)


# Get User input
def get_user_input(
    frontend_API: str = frontend_base_url,
    frontend_domain: str = frontend_domain,
    response_dict: dict = response_schema,
    model_specifications_dict_: dict = model_specifications,
    
):
    """
    Get user input about Exchange and for trade execution,
    Retrieve the frontend metadata of the user input: model's diagramatic representation with token pair and execution preferences for gas and slippage
    :param frontend_API:
    :param frontend_domain:
    :param response_dict:
    :param model_specifications_dict_:
    :return:
    """
    model_to_implement = {
        'infura_project_id': infura_project_id,
        'eth_mainnet_url': tx_fetch_endpoints['ETH_MAINNET'].format(infura_project_id),
        'eth_method': 'eth_getTransactionByHash',
        'tokens': '',
        'tx_hash': '',
        'model': {},
    }
    
    response_dict = frontendAPICall(
        response_dict=response_schema,
        frontend_API=frontend_API,
        frontend_domain=frontend_domain,
    )
    if response_dict is not None:
        token_pair = response_dict['data']['nodes']['data']['tokenPair']
        
        model_to_implement['model'].update(model_specifications_dict_[token_pair]['model'])
        modify_global_chain(
            new_value=model_to_implement['model'].keys()[0],
        )
    model_specs = fetch_tx_details(
        input_dict_params=model_to_implement,
        token_pair_=token_pair,
    )
    
    return model_specs


def frontendAPICall(
    response_dict: dict,
    frontend_API: str,
    frontend_domain: str,
):
    """
    Fetch the frontend metadata of the user input
    
    :param response_dict:
    :param frontend_API:
    :param frontend_domain:
    :return:
    """
    response_ = main_(
        base_url=frontend_API,
        domain_=frontend_domain,
        request_type='GET',
        response_schema=response_dict,
    )

    return response_
    

def fetch_tx_details(
    input_dict_params: dict,
    token_pair_: str,
    payload_d: dict = default_payload_dict,
):
    """
    Fetch transaction details in JSON format
    :param input_dict_params:
    :return:
    """
    
    fetch_url_tx = input_dict_params[token_pair_]['tx_details']['tx_fetch_url']
    fetch_url_price = input_dict_params[token_pair_]['tx_details']['tx_fetch_price']
    req_resp = fetch_tx_data(
        url_=fetch_url_tx,
        payload_=payload_d,
    )

    input_dict_params[token_pair_]['tx_hash'] = req_resp['hash']
    input_dict_params[token_pair_]['flare'] = fetch_flare_ftso_price(token_pair_)

    req_eth = requests.get(
        input_dict_params['eth_mainnet_url'].format(input_dict_params['infura_project_id']),
        json=payload_d['params'].append(input_dict_params['tx_hash']),
    )
    input_dict_params['tx_details']['eth'] = req_eth['tx_details']
    req_resp_price = requests.get(
        fetch_url_price.format(
            req_resp['hash']
        ),
        json=payload_d,
    )
    input_dict_params[token_pair_]['price'] = req_resp_price['price']
    return input_dict_params
    

    # req_payload_updated = payload_d
    # payload_t = default_payload_dict
    # payload_ = {
    #     'model': '',
    #     'tx_details': {},
    #     'fetch_tx_dict': {
    #         'url_': tx_fetch_endpoints[]
    #         'method_call': 'eth_getTransactionByHash',
    #         'payload_': {},
    #     },
    #     'url_': tx_fetch_endpoints['avax_tx'],
    # }
    #
    #


if __name__ == '__main__':
    breakpoint()