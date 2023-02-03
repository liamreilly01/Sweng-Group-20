
import requests



acts_2022 = []

for act_no in range(1, 53): #1 - 52 acts from 2022
    act_url = "https://www.irishstatutebook.ie/eli/2022/act/" + str(act_no) + "/enacted/en/xml"
    act_response = requests.get(act_url)

    if act_response.status_code == 200: #200 -> file found
        acts_2022.append(act_response.content)
        print("Found and added act: " + str(act_no))
    else: #bad status code, couldn't retrieve file for some reason
        print("Couldn't find act:" + str(act_no) + "   Status code: " + str(act_response.status_code))

