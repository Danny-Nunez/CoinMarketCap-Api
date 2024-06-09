import requests
import json
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables
API_KEY = os.getenv('CMC_API_KEY')
URL = 'https://pro-api.coinmarketcap.com/v1/global-metrics/quotes/latest'

# Headers for the request
headers = {
    'X-CMC_PRO_API_KEY': API_KEY,
}

# Make the API request
response = requests.get(URL, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    # Save the JSON response to a file
    with open('coinmarket.json', 'w') as json_file:
        json.dump(data, json_file, indent=4)
    print('Data saved to coinmarket.json')
else:
    print(f'Failed to fetch data. Status code: {response.status_code}')
