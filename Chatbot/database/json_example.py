#A short script demoing how to obtain data from the website in a json format
#Note: server must be running locally on your computer for this to work
import requests;    #needed to for requests function
import json

json_response = requests.get("http://127.0.0.1:8000/legislationList/") #html 'get' function
actsString = json_response.content
actsString = actsString.decode("utf-8")
#actsString = actsString.replace("b'", "{\"data\":", 1).replace("}]'", "}]}", 1)
actsString = "{\"data\":" + actsString.replace("}]", "}]}", 1)
print(actsString)
#out_file = open("myfile.json", "w")
  
#json.dump(actsString, out_file)
acts = json.loads(actsString)
print(acts["data"][7]["description"])
#print(actsString)
#print(json_response.status_code) #if 200, everything went well
#print(json_response.content)     #prints file