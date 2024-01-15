import requests 
from apiKeys import *
import json

def buy_order(symbol, shares):
    data = {
        "symbol": symbol,
        "qty": shares,
        "side": 'buy',
        "type": "market",
        "time_in_force": "day"
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    data = {}
    if response.status_code == 200 and response.json()['status'] == 'accepted':
        data = response.json()
        data = {data['id'], data['client_order_id']} 
    return response.status_code , data