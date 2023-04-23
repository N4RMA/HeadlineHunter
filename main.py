import requests
import logging
from bs4 import BeautifulSoup

# Initialize logging configuration
logging.basicConfig(filename='scraper.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s:%(message)s')

# Define a function for scraping news from Packet Storm Security
def packetstormsecurity_scraper():
    news = []
    try:
        # Send a GET request to the Packet Storm Security news page
        url = "https://packetstormsecurity.com/news/"
        response = requests.get(url)
        response.raise_for_status()  # Check if the request is successful

        # Parse the HTML content of the news page using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract the news items from the page
        news_items = soup.find_all('dl')

        # Extract the headline and date from each news item and log them using the logging module
        for news_item in news_items:
            try:
                headline = news_item.find('a', href=True, text=True)
                date = news_item.find('dd', class_='datetime').find('a').text
                if headline and date:
                    news_item = {"headline": headline.text.strip(), "date": date}
                    news.append(news_item)
                    logging.info(f"{headline.text.strip()}, {date}")
            except AttributeError as e:
                # Log the error if there is any issue in extracting the headline or date from news items
                logging.error(f"Failed to extract headline or date: {e}")

    except requests.exceptions.RequestException as e:
        # Log the error if there is any issue in making a request to the news page and raise it again
        logging.error(f"Failed to make request: {e}")
        raise e

    return news

def theregister_scraper():
    # Make a request to the page you want to scrape
    url = "https://theregister.com"
    headers = {
        'authority': 'www.theregister.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'accept-language': 'en-US,en;q=0.5',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'sec-ch-ua': '"Chromium";v="112", "Brave";v="112", "Not:A-Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'sec-gpc': '1',
        'upgrade-insecure-requests': '1',
        'referer': 'https://google.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'
    }
    response = requests.get(url, headers)
    print(response.content)
    
    # Parse the HTML content of the page using Beautiful Soup
    # soup = BeautifulSoup(response.content, "html.parser")

    # Find all the <article> tags on the page and extract the text inside them
    # articles = soup.find_all("article")
    # print(articles)
    # for article in articles:
    #     article_text = article.text.strip()  # get the text inside the article tag
    #     print(article_text)  # print the text inside the article tag



theregister_scraper()


# TODO: add scraping function for theregister.com headlines

