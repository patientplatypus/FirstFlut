
import 'package:flutter/material.dart';
import 'dart:core';
import 'package:http/http.dart' as http;
import 'dart:convert';
//import 'package:redux/redux.dart';
//import 'package:flutter_redux/flutter_redux.dart';


class MyPage4 extends StatefulWidget {
  const MyPage4(this.title);

  final String title;

  @override
  MyPage4Home createState() => new MyPage4Home(title);
}


class MyPage4Home extends State<MyPage4> {
  MyPage4Home(this.title);
  final String title;


  @override
  Widget build(BuildContext context) {

    Widget Greeting = new Row(
      children: <Widget>[
        new Text("hi.",
            style: new TextStyle(fontWeight: FontWeight.bold, fontSize: .2*MediaQuery.of(context).size.width, color: Colors.white)
        ),
        new Column(
          children: <Widget>[
            new Text("It's a pleasure to meet you,",
                style: new TextStyle(fontWeight: FontWeight.bold, fontSize: .05*MediaQuery.of(context).size.width, color: Colors.white)
            ),
            new Text("my name is Peter Weyand.",
                style: new TextStyle(fontWeight: FontWeight.bold, fontSize: .06*MediaQuery.of(context).size.width, color: Colors.white)
            ),
          ],
        )
      ],
    );

    Widget Greeting2 = new Row(
      children: <Widget>[
          new Expanded(
            child: new Padding(
              padding: const EdgeInsets.fromLTRB(5.0, 5.0, 5.0, 5.0),
              child:  new Text("Let's talk about how I can make your business money.",
                style: new TextStyle(fontWeight: FontWeight.bold, fontSize: .075*MediaQuery.of(context).size.width, color: Colors.white)
                      ),
            )
          )
        ]
    );

    void _openAddEntryDialog() {
      Navigator.of(context).push(new MaterialPageRoute<Null>(
          builder: (BuildContext context) {
            return new AddEntryDialog();
          },
          fullscreenDialog: true
      ));
    }



    Widget dialogButton() {
      return new Align(
        alignment: const Alignment(0.0, -0.2),
        child: new ButtonBar(
          mainAxisSize: MainAxisSize.min,
          children: <Widget>[
            new RaisedButton(
              color: Colors.purple,
              child:
                  new Text("Click to connect.",
                      style: new TextStyle(fontWeight: FontWeight.bold, fontSize: .1*MediaQuery.of(context).size.width, color: Colors.white)
                  ),
              onPressed: () {
//                showDialog(
//                    context: context,
//                    child: popSimple
//                );
                _openAddEntryDialog();
              },
            )
          ]
        ),
      );
    }

    return new MaterialApp(
      title: title,
      theme: new ThemeData(
        primarySwatch: Colors.blue,
        primaryColor: Colors.black,
        backgroundColor: Colors.black,
      ),
      home: new Scaffold(
          resizeToAvoidBottomPadding: false,
        body: new Container(
          height: 0.4*MediaQuery.of(context).size.height,
          width: MediaQuery.of(context).size.width,
          decoration: new BoxDecoration(color: Colors.black),
          child: new Column(
            mainAxisSize: MainAxisSize.min,
            children: <Widget>[
              Greeting,
              Greeting2,
              new Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: <Widget>[
                  dialogButton()
                ],
              )
            ],
          ),
        )
      )
    );
  }
}

class AddEntryDialog extends StatefulWidget {
  @override
  AddEntryDialogState createState() => new AddEntryDialogState();
}

class AddEntryDialogState extends State<AddEntryDialog> {
  final TextEditingController _name = new TextEditingController();
  final TextEditingController _email = new TextEditingController();
  final TextEditingController _message = new TextEditingController();


  bool ToastMe = false;

  saveContact() async {

    print("inside saveContact");

    var url = 'https://f1utt3rshi.herokuapp.com/saveContact';

    http.post(url,  headers: {'Content-type': 'application/json'}, body: JSON.encode({'name': _name.text, 'email': _email.text, 'message': _message.text})).then((response) {
      print("Response status: ${response.statusCode}");
      print("Response body: ${response.body}");
    }).catchError((onError){
      print("Oh no there was an error: " + onError);
    });

  }


