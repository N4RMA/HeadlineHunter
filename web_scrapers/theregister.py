import logging
import requests
from utils.selenium_utils import get_page_source


def theregister_scraper():
    # Make a request to the page you want to scrape
    url = "https://theregister.com"
    return get_page_source(url)
    
    # Parse the HTML content of the page using Beautiful Soup
    # soup = BeautifulSoup(response.content, "html.parser")

    # Find all the <article> tags on the page and extract the text inside them
    # articles = soup.find_all("article")
    # print(articles)
    # for article in articles:
    #     article_text = article.text.strip()  # get the text inside the article tag
    #     print(article_text)  # print the text inside the article tag



print(theregister_scraper())
