from io import BytesIO
import requests
from lxml import etree
from main import acts_to_json_format
from bs4 import BeautifulSoup


def fetch_acts(year):
    file = open("acts.json", "w", encoding="utf-8")  # "w" = overwrite, "a" = append

    act_url = "https://www.irishstatutebook.ie/eli/" + str(year) + "/act/10/enacted/en/html"
    act_response = requests.get(act_url)
    act_no = 1
    soup = BeautifulSoup(act_response.content, "html.parser")
    title = soup.title.text
    print(title)


fetch_acts(2022)

