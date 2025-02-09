import type { NextApiRequest, NextApiResponse } from 'next';
import { GraphData } from '@/types/graph';

export default async function handler(
    req: NextApiRequest,
    res: NextApiResponse
) {
    if (req.method !== 'POST') {
        return res.status(405).json({ message: 'Method not allowed' });
    }
    
    try {
        const graphData: GraphData = req.body;
        
        // Here you could:
        // 1. Validate the data
        // 2. Store it in a database
        // 3. Process it further
        
        // For now, we'll just return it formatted
        return res.status(200).json({
            success: true,
            data: graphData,
            metadata: {
                version: '1.0',
                timestamp: new Date().toISOString(),
                format: 'JSON',
                schema: 'graph-workflow'
            }
        });
    } catch (error) {
        console.error('Error processing graph data:', error);
        return res.status(500).json({
            success: false,
            error: 'Failed to process graph data'
        });
    }
}