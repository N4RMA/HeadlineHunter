from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def get_page_source(url):
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

