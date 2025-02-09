
## **Setup Instructions**

### **1. Prerequisites**
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