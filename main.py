# USAGE:
# pip install transformers

from transformers import pipeline
import json

# load json into python dictionary
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

# initiliase Question-Answer Model
qaModel = pipeline("question-answering", model="./model")

# user-generated question
question = input("Enter your question here: ")
# iterate through each act's details
# !!! Very inefficient !!!
maxScore = 0.0
for act in sampleActsDictionary["2022"]["acts"]:
    context = act["description"] # text that model will read
    result = qaModel(question=question, context=context) # generate response
    if result["score"] > maxScore:
        maxScore = result["score"]
        answer = result["answer"]

print("The answer is: \'", answer, "\', with a score of ", round(maxScore,4))
