import json
from io import BytesIO
import requests
from lxml import etree
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

def acts_to_json_format(title, description):
    object = "\t\t\t{\n\t\t\t\t\"title\": \"" + title + "\",\n\t\t\t\t\"description\": \"" + description + "\"\t\n\t\t\t}"
    return object

def get_details(soup):
    sect_list = soup.find("body").findAll("sect")
    details = ""
    for sect in sect_list:
        if "Amendment" and "amendment" and "Definitions" not in sect.find("title").text: #probably include definitions here
            #print(sect.find("title").text)
            #print("Found non-amendment paragraph")
            paragraph = sect.findChildren() #"a", recursive=True)
            for line in paragraph:
                    if line != "":
                        print(line.text)
                        #print("PRINTING LINE:" + line.text)
                        details += " " + line.text
    print(details)
    #print(sect_list)

def fetch_acts(year):
    try:
        with open("acts.json") as f:
            new_data = json.load(f)
    except:
        new_data = {
            str(year): {
                "acts": []
            }
        }

    act_url = "https://www.irishstatutebook.ie/eli/" + str(year) + "/act/1/enacted/en/xml"
    act_response = requests.get(act_url)
    act_no = 1
    while act_response.status_code == 200:
        if str(year) not in new_data:
            new_data[str(year)] = {}
            new_data[str(year)]["acts"] = []
            print(new_data[str(year)])
        new_data[str(year)]["acts"].append({})

        soup = BeautifulSoup(act_response.content, "xml")
        soup_title = soup.metadata.title
        description = soup.find("act").find("frontmatter").find("p", class_="0 8 0 left 1 0", recursive=False)
        replace_accents(description)
        replace_accents(soup_title)  # 2022 Act 33 does not use fada tags. e.g. $afada instead of <afada>
        title = soup_title.text
        details = get_details(soup)  # not currently being outputted to file

        if act_no == 33:
            title = title.replace("&ifada;", "í")
            title = title.replace("&afada;", "á")

        json_object = acts_to_json_format(title, description.text)
        new_data[str(year)]["acts"][act_no - 1]["url"] = act_url
        new_data[str(year)]["acts"][act_no - 1]["title"] = title
        new_data[str(year)]["acts"][act_no - 1]["description"] = description.text
        #print("ACT NO " + str(act_no) + ": " + description.text)
        #print(title)

        act_no += 1
        act_url = "https://www.irishstatutebook.ie/eli/" + str(year) + "/act/" + str(act_no) + "/enacted/en/xml"
        act_response = requests.get(act_url)

    print(new_data)

    with open("acts.json", 'w') as f:
        json.dump(new_data, f, indent=4, ensure_ascii=False)


fetch_acts(2022)

