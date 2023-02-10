from io import BytesIO

import requests
from lxml import etree


def acts_to_json_format(title, description):
    object = "{\"title\":\"" + title + "\", \"description\":\"" + description + "\"}"
    return object


acts_2022 = []
file = open("acts.json", "w", encoding="utf-8")  # "w" = overwrite, "a" = append

for act_no in range(1, 53):  # 1 - 52 acts from 2022
    act_url = "https://www.irishstatutebook.ie/eli/2022/act/" + str(act_no) + "/enacted/en/html"
    act_response = requests.get(act_url)

    if act_response.status_code == 200:
        parser = etree.HTMLParser(recover=True)
        act = act_response.content
        tree = etree.parse(BytesIO(act), parser)
        act_title = tree.find("head/title")
        if act_no != 44:
            act_description = tree.find("head/meta[@property='eli:description']").attrib["content"]
        else:
            act_description = "Error: description not found"
        json_object = acts_to_json_format(act_title.text, act_description)
        print("GENERATED JSON OBJECT: " + json_object)
        file.write(json_object + "\n")
    else:  # bad status code, couldn't retrieve file for some reason
        print("Couldn't find act:" + str(act_no) + "   Status code: " + str(act_response.status_code))

file.close()
