import requests
from bs4 import BeautifulSoup



def hackernews_scraper():
    # URL of the Hacker News homepage
    url = 'https://thehackernews.com/'
    page_src = requests.get(url).content
    soup = BeautifulSoup(page_src, 'html.parser')
    elements = soup.find_all('div', {'class': 'clear home-right'})
    for element in elements:
        print(element.text)


hackernews_scraper()
