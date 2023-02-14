from io import BytesIO

import requests
from lxml import etree


def acts_to_json_format(title, description):
    object = "{\"title\":\"" + title + "\", \"description\":\"" + description + "\"}"
    return object


def fetch_acts(year):
    file = open("acts.json", "w", encoding="utf-8")  # "w" = overwrite, "a" = append

    act_url = "https://www.irishstatutebook.ie/eli/" + str(year) + "/act/1/enacted/en/html"
    act_response = requests.get(act_url)
    act_no = 1

    while act_response.status_code == 200:
        parser = etree.HTMLParser(recover=True)
        act = act_response.content
        tree = etree.parse(BytesIO(act), parser)
        act_title = tree.find("head/title")
        try:
            act_description = tree.find("head/meta[@property='eli:description']").attrib["content"]
        except:
            act_description = "Error: description not found"
        json_object = acts_to_json_format(act_title.text, act_description)
        print("GENERATED JSON OBJECT: " + json_object)
        file.write(json_object + "\n")

        act_no += 1
        act_url = "https://www.irishstatutebook.ie/eli/" + str(year) + "/act/" + str(act_no) + "/enacted/en/html"
        act_response = requests.get(act_url)
    file.close()

fetch_acts(2022)


