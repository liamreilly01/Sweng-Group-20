import os
import json
import yake


#--------------------------Load Json code--------------------------
try:
    presetResponses = open('PresetResponses.json', "r")
    try:
        presetResponsesDictionary = json.loads(presetResponses.read())
    except:
        print("ERROR while loading and reading file PresetResponses.json")
    finally:
        presetResponses.close()
except:
    print("ERROR while opeing file PresetResponses.json")
#------------------------------------------------------------------


#------------------------YAKE Keyword Extraction code-------------
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
    return []

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
    return []
#-----------------------------------------------------------------


#---------------------very bad priority algorithm------------------
# !!!very basic priority algorithm!!!!!change to be better!!!
def findBestFitAsnwer(input):
    # save keyphrase and keywords of input
    inputKeyPhrase = getKeyPhrase(input)
    inputKeyWords = getKeyWords(input)
    
    # check for no keypharse to avoid null pointer error
    if len(inputKeyPhrase) > 0:
        # check for exact matching key phrase --- highest priority
        for phrase in presetResponsesDictionary["PresetResponses"]:
            if phrase["keyphrase"].lower() == inputKeyPhrase[0].lower():
                print("\nquestion we thinking you are asking -> " + phrase["question"])
                return phrase["answer"]
    
    # check for no keypwords to avoid null pointer error
    if len(inputKeyWords) > 0:
        # check for matching key words, largest number of them is chosen --- lowest priority
        closestMatchAnswer = [0, "no answer found"]
        closestMatchQuestion = [""]
        for words in presetResponsesDictionary["PresetResponses"]:
            currentCount = 0
            outputWordsList = words["keywords"]
            for outkeyword in outputWordsList:
                for inkeyword in inputKeyWords:
                    if outkeyword.lower() == inkeyword[0].lower():
                        currentCount += 1
                if currentCount > closestMatchAnswer[0]:
                    closestMatchAnswer[1] = phrase["answer"]
                    closestMatchQuestion = phrase["question"]
        print("\nquestion we thinking you are asking -> " + closestMatchQuestion)
        return closestMatchAnswer[1]
    
    # no answer found so returning error outout
    return "no answer found"
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
print(str(len(presetResponsesDictionary["PresetResponses"])) + " responses loaded from file")
while True:
    print("\nBOT: Hello! Do you have a question (currently only from the FAQ list)")
    terminalInput = input('USER: ')
    if terminalInput != "":
        print("\n" + processInput(terminalInput))
#-----------------------------------------------------------------
