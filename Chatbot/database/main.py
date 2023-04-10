# USAGE:
# pip install transformers
import os
import requests
from Chatbot.settings import BASE_DIR

import json
import requests
import time

def getModel():
    from transformers import pipeline
    pipeline = pipeline("question-answering", model="bert-large-uncased-whole-word-masking-finetuned-squad")
    print("can return")
    return pipeline

def apiQuery(payload):
    api_token = "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"
    API_URL = "https://api-inference.huggingface.co/models/sentence-transformers/msmarco-distilbert-base-tas-b"
    headers = {"Authorization": f"Bearer {api_token}"}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


def getMostLikelyAct(question):
    json_response = requests.get("http://127.0.0.1:8000/legislationList")
    actsString = json_response.content
    actsString = actsString.decode("utf-8")
    actsString = "{\"acts\":" + actsString.replace("}]", "}]}", 1)
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

    mostLikelyAct = acts["acts"][largestIndex]
    message = "[Found the Act most likely to contain your answer]"
    return mostLikelyAct


def getChatbotOutput(mostLikelyAct, pipeline, question):
    print("entered method")
    context = mostLikelyAct["title"] + ". " + mostLikelyAct["description"] + ". " + mostLikelyAct["details"]
    result = pipeline(question=question, context=context)  # generate response
    answer = result["answer"]
    mostLikelyAct["url"] = mostLikelyAct["url"].replace("xml", "html")

    finalAnswer = "Answer: \"" + answer + \
                  "\"<br>We found this answer in the Act: " + mostLikelyAct["title"] + \
                  "<br>Here is the Act URL: <a href=\"" + mostLikelyAct["url"] + "\">" + mostLikelyAct["url"] + "</a>"

    return finalAnswer
