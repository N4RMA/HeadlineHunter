from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from typing import Any

def get_page_source(url: str) -> str:
    """
    Returns the page source of the given URL using a headless Chrome browser.

    Args:
        url (str): The URL to retrieve the page source from.

    Returns:
        str: The page source of the given URL.

    Raises:
        Exception: If the page source cannot be retrieved.
    """
    try:
        # Set up Selenium options to run headless (without a GUI)
        options = Options()
        options.headless = True

        # Set up Chrome WebDriver with the options
        driver = webdriver.Chrome(options=options)

        # Request the webpage and retrieve its source code
        driver.get(url)
        page_source = driver.page_source

        # Close the WebDriver and return the page source
        driver.quit()
        return page_source

    except Exception as e:
        raise Exception(f"Error retrieving page source from {url}: {e}")
