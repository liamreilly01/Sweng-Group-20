# USAGE:
# pip install transformers
import os
from Chatbot.settings import BASE_DIR



def getChatbotOutput(question):
    import json
    from transformers import pipeline
    from pathlib import Path
    try:
        sampleActs = open('../acts.json', "r", encoding="utf-8")
        print("opended");
        try:
            sampleActsDictionary = json.loads(sampleActs.read())
            print("loaded");
        except:
            print("ERROR loading and reading Sample_Acts.json")
        finally:
            sampleActs.close()
    except:
        print("ERROR opening Sample_Acts.json")

    # initialise the Question-Answer Pipeline
    pipeline = pipeline("question-answering", model=(os.path.join(BASE_DIR, "model")))

    # user-generated question

    answer = ""
    maxScore = 0.0
    # iterate through each act's description
    # !!! Very inefficient !!!

    for act in sampleActsDictionary["2022"]["acts"]:
        context = act["details"] # text that model will read
        result = pipeline(question=question, context=context) # generate response
        if result["score"] > maxScore:
            maxScore = result["score"]
            answer = result["answer"]

    return "The answer is: \'", answer, "\', with a score of ", round(maxScore, 4)

question = "What details does the Irish Fishing Master Register contain?"
