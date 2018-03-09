
import sys, os.path
sys.path.append(os.path.abspath('../../'))
import requests_html
import requests
from app import *
from python_play.database import *

# session = BrowserSession()
session = requests_html.Session()

messageTable = MessageTable()

parsedTable8 = ParseTable8()
parsedTable9 = ParseTable9()
parsedTable10 = ParseTable10()
parsedTable11 = ParseTable11()
parsedTable12 = ParseTable12()
parsedTable13 = ParseTable13()
parsedTable14 = ParseTable14()
parsedTable15 = ParseTable15()
parsedTable16 = ParseTable16()
parsedTable17 = ParseTable17()
parsedTable18 = ParseTable18()


userTable = UsersTable()


# print 'inside testroute'
#
# from python_play.classes import *
# from python_play.utils import *


# returnserver = MyServer()

# https://stackoverflow.com/questions/22281059/set-object-is-not-json-serializable

def set_default(obj):
    if isinstance(obj, set):
        return list(obj)
    raise TypeError

# @app.route("/saveContact", methods=["POST"])
# def test():
#     test = request.form["test"]
#     return "TEST: %s" % test

@app.route('/', methods=['GET'])
def indexroute():
    return jsonify({'result' : 'hello there sailor'})

@app.route('/saveContact', methods=['POST'])
def saveContact():
    print("inside saveContact form and value of request: ")
    print(request.get_json())
    print("value of name")
    print(request.json['name'])
    # name/email/message
    messageTable.add_row(request.json['name'], request.json['email'], request.json['message'])

    # print(request.form["test"])
    # if request.method == 'POST':
    #     if valid_login(request.form['username'],
    #                    request.form['password']):
    #         return log_the_user_in(request.form['username'])
    #     else:
    #         error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    # return render_template('login.html', error=error)
    return jsonify({'result' : 'success'})

@app.route('/testuser', methods=['GET'])
def testuser():
    userTable.add_user("johnDoe", "superdupersecretpassword")
    return jsonify({'result' : 'added!'})

@app.route('/test1', methods=['GET'])
def test():
    star = mongo.db.stars
    star_id = star.insert({'name': 'pants', 'distance': 'billions'})
    new_star = star.find_one({'_id': star_id })
    output = {'name' : new_star['name'], 'distance' : new_star['distance']}
    return jsonify({'result' : output})

# @app.route('/hello/<name>')
# def hello(name=None):
#     return render_template('hello.html', name=name)

# @app.route('/getSXSWTABLE', methods=['GET'])
# def getSXSWTABLE():
#     # output = parsedTable.get_db
#     output = []
#     database = mongo.db.sxswdaycatalog
#     for s in database.find():
#         output.append({'title' : s['title'], 'date' : s['date'], 'time' : s['time'], 'venueLink' : s['venueLink'], 'eventLink' : s['eventLink'], 'locationName' : s['locationName']})
#     return jsonify({'result' : output})

@app.route('/getSXSWTABLE/<day>', methods=['GET'])
def getSXSWTABLE(day=None):
    # output = parsedTable.get_db
    print("inside GET REQUEST")
    print("value of day: " + day)
    output = []
    if day == "9":
        database = mongo.db.sxswdaycatalog9
    if day == "10":
        database = mongo.db.sxswdaycatalog10
    if day == "11":
        database = mongo.db.sxswdaycatalog11
    if day == "12":
        database = mongo.db.sxswdaycatalog12
    if day == "13":
        database = mongo.db.sxswdaycatalog13
    if day == "14":
        database = mongo.db.sxswdaycatalog14
    if day == "15":
        database = mongo.db.sxswdaycatalog15
    if day == "16":
        database = mongo.db.sxswdaycatalog16
    if day == "17":
        database = mongo.db.sxswdaycatalog17
    if day == "18":
        database = mongo.db.sxswdaycatalog18

    # database = mongo.db.sxswdaycatalog
    for s in database.find():
        output.append({'title' : s['title'], 'date' : s['date'], 'time' : s['time'], 'venueLink' : s['venueLink'], 'eventLink' : s['eventLink'], 'locationName' : s['locationName']})
    # print("value of output: " + output[0])
    return jsonify({'result' : output})

