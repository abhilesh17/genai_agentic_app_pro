
import requests
from bs4 import BeautifulSoup

class WebSearchTool:
    def search(self, query):
        url = f"https://en.wikipedia.org/wiki/{query.replace(' ', '_')}"
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            content = soup.find('p').text
            return content
        except Exception as e:
            return f"Search failed: {e}"
