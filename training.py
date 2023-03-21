from transformers import pipeline
import json

from transformers import AutoTokenizer

try:
    dataset = open('train-test.json', "r", encoding="utf-8")
    try:
        datasetDictionary = json.loads(dataset.read())
    except:
        print("ERROR loading and reading Sample_Acts.json")
    finally:
        datasetDictionary.close()
except:
    print("ERROR opening Sample_Acts.json")


tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")


# firstLoad()
#
# try:
#     trainingData = open('train-test.json', "r", encoding="utf-8")
#     try:
#         trainingDataDictionary = json.loads(trainingData.read())
#     except:
#         print("ERROR loading and reading Sample_Acts.json")
#     finally:
#         trainingData.close()
# except:
#     print("ERROR opening Sample_Acts.json")
#
# def firstLoad():
#     model = pipeline(model='distilbert-base-cased-distilled-squad')
#     model.save_pretrained('./model/')
