import sys, os.path
sys.path.append(os.path.abspath('../../'))
import requests_html
from app import *



class MessageTable(object):
    def __init__(self):
        self.database = mongo.db.messagetable

    def add_row(self, name, email, message):
        print("inside addrow")
        self.database.insert({"name": name, "email": email, "message": message})

    def get_db(self):
        output = []
        for s in database.find():
            output.append({'name' : s['name'], 'email' : s['email'], 'message' : s['message']})
        return output

    def show_db(self):
        print ('inside show_db')
        cursor = self.database.find({})
        for document in cursor:
            print(document)




class ParseTable(object):

    def __init__(self):
        self.database = mongo.db.sxswdaycatalog

    def add_row(self, row_title, row_date, row_time, row_venue, row_event, row_location):
        print("inside addrow")
        self.database.insert({"title": row_title, "date": row_date, "time": row_time, "venueLink": row_venue, "eventLink": row_event, "locationName": row_location})

    def get_db(self):
        output = []
        for s in database.find():
            output.append({'title' : s['title'], 'date' : s['date'], 'time' : s['time'], 'venueLink' : s['venueLink'], 'eventLink' : s['eventLink'], 'locationName' : s['locationName']})
        return output

    def show_db(self):
        print ('inside show_db')
        cursor = self.database.find({})
        for document in cursor:
            print(document)


class ParseTable8(object):

    def __init__(self):
        self.database = mongo.db.sxswdaycatalog8

    def add_row(self, row_title, row_date, row_time, row_venue, row_event, row_location):
        print("inside addrow")
        self.database.insert({"title": row_title, "date": row_date, "time": row_time, "venueLink": row_venue, "eventLink": row_event, "locationName": row_location})

    def get_db(self):
        output = []
        for s in database.find():
            output.append({'title' : s['title'], 'date' : s['date'], 'time' : s['time'], 'venueLink' : s['venueLink'], 'eventLink' : s['eventLink'], 'locationName' : s['locationName']})
        return output

    def show_db(self):
        print ('inside show_db')
        cursor = self.database.find({})
        for document in cursor:
            print(document)


class ParseTable9(object):

    def __init__(self):
        self.database = mongo.db.sxswdaycatalog9

    def add_row(self, row_title, row_date, row_time, row_venue, row_event, row_location):
        print("inside addrow")
        self.database.insert({"title": row_title, "date": row_date, "time": row_time, "venueLink": row_venue, "eventLink": row_event, "locationName": row_location})

    def get_db(self):
        output = []
        for s in database.find():
            output.append({'title' : s['title'], 'date' : s['date'], 'time' : s['time'], 'venueLink' : s['venueLink'], 'eventLink' : s['eventLink'], 'locationName' : s['locationName']})
        return output

    def show_db(self):
        print ('inside show_db')
        cursor = self.database.find({})
        for document in cursor:
            print(document)

class ParseTable10(object):

    def __init__(self):
        self.database = mongo.db.sxswdaycatalog10

    def add_row(self, row_title, row_date, row_time, row_venue, row_event, row_location):
        print("inside addrow")
        self.database.insert({"title": row_title, "date": row_date, "time": row_time, "venueLink": row_venue, "eventLink": row_event, "locationName": row_location})

    def get_db(self):
        output = []
        for s in database.find():
            output.append({'title' : s['title'], 'date' : s['date'], 'time' : s['time'], 'venueLink' : s['venueLink'], 'eventLink' : s['eventLink'], 'locationName' : s['locationName']})
        return output

    def show_db(self):
        print ('inside show_db')
        cursor = self.database.find({})
        for document in cursor:
            print(document)

class ParseTable11(object):

    def __init__(self):
        self.database = mongo.db.sxswdaycatalog11

    def add_row(self, row_title, row_date, row_time, row_venue, row_event, row_location):
        print("inside addrow")
        self.database.insert({"title": row_title, "date": row_date, "time": row_time, "venueLink": row_venue, "eventLink": row_event, "locationName": row_location})

    def get_db(self):
        output = []
        for s in database.find():
            output.append({'title' : s['title'], 'date' : s['date'], 'time' : s['time'], 'venueLink' : s['venueLink'], 'eventLink' : s['eventLink'], 'locationName' : s['locationName']})
        return output

    def show_db(self):
        print ('inside show_db')
        cursor = self.database.find({})
        for document in cursor:
            print(document)

class ParseTable12(object):

    def __init__(self):
        self.database = mongo.db.sxswdaycatalog12

    def add_row(self, row_title, row_date, row_time, row_venue, row_event, row_location):
        print("inside addrow")
        self.database.insert({"title": row_title, "date": row_date, "time": row_time, "venueLink": row_venue, "eventLink": row_event, "locationName": row_location})

    def get_db(self):
        output = []
        for s in database.find():
            output.append({'title' : s['title'], 'date' : s['date'], 'time' : s['time'], 'venueLink' : s['venueLink'], 'eventLink' : s['eventLink'], 'locationName' : s['locationName']})
        return output

    def show_db(self):
        print ('inside show_db')
        cursor = self.database.find({})
        for document in cursor:
            print(document)

