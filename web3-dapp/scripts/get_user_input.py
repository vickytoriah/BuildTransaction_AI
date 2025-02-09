# Copyright (c) 2023 [Victoria Gong]
# Licensed under the MIT License (see LICENSE for details)

import os
from dotenv import load_dotenv
from web3 import Web3
import requests
import json

solidity_contracts_mapper = {
    'AirSwapFlare': {
        'verifier_source': 'contracts/TradeVerifierFlare.sol',
        'executor_source': 'contracts/TradeExecutorAirswap.sol',
    },
    'UniV3LFJ': {
        'verifier_source': 'contracts/TradeVerifierUniV3.sol',
        'executor_source': 'contracts/TradeExecutorLFJ.sol',
    },
}

# Load environment variables from .env file
load_dotenv()

# Access environment variables
private_key = os.getenv("PRIVATE_KEY")
infura_project_id = os.getenv("INFURA_PROJECT_ID")


if __name__ == '__main__':
    breakpoint()