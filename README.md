# Sweng-Group-20

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


## Download library

# Current Progress

This branch "scikit-practise-branch" is the deveolpemnet branch for the chatbot. Brendan and Cillian are trying out various methods for creating an AI that can perform all the requirements we want it to.

Currently there are 2 main fetures in this branch
    1. Brendans input processing algorithm in the "texyPreProcessing.py" file that can take an input and return only the relevent information that an AI would need from it.

    2. Cillians cosin similarity utilisation in the "example.py" file that can match an input with a relevent output throught the use of scikit's AI functions.

These 2 implimentations will be necisary to complete the AI chatbot and are being update frequently.

We are talking with Propalon to help us develop the AI using more sophisticated techniques that should create i better result than are current methods.

## To run the current version of chatbot

run the following commands in the terminal:
> pip install django-import-export

## To migrate changes to the server

You apply migrations when u've added any changes to the models, but just to be safe create a migration when u've added any major changes to the code so it's in sync with server

To do this run the following commands in the terminal:
> python manage.py makemigrations chatdata
> python manage.py migrate

## To run the server

run the following command in the terminal: 
> python manage.py runserver

## To get into the admin page

> Once you run the server you will be given a link like http://127.0.0.1:8000 in your terminal
> Add /admin to the url like so: http://127.0.0.1:8000/admin which will then prompt you to log in 
> Your username will just be your name and your password is the beginning part of your email in all caps 



