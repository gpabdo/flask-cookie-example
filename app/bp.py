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
from flask import Blueprint


# Checkout http://flask.pocoo.org/docs/0.12/blueprints/
bp = Blueprint('bp', __name__, template_folder='templates', static_folder='static')

## ---- access denyed --------------------- ##
#
#
#
## ---------------------------------------- ##
@bp.errorhandler(401)
def custom_401(error):
    return Response('No access, denied!', 401)


## ---- huh? ------------------------------ ##
#
#
#
## ---------------------------------------- ##
@bp.errorhandler(404)
def custom_404(error):
    return Response('Custom 404 from bp fool', 404)


## ---- root ------------------------------ ##
#
# 
#
## ---------------------------------------- ##
@bp.route('/')
def index():

   if 'username' in session:
     return redirect( url_for( 'bp.hello', name = session['username'] ) )

   return redirect(url_for('bp.static', filename='login.html') )


## ---- login ----------------------------- ##
#
# login
#
## ---------------------------------------- ##
@bp.route('/login', methods=['POST', 'GET'])
def login():
     
    error = None

    if request.method == 'POST':
        username = request.form['username']
        if username == "greg":
          if request.form['password'] == "greg":
             resp = make_response( redirect( url_for( 'bp.hello', name = username ) ) )
             session['username'] = username
             return resp
        else:
            error = 'Invalid username/password'

    return redirect( url_for( 'bp.static', filename='login.html')) 


## ---- render template ------------------- ##
#
# 
#
## ---------------------------------------- ##
@bp.route('/hello/<name>')
def hello(name=None):
  if 'username' in session:
    return render_template('hello.html', name=name)

  return redirect( url_for( 'bp.static', filename='login.html')) 


## ---- view the data --------------------- ##
#
#
#
## ---------------------------------------- ##
@bp.route('/data/view')
def viewData():
   if 'username' not in session:
      return redirect( url_for( 'bp.login' ) )
  
   resp = make_response( redirect( url_for( 'bp.static', filename='data.html' ) ) )
   return resp


## ---- get the  data --------------------- ##
#
#
#
## ---------------------------------------- ##
@bp.route('/data')
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
@bp.route('/logout')
def logout():

   resp = make_response( redirect( url_for( 'bp.static', filename='logout.html' ) ) )
   session.pop('username', None)
   return resp
