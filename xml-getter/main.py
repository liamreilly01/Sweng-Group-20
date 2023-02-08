from io import BytesIO

import requests
import xmltodict
import json
from lxml import etree


acts_2022 = []
file = open("acts.json", "w") #"w" means write; overwrites all data. can change to "a" to append later

for act_no in range(1, 53): #1 - 52 acts from 2022
    act_url = "https://www.irishstatutebook.ie/eli/2022/act/" + str(act_no) + "/enacted/en/html"
    act_response = requests.get(act_url)

    if act_response.status_code == 200:

        parser = etree.HTMLParser(recover=True)
        act = act_response.content
        tree = etree.parse(BytesIO(act), parser)
        element = tree.find("head/title")
        print(element.text)
        # acts_2022.append(act)
        # print("Found and added act: " + str(act_no))
        # metadata = xmltodict.parse(etree.tostring(act.find('metadata')))
        # s = json.dumps(metadata)
        # file.write(s + "\n")
        # print(s)
    else: #bad status code, couldn't retrieve file for some reason
        print("Couldn't find act:" + str(act_no) + "   Status code: " + str(act_response.status_code))

file.close()