@app.route('/getRSVPSTERTABLE', methods=['GET'])
def getRSVPSTERTABLE():
    # output = parsedTable.get_db
    output = []
    database = mongo.db.rsvpster
    for s in database.find():
        output.append({'partyArray' : s['partyArray']});
    return jsonify({'result' : output})


@app.route('/scrapeSXSWTABLE8', methods=['GET'])
def scrapeSXSWTABLE8():
    r = session.get('https://schedule.sxsw.com/2018/03/08/events')
    # about = r.html.find('#about', first=True)
    # print(r.html.links)
    # return jsonify({'result': r.html.links})
    eventTable = r.html.find('.event-list', first=True)

    for x in range(0, len(eventTable.find('.single-event')) - 1):
        singleEvent = eventTable.find('.single-event')[x]
        eventLinks = singleEvent.absolute_links
        eventLinksClean = set_default(eventLinks)
        eventSave = ""
        venueSave = ""
        titleSave = ""
        dateSave  = ""
        timeSave  = ""
        locationNameSave = ""
        for z in range(0, len(eventLinksClean)):
            if("2018/events/PP" in str(eventLinksClean[z])):
                eventSave = str(eventLinksClean[z])
            if("2018/venues/V" in str(eventLinksClean[z])):
                venueSave = str(eventLinksClean[z])
        for y in range(0, len(singleEvent.find('.columns'))-1):
            singleElement = singleEvent.find('.columns')[y]
            if y == 0:
                titleSave = singleElement.text.replace("Add to Favorites", "")
            if y == 1:
                testIndex = singleElement.text.index("2018")
                midIndex = testIndex + 4
                dateSave = singleElement.text[0:midIndex]
                timeSave = singleElement.text[midIndex+1:len(singleElement.text)]
            if y == 2:
                locationNameSave = singleElement.text
        # print("VALUES OF ALL THE SAVED VARIABLES")
        # print("eventSave: " + eventSave)
        # print("venueSave: " + venueSave)
        # print("titleSave: " + titleSave)
        # print("dateSave: " + dateSave)
        # print("timeSave: " + timeSave)
        # print("locationNameSave: " + locationNameSave)
        print("iteration: " + str(x))
        parsedTable8.add_row(titleSave, dateSave, timeSave, venueSave, eventSave, locationNameSave)
    # showDB = parsedTable.show_db()
    # print("value of returnedDB: " + showDB)
    # cleanTable = set_default()
    # return jsonify({"TABLE", parsedTable.return_db()})
    # parseDB = parsedTable.return_db()
    return jsonify({'result' : 'FINISHED!'})
    # return result

@app.route('/scrapeSXSWTABLE9', methods=['GET'])
def scrapeSXSWTABLE9():
    r = session.get('https://schedule.sxsw.com/2018/03/09/events')
    # about = r.html.find('#about', first=True)
    # print(r.html.links)
    # return jsonify({'result': r.html.links})
    eventTable = r.html.find('.event-list', first=True)

    for x in range(0, len(eventTable.find('.single-event')) - 1):
        singleEvent = eventTable.find('.single-event')[x]
        eventLinks = singleEvent.absolute_links
        eventLinksClean = set_default(eventLinks)
        eventSave = ""
        venueSave = ""
        titleSave = ""
        dateSave  = ""
        timeSave  = ""
        locationNameSave = ""
        for z in range(0, len(eventLinksClean)):
            if("2018/events/PP" in str(eventLinksClean[z])):
                eventSave = str(eventLinksClean[z])
            if("2018/venues/V" in str(eventLinksClean[z])):
                venueSave = str(eventLinksClean[z])
        for y in range(0, len(singleEvent.find('.columns'))-1):
            singleElement = singleEvent.find('.columns')[y]
            if y == 0:
                titleSave = singleElement.text.replace("Add to Favorites", "")
            if y == 1:
                testIndex = singleElement.text.index("2018")
                midIndex = testIndex + 4
                dateSave = singleElement.text[0:midIndex]
                timeSave = singleElement.text[midIndex+1:len(singleElement.text)]
            if y == 2:
                locationNameSave = singleElement.text
        # print("VALUES OF ALL THE SAVED VARIABLES")
        # print("eventSave: " + eventSave)
        # print("venueSave: " + venueSave)
        # print("titleSave: " + titleSave)
        # print("dateSave: " + dateSave)
        # print("timeSave: " + timeSave)
        # print("locationNameSave: " + locationNameSave)
        print("iteration: " + str(x))
        parsedTable9.add_row(titleSave, dateSave, timeSave, venueSave, eventSave, locationNameSave)
    # showDB = parsedTable.show_db()
    # print("value of returnedDB: " + showDB)
    # cleanTable = set_default()
    # return jsonify({"TABLE", parsedTable.return_db()})
    # parseDB = parsedTable.return_db()
    return jsonify({'result' : 'FINISHED!'})
    # return result

