import json
import requests
from bs4 import BeautifulSoup

def parse_article(element):
    data = {}

    # Extract title
    title = element.find('h2', {'class': 'home-title'})
    if title:
        data["title"] = title.text.strip()

    # Extract date and category
    label = element.find('div', {'class': 'item-label'})
    if label:
        date_and_category = label.find_all('span')
        if len(date_and_category) == 2:
            data["date"] = date_and_category[0].text.strip()
            data["category"] = date_and_category[1].text.strip()

    # Extract summary
    summary = element.find('div', {'class': 'home-desc'})
    if summary:
        data["summary"] = summary.text.strip()

    return json.dumps(data, indent=4)


def hackernews_scraper():
    url = 'https://thehackernews.com/'
    page_src = requests.get(url).content
    soup = BeautifulSoup(page_src, 'html.parser')
    elements = soup.find_all('div', {'class': 'clear home-right'})
    for element in elements:
        json_data = parse_article(element)
        print(json_data)
        break

hackernews_scraper()
