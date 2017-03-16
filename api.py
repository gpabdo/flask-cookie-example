#!/usr/bin/python

#
# Checkout http://flask.pocoo.org/docs/0.12/quickstart/
#

import os
from flask import Flask
from flask import request
from flask import render_template
from flask import make_response
from flask import abort
from flask import redirect
from flask import url_for
from flask import session

app = Flask(__name__)


## ---- root ------------------------------ ##
#
# 
#
## ---------------------------------------- ##
@app.route('/')
def hello_world():
 
   # Is this a known user?
   username = request.cookies.get('username')

   if username != 'asshole': 
     return redirect(url_for('static', filename='login.html') )

   # Known user, say hello.
   return redirect( url_for( '.hello', name = username ) )


## ---- login ----------------------------- ##
#
# login
#
## ---------------------------------------- ##
@app.route('/login', methods=['POST', 'GET'])
def login():
     
    error = None

    if request.method == 'POST':
        username = request.form['username']
        if username == "greg":
          if request.form['password'] == "greg":
             resp = make_response( redirect( url_for( '.hello', name = username ) ) )
             resp.set_cookie('username', 'asshole')
             return resp
        else:
            error = 'Invalid username/password'

    return redirect( url_for( 'static', filename='login.html')) 


## ---- render template ------------------- ##
#
# 
#
## ---------------------------------------- ##
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


## ---- logout ---------------------------- ##
#
#
#
## ---------------------------------------- ##
@app.route('/logout')
def logout():

   resp = make_response( redirect( url_for( 'static', filename='logout.html' ) ) )
   resp.set_cookie('username', '', expires=0)
   return resp


## ---- main ------------------------------ ##
#
#
#
## ---------------------------------------- ##
if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    app.run()
