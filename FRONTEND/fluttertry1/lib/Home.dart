
import 'package:flutter/material.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart';
import 'package:flutter/animation.dart';
//import 'main.dart';

typedef bool SunCallBack(bool);
typedef String DateCallBack(bool);

class HeaderPage extends StatefulWidget {

  const HeaderPage({
  Key key,
  this.goToVar, this.sunString, this.sunCallBack, this.dateCallBack
  }) : super(key: key);

  final String goToVar;
  final String sunString;
  final SunCallBack sunCallBack;
  final DateCallBack dateCallBack;
//  final VoidCallback SunCallBack;


  @override
  HeaderPageState createState() => new HeaderPageState();
}


class HeaderPageState extends State<HeaderPage>{

  var sunIsShining = true;
  String dateButtonText;


  @override
  void initState() {
    super.initState();
    dateButtonText = "March " + widget.sunString + "th";
  }

  iterateDate(){
    if (widget.sunString=="17"){
      widget.dateCallBack("9");
      var intNum = 9;
      dateButtonText = "March " + intNum.toString() + "th";
      setState(() {dateButtonText = dateButtonText;});
    }else{
      var intNum = int.parse(widget.sunString);
      intNum++;
      print("value of intNum.toString in iterateDate: " + intNum.toString());
      widget.dateCallBack(intNum.toString());
      dateButtonText = "March " + intNum.toString() + "th";
      setState(() {dateButtonText = dateButtonText;});
    }
  }

  sunToggle(value){
    print("inside sunToggle && sunIsShining: " + sunIsShining.toString());
    sunIsShining = value;
    setState(() {sunIsShining = value;});
    widget.sunCallBack(value);
  }

  @override
  Widget build(BuildContext context) {

    Widget SunIcon(){
      if (sunIsShining){
        return new Icon(FontAwesomeIcons.sun, color: Colors.yellow,
            size: 50.0);
      }else{
        return new Icon(FontAwesomeIcons.sun, color: Colors.purple,
            size: 50.0);
      }
    }

    Widget StarsIcon(){
      if (sunIsShining){
        return new Icon(FontAwesomeIcons.moon, color: Colors.purple,
            size: 50.0);
      }else{
        return new Icon(FontAwesomeIcons.moon, color: Colors.yellow,
            size: 50.0);
      }
    }


    Widget Page4Val(){
      return new Container(
        child: new SizedBox(
          height: 0.4*MediaQuery.of(context).size.height,
          width: 0.5*MediaQuery.of(context).size.width,
          child: new Scaffold(
            body: new Container(
              decoration: new BoxDecoration(
                gradient: new LinearGradient(
                  begin: const Alignment(-1.0, 1.0),
                  end: const Alignment(1.0, -1.0),
                  colors: <Color>[
                    const Color(0xfffa9a37),
                    const Color(0xff73497a)
                  ],
                ),
              ),
              child: new Column(
                mainAxisAlignment: MainAxisAlignment.start,
                children: <Widget>[
                  new Padding(
                    padding: const EdgeInsets.all(15.0),
                  ),
                  new Row(
                    children: <Widget>[
                      new Flexible(
                        child: new Padding(
                          padding: const EdgeInsets.fromLTRB(15.0, 0.0, 0.0, 0.0),
                          child:  new CloudAnimation1()
                        )
                      ),
                      new Flexible(
                          flex: 2,
                          child: new Text("   ENGINEER @",
                              style: new TextStyle(fontWeight: FontWeight.bold, fontSize: 18.0, color: Colors.white))
                      )
                    ],
                  ),
                  new Row(
                      mainAxisAlignment: MainAxisAlignment.center,
                      mainAxisSize: MainAxisSize.max,
                      children: <Widget>[
                        new Image.asset(
                          'images/oracle-logo-transparent.png',
                          height: 0.04*MediaQuery.of(context).size.height,
                          width: 0.5*MediaQuery.of(context).size.width,
                          alignment: Alignment.center,
                          fit: BoxFit.cover,
                        ),
                      ]
                  ),
                  new Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: <Widget>[
                      new Expanded(
                        child: new Padding(padding: const EdgeInsets.fromLTRB(15.0, 15.0, 15.0, 0.0),
                              child: new Text("Making Cloud",
                                  style: new TextStyle(fontWeight: FontWeight.bold, fontSize: 20.0, color: Colors.white))
                        ),
                      ),
                    ]
                  ),
                  new Row(
                      mainAxisAlignment: MainAxisAlignment.center,
                      children: <Widget>[
                        new Expanded(
                          child: new Padding(padding: const EdgeInsets.fromLTRB(15.0, 0.0, 15.0, 0.0),
                              child: new Text("Happen",
                                  style: new TextStyle(fontWeight: FontWeight.bold, fontSize: 35.0, color: Colors.white))
                          ),
                        ),
                      ]
                  ),
                  new Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: <Widget>[
                      new Expanded(
                        child: new Padding(padding: const EdgeInsets.fromLTRB(15.0, 10.0, 15.0, 0.0),
                            child: new CogAnimation1()
                        ),
                      )
                    ],
                  ),
                ],
              ),
            ),
          ),
        ),
      );
    }

    Widget Page3Val(){
      return new Container(
        child: new SizedBox(
          height: 0.4*MediaQuery.of(context).size.height,
          width: 0.5*MediaQuery.of(context).size.width,
          child: new Scaffold(
            body: new Container(
              decoration: new BoxDecoration(
                gradient: new LinearGradient(
                  begin: const Alignment(-1.0, 1.0),
                  end: const Alignment(1.0, -1.0),
                  colors: <Color>[
                    const Color(0xfffa9a37),
                    const Color(0xff73497a)
                  ],
                ),
              ),
              child: new Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: <Widget>[
                  new Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    mainAxisSize: MainAxisSize.max,
                    children: <Widget>[
                      new Flexible(
                          child: new RawMaterialButton(
                              onPressed: () => sunToggle(true),
                              child: SunIcon()
                          )
                      ),
                      new Flexible(
                          child: new RawMaterialButton(
                              onPressed: () => sunToggle(false),
                              child: StarsIcon()
                          )
                      ),
                    ],
                  ),
                  new Row(
                    children: <Widget>[
                      new Expanded(
                          child: new FlatButton(
                              onPressed: () => iterateDate(),
                              child: new Text(this.dateButtonText,
                                  style: new TextStyle(fontWeight: FontWeight.bold, fontSize: 25.0, color: Colors.white))
                          )
                      )
                    ],
                  )
                ],
              ),
            ),
          ),
        ),
      );
    }

    Widget ButtonGrad(){
      if (widget.goToVar=="/page3") {
        return Page3Val();
      }else if (widget.goToVar=="/page4"){
        return Page4Val();
      }else{
        return new Container();
      }
    }


    return new MaterialApp(
      theme: new ThemeData(
        primarySwatch: Colors.blue,
      ),
      home:  new Row(
          children: <Widget>[
            new Column(
              children: <Widget>[
                new Image.asset(
                  'images/sxsw.png',
                  height: 0.1*MediaQuery.of(context).size.height,
                  width: 0.5*MediaQuery.of(context).size.width,
                  alignment: Alignment.centerLeft,
                  fit: BoxFit.cover,
                ),
                new Image.asset(
                  'images/avatar.jpg',
                  height: 0.3*MediaQuery.of(context).size.height,
                  width: 0.5*MediaQuery.of(context).size.width,
                  alignment: Alignment.centerLeft,
                  fit: BoxFit.cover,
                ),
              ],
            ),
            new Column(
              children: <Widget>[
                ButtonGrad()
              ],
            )
          ]
      ),
    );
  }
}

