## On-chain and off-chain flow
To represent the model's actions and their on-chain/off-chain characteristics, we can create a **flowchart** that categorizes the components into **on-chain actions**, **off-chain actions**, and **nodes** as the initiation points. Below is a textual representation of the flowchart, followed by an explanation of each component.

---

## **Flowchart Representation**

### **Nodes (Initiation Points)**
1. **User Node**:
   - Initiates the process by triggering the dApp.
2. [**Off-Chain Node**]():
   - Executes off-chain computations and strategy analysis.
3. **On-Chain Node**:
   - Interacts with blockchain networks (e.g., Ethereum, Avalanche).

---

### **Off-Chain Actions**
1. **Data Retrieval**:
   - Fetch on-chain data (e.g., transaction data, price feeds) using APIs.
   - Tools: Avalanche C-Chain API, Ethereum JSON-RPC, Flare FTSO.
2. **Strategy Analysis**:
   - Perform off-chain computations to generate trade signals.
   - Tools: Python scripts (`strategy_analysis.py`).
3. **SubQuery Indexing**:
   - Index and query on-chain data for efficient retrieval.
   - Tools: SubQuery.

---

### **On-Chain Actions**
1. **Data Verification**:
   - Verify trade prices using Uniswap V3 oracles.
   - Tools: Solidity contracts (`TradeVerifier.sol`).
2. **Trade Execution**:
   - Execute trades on a DEX (e.g., AirSwap, LFG).
   - Tools: Solidity contracts (`TradeExecutor.sol`).

---

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

## **Explanation of the Flowchart**
(Low-code UI Builder: BuildTransactionAI)[http://github.com/AidanTHWong/BuildTransactionAI.git]
[http://github.com/vickytoriah/BuildTransactions_AI.git](Cross-chain Transaction Builder: Backend)

### **1. User Node**
- The **User Node** is the initiation point where the user interacts with the dApp (e.g., through a frontend interface).
- Actions:
  - Triggers the dApp to start the process.

---

### **2. Off-Chain Node**
- The **Off-Chain Node** handles all computations and actions that do not require blockchain interaction.
- Actions:
  - **Data Retrieval**:
    - Fetch on-chain data (e.g., transaction data, price feeds) using APIs like Avalanche C-Chain API, Ethereum JSON-RPC, and Flare FTSO.
  - **Strategy Analysis**:
    - Perform off-chain computations to analyze data and generate trade signals.
  - **SubQuery Indexing**:
    - Use SubQuery to index and query on-chain data for efficient retrieval.

---

### **3. On-Chain Node**
- The **On-Chain Node** handles all actions that require interaction with the blockchain.
- Actions:
  - **Data Verification**:
    - Verify trade prices using Uniswap V3 oracles to ensure the trade is executed at the best possible price.
  - **Trade Execution**:
    - Execute trades on a DEX (e.g., AirSwap, LFG) using smart contracts.

---

## **Flow of Actions**

1. **User Node** triggers the dApp.
2. **Off-Chain Node** retrieves on-chain data and performs strategy analysis.
3. **On-Chain Node** verifies the data and executes the trade.
4. The results of the trade execution are sent back to the **User Node** (e.g., through a frontend interface).

---


---

## **Summary of Components**

| **Component**         | **Type**       | **Description**                                                                 |
|------------------------|----------------|---------------------------------------------------------------------------------|
| **User Node**          | Initiation     | Triggers the dApp and receives results.                                         |
| **Off-Chain Node**     | Off-Chain      | Handles data retrieval, strategy analysis, and SubQuery indexing.               |
| **On-Chain Node**      | On-Chain       | Handles data verification and trade execution using smart contracts.            |
| **Data Retrieval**     | Off-Chain      | Fetches on-chain data using APIs.                                               |
| **Strategy Analysis**  | Off-Chain      | Performs off-chain computations to generate trade signals.                      |
| **SubQuery Indexing**  | Off-Chain      | Indexes and queries on-chain data for efficient retrieval.                      |
| **Data Verification**  | On-Chain       | Verifies trade prices using Uniswap V3 oracles.                                 |
| **Trade Execution**    | On-Chain       | Executes trades on a DEX using smart contracts.                                 |

---

This flowchart and categorization provide a clear overview of the model's actions and their on-chain/off-chain characteristics. Let me know if you need further clarification or adjustments!