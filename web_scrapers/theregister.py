import logging
import requests


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


