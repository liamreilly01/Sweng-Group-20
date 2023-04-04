# USAGE:
# pip install transformers
import os
import requests
from Chatbot.settings import BASE_DIR



def getChatbotOutput(question):
    import json
    from transformers import pipeline
    from pathlib import Path

    json_response = requests.get("http://127.0.0.1:8000/legislationList")
    actsString = str(json_response.content)
    actsString = actsString.replace("b'", "{\"acts\":", 1).replace("}]'", "}]}", 1)
    actsString = actsString.encode("unicode_escape")
    #print(actsString)
    acts = json.loads(actsString)
    # try:
    #     sampleActs = open('../acts.json', "r", encoding="utf-8")
    #     print("opended");
    #     try:
    #         sampleActsDictionary = json.loads(sampleActs.read())
    #         print("loaded");
    #     except:
    #         print("ERROR loading and reading Sample_Acts.json")
    #     finally:
    #         sampleActs.close()
    # except:
    #     print("ERROR opening Sample_Acts.json")

    # initialise the Question-Answer Pipeline
    pipeline = pipeline("question-answering", model=(os.path.join(BASE_DIR, "model")))

    # user-generated question

    answer = ""
    maxScore = 0.0
    # iterate through each act's description
    # !!! Very inefficient !!!

    for i in range(1,4):
        context = acts["acts"][i]["details"] # text that model will read
        result = pipeline(question=question, context=context) # generate response
        if result["score"] > maxScore:
            maxScore = result["score"]
            answer = result["answer"]

    return "The answer is: \'", answer, "\', with a score of ", round(maxScore, 4)

question = "What details does the Irish Fishing Master Register contain?"
