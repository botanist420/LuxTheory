import os
import requests
import pandas as pd

# Read the API key from an environment variable
api_key = os.environ.get("BINANCE_API_KEY")

# Define the API endpoint
url = "https://api.binance.com/api/v3/klines"

# Define the symbol and interval
symbol = "BTCUSDT"
interval = "1d"

# Make the API call
response = requests.get(f"{url}?symbol={symbol}&interval={interval}", headers={
    "X-MBX-APIKEY": api_key
})

# Parse the JSON data
data = response.json()

# Convert the data to a Pandas dataframe
df = pd.DataFrame(data, columns=["Open time", "Open", "High", "Low", "Close", "Volume", "Close time", "Quote asset volume", "Number of trades", "Taker buy base asset volume", "Taker buy quote asset volume", "Ignore"])

# Preview the data
print(df.head())
