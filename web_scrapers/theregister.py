import logging
import requests
from bs4 import BeautifulSoup
from utils.selenium_utils import get_page_source


def theregister_scraper():
    # Make a request to the page you want to scrape
    url = "https://theregister.com"
    page_src = get_page_source(url)
    
    # Parse the HTML content of the page using Beautiful Soup
    soup = BeautifulSoup(page_src, "html.parser")
    return page_src


print(theregister_scraper())