  @override
  Widget build(BuildContext context) {
    final mediaQuery = MediaQuery.of(context);

    Widget MediaHolder = new MediaQuery(
      data: mediaQuery.copyWith( viewInsets: EdgeInsets.zero ),
      child: new Scaffold(
        backgroundColor: Colors.black,
        body: new Column(
          crossAxisAlignment: CrossAxisAlignment.center,
          mainAxisAlignment: MainAxisAlignment.start,
          children: <Widget>[
            new Padding(
              padding: const EdgeInsets.all(15.0),
            ),
            new Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: <Widget>[
                new SizedBox(
                  height: .1*MediaQuery.of(context).size.height,
                  width: .8*MediaQuery.of(context).size.width,
                  child: new Card(
                    color: Colors.white,
                    child: new Padding(
                      padding: const EdgeInsets.all(10.0),
                      child: new TextField(
                        controller: _name,
                        decoration: new InputDecoration(
                          hintText: "What's your name?",
                        ),
                      ),
                    )
                  )
                ),
              ],
            ),
            new Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: <Widget>[
                new SizedBox(
                    height: .1*MediaQuery.of(context).size.height,
                    width: .8*MediaQuery.of(context).size.width,
                    child: new Card(
                        color: Colors.white,
                        child: new Padding(
                          padding: const EdgeInsets.all(10.0),
                          child: new TextField(
                            controller: _email,
                            decoration: new InputDecoration(
                              hintText: "What's your email?",
                            ),
                          ),
                        )
                    )
                ),
              ],
            ),
            new Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: <Widget>[
                new SizedBox(
                    height: .2*MediaQuery.of(context).size.height,
                    width: .8*MediaQuery.of(context).size.width,
                    child: new Card(
                        color: Colors.white,
                        child: new Padding(
                          padding: const EdgeInsets.all(10.0),
                          child: new TextField(
                            maxLines: 4,
                            controller: _message,
                            decoration: new InputDecoration(
                              hintText: "Write a message!",
                            ),
                          ),
                        )
                    )
                ),
              ],
            ),
            new Padding(
              padding: const EdgeInsets.all(15.0),
            ),
            new Stack(
              alignment: const Alignment(0.7, 0.6),
              children: <Widget>[
                new Image.asset(
                  'images/platypusimage.jpeg',
                  height: 0.3*MediaQuery.of(context).size.height,
                  width: MediaQuery.of(context).size.width,
                  alignment: Alignment.centerLeft,
                  fit: BoxFit.cover,
                ),
                new Container(
                  decoration: new BoxDecoration(
                    color: Colors.purple,
                    borderRadius: new BorderRadius.circular(25.0)
                  ),
                  child: new Padding(
                      padding: const EdgeInsets.all(5.0),
                      child: new Text("check out github.com/patientplatypus",
                          style: new TextStyle(color: Colors.white, fontWeight: FontWeight.bold, fontSize: .037*MediaQuery.of(context).size.width)),
                  )
                )
              ],
            ),
          ],
        )
      )
    );




    return new Scaffold(
      backgroundColor: Colors.black,
      appBar: new AppBar(
        backgroundColor: Colors.purple,
        title: const Text("Let's talk!"),
        actions: [
          new FlatButton(
              onPressed: () {
                saveContact();
                Navigator.pop(context);

                //TODO: Handle save
              },
              child: new Text('SAVE',
                  style: Theme
                      .of(context)
                      .textTheme
                      .subhead
                      .copyWith(color: Colors.white, fontWeight: FontWeight.bold))),
        ],
      ),
      body: MediaHolder,
    );
  }
}

//@override Widget build(BuildContext context) { final mediaQuery = MediaQuery.of(context); return new MediaQuery( data: mediaQuery.copyWith( viewInsets: EdgeInsets.zero ), child: new Scaffold( // usual stuff here ), );

//
//new TextField(
//controller: _controller,
//style: new TextStyle(color: Colors.white, ),
//decoration: new InputDecoration(
//hintText: "Let's connect!",
//),
//)


//Widget popSimple = new SimpleDialog(
//  contentPadding: new EdgeInsets.all(10.0),
//  children: <Widget>[
//    new Column(
//        mainAxisAlignment: MainAxisAlignment.start,
//        crossAxisAlignment: CrossAxisAlignment.center,
//        children: <Widget>[
//          new SizedBox(
//            height: .1*MediaQuery.of(context).size.height,
//            width: .6*MediaQuery.of(context).size.width,
//            child: new TextField(
//              controller: _name,
//              decoration: new InputDecoration(
//                hintText: "What's your name?",
//              ),
//            ),
//          ),
//          new SizedBox(
//            height: .1*MediaQuery.of(context).size.height,
//            width: .6*MediaQuery.of(context).size.width,
//            child: new TextField(
//              controller: _email,
//              decoration: new InputDecoration(
//                hintText: "What's your email?",
//              ),
//            ),
//          ),
//          new SizedBox(
//            height: .1*MediaQuery.of(context).size.height,
//            width: .6*MediaQuery.of(context).size.width,
//            child: new Container(
//            ),
//          ),
//        ]
//    ),
//  ],
//);