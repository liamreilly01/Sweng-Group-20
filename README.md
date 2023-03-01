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



