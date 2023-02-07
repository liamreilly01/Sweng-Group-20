
import requests
import xml.etree.ElementTree as ET
import xmltodict
import json


acts_2022 = []

for act_no in range(1, 53): #1 - 52 acts from 2022
    act_url = "https://www.irishstatutebook.ie/eli/2022/act/" + str(act_no) + "/enacted/en/xml"
    act_response = requests.get(act_url)

    # Acts 2 and 4 have badly formed xml and cause errors
    if act_no != 2 and act_no != 4 and act_response.status_code == 200:
        act = ET.fromstring(act_response.content)
        acts_2022.append(act)
        print("Found and added act: " + str(act_no))
        metadata = xmltodict.parse(ET.tostring(act.find('metadata')))
        s = json.dumps(metadata)
        print(s)
    else: #bad status code, couldn't retrieve file for some reason
        print("Couldn't find act:" + str(act_no) + "   Status code: " + str(act_response.status_code))