@app.route('/scrapeSXSWTABLE10', methods=['GET'])
def scrapeSXSWTABLE10():
    r = session.get('https://schedule.sxsw.com/2018/03/10/events')
    # about = r.html.find('#about', first=True)
    # print(r.html.links)
    # return jsonify({'result': r.html.links})
    eventTable = r.html.find('.event-list', first=True)

    for x in range(0, len(eventTable.find('.single-event')) - 1):
        singleEvent = eventTable.find('.single-event')[x]
        eventLinks = singleEvent.absolute_links
        eventLinksClean = set_default(eventLinks)
        eventSave = ""
        venueSave = ""
        titleSave = ""
        dateSave  = ""
        timeSave  = ""
        locationNameSave = ""
        for z in range(0, len(eventLinksClean)):
            if("2018/events/PP" in str(eventLinksClean[z])):
                eventSave = str(eventLinksClean[z])
            if("2018/venues/V" in str(eventLinksClean[z])):
                venueSave = str(eventLinksClean[z])
        for y in range(0, len(singleEvent.find('.columns'))-1):
            singleElement = singleEvent.find('.columns')[y]
            if y == 0:
                titleSave = singleElement.text.replace("Add to Favorites", "")
            if y == 1:
                testIndex = singleElement.text.index("2018")
                midIndex = testIndex + 4
                dateSave = singleElement.text[0:midIndex]
                timeSave = singleElement.text[midIndex+1:len(singleElement.text)]
            if y == 2:
                locationNameSave = singleElement.text
        # print("VALUES OF ALL THE SAVED VARIABLES")
        # print("eventSave: " + eventSave)
        # print("venueSave: " + venueSave)
        # print("titleSave: " + titleSave)
        # print("dateSave: " + dateSave)
        # print("timeSave: " + timeSave)
        # print("locationNameSave: " + locationNameSave)
        print("iteration: " + str(x))
        parsedTable10.add_row(titleSave, dateSave, timeSave, venueSave, eventSave, locationNameSave)
    # showDB = parsedTable.show_db()
    # print("value of returnedDB: " + showDB)
    # cleanTable = set_default()
    # return jsonify({"TABLE", parsedTable.return_db()})
    # parseDB = parsedTable.return_db()
    return jsonify({'result' : 'FINISHED!'})
    # return result

@app.route('/scrapeSXSWTABLE11', methods=['GET'])
def scrapeSXSWTABLE11():
    r = session.get('https://schedule.sxsw.com/2018/03/11/events')
    # about = r.html.find('#about', first=True)
    # print(r.html.links)
    # return jsonify({'result': r.html.links})
    eventTable = r.html.find('.event-list', first=True)

    for x in range(0, len(eventTable.find('.single-event')) - 1):
        singleEvent = eventTable.find('.single-event')[x]
        eventLinks = singleEvent.absolute_links
        eventLinksClean = set_default(eventLinks)
        eventSave = ""
        venueSave = ""
        titleSave = ""
        dateSave  = ""
        timeSave  = ""
        locationNameSave = ""
        for z in range(0, len(eventLinksClean)):
            if("2018/events/PP" in str(eventLinksClean[z])):
                eventSave = str(eventLinksClean[z])
            if("2018/venues/V" in str(eventLinksClean[z])):
                venueSave = str(eventLinksClean[z])
        for y in range(0, len(singleEvent.find('.columns'))-1):
            singleElement = singleEvent.find('.columns')[y]
            if y == 0:
                titleSave = singleElement.text.replace("Add to Favorites", "")
            if y == 1:
                testIndex = singleElement.text.index("2018")
                midIndex = testIndex + 4
                dateSave = singleElement.text[0:midIndex]
                timeSave = singleElement.text[midIndex+1:len(singleElement.text)]
            if y == 2:
                locationNameSave = singleElement.text
        # print("VALUES OF ALL THE SAVED VARIABLES")
        # print("eventSave: " + eventSave)
        # print("venueSave: " + venueSave)
        # print("titleSave: " + titleSave)
        # print("dateSave: " + dateSave)
        # print("timeSave: " + timeSave)
        # print("locationNameSave: " + locationNameSave)
        print("iteration: " + str(x))
        parsedTable11.add_row(titleSave, dateSave, timeSave, venueSave, eventSave, locationNameSave)
    # showDB = parsedTable.show_db()
    # print("value of returnedDB: " + showDB)
    # cleanTable = set_default()
    # return jsonify({"TABLE", parsedTable.return_db()})
    # parseDB = parsedTable.return_db()
    return jsonify({'result' : 'FINISHED!'})
    # return result

