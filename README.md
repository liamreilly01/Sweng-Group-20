# Sweng-Group-20

# Transfer the following file into the model folder
https://drive.google.com/file/d/1NR5wYN1hkLvl16T0mhRajdtV6hJiYE-n/view?usp=share_link
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

# Current Progress

Chatbot model is pretrained on distilbert, fine-tuned on squad and our own custom sample QA
dataset. We can successfully train the model. The goal is to implement cosine Similarity
to make the algorithm more efficient.