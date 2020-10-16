# project2-m2-js843

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
### MAKE SURE YOU SETUP POSTGRESQL STUFF FIRST 
* `sudo yum install postgresql postgresql-server postgresql-devel postgresql-contrib postgresql-docs`
* `sudo service postgresql initdb`
* `sudo service postgresql start`
* `sudo -u postgres createuser --superuser $USER`
* `sudo -u postgres createdb $USER`
* `psql`
* `create user some_username_here superuser password 'some_unique_new_password_here';`

### Deployment
* Make a heroku account if you don't already have one!!!
* clone this repo `https://github.com/NJIT-CS490/project2-m1-js843.git`
* `cd project2-m1-js843`
* `heroku login -i`
* `heroku create`
* `heroku addons:create heroku-postgresql:hobby-dev`
* `heroku pg:wait`
* `psql`
* `ALTER DATABASE Postgres OWNER '{YOUR_USERNAME}'`
* `heroku pg:push postgres DATABASE_URL` this is the password you use to log into the db
* `git push heroku master`
* Click on the link deployment message gives then use the app.

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



