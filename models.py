import flask_sqlalchemy
from main import db

class Messages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120))
    message = db.Column(db.String(1000))
    
    def __init__(self, u, m):
        self.username = u
        self.message = m
        
    def __repr__(self):
        return f"<Message Data: {self.username}, {self.message}>"