import pandas as pd
import requests

# Define indicator
indicator = "macd"

# Define endpoint
endpoint = f"https://api.taapi.io/{indicator}"

# List of symbols to fetch MACD for
symbols = ["BTC/USDT", "ETH/USDT", "SOL/USDT"]

# Define common parameters for the API request
common_params = {
    'secret': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbHVlIjoiNjRkYThkM2Q0OThkNzVkYTM2MzU1ZTBjIiwiaWF0IjoxNjkyMDQ0NzE2LCJleHAiOjMzMTk2NTA4NzE2fQ.3rLKAJmqPWv8gNkkgnXIiHotR_o5-nWay-iWrZoGjME',  # Replace with your actual secret key
    'exchange': 'binance',
    'interval': '15m'
}

# Function to get color based on comparison
def get_color(value1, value2):
    if value1 > value2:
        return '\033[92m'  # Green color
    else:
        return '\033[0m'   # Reset color

# create an empty list to store data
data = []

# Loop through each symbol
for symbol in symbols:
    # Add symbol-specific parameter
    params = common_params.copy()
    params['symbol'] = symbol

    # Send get request and save the response as response object
    response = requests.get(url=endpoint, params=params)

    # Extract data in json format
    result = response.json()

    # Get MACD and MACD Signal values
    macd = result.get('valueMACD')
    macd_signal = result.get('valueMACDSignal')

    # Get color based on comparison
    color = get_color(macd_signal, macd)
    
    # append data to the list
    data.append([symbol, macd, f"{color}{macd}\033[0m", macd_signal, f"{color}{macd_signal}\033[0m"])

# create a DataFrame from the list
df = pd.DataFrame(data)

# Save the styled DataFrame to an HTML file
#styled_df = df.style.applymap()

# Display the Styled DataFrame
#styled_df

# Print the Styled DataFrame
print(df)


# Save the DF to a file
styled_output_path = 'styled_macd_data.html'
df.to_html(styled_output_path)
print(f"Styled Dataframe saved to {styled_output_path}")