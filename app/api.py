#!/usr/bin/python

#
# Checkout http://flask.pocoo.org/docs/0.12/quickstart/
#

import os
from flask import Flask
#from flask import request
#from flask import render_template
#from flask import make_response
#from flask import Response
#from flask import json
#from flask import abort
#from flask import redirect
#from flask import url_for
#from flask import session
from flask import Blueprint
from bp import bp

app = Flask(__name__)
app.secret_key = os.urandom(24)

app.register_blueprint(bp, url_prefix='/flask')


## ---- main ------------------------------ ##
#
#
#
## ---------------------------------------- ##
if __name__ == "__main__":
    # More settings: http://flask.pocoo.org/docs/0.12/api/
    app.debug = True
    app.run( host = "0.0.0.0")

