from flask import Flask, render_template, redirect, url_for, request, jsonify, request
import json
from flask_cors import CORS, cross_origin

from flask_pymongo import PyMongo



app = Flask(__name__)
with app.app_context():
    CORS(app)
    app.config['MONGO_DBNAME'] = 'sxswnotester'
    # app.config['MONGO_URI'] = 'mongodb://localhost:27017/restdb'
    app.config['MONGO_URI'] = 'mongodb://patientplatypus:Fvnjty0b@ds249398.mlab.com:49398/sxswnotester'
    mongo = PyMongo(app)

    from python_play import *

if __name__ == '__main__':
    app.run()
    # port = 8000 #the custom port you want
    # app.run(host='0.0.0.0', port=port)
