from typing import List
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.parse import urldefrag
import requests


def get_links(url:str):
    """Find all links on page at the given url.

    Returns:
        a list of all unique hyperlinks on the page,
        without page fragments or query parameters.
    """
    driver = webdriver.Chrome(r'C:\Users\MSI GF63\Desktop\ISP-review\chromedriver.exe')
    driver.get(url)

    url_elements = driver.find_elements_by_tag_name("a")
    url_list = []
    url_no_duplicate = []
    #append urls link from the main page with no duplicate links
    for url in url_elements:
        page_url = url.get_attribute("href")
        if page_url != None:
            page_url = urldefrag(page_url)
            url_list.append(page_url.geturl())
    [url_no_duplicate.append(x) for x in url_list if x not in url_no_duplicate]

    return url_no_duplicate


def is_valid_url(url: str):
    """Validate the urls in urllist and return a new list containing
    the invalid or unreachable urls.
    """
    try:
        requests.get(url)
        return True
    except:
        return False

def invalid_urls(urllist: List[str]) -> List[str]:
    """Validate the urls in urllist and return a new list containing
    the invalid or unreachable urls.
    """
    pass

print(is_valid_url("https://www.youtube.com/"))