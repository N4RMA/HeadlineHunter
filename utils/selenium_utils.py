"""
Module to retrieve the page source of a given URL using a headless Chrome browser.
"""

from typing import Any
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


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
        chrome_options = Options()
        chrome_options.headless = True

        chrome_driver = webdriver.Chrome(
            executable_path=ChromeDriverManager().install(),
            options=chrome_options
        )

        chrome_driver.get(url)
        page_source = chrome_driver.page_source

        chrome_driver.quit()
        return page_source

    except Exception as e:
        raise Exception(f"Error retrieving page source from {url}: {e}")



print(get_page_source("https://theregister.com/"))
