import os
import json
import yake


#--------------------------Load Json code--------------------------
try:
    presetResponses = open('PresetResponses.json', "r", encoding="utf-8")
    try:
        presetResponsesDictionary = json.loads(presetResponses.read())
    except:
        print("ERROR while loading and reading file PresetResponses.json")
    finally:
        presetResponses.close()
except:
    print("ERROR while opeing file PresetResponses.json")

print(str(len(presetResponsesDictionary["PresetResponses"])) + " responses loaded from file\n")
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
    # save keyphrase and keywords of input to reduce amount of times they are called
    inputKeyPhrase = getKeyPhrase(input)
    inputKeyWords = getKeyWords(input)
    
    # check for no keypharse to avoid null pointer error
    if len(inputKeyPhrase) > 0:
        # check for exact matching key phrase --- highest priority
        for phrase in presetResponsesDictionary["PresetResponses"]:
            if phrase["keyphrase"].lower() == inputKeyPhrase[0].lower():
                print("\nquestion we think you are asking -> " + phrase["question"])
                print("found by matching key phrase")
                return phrase["answer"]
    
    # check for no keywords to avoid null pointer error
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
                    closestMatchAnswer[1] = words["answer"]
                    closestMatchAnswer[0] = currentCount
                    closestMatchQuestion = words["question"]
        print("\nquestion we think you are asking -> " + str(closestMatchQuestion))
        print("found by matching key words, amount of matches = " + str(closestMatchAnswer[0]))

        if (closestMatchAnswer[0] == 0):
            return "no answer found"
        else:
            return closestMatchAnswer[1]

    return "no answer found"
    

#-----------------------------------------------------------------


#----Hard coded FAQ reply code and algorithm output when hardcode fails----
def processInput(input):
    print("\nkeywords and phrase: ")
    printKeyWords(input)
    if (isFAQResponse(input)):
        print("[Question matches preset perfectly, giving preset answer]")
        return getFAQResponse(input)
    
    print('[I do not understand so I will try to use my keyword extraction and analysis to make a guess based on my preset answers]')
    return findBestFitAsnwer(input)

# determines whether a question is a perfect match to an FAQ
def isFAQResponse(input):
    for phrase in presetResponsesDictionary["PresetResponses"]:
        if phrase["question"].lower() == input.lower():
            return True
    return False

# returns associated answer to perfectly matched FAQ
def getFAQResponse(input):
    for phrase in presetResponsesDictionary["PresetResponses"]:
        if phrase["question"].lower() == input.lower():
            return phrase["answer"]
    return False
#-----------------------------------------------------------------


#-----basic input-output code to be added to a chat interface-----
print("BOT  : Hello! How may I help today? (Only FAQ)")
terminalInput = input('USER : ')

while (terminalInput != ""):
    print(processInput(terminalInput))
    print("\nBOT  : Do you have any other questions? (Only FAQ)")
    terminalInput = input('USER : ')

print("\nBOT  : I hope I was able to help. Goodbye!")
#-----------------------------------------------------------------
