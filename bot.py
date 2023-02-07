import os
import json
import yake


#--------------------------Load Json code--------------------------
presetResponses = open('PresetResponses.json', "r")
presetResponsesDictionary = json.loads(presetResponses.read())
presetResponses.close()
#------------------------------------------------------------------


#------------------------YAKE Keyword Exctration code-------------
def printKeyWords(input):
    keywords = getKeyWords(input)
    for kw in keywords:
        print(kw)

def getKeyWords(input):
    language = "en"
    max_ngram_size = 3
    deduplication_threshold = 0.9
    deduplication_algo = 'seqm'
    windowSize = 1
    numOfKeywords = 20

    custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, dedupFunc=deduplication_algo, windowsSize=windowSize, top=numOfKeywords, features=None)
    keywords = custom_kw_extractor.extract_keywords(input)

    if len(keywords) > 0:
        return keywords
    return [""]

def getKeyPhrase(input):
    language = "en"
    max_ngram_size = 3
    deduplication_threshold = 0.9
    deduplication_algo = 'seqm'
    windowSize = 1
    numOfKeywords = 20

    custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, dedupFunc=deduplication_algo, windowsSize=windowSize, top=numOfKeywords, features=None)
    keywords = custom_kw_extractor.extract_keywords(input)

    if len(keywords) > 0:
        return keywords[0]
    return [""]
#-----------------------------------------------------------------


#---------------------very bad prority algorithm------------------
# !!!very basic priority algorithm!!!!!change to be better!!!
def findBestFitAsnwer(input):
    # check for exact matching key phrase --- highest priority
    for phrase in presetResponsesDictionary["PresetResponses"]:
        inputkeyphrase = getKeyPhrase(input)[0]
        if phrase["keyphrase"].lower() == inputkeyphrase.lower():
            return phrase["answer"]
    
    # check for matching key words, largest number of them is chosen --- loweset priority
    closestMatch = [0, " no answer found"]
    for phrase in presetResponsesDictionary["PresetResponses"]:
        currentCount = 0
        for i in range(len(phrase["keywords"])):
            list = phrase["keywords"]
            keywordList = getKeyWords(input)
            for j in range(len(keywordList)):
                if list[i].lower() == keywordList[j][0].lower():
                    currentCount += 1
            if currentCount > closestMatch[0]:
                closestMatch[1] = phrase["answer"]
    return closestMatch[1]
#-----------------------------------------------------------------


#----Hard coded FAQ reply code and algorithm output when hardcode fails----
def processInput(input):
    print("keywords and phrase: ")
    printKeyWords(input)
    if (isFAQResponse(input) != False):
        return isFAQResponse(input)
    
    print('I dont understand so i will try to use my keyword extraction and analysis to make a guess bassed on my preset answers: ')
    return findBestFitAsnwer(input)


def isFAQResponse(input):
    for phrase in presetResponsesDictionary["PresetResponses"]:
        if phrase["question"].lower() == input.lower():
            print("question matches preset one perfectly, giving wepset answer: ")
            print(phrase["answer"])
            return phrase["answer"]
    return False
#-----------------------------------------------------------------


#-----basic input-output code to be added to a chat interface-----
while True:
    print("BOT: Hello! do you a question (currently only from the FAQ list)")
    terminalInput = input('USER: ')
    if terminalInput != "":
        print(processInput(terminalInput))
#-----------------------------------------------------------------