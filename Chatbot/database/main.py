# USAGE:
# pip install transformers
import os
import requests
from Chatbot.settings import BASE_DIR

import json
import requests
import time

def apiQuery(payload):
    api_token = "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"
    API_URL = "https://api-inference.huggingface.co/models/sentence-transformers/msmarco-distilbert-base-tas-b"
    headers = {"Authorization": f"Bearer {api_token}"}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


def getMostLikelyAct(question):
    json_response = requests.get("http://127.0.0.1:8000/legislationList")
    actsString = str(json_response.content)
    actsString = actsString.replace("b'", "{\"acts\":", 1).replace("}]'", "}]}", 1)
    actsString = actsString.encode("unicode_escape")
    acts = json.loads(actsString)

    data = {
        "inputs": {
            "source_sentence": question,
            "sentences": []
        }
    }

    for act in acts["acts"]:
        data["inputs"]["sentences"].append(act["title"] + ". " + act["description"] + ". " + act["details"])

    response = apiQuery(data)
    length = len(response)

    count = 0
    while "error" in response:
        response = apiQuery(data)
        count += 1

    print("\n" + str(count) + " iterations before API call\n")

    maxScore = 0.0
    largestIndex = 0
    for i in range(1, length):
        if (response[i] > maxScore):
            largestIndex = i
            maxScore = response[i]

    return acts["acts"][largestIndex]

def getChatbotOutput(question):
    print("[Importing necessary libraries]")
    from transformers import pipeline

    # initialise the Question-Answer Pipeline
    print("[Loading in the pretrained model]")
    pipeline = pipeline("question-answering", model="bert-large-uncased-whole-word-masking-finetuned-squad")

    print("[Finding most likely act to contain your question]")
    act = getMostLikelyAct(question)

    print("[Searching this act for the best answer]")
    print("Disclaimer: This bot is not legally reliable. Do not use this in a court of law.\n")

    context = act["details"]
    result = pipeline(question=question, context=act["details"])  # generate response
    answer = result["answer"]
    score = result["score"]

    finalAnswer = "Answer: \"" + answer + "\"\nScore: " + str(round(score,4)) + ".\nAct Title: " + act["title"] + "\nAct URL: " + act["url"]

    return finalAnswer

# try:
#     sampleActs = open('Sample_Acts.json', "r", encoding="utf-8")
#     try:
#         acts = json.loads(sampleActs.read())
#     except:
#         print("ERROR loading and reading Sample_Acts.json")
#     finally:
#         sampleActs.close()
# except:
#     print("ERROR opening Sample_Acts.json")

# question = input("\nWhat would you like to know? ")
# startTime = time.time()
# print(getChatbotOutput(question))
# endTime = time.time()
# print("\nRuntime:" , round((endTime - startTime), 2) , "seconds")

# def getChatbotOutput(question):
#     import json
#     from transformers import pipeline
#     from pathlib import Path

#     json_response = requests.get("http://127.0.0.1:8000/legislationList")
#     actsString = str(json_response.content)
#     actsString = actsString.replace("b'", "{\"acts\":", 1).replace("}]'", "}]}", 1)
#     actsString = actsString.encode("unicode_escape")
#     #print(actsString)
#     acts = json.loads(actsString)
#     # try:
#     #     sampleActs = open('../acts.json', "r", encoding="utf-8")
#     #     print("opended");
#     #     try:
#     #         acts = json.loads(sampleActs.read())
#     #         print("loaded");
#     #     except:
#     #         print("ERROR loading and reading Sample_Acts.json")
#     #     finally:
#     #         sampleActs.close()
#     # except:
#     #     print("ERROR opening Sample_Acts.json")

#     # initialise the Question-Answer Pipeline
#     pipeline = pipeline("question-answering", model=(os.path.join(BASE_DIR, "model")))

#     # user-generated question

#     answer = ""
#     maxScore = 0.0
#     # iterate through each act's description
#     # !!! Very inefficient !!!

#     for i in range(1,4):
#         context = acts["acts"][i]["details"] # text that model will read
#         result = pipeline(question=question, context=context) # generate response
#         if result["score"] > maxScore:
#             maxScore = result["score"]
#             answer = result["answer"]

#     return "The answer is: \'", answer, "\', with a score of ", round(maxScore, 4)

# question = "What details does the Irish Fishing Master Register contain?"
