# BuildTransaction_AI
# BuildTransaction_AI
Below, is an introduction to the model's purpose, folder structure, resources used, and setup instructions.

---

# Web3 dApp for On-Chain Data Retrieval and Trade Execution

## **Introduction**
This repository contains a Web3 decentralized application (dApp) that retrieves on-chain data, performs off-chain strategy analysis, and executes trades on decentralized exchanges (DEXs) such as **AirSwap** and **LFG**. The dApp integrates with **Uniswap V3** for price verification and supports both **Ethereum Mainnet** and **Avalanche C-Chain**.

The model's purpose is to:
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
│   ├── TradeVerifierUniV3.sol     # Flare FTSO price verification
│   ├── TradeExecutorAvalanche.sol # AirSwap or LFG trade execution
│   ├── TradeExecutorLFG.sol       # AirSwap or LFG trade execution
├── scripts/                       # Python scripts for off-chain logic
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

## **Setup Instructions**

### **1. Prerequisites**
- Python 3.8 or higher.
- Node.js (for SubQuery).
- Solidity compiler (`solc`).
- Web3.py library.
- Infura project ID (for Ethereum/Avalanche node access).

### **2. Clone the Repository**
```bash
git clone https://github.com/your-username/web3-dapp.git
cd web3-dapp
```

### **3. Set Up the Environment**
1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Install Solidity compiler:
   ```bash
   pip install py-solc-x
   ```

### **4. Configure Secrets**
1. Create a `config/secrets.json` file:
   ```json
   {
     "private_key": "YOUR_PRIVATE_KEY",
     "infura_project_id": "YOUR_INFURA_PROJECT_ID"
   }
   ```
    - Replace `YOUR_PRIVATE_KEY` with your wallet's private key.
    - Replace `YOUR_INFURA_PROJECT_ID` with your Infura project ID.

2. Ensure `config/secrets.json` is added to `.gitignore` to avoid committing sensitive data.

### **5. Deploy Contracts**
1. Compile and deploy the contracts:
   ```bash
   python scripts/deploy_contracts.py
   ```
    - This will save the deployed contract addresses in `config/deployed_contracts.json`.

### **6. Run the dApp**
1. Fetch on-chain data:
   ```bash
   python scripts/fetch_data.py
   ```
2. Perform off-chain strategy analysis:
   ```bash
   python scripts/strategy_analysis.py
   ```
3. Execute a trade:
   ```bash
   python scripts/execute_trade.py
   ```

### **7. SubQuery Setup (Optional)**
1. Install SubQuery CLI:
   ```bash
   npm install -g @subql/cli
   ```
2. Navigate to the `subquery` folder:
   ```bash
   cd subquery
   ```
3. Install dependencies:
   ```bash
   npm install
   ```
4. Start the SubQuery node:
   ```bash
   subql-node
   ```

---

## **Contributing**
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

---

## **License**
This project is licensed under the MIT License. See the [LICENSE](AI_BuildTrade/web3-dapp/LICENSE) file for details.

---

## **Contact**
For questions or feedback, please contact:
- **Your Name**: [victoria.gong1@gmail.com](mailto:victoria.gong1@gmail.com)
- **GitHub**: [vickytoriah](https://github.com/vickytoriah)

---

This `README.md` provides a clear overview of the project, its structure, and setup instructions. Let me know if you need further adjustments!