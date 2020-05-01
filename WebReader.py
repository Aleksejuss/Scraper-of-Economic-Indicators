from bs4 import BeautifulSoup
import requests

def get_url_content(url: str) -> str:
    # Get url content as text
    try:
        req = requests.get(url)
        return req.text
    except:
        return None


def parse_content(url: str, element_tag: str, class_name: str):
    data = get_url_content(url)
    soup = BeautifulSoup(data, "html.parser")
    # get and parse table data, ignoring details and graph
    table = soup.find(element_tag, class_=class_name)
    return table