@app.route('/scrapeSXSWTABLE12', methods=['GET'])
def scrapeSXSWTABLE12():
    r = session.get('https://schedule.sxsw.com/2018/03/12/events')
    # about = r.html.find('#about', first=True)
    # print(r.html.links)
    # return jsonify({'result': r.html.links})
    eventTable = r.html.find('.event-list', first=True)

    for x in range(0, len(eventTable.find('.single-event')) - 1):
        singleEvent = eventTable.find('.single-event')[x]
        eventLinks = singleEvent.absolute_links
        eventLinksClean = set_default(eventLinks)
        eventSave = ""
        venueSave = ""
        titleSave = ""
        dateSave  = ""
        timeSave  = ""
        locationNameSave = ""
        for z in range(0, len(eventLinksClean)):
            if("2018/events/PP" in str(eventLinksClean[z])):
                eventSave = str(eventLinksClean[z])
            if("2018/venues/V" in str(eventLinksClean[z])):
                venueSave = str(eventLinksClean[z])
        for y in range(0, len(singleEvent.find('.columns'))-1):
            singleElement = singleEvent.find('.columns')[y]
            if y == 0:
                titleSave = singleElement.text.replace("Add to Favorites", "")
            if y == 1:
                testIndex = singleElement.text.index("2018")
                midIndex = testIndex + 4
                dateSave = singleElement.text[0:midIndex]
                timeSave = singleElement.text[midIndex+1:len(singleElement.text)]
            if y == 2:
                locationNameSave = singleElement.text
        # print("VALUES OF ALL THE SAVED VARIABLES")
        # print("eventSave: " + eventSave)
        # print("venueSave: " + venueSave)
        # print("titleSave: " + titleSave)
        # print("dateSave: " + dateSave)
        # print("timeSave: " + timeSave)
        # print("locationNameSave: " + locationNameSave)
        print("iteration: " + str(x))
        parsedTable12.add_row(titleSave, dateSave, timeSave, venueSave, eventSave, locationNameSave)
    # showDB = parsedTable.show_db()
    # print("value of returnedDB: " + showDB)
    # cleanTable = set_default()
    # return jsonify({"TABLE", parsedTable.return_db()})
    # parseDB = parsedTable.return_db()
    return jsonify({'result' : 'FINISHED!'})
    # return result

