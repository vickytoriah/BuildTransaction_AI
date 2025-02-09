import httpx
import requests
import json
import asyncio
from typing import Dict, Optional
from datetime import datetime
from .response_format import response_schema


class GraphClient:
    def __init__(
        self,
        base_url: str = "{}/api/python-graph",
        domain_: str = "http://localhost:3000",
        response_dict: Dict = response_schema,
    ):
        self.json_schema = response_schema
        self.json_response = response_dict
        self.base_url = base_url
        self.domain = domain_
        self.endpoint = self.base_url.format(self.domain)
    
    def get_graph_data(
        self,
        
    ):
        """

        :return:
        """
        try:
            response = requests.post(
                self.endpoint
            )
            if response.status_code == 200:
                data = response.json()
                self.json_response['data'].update(data['data'])
                print(f'Graph data received: Success')
                return self.json_response
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
    
    
    async def send_graph_data(
        self,
        graph_data: Dict,
    ) -> Dict:
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


async def main(
    request_type: str = 'GET',
    domain_: str = "http://localhost:3000",
    json_post_dict: Dict = None,
    base_url: str = "{}/api/python-graph",
):
    """
    
    :param request_type:
    :param domain_:
    :param json_post_dict:
    :param base_url:
    :return:
    """
    
    client = GraphClient(
        domain_=domain_,
        base_url=base_url,
    )
    if request_type.lower() == 'get':
        graph_data = client.get_graph_data()
        print(json.dumps(graph_data, indent=2))
        return graph_data
    else:
        if json_post_dict is None:
            print('Post data is sample data, not results')
            # Create sample graph data
            json_post_dict = {
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

        try:
            result = await client.send_graph_data(
                graph_data=json_post_dict,
            )
            print("Success! API Response:")
            print(json.dumps(result, indent=2))
        except Exception as e:
            print(f"Failed to send graph data: {e}")

# Run the examples
if __name__ == "__main__":
    asyncio.run(main())