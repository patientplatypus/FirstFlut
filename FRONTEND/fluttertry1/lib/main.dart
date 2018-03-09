import 'package:flutter/material.dart';
import 'package:flutter/animation.dart';
import 'package:flutter/scheduler.dart';
import 'Page1.dart';
import 'Page2.dart';
import 'Page3.dart';
import 'Page4.dart';
import 'Home.dart';


void main() => runApp(new MyApp());

class MyApp extends StatelessWidget {
  // This widget is the root of your application.

  @override
  Widget build(BuildContext context) {
    return new MaterialApp(
      title: 'Flutter Demo',
      theme: new ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: new MyNavigationHolder(title: 'Flutter Demo Home Page')
    );
  }
}

class MyNavigationHolder extends StatefulWidget {
  MyNavigationHolder({Key key, this.title}) : super(key: key);
  final String title;

  @override
  NavigationState createState() => new NavigationState();
}

class NavigationState extends State<MyNavigationHolder> {
  var goToPass = "/page4";
  bool sunBool = true;
  String sunString = "9";

  assignPass(page){
    print("inside assignPass");
    print("value of page: " + page);
//    goToPass = page;
    setState(() {goToPass = page;});
  }

  @override
  Widget build(BuildContext context) {

    Widget HeaderConfig(){
      return new HeaderPage(goToVar: goToPass,
          sunString: sunString,
          sunCallBack: (value){setState(() {sunBool = value;});},
          dateCallBack: (value){setState(() {sunString = value;});});
    }

    Widget Card1 = new Container(
        child: new SizedBox(
            height: 0.1 * MediaQuery
                .of(context)
                .size
                .height,
            width: 0.5 * MediaQuery
                .of(context)
                .size
                .width,
            child: new RawMaterialButton(
                onPressed: () => assignPass("/page1"),
                fillColor: Colors.black,
                splashColor: Colors.black,
                highlightColor: Colors.black,
                child: new Card(
                    color: Colors.black,
                    child: new Column(
                      children: <Widget>[
                        new Expanded(child: new Icon(
                            Icons.home, color: Colors.white, size: 50.0))
                      ],
                    )
                )
            )
        )
    );

    Widget Card2 = new Container(
        child: new SizedBox(
            height: 0.1 * MediaQuery
                .of(context)
                .size
                .height,
            width: 0.5 * MediaQuery
                .of(context)
                .size
                .width,
            child: new RawMaterialButton(
                onPressed: () => assignPass("/page2"),
                fillColor: Colors.black,
                splashColor: Colors.black,
                highlightColor: Colors.black,
                child: new Card(
                    color: Colors.black,
                    child: new Column(
                      children: <Widget>[
                        new Expanded(child: new Icon(
                            Icons.calendar_today, color: Colors.white,
                            size: 50.0))
                      ],
                    )
                )
            )
        )
    );


    Widget Card3 = new Container(
        child: new SizedBox(
            height: 0.2 * MediaQuery
                .of(context)
                .size
                .height,
            width: 0.5 * MediaQuery
                .of(context)
                .size
                .width,
            child: new RawMaterialButton(
                onPressed: () => assignPass("/page3"),
                fillColor: Colors.black,
                splashColor: Colors.black,
                highlightColor: Colors.black,
                child: new Card(
                    color: Colors.black,
                    child: new Column(
                      children: <Widget>[
                        new Expanded(child: new Icon(
                            Icons.format_list_numbered, color: Colors.white,
                            size: 50.0))
                      ],
                    )
                )
            )
        )
    );

    Widget Card4 = new Container(
        child: new SizedBox(
            height: 0.2 * MediaQuery
                .of(context)
                .size
                .height,
            width: 0.5 * MediaQuery
                .of(context)
                .size
                .width,
            child: new RawMaterialButton(
                onPressed: () => assignPass("/page4"),
                fillColor: Colors.black,
                splashColor: Colors.black,
                highlightColor: Colors.black,
                child: new Card(
                    color: Colors.black,
                    child: new Column(
                      children: <Widget>[
                        new Expanded(child: new Icon(
                            Icons.supervised_user_circle, color: Colors.white,
                            size: 50.0))
                      ],
                    )
                )
            )
        )
    );

    return new MaterialApp(
        home: new Scaffold(
            body: new Column(
                mainAxisSize: MainAxisSize.min,
                children: <Widget>[
                  new Flexible(
                    child: HeaderConfig()
                  ),
                  new Flexible(
                    child: new RouterClass(goTo: goToPass, sunBool: sunBool, sunString: sunString)
                  ),
//                  new Row(
//                    children: <Widget>[
//                      Card1,
//                      Card2
//                    ],
//                  ),
                  new Row(
                    children: <Widget>[
                      Card3,
                      Card4
                    ],
                  )
                ]
            )
        )
    );
  }
}

class RouterClass extends StatelessWidget{
  const RouterClass({
    Key key,
    this.goTo,
    this.sunBool,
    this.sunString
  }) : super(key: key);

  final String goTo;
  final bool sunBool;
  final String sunString;

  @override
  Widget build(BuildContext context) {
    if(this.goTo=="/page1"){
      return new MyPage1("Page1");
    }else if(this.goTo =="/page2"){
      return new MyPage2("Page2");
    }else if(this.goTo =="/page3"){
      return new MyPage3("Page3", this.sunBool, this.sunString);
    }else if (this.goTo =="/page4"){
      return new MyPage4("Page4");
    }else{
      return null;
    }
  }
}


