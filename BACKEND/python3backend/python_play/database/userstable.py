import sys, os.path
sys.path.append(os.path.abspath('../../'))
import requests_html
from app import *



class UsersTable(object):

    def __init__(self):
        self.database = mongo.db.userscollection

    def add_user(self, username, password):
        print("inside addrow")
        self.database.insert({"username": username, "password": password})
