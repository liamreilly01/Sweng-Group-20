from io import BytesIO
import requests
from lxml import etree
from main import acts_to_json_format
from bs4 import BeautifulSoup

def replace_accents(tag):
    try:
        tag.afada.replace_with('á')
    except:
        pass
    try:
        tag.Afada.replace_with("Á")
    except:
        pass

    try:
        tag.efada.replace_with('é')
    except:
        pass
    try:
        tag.Efada.replace_with("É")
    except:
        pass

    try:
        tag.ifada.replace_with('í')
    except:
        pass
    try:
        tag.Ifada.replace_with("Í")
    except:
        pass

    try:
        tag.ofada.replace_with('ó')
    except:
        pass
    try:
        tag.Ofada.replace_with("Ó")
    except:
        pass

    try:
        tag.ufada.replace_with("ú")
    except:
        pass
    try:
        tag.Ufada.replace_with("Ú")
    except:
        pass

def fetch_acts(year):
    file = open("acts.json", "w", encoding="utf-8")  # "w" = overwrite, "a" = append

    act_url = "https://www.irishstatutebook.ie/eli/" + str(year) + "/act/1/enacted/en/xml"
    act_response = requests.get(act_url)
    act_no = 1

    while act_response.status_code == 200:
        soup = BeautifulSoup(act_response.content, "xml")
        title = soup.metadata.title
        replace_accents(title) # 2022 Act 33 does not use fada tags. e.g. $afada instead of <afada>
        print(title.text)

        act_no += 1
        act_url = "https://www.irishstatutebook.ie/eli/" + str(year) + "/act/" + str(act_no) + "/enacted/en/xml"
        act_response = requests.get(act_url)


fetch_acts(2022)

