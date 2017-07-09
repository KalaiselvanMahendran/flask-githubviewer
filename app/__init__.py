# app/__init__.py

from flask import Flask, jsonify, request 
import urllib2
import json

# Initialize the app
app = Flask(__name__, instance_relative_config=True)

# Form Submit
@app.route('/search', methods=['POST'])
def search():
    if request.method == "POST":
    	name = request.form['username']
    	userData = urllib2.urlopen("https://api.github.com/users/" + name + "/repos").read()
    	return userData

# Load the views
from app import views

# Load the config file
app.config.from_object('config')