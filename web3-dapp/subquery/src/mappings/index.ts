import { Transaction, Transfer } from "../types";
import { EthereumTransaction, EthereumLog } from "@subql/types-ethereum";
import { AvalancheTransaction, AvalancheLog } from "@subql/types-avalanche";

export async function handleTransaction(tx: EthereumTransaction | AvalancheTransaction): Promise<void> {
    const transaction = Transaction.create({
        id: tx.hash,
        blockNumber: BigInt(tx.blockNumber),
        from: tx.from,
        to: tx.to,
        value: BigInt(tx.value),
        gasUsed: BigInt(tx.gasUsed),
    });
    await transaction.save();
}

export async function handleLog(log: EthereumLog | AvalancheLog): Promise<void> {
    const transfer = Transfer.create({
        id: log.transactionHash,
        from: log.topics[1],
        to: log.topics[2],
        value: BigInt(log.data),
        contractAddress: log.address,
    });
    await transfer.save();
}