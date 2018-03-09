
import 'package:flutter/material.dart';


class MyPage1 extends StatefulWidget {
  const MyPage1(this.title);

  final String title;

  @override
  MyPage1Home createState() => new MyPage1Home(title);
}


class MyPage1Home extends State<MyPage1> {
  MyPage1Home(this.title);
  final String title;

  @override
  Widget build(BuildContext context) {
    return new MaterialApp(
      title: title,
      theme: new ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: new Container(
        child: new Row(
          children: <Widget>[
            new Text("page 1")
          ],
        ),
      )
    );
  }
}