@app.route('/scrapeSXSWTABLE13', methods=['GET'])
def scrapeSXSWTABLE13():
    r = session.get('https://schedule.sxsw.com/2018/03/13/events')
    # about = r.html.find('#about', first=True)
    # print(r.html.links)
    # return jsonify({'result': r.html.links})
    eventTable = r.html.find('.event-list', first=True)

    for x in range(0, len(eventTable.find('.single-event')) - 1):
        singleEvent = eventTable.find('.single-event')[x]
        eventLinks = singleEvent.absolute_links
        eventLinksClean = set_default(eventLinks)
        eventSave = ""
        venueSave = ""
        titleSave = ""
        dateSave  = ""
        timeSave  = ""
        locationNameSave = ""
        for z in range(0, len(eventLinksClean)):
            if("2018/events/PP" in str(eventLinksClean[z])):
                eventSave = str(eventLinksClean[z])
            if("2018/venues/V" in str(eventLinksClean[z])):
                venueSave = str(eventLinksClean[z])
        for y in range(0, len(singleEvent.find('.columns'))-1):
            singleElement = singleEvent.find('.columns')[y]
            if y == 0:
                titleSave = singleElement.text.replace("Add to Favorites", "")
            if y == 1:
                testIndex = singleElement.text.index("2018")
                midIndex = testIndex + 4
                dateSave = singleElement.text[0:midIndex]
                timeSave = singleElement.text[midIndex+1:len(singleElement.text)]
            if y == 2:
                locationNameSave = singleElement.text
        # print("VALUES OF ALL THE SAVED VARIABLES")
        # print("eventSave: " + eventSave)
        # print("venueSave: " + venueSave)
        # print("titleSave: " + titleSave)
        # print("dateSave: " + dateSave)
        # print("timeSave: " + timeSave)
        # print("locationNameSave: " + locationNameSave)
        print("iteration: " + str(x))
        parsedTable13.add_row(titleSave, dateSave, timeSave, venueSave, eventSave, locationNameSave)
    # showDB = parsedTable.show_db()
    # print("value of returnedDB: " + showDB)
    # cleanTable = set_default()
    # return jsonify({"TABLE", parsedTable.return_db()})
    # parseDB = parsedTable.return_db()
    return jsonify({'result' : 'FINISHED!'})
    # return result

@app.route('/scrapeSXSWTABLE14', methods=['GET'])
def scrapeSXSWTABLE14():
    r = session.get('https://schedule.sxsw.com/2018/03/14/events')
    # about = r.html.find('#about', first=True)
    # print(r.html.links)
    # return jsonify({'result': r.html.links})
    eventTable = r.html.find('.event-list', first=True)

    for x in range(0, len(eventTable.find('.single-event')) - 1):
        singleEvent = eventTable.find('.single-event')[x]
        eventLinks = singleEvent.absolute_links
        eventLinksClean = set_default(eventLinks)
        eventSave = ""
        venueSave = ""
        titleSave = ""
        dateSave  = ""
        timeSave  = ""
        locationNameSave = ""
        for z in range(0, len(eventLinksClean)):
            if("2018/events/PP" in str(eventLinksClean[z])):
                eventSave = str(eventLinksClean[z])
            if("2018/venues/V" in str(eventLinksClean[z])):
                venueSave = str(eventLinksClean[z])
        for y in range(0, len(singleEvent.find('.columns'))-1):
            singleElement = singleEvent.find('.columns')[y]
            if y == 0:
                titleSave = singleElement.text.replace("Add to Favorites", "")
            if y == 1:
                testIndex = singleElement.text.index("2018")
                midIndex = testIndex + 4
                dateSave = singleElement.text[0:midIndex]
                timeSave = singleElement.text[midIndex+1:len(singleElement.text)]
            if y == 2:
                locationNameSave = singleElement.text
        # print("VALUES OF ALL THE SAVED VARIABLES")
        # print("eventSave: " + eventSave)
        # print("venueSave: " + venueSave)
        # print("titleSave: " + titleSave)
        # print("dateSave: " + dateSave)
        # print("timeSave: " + timeSave)
        # print("locationNameSave: " + locationNameSave)
        print("iteration: " + str(x))
        parsedTable14.add_row(titleSave, dateSave, timeSave, venueSave, eventSave, locationNameSave)
    # showDB = parsedTable.show_db()
    # print("value of returnedDB: " + showDB)
    # cleanTable = set_default()
    # return jsonify({"TABLE", parsedTable.return_db()})
    # parseDB = parsedTable.return_db()
    return jsonify({'result' : 'FINISHED!'})
    # return result

