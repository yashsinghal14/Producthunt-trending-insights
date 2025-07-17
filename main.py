import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Paste your access token here
access_token =os.getenv("ACCESS_TOKEN")

url = "https://api.producthunt.com/v2/api/graphql"

query = """
{
  posts(first: 5, order: VOTES) {
    edges {
      node {
        name
        tagline
        url
        votesCount
        commentsCount
        topics {
          edges {
            node {
              name
            }
          }
        }
      }
    }
  }
}
"""

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json",
    "Accept": "application/json"
}

response = requests.post(url, json={'query': query}, headers=headers)
data = response.json()

# Print the results
for post in data['data']['posts']['edges']:
    node = post['node']
    print("📌", node['name'])
    print("📝", node['tagline'])
    print("🔗", node['url'])
    print("🔥 Upvotes:", node['votesCount'], "| 💬 Comments:", node['commentsCount'])
    print("🏷️ Tags:", ", ".join([t['node']['name'] for t in node['topics']['edges']]))
    print("-" * 60)
