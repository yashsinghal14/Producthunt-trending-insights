from flask import Flask, render_template
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

@app.route('/')
def home():
    url = "https://api.producthunt.com/v2/api/graphql"
    query = """
    {
      posts(first: 10, order: VOTES) {
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
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    response = requests.post(url, json={'query': query}, headers=headers)
    posts = response.json()['data']['posts']['edges']

    trending = []
    for post in posts:
        node = post['node']
        trending.append({
            'name': node['name'],
            'tagline': node['tagline'],
            'url': node['url'],
            'votes': node['votesCount'],
            'comments': node['commentsCount'],
            'tags': [t['node']['name'] for t in node['topics']['edges']]
        })

    return render_template('index.html', products=trending)

if __name__ == '__main__':
    app.run(debug=True)