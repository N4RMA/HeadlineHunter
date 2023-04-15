import requests
from bs4 import BeautifulSoup


try:
    # Send a GET request to the Packet Storm Security news page
    url = "https://packetstormsecurity.com/news/"
    response = requests.get(url)
    response.raise_for_status()  # check if the request is successful

    # Parse the HTML content of the news page
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the news items from the page
    news_items = soup.find_all('dl')

    # Extract the headline and date from each news item and log them using the logging module
    for news_item in news_items:
        try:
            headline = news_item.find('a', href=True, text=True)
            date = news_item.find('dd', class_='datetime').find('a').text
            if headline and date:
                print(f"Headline: {headline.text.strip()}")
                print(f"Date: {date}")
        except AttributeError as e:
            print(f"Failed to extract headline or date: {e}")

except requests.exceptions.RequestException as e:
    # Log the error and raise it again
    print(f"Failed to make request: {e}")
    raise e