//class RouterClass extends StatefulWidget{
//    const RouterClass({
//    Key key,
//    this.goTo
//  }) : super(key: key);
//
//  final String goTo;
//
//  initState(){
//   print("hello there RouterClass!");
//  }
//
//  RouterClassState createState() => new RouterClassState();
//}
//
//class RouterClassState extends State<RouterClass>{
//
//  String localGoTo;
//
//  @override
//  void didUpdateWidget(RouterClass oldWidget) {
//    super.didUpdateWidget(oldWidget);
//    if (oldWidget.goTo!=widget.goTo){
//      print("inside didUpdateWidget && localGoTo: " + localGoTo);
//      localGoTo = widget.goTo;
//    }
//  }
//
//  @override
//  void initState() {
//    super.initState();
//    print("value of widget.goTo: " + widget.goTo);
//    localGoTo = widget.goTo;
//  }
//
//  @override
//  Widget build(BuildContext context) {
//    print("this.goTo"+ localGoTo);
//    if(localGoTo=="/page1"){
//      return new MyPage1("Page1");
//    }else if(localGoTo =="/page2"){
//      return new MyPage2("Page2");
//    }else if(localGoTo =="/page3"){
//      return new MyPage3("Page3");
//    }else if (localGoTo =="/"){
//      return new MyHomePage("Home");
//    }else{
//      return null;
//    }
//  }
//}

//new RouterClassInherit(
//goTo: goToPass,
//child: const RouterClass()),

//class RouterClassInherit extends InheritedWidget{
//
//  const RouterClassInherit({
//    Key key,
//    this.goTo,
//    Widget child}) : super(key: key, child: child);
//
//  final String goTo;
//
//  @override
//  bool updateShouldNotify(RouterClassInherit old) {
//    return this.goTo != old.goTo;
//  }
//
//  static RouterClassInherit of(BuildContext context) {
//    return context.inheritFromWidgetOfExactType(RouterClassInherit);
//  }
//}
//
//class RouterClass extends StatelessWidget{
//
//  const RouterClass();
//
//  @override
//  Widget build(BuildContext context) {
//    final inheritWidget = RouterClassInherit.of(context);
//    print("this.goTo"+ inheritWidget.goTo);
//    if(inheritWidget.goTo=="/page1"){
//      return new MyPage1("Page1");
//    }else if(inheritWidget.goTo=="/page2"){
//      return new MyPage2("Page2");
//    }else if(inheritWidget.goTo=="/page3"){
//      return new MyPage3("Page3");
//    }else if (inheritWidget.goTo=="/"){
//      return new MyHomePage("Home");
//    }else{
//      return null;
//    }
//  }
//}

//class RouterClass extends StatefulWidget{
//
//  const RouterClass({
//    Key key,
//    this.goTo
//  }) : super(key: key);
//
//  final String goTo;
//
//  initState(){
//   print("hello there RouterClass!");
//  }
//
//  RouterClassState createState() => new RouterClassState();
//
//}
//
//class RouterClassState extends State<RouterClass>{
//
//  @override
//  void initState() {
//    super.initState();
//    print("value of widget.goTo: " + widget.goTo);
//  }
//
//  @override
//  Widget build(BuildContext context) {
//    print("this.goTo"+ widget.goTo);
//    if(widget.goTo=="/page1"){
//      return new MyPage1("Page1");
//    }else if(widget.goTo=="/page2"){
//      return new MyPage2("Page2");
//    }else if(widget.goTo=="/page3"){
//      return new MyPage3("Page3");
//    }else if (widget.goTo=="/"){
//      return new MyHomePage("Home");
//    }else{
//      return null;
//    }
//  }
//}

//class RouterClass extends StatefulWidget{
////  RouterClass({Key key, this.goTo}) : super(key: key);
//
//  const RouterClass({
//    Key key,
//    this.goTo
//  }) : super(key: key);
//
//  final String goTo;
//
//  @override
//  RouterClassState createState() => new RouterClassState();
//}
//
//class RouterClassState extends State<RouterClass>{
//
////  const RouterClassState(this.goTo);
////
////  final String goTo;
//
//  static const Page1Title = "Page1";
//  static const Page2Title = "Page2";
//  static const Page3Title = "Page3";
//
////  const RouterClass(this.goTo);
////  final String goTo;
//  initState() {
//    super.initState();
//    print("inside initState!~");
//    print(widget.goTo);
//  }
//
//  @override
//  Widget build(BuildContext context) {
////    SchedulerBinding.instance.addPostFrameCallback((_) {
////      Navigator.of(context).pushNamed(goTo);
////    });
//    return new MaterialApp(
//        title: 'Flutter Demo',
//        routes: <String, WidgetBuilder> {
//          '/': (BuildContext context) => new MyHomePage("Home"),
//          '/page1': (BuildContext context) => new MyPage1(Page1Title),
//          '/page2': (BuildContext context) => new MyPage2(Page2Title),
//          '/page3': (BuildContext context) => new MyPage3(Page3Title),
//        },
//        theme: new ThemeData(
//          primarySwatch: Colors.blue,
//        ),
//    );
//  }
//}