class ParseTable13(object):

    def __init__(self):
        self.database = mongo.db.sxswdaycatalog13

    def add_row(self, row_title, row_date, row_time, row_venue, row_event, row_location):
        print("inside addrow")
        self.database.insert({"title": row_title, "date": row_date, "time": row_time, "venueLink": row_venue, "eventLink": row_event, "locationName": row_location})

    def get_db(self):
        output = []
        for s in database.find():
            output.append({'title' : s['title'], 'date' : s['date'], 'time' : s['time'], 'venueLink' : s['venueLink'], 'eventLink' : s['eventLink'], 'locationName' : s['locationName']})
        return output

    def show_db(self):
        print ('inside show_db')
        cursor = self.database.find({})
        for document in cursor:
            print(document)

class ParseTable14(object):

    def __init__(self):
        self.database = mongo.db.sxswdaycatalog14

    def add_row(self, row_title, row_date, row_time, row_venue, row_event, row_location):
        print("inside addrow")
        self.database.insert({"title": row_title, "date": row_date, "time": row_time, "venueLink": row_venue, "eventLink": row_event, "locationName": row_location})

    def get_db(self):
        output = []
        for s in database.find():
            output.append({'title' : s['title'], 'date' : s['date'], 'time' : s['time'], 'venueLink' : s['venueLink'], 'eventLink' : s['eventLink'], 'locationName' : s['locationName']})
        return output

    def show_db(self):
        print ('inside show_db')
        cursor = self.database.find({})
        for document in cursor:
            print(document)


class ParseTable15(object):

    def __init__(self):
        self.database = mongo.db.sxswdaycatalog15

    def add_row(self, row_title, row_date, row_time, row_venue, row_event, row_location):
        print("inside addrow")
        self.database.insert({"title": row_title, "date": row_date, "time": row_time, "venueLink": row_venue, "eventLink": row_event, "locationName": row_location})

    def get_db(self):
        output = []
        for s in database.find():
            output.append({'title' : s['title'], 'date' : s['date'], 'time' : s['time'], 'venueLink' : s['venueLink'], 'eventLink' : s['eventLink'], 'locationName' : s['locationName']})
        return output

    def show_db(self):
        print ('inside show_db')
        cursor = self.database.find({})
        for document in cursor:
            print(document)


class ParseTable16(object):

    def __init__(self):
        self.database = mongo.db.sxswdaycatalog16

    def add_row(self, row_title, row_date, row_time, row_venue, row_event, row_location):
        print("inside addrow")
        self.database.insert({"title": row_title, "date": row_date, "time": row_time, "venueLink": row_venue, "eventLink": row_event, "locationName": row_location})

    def get_db(self):
        output = []
        for s in database.find():
            output.append({'title' : s['title'], 'date' : s['date'], 'time' : s['time'], 'venueLink' : s['venueLink'], 'eventLink' : s['eventLink'], 'locationName' : s['locationName']})
        return output

    def show_db(self):
        print ('inside show_db')
        cursor = self.database.find({})
        for document in cursor:
            print(document)


class ParseTable17(object):

    def __init__(self):
        self.database = mongo.db.sxswdaycatalog17

    def add_row(self, row_title, row_date, row_time, row_venue, row_event, row_location):
        print("inside addrow")
        self.database.insert({"title": row_title, "date": row_date, "time": row_time, "venueLink": row_venue, "eventLink": row_event, "locationName": row_location})

    def get_db(self):
        output = []
        for s in database.find():
            output.append({'title' : s['title'], 'date' : s['date'], 'time' : s['time'], 'venueLink' : s['venueLink'], 'eventLink' : s['eventLink'], 'locationName' : s['locationName']})
        return output

    def show_db(self):
        print ('inside show_db')
        cursor = self.database.find({})
        for document in cursor:
            print(document)


class ParseTable18(object):

    def __init__(self):
        self.database = mongo.db.sxswdaycatalog18

    def add_row(self, row_title, row_date, row_time, row_venue, row_event, row_location):
        print("inside addrow")
        self.database.insert({"title": row_title, "date": row_date, "time": row_time, "venueLink": row_venue, "eventLink": row_event, "locationName": row_location})

    def get_db(self):
        output = []
        for s in database.find():
            output.append({'title' : s['title'], 'date' : s['date'], 'time' : s['time'], 'venueLink' : s['venueLink'], 'eventLink' : s['eventLink'], 'locationName' : s['locationName']})
        return output

    def show_db(self):
        print ('inside show_db')
        cursor = self.database.find({})
        for document in cursor:
            print(document)
