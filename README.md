# Web3 dApp for On-Chain Data Retrieval and Trade Execution

## **Introduction**
This repository contains a Web3 decentralized application (dApp) that retrieves on-chain data, performs off-chain strategy analysis, and executes trades on decentralized exchanges (DEXs) such as **AirSwap** and **LFG**. The dApp integrates with **Uniswap V3** for price verification and supports both **Ethereum Mainnet** and **Avalanche C-Chain**.

### The model's purpose is to:
1. Retrieve on-chain data using Avalanche C-Chain API and Flare FTSO. (e.g., transaction data, price feeds)
2. Perform off-chain strategy analysis to generate trade signals.
   1. Index data using SubQuery for efficient querying.
3. Verify trade prices using Uniswap V3 or Flare FTSO's on-chain interface.
4. Execute trades on a DEX (AirSwap or LFG).

### This setup ensures secure, decentralized, and efficient data retrieval, verification, and trade execution.

---

## **Folder Structure**
```
web3-dapp/
├── contracts/                     # Solidity smart contracts
│   ├── TradeVerifierFlare.sol     # Flare FTSO price verification
│   ├── TradeVerifierUniV3.sol     # Flare UniSwapV3 price verification
│   ├── TradeExecutorAvalanche.sol # AirSwap trade execution
│   ├── TradeExecutorLFG.sol       # LFG trade execution
├── scripts/                       # Python scripts for off-chain logic
│   ├── frontendAPI/               # Communites with the frontend and integrates a user generated input for the Exchange Mapper and trade execution
│   │   ├── examples/*             # Examples of frontend API usage
│   │   ├── graph_client.py        # GraphClient frontend class 
│   │   ├── post_spec.md           # Overview of the frontend usage 
│   ├── fetch_data.py              # Fetch on-chain data
│   ├── get_user_input.py          # Retrieves user input from frontend diagram for Exchange mapper
│   ├── strategy_analysis.py       # Off-chain strategy analysis
│   ├── deploy_contracts.py        # Deploy contracts
│   ├── execute_trade.py           # Execute trade
├── subquery/                      # SubQuery configuration for indexing
│   ├── project.yaml               # SubQuery configuration
│   ├── schema.graphql             # SubQuery GraphQL schema
│   ├── package.json               #  Node.js dependencies
│   ├── src/
│   │   ├── dist/                   # Compiled files
│   │   ├── mappings/
│   │   │   ├── index.ts           # SubQuery handler Mapper (includes handleTransaction)
├── config/                        # Configuration files
│   ├── secrets.json               # Store private keys securely
│   ├── deployed_contracts.json    # Store deployed contract addresses
├── requirements.txt               # Python dependencies
├── .gitignore                     # Ignore sensitive files
├── README.md                      # Project documentation
```

---

## **Resources Used**
- **AirSwap Protocol**: For decentralized trading and price discovery.
    - [AirSwap Documentation](https://about.airswap.xyz/technology/protocols)
- **Avalanche C-Chain API**: For fetching transaction data on Avalanche.
    - [Avalanche C-Chain API Reference](https://build.avax.network/docs/api-reference/c-chain/txn-format)
- **Flare Network FTSO**: For verified price feeds.
    - [Flare FTSO Documentation](https://dev.flare.network/ftso/solidity-reference/FtsoV2Interface)
- **Uniswap V3**: For on-chain price verification.
    - [Uniswap V3 Documentation](https://docs.uniswap.org/protocol/reference/core/interfaces/pool/IUniswapV3PoolState)
- **SubQuery**: For indexing and querying on-chain data.
    - [SubQuery Documentation](https://academy.subquery.network/indexer/build/introduction.html#evm-and-cosmos-project-scaffolding)
- **LFG (LooksFarGood)**: For trade execution on Avalanche and Ethereum.
    - [LFG Documentation](https://docs.lfj.gg/)

---

### **Model Structure**

## **Visual Representation Flowchart**

```plaintext
+-------------------+       +-------------------+       +-------------------+
|   User Node       |       | Off-Chain Node    |       | On-Chain Node     |
|                   |       |                   |       |                   |
| 1. Trigger dApp   | ----> | 2. Data Retrieval | ----> | 3. Data Verification |
|                   |       |                   |       |                   |
+-------------------+       +-------------------+       +-------------------+
                                   |                           |
                                   v                           v
+-------------------+       +-------------------+       +-------------------+
|                   |       |                   |       |                   |
| 4. Strategy       | <---- | 5. SubQuery       |       | 6. Trade Execution |
|    Analysis       |       |    Indexing       |       |                   |
|                   |       |                   |       |                   |
+-------------------+       +-------------------+       +-------------------+
```

---
### **Prerequisites**
- Python 3.8 or higher.
- Node.js (for SubQuery).
- Solidity compiler (`solc`).
- Web3.py library.
- Infura project ID (for Ethereum/Avalanche node access).


---
## **Disclaimer**
This is a product used as a demo use case of a low-code AI platform, that uses the metadata of a diagrammatic representation from a frontend API to produce the desired on-chain and off-chain functionalities. 

Whilst the cross-chain **method** used to call on-chain data for off-chain analysis, and cross-chain execution incorporates validation and verification steps, it is unadvised to attempt to execute this. The strategy analysis model is not financial advice, not backtested, and should not be used for real trading. AI alone should not be used for smart contract creation.

Always do your own research before making any investment/deployment actions.


## **Contributing**
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

---

## **License**

This project is licensed under the MIT License. See the [LICENSE](BuildTransactions_AI/LICENSE) file for details.
---

## **Contact**
For questions or feedback, please contact:
- **Victoria Gong**: [victoria.gong1@gmail.com](mailto:victoria.gong1@gmail.com)
- **GitHub**: [vickytoriah](https://github.com/vickytoriah)

---