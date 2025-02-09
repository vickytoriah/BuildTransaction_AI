import { AvalancheTransaction } from "@subql/types-avalanche";

export async function handleTransaction(tx: AvalancheTransaction): Promise<void> {
    logger.info(`New transaction: ${tx.hash}`);
    // Store transaction data in SubQuery database
}