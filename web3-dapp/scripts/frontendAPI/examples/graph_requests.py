import requests
import json


def get_graph_data():
    url = 'http://your-domain/api/graph-data'
    
    try:
        response = requests.post(
            url
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


# Example usage
graph_data = get_graph_data()
if graph_data:
    # Access nodes
    nodes = graph_data['nodes']
    for node in nodes:
        print(
            f"Node type: {node['type']}"
        )
        print(
            f"Position: {node['position']}"
        )
        if node.get(
            'data'
        ):
            print(
                f"Data: {node['data']}"
            )
    
    # Access connections
    connections = graph_data['connections']
    for conn in connections:
        print(
            f"Connection from {conn['sourceId']} to {conn['targetId']}"
        )