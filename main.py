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

# initialise the Question-Answer Pipeline
pipeline = pipeline("question-answering", model="./model")

# user-generated question
question = input("Enter your question here: ")
answer = ""
maxScore = 0.0
# iterate through each act's description
# !!! Very inefficient !!!

for act in sampleActsDictionary["2022"]["acts"]:
    context = act["description"] # text that model will read
    result = pipeline(question=question, context=context) # generate response
    if result["score"] > maxScore:
        maxScore = result["score"]
        answer = result["answer"]

print("The answer is: \'", answer, "\', with a score of ", round(maxScore, 4))