@app.route('/scrapeSXSWTABLE15', methods=['GET'])
def scrapeSXSWTABLE15():
    r = session.get('https://schedule.sxsw.com/2018/03/15/events')
    # about = r.html.find('#about', first=True)
    # print(r.html.links)
    # return jsonify({'result': r.html.links})
    eventTable = r.html.find('.event-list', first=True)

    for x in range(0, len(eventTable.find('.single-event')) - 1):
        singleEvent = eventTable.find('.single-event')[x]
        eventLinks = singleEvent.absolute_links
        eventLinksClean = set_default(eventLinks)
        eventSave = ""
        venueSave = ""
        titleSave = ""
        dateSave  = ""
        timeSave  = ""
        locationNameSave = ""
        for z in range(0, len(eventLinksClean)):
            if("2018/events/PP" in str(eventLinksClean[z])):
                eventSave = str(eventLinksClean[z])
            if("2018/venues/V" in str(eventLinksClean[z])):
                venueSave = str(eventLinksClean[z])
        for y in range(0, len(singleEvent.find('.columns'))-1):
            singleElement = singleEvent.find('.columns')[y]
            if y == 0:
                titleSave = singleElement.text.replace("Add to Favorites", "")
            if y == 1:
                testIndex = singleElement.text.index("2018")
                midIndex = testIndex + 4
                dateSave = singleElement.text[0:midIndex]
                timeSave = singleElement.text[midIndex+1:len(singleElement.text)]
            if y == 2:
                locationNameSave = singleElement.text
        # print("VALUES OF ALL THE SAVED VARIABLES")
        # print("eventSave: " + eventSave)
        # print("venueSave: " + venueSave)
        # print("titleSave: " + titleSave)
        # print("dateSave: " + dateSave)
        # print("timeSave: " + timeSave)
        # print("locationNameSave: " + locationNameSave)
        print("iteration: " + str(x))
        parsedTable15.add_row(titleSave, dateSave, timeSave, venueSave, eventSave, locationNameSave)
    # showDB = parsedTable.show_db()
    # print("value of returnedDB: " + showDB)
    # cleanTable = set_default()
    # return jsonify({"TABLE", parsedTable.return_db()})
    # parseDB = parsedTable.return_db()
    return jsonify({'result' : 'FINISHED!'})
    # return result

@app.route('/scrapeSXSWTABLE16', methods=['GET'])
def scrapeSXSWTABLE16():
    r = session.get('https://schedule.sxsw.com/2018/03/16/events')
    # about = r.html.find('#about', first=True)
    # print(r.html.links)
    # return jsonify({'result': r.html.links})
    eventTable = r.html.find('.event-list', first=True)

    for x in range(0, len(eventTable.find('.single-event')) - 1):
        singleEvent = eventTable.find('.single-event')[x]
        eventLinks = singleEvent.absolute_links
        eventLinksClean = set_default(eventLinks)
        eventSave = ""
        venueSave = ""
        titleSave = ""
        dateSave  = ""
        timeSave  = ""
        locationNameSave = ""
        for z in range(0, len(eventLinksClean)):
            if("2018/events/PP" in str(eventLinksClean[z])):
                eventSave = str(eventLinksClean[z])
            if("2018/venues/V" in str(eventLinksClean[z])):
                venueSave = str(eventLinksClean[z])
        for y in range(0, len(singleEvent.find('.columns'))-1):
            singleElement = singleEvent.find('.columns')[y]
            if y == 0:
                titleSave = singleElement.text.replace("Add to Favorites", "")
            if y == 1:
                testIndex = singleElement.text.index("2018")
                midIndex = testIndex + 4
                dateSave = singleElement.text[0:midIndex]
                timeSave = singleElement.text[midIndex+1:len(singleElement.text)]
            if y == 2:
                locationNameSave = singleElement.text
        # print("VALUES OF ALL THE SAVED VARIABLES")
        # print("eventSave: " + eventSave)
        # print("venueSave: " + venueSave)
        # print("titleSave: " + titleSave)
        # print("dateSave: " + dateSave)
        # print("timeSave: " + timeSave)
        # print("locationNameSave: " + locationNameSave)
        print("iteration: " + str(x))
        parsedTable16.add_row(titleSave, dateSave, timeSave, venueSave, eventSave, locationNameSave)
    # showDB = parsedTable.show_db()
    # print("value of returnedDB: " + showDB)
    # cleanTable = set_default()
    # return jsonify({"TABLE", parsedTable.return_db()})
    # parseDB = parsedTable.return_db()
    return jsonify({'result' : 'FINISHED!'})
    # return result

