---
title: indexOf有趣的现象
date: 2016-06-18
tags: [Array]
categories: Dynamic
---

```javascript
    var person = {name: "wmsj"};
    var person2 = {name: "wmsj100"};
    var morePerson = [person,person2];
    morePerson.indexOf(person); //0
    morePerson.indexOf(person2);    //1
```

这个比较与意思，`morePerson`是一个数组，但是内部是俩个对象，而这俩个对象是有名字的，通过`indexOf`可以调用，但是通过`morePerson.person`或者`morePerson[person]`返回的都是`undefined`；所以比较怪；
