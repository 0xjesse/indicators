import pandas as pd
import requests

# API endpoint
url = "https://api.taapi.io/rsi"

# List of symbols to fetch RSI for
symbols = ["SOL/USDT", "ETH/USDT", "BTC/USDT", "LTC/USDT", "ADA/USDT"]  # Add more symbols as needed

# Initialize an empty list to store RSI data
rsi_data = []

# Loop through each symbol
for symbol in symbols:
    # API parameters for the current symbol
    params = {
        "secret": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbHVlIjoiNjRkYThkM2Q0OThkNzVkYTM2MzU1ZTBjIiwiaWF0IjoxNjkyMDQ0NzE2LCJleHAiOjMzMTk2NTA4NzE2fQ.3rLKAJmqPWv8gNkkgnXIiHotR_o5-nWay-iWrZoGjME",  # Replace with your secret key
        "exchange": "binance",
        "symbol": symbol,
        "interval": "15m"
    }

    # Send GET request for 15-minute interval RSI
    response_15m = requests.get(url, params=params)

    # Check if the request was successful
    if response_15m.status_code == 200:
        data_15m = response_15m.json()
        rsi_15m = data_15m.get("value")
    else:
        print(f"Error fetching 15m interval RSI for {symbol}. Status code:", response_15m.status_code)
        rsi_15m = "N/A"

    # Update interval parameter for 1-minute interval
    params["interval"] = "1m"

    # Send GET request for 1-minute interval RSI
    response_1m = requests.get(url, params=params)

    # Check if the request was successful
    if response_1m.status_code == 200:
        data_1m = response_1m.json()
        rsi_1m = data_1m.get("value")
    else:
        print(f"Error fetching 1m interval RSI for {symbol}. Status code:", response_1m.status_code)
        rsi_1m = "N/A"

    # Add RSI data to the list
    rsi_data.append({"Name": symbol, "15m": rsi_15m, "1m": rsi_1m})

# Create a Pandas DataFrame
df = pd.DataFrame(rsi_data)

# Style the DataFrame
styled_df = df.style.applymap(lambda x: 'background-color: yellow' if isinstance(x, float) and x > 60 else '')

# Display the styled DataFrame
#styled_df

# Print the DataFrame
#print(df)

# Save the styled DataFrame to a file
#styled_output_path = 'styled_output.html'
#styled_df.to_html(styled_output_path)
#print(f"Styled DataFrame saved to {styled_output_path}")


