import requests
from pprint import pprint

BASE_URL = "https://api.bithumb.com"
path = "/public/ticker"
params = {
    "order_currency" : "BTC",
    "payment_currency" : "KRW"
}

response = requests.get(BASE_URL + path, params = params).json()
pprint(response["data"]["prev_closing_price"])