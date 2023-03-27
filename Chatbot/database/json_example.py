#A short script demoing how to obtain data from the website in a json format
#Note: server must be running locally on your computer for this to work
import requests;    #needed to for requests function

json_response = requests.get("http://127.0.0.1:8000/legislationList/") #html 'get' function
print(json_response.status_code) #if 200, everything went well
print(json_response.content)     #prints file