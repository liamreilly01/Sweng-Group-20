# imports
import string
import nltk
# nltk.download() # uncomment for first-time usage. download all by pressing 'd', then 'all' (using the installer)
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

# pre-processes text for further ML analysis:
# (a) lower casing, (b) punctuation removal (c) tokenize
# (d) stop-word removal (e) lemmatize
# returns as a list

def textPreProcessing(input):
    preProcessedText = []

    # (a) lower casing
    input = input.lower()
    print("\nLower Casing: " + input)

    # (b) punctuation removal
    text = [c for c in input if c not in string.punctuation]
    text = ''.join(text)
    print("\nPunctuation Removal: " + text)

    # (c) tokenize
    text = nltk.word_tokenize(text)
    print("\nTokenize: ")
    for t in text:
        print(t)

    # (d) stop-word removal
    stopwordsList = stopwords.words('english')
    preProcessedText = [t for t in text if t not in stopwordsList]
    print("\nstopword removal: ")
    for ppt in preProcessedText:
        print(ppt)

    # (e) lemmatize
    print("\nLemmatizer: ")

    lemmatizer = WordNetLemmatizer()

    i = 0
    for i in range (len(preProcessedText)):
        word = preProcessedText[i]
        preProcessedText[i] = lemmatizer.lemmatize(word, getWordnetPos(word))
        print(preProcessedText[i])

    return preProcessedText


# gets POS (part-of-speech) tag of a string
def getWordnetPos(word):
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}

    return tag_dict.get(tag, wordnet.NOUN)


# main for testing
text = input("input: ")
list = textPreProcessing(text)