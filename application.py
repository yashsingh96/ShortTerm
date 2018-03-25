import os
import sys
import json
from utils import debug
import rekognize
import url
from flask import Flask, render_template, redirect, url_for, request, session
# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy


# EB looks for an 'application' callable by default.
application = Flask(__name__)

# Configurations
application.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(application)
from models import *

db.drop_all()

@application.route('/')
def index():
    datasets = Dataset.query.all()
    return render_template("index.html", 
                           datasets=datasets)
    
                           
@application.route('/search')
def search():
    return render_template("search.html")
    
@application.route('/new', )
def new():
    return render_template("form.html")
    
@application.route('/add', methods=['GET', 'POST'])
def process_data():
    try:
        name =  request.form['name']
        print(name)
        
        url_string = request.form['url_string']
        print(url_string)
        
        
        #Assuming either image will be input or url (not perfect)
        #if(image is None):
        text = url.TEXTviaURL(url_string)
        #else:
          #  data = rekognize.analyze(image, image.filename)
           # text = ""
            #for d in data:
            	#text += d
        print(text)
        description = url.summarize(url.wordSearch(text))
        print(description)
        #Adds new value to db   
        dataset = Dataset(name, description)
        print(dataset)
        db.session.add(dataset)
        db.session.commit()
        
    except Exception as e:
        name =  request.form['name']
        image = request.files['image']
        print("getting data from image...")
        data = rekognize.analyze(image, image.filename)
        text = ""
        for d in data:
            text += d + " "
        print(text)
        description = url.summarize(url.wordSearch(text))
        print(description)
        #Adds new value to db   
        dataset = Dataset(name, description)
        print(dataset)
        db.session.add(dataset)
        db.session.commit()
                
        #print(debug("Failed to input data:", e))
        #pass
    return redirect(url_for('index'))

#def clear_data(session):
#	meta = db.metadata
#	for table in reversed(meta.sorted_tables):
#	    print ('Clear table %s' % table)
#	    session.execute(table.delete())
 #   session.commit()
    
# run the app.
if __name__ == "__main__":
    # Build the database:
    # This will create the database file using SQLAlchemy
    #clear_data(db.session)
    db.drop_all()
    db.create_all()
    
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run(host='0.0.0.0', port=5005)

