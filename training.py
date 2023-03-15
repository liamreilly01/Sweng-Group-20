from transformers import pipeline

def firstLoad():
    model = pipeline(model='distilbert-base-cased-distilled-squad')
    model.save_pretrained('./model/')

firstLoad()