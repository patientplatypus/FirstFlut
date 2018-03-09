
import 'package:flutter/material.dart';
import 'dart:io';
import 'dart:convert';
import 'dart:core';
import 'dart:collection';
import 'package:http/http.dart' as http;

class MyPage3 extends StatefulWidget {
  const MyPage3(this.title, this.sunBool, this.sunString);

  final String title;
  final bool sunBool;
  final String sunString;



  @override
  MyPage3Home createState() => new MyPage3Home(title);
}


class MyPage3Home extends State<MyPage3> {
  MyPage3Home(this.title);
  final String title;
  List partyList = new List();
  List activityList = new List();

  @override
  void didUpdateWidget(MyPage3 oldWidget) {
    // TODO: implement didUpdateWidget
    super.didUpdateWidget(oldWidget);
    print("widget.sunBool in update: " + widget.sunBool.toString());
    print("oldWidget.sunBool in update: " + oldWidget.sunBool.toString());
    if (widget.sunBool == true){
      getActivityList();
    }else{
      getPartyList();
    }
  }

  @override
  void initState() {
    super.initState();
    if (widget.sunBool == true){
      getActivityList();
    }else{
      getPartyList();
    }
  }

  getPartyList() async {

    var httpClient = new HttpClient();
    print("inside getPartyList");
    String result;
    List partyReturn = new List();
    try {
      var uri = new Uri.https('f1utt3rshi.herokuapp.com', '/getRSVPSTERTABLE');
      var request = await httpClient.getUrl(uri);
      var response = await request.close();
      if (response.statusCode == HttpStatus.OK) {
        var json = await response.transform(UTF8.decoder).join();
        var data = JSON.decode(json);
        print(data['result'][0]['partyArray']);
        var parties = data['result'][0]['partyArray'];
        for (var i = 0; i < parties.length; i++){
          partyReturn.add(parties[i]);
        }

      } else {
        result =
        'Error getting List:\nHttp status ${response.statusCode}';
      }
    } catch (exception) {
      result = 'Failed getting List: ' + exception.toString();
    }

    print(result);
//    print(activityList[4]['date']);

    // If the widget was removed from the tree while the message was in flight,
    // we want to discard the reply rather than calling setState to update our
    // non-existent appearance.
    if (!mounted) return;
    setState(() {
      partyList = partyReturn;
    });
  }

  getActivityList() async {

    var httpClient = new HttpClient();
      print("inside getActivityList");
      String result;
      List activityReturn = new List();
      try {
        var endpt = '/getSXSWTABLE/'+widget.sunString;
        print("value of endpt: " + endpt);
        var url = 'https://f1utt3rshi.herokuapp.com'+endpt.toString();
        print("value or url " + url);
        var uri = new Uri.https('f1utt3rshi.herokuapp.com', endpt.toString());
        var request = await httpClient.getUrl(uri);
        var response = await request.close();
        if (response.statusCode == HttpStatus.OK) {
          var json = await response.transform(UTF8.decoder).join();
          var data = JSON.decode(json);

//          result = data['result'][0]['date'];
//          print("value of data: ${data['result'][0]}");
//          print("value of data: "+data['result'][0].toString());
          for (var i = 0; i < data['result'].length; i++){
            activityReturn.add({
              "date": data['result'][i]['date'],
              "eventLink": data['result'][i]['eventLink'],
              "locationName": data['result'][i]['locationName'],
              "time": data['result'][i]['time'],
              "title": data['result'][i]['title'],
              "venueLink": data['result'][i]['venueLink'],
            });
          }

      } else {
        result =
        'Error getting List:\nHttp status ${response.statusCode}';
      }
    } catch (exception) {
      result = 'Failed getting List: ' + exception.toString();
    }

    print(result);

//    var endpt = '/getSXSWTABLE/'+widget.sunString;
//    var url = 'https://f1utt3rshi.herokuapp.com'+endpt;
//
//    http.get(url,  headers: {'Content-type': 'application/json'}).then((response) {
//      var json = await response.body.transform(UTF8.decoder).join();
//      var data = JSON.decode(json);
//      for (var i = 0; i < data['result'].length; i++){
//        activityReturn.add({
//          "date": data['result'][i]['date'],
//          "eventLink": data['result'][i]['eventLink'],
//          "locationName": data['result'][i]['locationName'],
//          "time": data['result'][i]['time'],
//          "title": data['result'][i]['title'],
//          "venueLink": data['result'][i]['venueLink'],
//        });
//      }
//    }).catchError((onError){
//      print("Oh no there was an error: " + onError);
//    });


    // If the widget was removed from the tree while the message was in flight,
    // we want to discard the reply rather than calling setState to update our
    // non-existent appearance.
    if (!mounted) return;
    setState(() {
      activityList = activityReturn;
    });
  }


