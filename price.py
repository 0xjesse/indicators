import requests

# API endpoint
url = "https://api.taapi.io/price"

# API parameters for different symbols
symbols = ["BTC/USDT", "ETH/USDT", "SOL/USDT", "LTC/USDT", "ADA/USDT"]
params = {
    "secret": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbHVlIjoiNjRkYThkM2Q0OThkNzVkYTM2MzU1ZTBjIiwiaWF0IjoxNjkyMDQ0NzE2LCJleHAiOjMzMTk2NTA4NzE2fQ.3rLKAJmqPWv8gNkkgnXIiHotR_o5-nWay-iWrZoGjME",  # Replace with your secret key
    "exchange": "binance",
    "interval": "30m"
}

# Dictionary mapping tickers to names
symbol_names = {
    "BTC/USDT": "Bitcoin",
    "ETH/USDT": "Ethereum",
    "SOL/USDT": "Solana",
    "LTC/USDT": "Litecoin",
    "ADA/USDT": "Cardano"

}

#

# Loop through symbols and retrieve prices
for symbol in symbols:
    params["symbol"] = symbol
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        price = data.get("value")
        symbol_name = symbol_names.get(symbol, symbol)
        print(f"Price of {symbol_name}: {price}")
    else:
        print(f"Error fetching price for {symbol}. Status code:", response.status_code)