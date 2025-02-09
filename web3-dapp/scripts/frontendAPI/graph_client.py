import httpx, requests
import json
from typing import Dict, Optional
from datetime import datetime
import asyncio

class GraphClient:
    def __init__(
        self,
        base_url: str = "{}/api/python-graph",
        domain_: str = "http://localhost:3000",
    ):
        self.base_url = base_url
        self.domain = domain_
        self.endpoint = self.base_url.format(self.domain)
    
    def get_graph_data(
        self,
        
    ):
        try:
            response = requests.post(
                self.endpoint
            )
            if response.status_code == 200:
                data = response.json()
                return data['data']
            else:
                print(
                    f"Error: {response.status_code}"
                )
                return None
        except Exception as e:
            print(
                f"Request failed: {e}"
            )
            return None
    
    
    async def send_graph_data(self, graph_data: Dict) -> Dict:
        """
        Send graph data to the API endpoint using httpx.
        
        Args:
            graph_data (Dict): The graph data to send
            
        Returns:
            Dict: The API response
        """
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    self.endpoint,
                    json=graph_data,
                    headers={
                        "Content-Type": "application/json",
                    },
                    timeout=30.0
                )
                
                response.raise_for_status()
                return response.json()
                
        except httpx.HTTPStatusError as e:
            print(f"HTTP Error: {e.response.status_code} - {e.response.text}")
            raise
        except httpx.RequestError as e:
            print(f"Request Error: {e}")
            raise
        except Exception as e:
            print(f"Unexpected error: {e}")
            raise

# Example usage
async def main():
    # Create sample graph data
    sample_data = {
        "nodes": [
            {
                "id": "node-1",
                "type": "circle",
                "position": {"x": 100, "y": 200},
                "data": {
                    "tokenPair": "AVAX/USDT",
                    "tradeType": "Buy",
                    "tradeAmount": "1 AVAX",
                    "slippageTolerance": "1%"
                }
            }
        ],
        "connections": [
            {
                "id": "conn-1",
                "sourceId": "node-1",
                "targetId": None
            }
        ],
        "version": "1.0",
        "timestamp": int(datetime.now().timestamp())
    }

    client = GraphClient()
    try:
        result = await client.send_graph_data(sample_data)
        print("Success! API Response:")
        print(json.dumps(result, indent=2))
    except Exception as e:
        print(f"Failed to send graph data: {e}")

# Run the examples
if __name__ == "__main__":
    asyncio.run(main())