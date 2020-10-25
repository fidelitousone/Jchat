# project2-m3-js843

React chat application with a python backend.

[![JavaScript Style Guide](https://img.shields.io/badge/code_style-standard-brightgreen.svg)](https://standardjs.com)

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

### Make a Google Developer Account

* Go to `developer.google.com`
* Make an account NOT USING YOUR NJIT EMAIL!!!!!!!!!!!!!!
* Make a new project 
* Name it ANYTHING BUT DON'T USE GOOGLE IN THE NAME
* Go to credentials
* Configure Consent
* Select External
* Name the application ANYTHING BUT DON'T USE GOOGLE IN THE NAME
* Create App
* Go to Create OAuth ID
* Select Web application
* Add the website you're using to the authorized domain/java and both to authorized redirect, it might take a little bit just wait
* Copy the client ID
* Paste into the React component with the correct ID

### MAKE SURE YOU SETUP POSTGRESQL STUFF FIRST 
* `sudo yum install postgresql postgresql-server postgresql-devel postgresql-contrib postgresql-docs`
* `sudo service postgresql initdb`
* `sudo service postgresql start`
* `sudo -u postgres createuser --superuser $USER`
* `sudo -u postgres createdb $USER`
* `psql`
* `create user some_username_here superuser password 'some_unique_new_password_here';`

### Running locally
* clone this repo `https://github.com/NJIT-CS490/project2-m3-js843.git`
* cd `https://github.com/NJIT-CS490/project2-m3-js843.git`
* `npm install`
* `npm run watch` Open a separate terminal and do this
* `python -m venv .venv`
* `pip install -r requirements.txt`
* touch `sql.env` Fill it with: DATABASE_URL='postgresql://{YOUR_USERNAME}:{YOUR_PASSWORD}@localhost/postgres'
* `python main.py`
* navigate to URL `localhost:8080`
* If you are using cloud9, navigate to the preview running application tab
* Refresh with ctrl-shift-r 

### Deployment
* Make a heroku account if you don't already have one!!!
* clone this repo `https://github.com/NJIT-CS490/project2-m3-js843.git`
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

### Setting up Continuous Integration
* Make a CircleCI Account
* Connect your Github account to CircleCI
* Go to Dashboard
* Set up CI for this project
* Get your heroku API key from heroku
* add it as an environment variable in your project

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

### Conditionally Rendering Messages

I thought rendering user messages into their respective formats to account for whether a message is a link or not was going to easy. However, the part that proved to
be challenging was the fact that I was trying to use a map to iterate over objects instead of using a different function that’ll handle the rendering properly for me.
The issue was, that with a map, you can’t edit or use control flow on the items, so the solution I found was to make another function that handles returning the 
proper render of either a link or an image

### Displaying Links, Images, and Messages

This integration in my program truly revealed that my original implementation of displaying messages in Milestone 1 was not very good at all. Originally what I was 
doing is concatting both the user AND the message itself as a whole message and sent that back to the front end. I had to use extremely complicated methods of 
string splitting which weren't fun all to even determine what's a link, a message, or even an image. The solution was to completely redo the way messages are sent,
that way, I was delivering an array of dictionaries which had its information separately to be passed to a prop.

## Known Issues
### The Scrollbar Doesn't Automatically Go Down!

Obviously one of the things expected of every modern chat program is an option 
to automatically scroll the chat down when there's a new message that's sent.
Given more time this probably could have been implemented.

### The HTML Styling is poor.

The current HTML styling borrows quite heavily from my previous project, and 
currently the way the HTML looks isn't so great. I dedicated a vast majority of 
my time to ensure the mechanics of the program itself worked rather than the 
aesthetic components of it.

### Too many refreshes kills the program

I'm not sure why, but whenever an excessive amount of messages are sent, the
database decides to lock up and not function. Given more time I could use a 
session implementation to stop the database from crashing the entire server after
a few messages are sent.