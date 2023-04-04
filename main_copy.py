# USAGE:
# pip install transformers


import json
import requests


def apiQuery(payload):
    api_token = "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"
    API_URL = "https://api-inference.huggingface.co/models/sentence-transformers/msmarco-distilbert-base-tas-b"
    headers = {"Authorization": f"Bearer {api_token}"}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


def getMostLikelyAct(question):

    data = {
        "inputs": {
            "source_sentence": "",
            "sentences": []
        }
    }

    for act in sampleActsDictionary["2022"]["acts"]:
        data["inputs"]["sentences"].append(act["details"])

    response = apiQuery(data)

    length = len(response)
    maxScore = 0.0
    largestIndex = 0
    for i in range(0, length):
        if (response[i] > maxScore):
            largestIndex = i
            maxScore = response[i]

    return sampleActsDictionary["2022"]["acts"][largestIndex]

def getChatbotOutput(question):
    from transformers import pipeline

    # initialise the Question-Answer Pipeline
    pipeline = pipeline("question-answering", model="./model")


    # act = getMostLikelyAct(question)
    act = sampleActsDictionary["2022"]["acts"][1]

    context = act["details"]
    result = pipeline(question=question, context=context)  # generate response
    answer = result["answer"]
    score = result["score"]

    finalAnswer = answer , "\nwith a score of " , round(score,4) , ".\nWe think your answer is in:" , act["title"] , \
        "\nThe URL for this act: " , act["url"]
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

question = "How do I register for the Irish Fishing Master Register?"
print(getChatbotOutput(question))