  @override
  Widget build(BuildContext context) {
    if (widget.sunBool==true){
      if (activityList.length > 0){
        return new MaterialApp(
            title: title,
            theme: new ThemeData(
              primarySwatch: Colors.blue,
            ),
            home: new Scaffold(
                body: new ListView.builder(
                    padding: new EdgeInsets.all(0.0),
                    itemBuilder: (BuildContext context, int index){
                      return new Container(
                          color: Colors.black,
                          padding: new EdgeInsets.fromLTRB(0.0, 12.0, 0.0, 12.0),
                          child: new Column(
                            children: <Widget>[
                              new Row(
                                children: <Widget>[
                                  new Flexible(
                                    child:new Text(activityList[index]['title'],
                                        style: new TextStyle(fontWeight: FontWeight.bold, fontSize: 25.0, color: Colors.orange)
                                    )
                                  )
                                ],
                              ),
                              new Row(
                                  children: <Widget>[
                                    new Flexible(
                                      child: new Column(
                                        children: <Widget>[
                                          new Text(activityList[index]['date'],
                                              style: new TextStyle(fontStyle: FontStyle.italic, fontSize: 20.0, color: Colors.white)
                                          ),
                                          new Text(activityList[index]['time'],
                                              style: new TextStyle(fontStyle: FontStyle.italic, fontSize: 20.0, color: Colors.white)
                                          ),
                                        ],
                                      ),
                                    ),
                                    new Flexible(
                                        flex: 2,
                                        child: new Text(activityList[index]['locationName'],
                                            style: new TextStyle(fontStyle: FontStyle.italic, fontSize: 20.0, color: Colors.white)
                                        )
                                    ),
                                  ]
                              )
                            ],
                          )
                      );
                    }
                )
            )
        );
      }else{
        return new MaterialApp(
            title: title,
            theme: new ThemeData(
              primarySwatch: Colors.blue,
            ),
            home: new Container(
                color: Colors.black,
                child: new Text("Loading...")
            )
        );
      }
    }else{
      if (partyList.length > 0){
        return new MaterialApp(
            title: title,
            theme: new ThemeData(
              primarySwatch: Colors.blue,
            ),
            home: new Scaffold(
                body: new ListView.builder(
                    padding: new EdgeInsets.all(0.0),
                    itemBuilder: (BuildContext context, int index){
                      return new Container(
                          color: Colors.black,
                          padding: new EdgeInsets.fromLTRB(0.0, 15.0, 0.0, 15.0),
                          child: new Row(
                              children: <Widget>[
                                new Expanded(
                                    child: new Text(partyList[index],
                                        style: new TextStyle(fontStyle: FontStyle.italic, fontSize: 20.0, color: Colors.white)
                                    )
                                )
                              ]
                          )
                      );
                    }
                )
            )
        );
      }else{
        return new MaterialApp(
            title: title,
            theme: new ThemeData(
              primarySwatch: Colors.blue,
            ),
            home: new Container(
                color: Colors.black,
                child: new Text("Loading...")
            )
        );
      }
    }
  }
}