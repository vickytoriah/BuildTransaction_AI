response_schema = {
  "success": bool,
  "data": {
    "nodes": [
      {
        "id": str,  # "node-1"
        "type": str,  # "circle"
        "position": {
          "x": int,  # 100
          "y": int,  # 200
        },
        "data": {
          "tokenPair": str,  # "AVAX/USDT"
          "tradeType": str,  # "Buy"
        },
      },
    ],
    "connections": [
      {
        "id": str,  # "conn-1"
        "sourceId": str,  # "node-1"
        "targetId": str,  #"node-2"
      },
    ],
    "version": "1.0",
    "timestamp": 1234567890
  },
  "metadata": {
    "version": "1.0",
    "timestamp": "2024-03-14T12:00:00Z",
    "format": "JSON",
    "schema": "graph-workflow"
  }
}

fail_response_schema = {
  "success": bool,  #false,
  "error": str,  #"Failed to process graph data",
  "details": str,  #"Invalid node type provided",
}