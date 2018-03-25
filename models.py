import datetime

# Import the database object (db) from the main application module
# We will define this inside /app/__init__.py in the next sections.
from application import db

# Define a base model for other database tables to inherit
class Base(db.Model):

    __abstract__    = True

    id              = db.Column(db.Integer, primary_key=True)
    
    
class Dataset(Base):

    name     = db.Column(db.String(50))
    description  = db.Column(db.String(500000000))


    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return '<Course %r>' % self.name