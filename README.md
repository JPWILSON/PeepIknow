# Simple HTTP Server Refresher

________________________________________________________

## Overview 
### Intended audience
This is just a basic web app, making use of an HTTP Test server, to recap how to build a test network,
or for those learning how to build web apps.
It is hosted on Heroku (see the requirement.txt and Procfile), and makes use of sqlite (sadly that means that it is 
reset each time Heroku spins up the instance (your database will not persist).

It is a simple app that allows you to fill in the name and relationship of all the people you know (silly alternate version of 
a shopping list app - but that you could build upon for a 'degrees of separation' app). To see it in use, go to
this [link](https://people-i-know.herokuapp.com/). The names already in the db are written in 
the database_setup.py file, discussed below. 

You can use the code if you are learning to build web apps with CRUD functionality, and want to learn the nuts and bolts 
of the htt request and responce cycle before moving to a framework like Flask or Django. 
It should be noted that Python's simple server (although it can handle multithreading with certain module imports) should
not be used in production - use Apache2. And, in my opinion, just get started with pqsl as soon as possible. 
The simple server means that the python code, via commenting is the 
method of writing to the database. This is not ideal as there is no error checking 
for you to pin point if there was a problem with your SQL (SqlAlchemy is a better way to go in production). 

### Prerequisites
But.... this is a great way to learn the basics. All you need to know is some basic python, how to make use of the built in libraries
(importing them into your module), referring to http on Wikipedia and some html. 

## Approach
You can look at the development process in two ways, you could start with wireframes, build a GUI and then work backwards, ending 
with an ERD and then a DB structure. I prefer to start by understanding the fundamental relationships, and then designing 
their interactions in the database with an ERD (see Data.jpg for this super simple one-table design). 
Once you have the design, you would write the python code to set up the database (database_setup.py). 
Then, you would write the logic for how to add people to your database, via a basic web form. This is shown in People.py
For more complex apps, it is best practice to separate your html from your python code, via a 
template engine such as jinja2 (you can find examples of a larger, complete web app [here](https://github.com/JPWILSON/JPS_V2/tree/master/Project)). 
but I just put the html in the python code for this example. 

Once you write one or two of these, you get the feel for how CRUD functionality is implemented, and not much changes,
for larger web apps conceptually. The frameworks simply take away a lot of the repetitive work. 

I hope this is useful for you in some way. 




