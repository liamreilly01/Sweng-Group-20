# Sweng-Group-20
looooooooooool
Group members:

3rd year students:
Mylana Bulat,
Liam Reilly,
William Walsh-Dowd, 
Conall O Toole

2nd year students:
Grace Bokunde,
Cillian French,
Mahir Masud,
Declan McCabe,
Brendan McCann,
Jake McKenna

Project discription:
This is an implementation of AI chatbot based on the website, www.irishstatute.ie.  The users may have trouble finding the information they need quickly and efficiently, particularly if they are not familiar with the legal terminology and structure of the legislation.
There is a growing demand for accessible and user-friendly ways of accessing legal information, and chatbots can play a role in meeting this need. By providing an alternative to traditional methods of accessing legal information, the chatbot system can help to make the law more accessible and understandable to a wider audience. The main purpose of this bot is to make search through the Irish Statute easier for general users.

In the first two releases we aim to train the bot to answer general questions about the Irish law and legal system through pointing out a link using trigger words. 
Potentially the bot will be able to act as a human lawyer, answering user questions with a generated reply that would clarify the topic for the user. 

## To run the current version of chatbot

run the following commands in the terminal: 
> pip install nltk

> pip install yake

> Python3 -m nltk.downloader wordnet

> Python3 bot.py

## To run the current version of xml-getter

go to the xml getter directory 

> pip install lxml

> Python3 main.py


# JSON File Documentation
each JSON object refers to a specific FAQ from the eISB website (https://www.irishstatutebook.ie/eli/faq.html)

"keywords" and "keyphrases" attributes are taken from yake's interpretation.
These attributes are not done manually, unless in exceptional cases.

Manually added in hyperlinks to answers

Line 160: manually added "help" keyword to "how can i get help with this site?"
Line 160: inserted most probable keyword to "how can i get help with this site?" and "How do I search for a word containing a fada?" as yake yielded no key phrases with length > 1

Line 46: "How will I know if a piece of legislation has been amended?" - should we manually add "changed" to keywords? more casual and less specific compared to "altered"

## Definitions
Synset - Set of words that are semantically equivalent (very similar to synonyms).
Lemma - the basic form of a word, for example the lemma of "breaking" and "broke" is 'break'.
