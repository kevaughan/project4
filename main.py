""" main.py is the top level script.

Return "Hello World" at the root URL.
"""


import os
import webapp2
import sys
# Import the Flask Framework
from flask import Flask, request
from flask import render_template
import urllib2
import json
import random
import uuid
from google.appengine.api import users
from google.appengine.api import channel
from utilities import funnames



#import sys
# sys.path includes 'server/lib' due to appengine_config.py
#from flask import Flask
#from flask import render_template
app = Flask(__name__.split('.')[0])
                                       
@app.route('/')
@app.route('/')
def mainpage(name=None):
  """ Return me template at application /me URL."""
  return render_template('headerpg.html', name=name)
  
@app.route('/memory')
def memory(name=None):
  """ Return me template at application /me URL."""
  return render_template('memory.html', name=name)


@app.route('/memory2')
def memory2(name=None):
  """ Return me template at application /me URL."""
  return render_template('memory2.html', name=name)


@app.route('/networkmain')
def networkmain(name=None):
  """ Return me template at application /me URL."""
  return render_template('networkmain.html', name=name)



@app.route('/index')
def index():
    """Setup a chat"""
    roomid = generate_id()
    template_values = {
                       "roomid":roomid
                                     }
    return render_template("index.html",values=template_values)

@app.route('/<roomid>/<name>')
def chatroom_and_name(roomid,name):
    """Return a chat page"""
    token = channel.create_channel(name + roomid) 
    template_values = {
                       "roomid":roomid,
                        "token": channel.create_channel(name + roomid),
                        "yourname": name
                       }
    return render_template("chat.html",values=template_values)

@app.route('/<roomid>')
def chatroom(roomid):
    """Return a chat page prompt for name
    then redirect to chatroom_and_name"""
    
    template_values = {
                       "roomid":roomid,
                       }
    return render_template("getname.html",values=template_values)
    

@app.route('/sendmessage/<user>/<roomid>', methods=['GET', 'POST'])
def sendmessage(user,roomid):
    """sends a message that is useless"""
    message = request.form['message']
    channel.send_message(user+roomid,message)
    
@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, No Valid Chatroom There.', 404

def generate_id():
    """Return a game id"""
    return "%s-%s" % (str(uuid.uuid4())[:4],random.choice(funnames).lower())