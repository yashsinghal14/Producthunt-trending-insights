import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Replace with your own credentials
client_id = os.getenv("CLIENT_ID")        
client_secret = os.getenv("CLIENT_SECRET")

# URL for Product Hunt OAuth2 token
url = "https://api.producthunt.com/v2/oauth/token"

# Data required to get the token
data = {
    "grant_type": "client_credentials",
    "client_id": client_id,
    "client_secret": client_secret
}

# Send request
response = requests.post(url, data=data)

# Show result
if response.status_code == 200:
    access_token = response.json()['access_token']
    print("✅ Access Token:", access_token)
else:
    print("❌ Error:", response.status_code, response.text)
