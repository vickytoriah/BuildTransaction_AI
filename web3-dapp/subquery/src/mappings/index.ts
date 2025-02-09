import { Transaction, Transfer } from "../types";
import { EthereumTransaction, EthereumLog } from "@subql/types-ethereum";
import { AvalancheTransaction, AvalancheLog } from "@subql/types-avalanche";

// Handle Ethereum or Avalanche transactions
export async function handleTransaction(tx: EthereumTransaction | AvalancheTransaction): Promise<void> {
    // Create a new Transaction entity
    const transaction = Transaction.create({
        id: tx.hash,                      // Transaction hash
        blockNumber: BigInt(tx.blockNumber), // Block number
        from: tx.from,                    // Sender address
        to: tx.to,                        // Receiver address
        value: BigInt(tx.value),          // Value transferred (in wei)
        gasUsed: BigInt(tx.gasUsed),      // Gas used
        timestamp: BigInt(tx.blockTimestamp), // Block timestamp
    });
    
    // Save the Transaction entity to the database
    await transaction.save();
}

// Handle Ethereum or Avalanche logs (e.g., ERC20 transfers)
export async function handleLog(log: EthereumLog | AvalancheLog): Promise<void> {
    // Check if the log is an ERC20 Transfer event
    if (log.topics[0] === "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef") {
        // Create a new Transfer entity
        const transfer = Transfer.create({
            id: `${log.transactionHash}-${log.logIndex}`, // Unique identifier
            from: log.topics[1],                         // Sender address
            to: log.topics[2],                           // Receiver address
            value: BigInt(log.data),                     // Value transferred (in wei)
            contractAddress: log.address,                // Token contract address
            transactionHash: log.transactionHash,        // Transaction hash
            timestamp: BigInt(log.blockTimestamp),       // Block timestamp
        });
        
        // Save the Transfer entity to the database
        await transfer.save();
    }
}