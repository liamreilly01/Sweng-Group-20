# imports
import string
import nltk
# nltk.download() # uncomment for first-time usage. download all by pressing 'd', then 'all' (using the installer)
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
from nltk.corpus import stopwords
stopwordsList = stopwords.words('english')
stopwordsList.append("i\'m")

# pre-processes text for further ML analysis:
# 1. Lower casing
# 2. Tokenizing
# 3. Stopword Removal
# 4. Punctuation Removal
# 5. Lemmatize
# returns as a list of tokens

def textPreProcessing(input):

    # 1. Lower casing
    input = input.lower()
    print("\nLower Casing:" + input)

    # 2. Tokenizing
    # still a minor bug with whitespaces (e.g. try: "???????      can you help me?")
    tokens = input.split(" ")

    print("\nTokenize:")
    for t in tokens:
        print(t)

    # 3. Stopword Removal
    tokens = [t for t in tokens if t not in stopwordsList]
    print("\nstopword removal:")
    for t in tokens:
        print(t)

    # 4. Punctuation Removal
    i = 0
    for t in tokens:
        temp = [char for char in t if char not in string.punctuation]
        tokens[i] = ''.join(temp)
        i += 1

    print("\nPunctuation Removal:")
    for t in tokens:
        print(t)

    # 5. lemmatize
    print("\nLemmatize:")

    i = 0
    for i in range (len(tokens)):
        word = tokens[i]
        tokens[i] = lemmatizer.lemmatize(word, getWordnetPos(word))
        print(tokens[i])

    return tokens


# gets POS (part-of-speech) tag of a string
def getWordnetPos(word):
    tag = nltk.pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}

    return tag_dict.get(tag, wordnet.NOUN)


# main for testing
def main():
    text = input("input: ")
    list = textPreProcessing(text)


if __name__ == "__main__":
    main()