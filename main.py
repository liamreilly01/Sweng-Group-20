# USAGE:
# pip install transformers


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

    data = {
        "inputs": {
            "source_sentence": question,
            "sentences": []
        }
    }

    for act in sampleActsDictionary["2022"]["acts"]:
        data["inputs"]["sentences"].append(act["details"])

    response = apiQuery(data)

    length = len(response)

    if length == 0:
        return "error"

    maxScore = 0.0
    largestIndex = 0
    for i in range(0, length):
        if (response[i] > maxScore):
            largestIndex = i
            maxScore = response[i]

    return sampleActsDictionary["2022"]["acts"][largestIndex]

def getChatbotOutput(question):
    print("[Importing necessary libraries]")
    from transformers import pipeline

    # initialise the Question-Answer Pipeline
    print("[Loading in the pretrained model]")
    pipeline = pipeline("question-answering", model="bert-large-uncased-whole-word-masking-finetuned-squad")

    print("[Finding most likely act to contain your question]")
    act = getMostLikelyAct(question)

    if act == "error":
        return "Error with Text Similarity API. Please Try Again."

    print("[Searching this act for the best answer]")
    print("Disclaimer: This bot is not legally reliable. Do not use this in a court of law.\n")

    context = act["details"]
    result = pipeline(question=question, context=act["details"])  # generate response
    answer = result["answer"]
    score = result["score"]

    finalAnswer = "Answer: \"" + answer + "\"\nScore: " + str(round(score,4)) + ".\nAct Title: " + act["title"] + "\nAct URL: " + act["url"]

    return finalAnswer

try:
    sampleActs = open('Sample_Acts.json', "r", encoding="utf-8")
    try:
        sampleActsDictionary = json.loads(sampleActs.read())
    except:
        print("ERROR loading and reading Sample_Acts.json")
    finally:
        sampleActs.close()
except:
    print("ERROR opening Sample_Acts.json")

question = input("\nWhat would you like to know? ")
startTime = time.time()
print(getChatbotOutput(question))
endTime = time.time()
print("\nRuntime:" , round((endTime - startTime), 2) , "seconds")
