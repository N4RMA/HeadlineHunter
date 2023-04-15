import requests
from bs4 import BeautifulSoup

# Send a GET request to the Packet Storm Security news page
url = "https://packetstormsecurity.com/news/"
response = requests.get(url)

# Parse the HTML content of the news page
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the news items from the page
news_items = soup.find_all('dl')

# Extract the headline and date from each news item and print them to the console
for news_item in news_items:
    headline = news_item.find('a', href=True, text=True)
    date = news_item.find('dd', class_='datetime').find('a').text
    if headline and date:
        print(f"Headline: {headline.text.strip()}")
        print(f"Date: {date}\n")

