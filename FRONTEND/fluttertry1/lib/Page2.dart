
import 'package:flutter/material.dart';


class MyPage2 extends StatefulWidget {
  const MyPage2(this.title);

  final String title;

  @override
  MyPage2Home createState() => new MyPage2Home(title);
}


class MyPage2Home extends State<MyPage2> {
  MyPage2Home(this.title);
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
              new Text("page 2")
            ],
          ),
        )
    );
  }
}