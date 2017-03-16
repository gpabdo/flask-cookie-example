#!/usr/bin/python

#
# Checkout http://flask.pocoo.org/docs/0.12/quickstart/
#

import os
from flask import Flask
from flask import request
from flask import render_template
from flask import make_response
from flask import Response
from flask import json
from flask import abort
from flask import redirect
from flask import url_for
from flask import session

app = Flask(__name__)


## ---- access denyed --------------------- ##
#
#
#
## ---------------------------------------- ##
@app.errorhandler(401)
def custom_401(error):
    return Response('No access, denied!', 401)


## ---- root ------------------------------ ##
#
# 
#
## ---------------------------------------- ##
@app.route('/')
def hello_world():
 
   if 'username' in session:
     return redirect( url_for( '.hello', name = session['username'] ) )

   return redirect(url_for('static', filename='login.html') )


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
             session['username'] = username
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
  if 'username' in session:
    return render_template('hello.html', name=name)

  return  


## ---- view the data --------------------- ##
#
#
#
## ---------------------------------------- ##
@app.route('/data/view')
def viewData():
   if 'username' not in session:
      return redirect( url_for( 'login' ) )
  
   resp = make_response( redirect( url_for( 'static', filename='data.html' ) ) )
   return resp


## ---- get the  data --------------------- ##
#
#
#
## ---------------------------------------- ##
@app.route('/data')
def getData():
  
  if 'username' not in session:
    abort(401)

  with open('data.json', 'r') as myfile:
    data = myfile.read()

  response = app.response_class(
    response=json.dumps(data),
    status=200,
    mimetype='application/json'
  )
 
  return response

## ---- logout ---------------------------- ##
#
#
#
## ---------------------------------------- ##
@app.route('/logout')
def logout():

   resp = make_response( redirect( url_for( 'static', filename='logout.html' ) ) )
   session.pop('username', None)
   return resp


## ---- main ------------------------------ ##
#
#
#
## ---------------------------------------- ##
if __name__ == "__main__":
    # More settings: http://flask.pocoo.org/docs/0.12/api/

    app.secret_key = os.urandom(24)
    app.debug = False
    app.run( host = '0.0.0.0' )
