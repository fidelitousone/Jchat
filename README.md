# project2-m1-js843

React chat application with a python backend.

## Table of Contents
* [Technologies](#technologies)
* [Setup](#setup)
* [Technical Difficulties](#technical-difficulties)
* [Known Issues](#known-issues)

## Technologies
* Python
* pip 
* Flask 
* python-dotenv 
* React
* Javascript
* Flask-SocketIO
* Postgresql

## Setup

## Technical Difficulties
### Hooking up SocketIO from the front end to the backend.

The first problem I encountered when writing this app was actually making 
socketIO connect from from the frontend to the backend. For this, I used one of
the examples of socket. However, I poorly understood what `Socket.jsx` actually 
did. It turns out to even get both the front-end and backend connected I needed
to import socket itself into one of the components I had.

### Using event handlers properly in react

This issue covers two problems I had dealing with actually getting the message
from the component and actually getting the data itself from input text box. I 
wasn't sure on how to get these only because my knowledge of useStates in react were limited
so, using help from a friend and doing checking lecture 8 and 10 helped reinforced
how to retrieve the data. In addition this website `https://reactgo.com/react-get-input-value/`

### Hooking up the databases

This part was a bit of a challenge, but I found the solution by following the 
lecture video for Lecture 11 Demo 2 `https://www.youtube.com/watch?v=GuRUFYlzA-U&list=PLejYYoWvB7A1lGuvAWTRKnrxzC-5Th5ru&index=25`
The biggest problem that held me up was actually querying the data itself to send it back to
the user connected to the session. I kept getting an error saying that a table didn't exist
that I created following the example of the Usps database table provided in the lecture.
It turned out for some reason I needed to call `models.db.create_all()` in order to make
sure that the database table itself  was being created.

## Known Issues
### The Scrollbar Doesn't Automatically Go Down!

Obviously one of the things expected of every modern chat program is an option 
to automatically scroll the chat down when there's a new message that's sent.
Given more time this probably could have been implemented.


### There is no count of users being updated.

A glaring issue, but there is no count of users that are updated whenever a 
new user joins or leave. This is due to the fact that I don't understand how
to uniquely assign an id or get unique IDs from sockets. Additionally, there's
the issue of how do I keep track of the current users connected? If given more
time this could have been cleared up.

### The HTML Styling is poor.

The current HTML styling borrows quite heavily from my previous project, and 
currently the way the HTML looks isn't so great. I dedicated a vast majority of 
my time to ensure the mechanics of the program itself worked rather than the 
aesthetic components of it.



