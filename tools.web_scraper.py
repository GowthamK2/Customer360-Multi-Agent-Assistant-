import requests
from bs4 import BeautifulSoup

def scrape_site(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup.get_text()[:500]  # Return first 500 chars