@app.route('/scrapeSXSWTABLE17', methods=['GET'])
def scrapeSXSWTABLE17():
    r = session.get('https://schedule.sxsw.com/2018/03/17/events')
    # about = r.html.find('#about', first=True)
    # print(r.html.links)
    # return jsonify({'result': r.html.links})
    eventTable = r.html.find('.event-list', first=True)

    for x in range(0, len(eventTable.find('.single-event')) - 1):
        singleEvent = eventTable.find('.single-event')[x]
        eventLinks = singleEvent.absolute_links
        eventLinksClean = set_default(eventLinks)
        eventSave = ""
        venueSave = ""
        titleSave = ""
        dateSave  = ""
        timeSave  = ""
        locationNameSave = ""
        for z in range(0, len(eventLinksClean)):
            if("2018/events/PP" in str(eventLinksClean[z])):
                eventSave = str(eventLinksClean[z])
            if("2018/venues/V" in str(eventLinksClean[z])):
                venueSave = str(eventLinksClean[z])
        for y in range(0, len(singleEvent.find('.columns'))-1):
            singleElement = singleEvent.find('.columns')[y]
            if y == 0:
                titleSave = singleElement.text.replace("Add to Favorites", "")
            if y == 1:
                testIndex = singleElement.text.index("2018")
                midIndex = testIndex + 4
                dateSave = singleElement.text[0:midIndex]
                timeSave = singleElement.text[midIndex+1:len(singleElement.text)]
            if y == 2:
                locationNameSave = singleElement.text
        # print("VALUES OF ALL THE SAVED VARIABLES")
        # print("eventSave: " + eventSave)
        # print("venueSave: " + venueSave)
        # print("titleSave: " + titleSave)
        # print("dateSave: " + dateSave)
        # print("timeSave: " + timeSave)
        # print("locationNameSave: " + locationNameSave)
        print("iteration: " + str(x))
        parsedTable17.add_row(titleSave, dateSave, timeSave, venueSave, eventSave, locationNameSave)
    # showDB = parsedTable.show_db()
    # print("value of returnedDB: " + showDB)
    # cleanTable = set_default()
    # return jsonify({"TABLE", parsedTable.return_db()})
    # parseDB = parsedTable.return_db()
    return jsonify({'result' : 'FINISHED!'})
    # return result


@app.route('/scrapeSXSWTABLE18', methods=['GET'])
def scrapeSXSWTABLE18():
    r = session.get('https://schedule.sxsw.com/2018/03/18/events')
    # about = r.html.find('#about', first=True)
    # print(r.html.links)
    # return jsonify({'result': r.html.links})
    eventTable = r.html.find('.event-list', first=True)

    for x in range(0, len(eventTable.find('.single-event')) - 1):
        singleEvent = eventTable.find('.single-event')[x]
        eventLinks = singleEvent.absolute_links
        eventLinksClean = set_default(eventLinks)
        eventSave = ""
        venueSave = ""
        titleSave = ""
        dateSave  = ""
        timeSave  = ""
        locationNameSave = ""
        for z in range(0, len(eventLinksClean)):
            if("2018/events/PP" in str(eventLinksClean[z])):
                eventSave = str(eventLinksClean[z])
            if("2018/venues/V" in str(eventLinksClean[z])):
                venueSave = str(eventLinksClean[z])
        for y in range(0, len(singleEvent.find('.columns'))-1):
            singleElement = singleEvent.find('.columns')[y]
            if y == 0:
                titleSave = singleElement.text.replace("Add to Favorites", "")
            if y == 1:
                testIndex = singleElement.text.index("2018")
                midIndex = testIndex + 4
                dateSave = singleElement.text[0:midIndex]
                timeSave = singleElement.text[midIndex+1:len(singleElement.text)]
            if y == 2:
                locationNameSave = singleElement.text
        # print("VALUES OF ALL THE SAVED VARIABLES")
        # print("eventSave: " + eventSave)
        # print("venueSave: " + venueSave)
        # print("titleSave: " + titleSave)
        # print("dateSave: " + dateSave)
        # print("timeSave: " + timeSave)
        # print("locationNameSave: " + locationNameSave)
        print("iteration: " + str(x))
        parsedTable18.add_row(titleSave, dateSave, timeSave, venueSave, eventSave, locationNameSave)
    # showDB = parsedTable.show_db()
    # print("value of returnedDB: " + showDB)
    # cleanTable = set_default()
    # return jsonify({"TABLE", parsedTable.return_db()})
    # parseDB = parsedTable.return_db()
    return jsonify({'result' : 'FINISHED!'})
    # return result