class CogAnimation1 extends StatefulWidget {
  @override
  CogAnimation1State createState() => new CogAnimation1State();
}


class CogAnimation1State extends State<CogAnimation1> with SingleTickerProviderStateMixin {
  Animation<double> animation;
  AnimationController controller;

  initState() {
    super.initState();
    controller = new AnimationController(
        duration: const Duration(milliseconds: 2000), vsync: this);
    animation = new Tween(begin: 0.0, end: 1.0).animate(controller);

    animation.addStatusListener((status) {
      if (status == AnimationStatus.completed) {
        controller.reset();
        controller.forward();
      } else if (status == AnimationStatus.dismissed) {
        controller.reset();
        controller.forward();
      }
    });

    controller.forward();
  }


  @override
  Widget build(BuildContext context) {
    return new Container(
      child: new MyAnimatedCog(
        animation: animation,
        icon: FontAwesomeIcons.cog,
      ),
    );
  }

  dispose() {
    controller.dispose();
    super.dispose();
  }

}

class MyAnimatedCog extends AnimatedWidget {
  MyAnimatedCog({Key key, Animation<double> animation, this.icon}) :super(key: key, listenable: animation);
  final IconData icon;

  @override Widget build(BuildContext context) {
    final Animation<double> animation = listenable;
//    return new Icon(icon, color: animation.value, size: 40.0);
    return new RotationTransition(
      key: key,
      turns: animation,
      child:
        new Icon(icon, color: Colors.yellow, size: 50.0)
    );
  }
}


class CloudAnimation1 extends StatefulWidget {

  @override
  CloudAnimation1State createState() => new CloudAnimation1State();
}

class CloudAnimation1State extends State<CloudAnimation1> with SingleTickerProviderStateMixin {

  Animation<Color> animation;
  AnimationController controller;

  initState() {
    super.initState();
    controller = new AnimationController(
        duration: const Duration(milliseconds: 2000), vsync: this);
    final Animation curve = new CurvedAnimation(parent: controller, curve: Curves.easeInOut);
    animation = new ColorTween(begin: Colors.orange, end: Colors.purple).animate(curve);


    animation.addStatusListener((status) {
      if (status == AnimationStatus.completed) {
        controller.reverse();
      } else if (status == AnimationStatus.dismissed) {
        controller.forward();
      }
    });
    controller.forward();
  }

  @override
  Widget build(BuildContext context) {
    return new Container(
      child: new MyAnimatedCloud(
        animation: animation,
        icon: FontAwesomeIcons.cloud,
      ),
    );
  }

  dispose() {
    controller.dispose();
    super.dispose();
  }

}

class MyAnimatedCloud extends AnimatedWidget {
  MyAnimatedCloud({Key key, Animation<Color> animation, this.icon}) :super(key: key, listenable: animation);
  final IconData icon;

  @override Widget build(BuildContext context) {
    final Animation<Color> animation = listenable;
    return new Icon(icon, color: animation.value, size: 40.0);
  }
}