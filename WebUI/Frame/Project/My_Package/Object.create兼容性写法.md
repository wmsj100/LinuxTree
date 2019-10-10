---
title: 用Object.create来创建对象，及其兼容性写法
date: 2016-05-29
tags: [兼容,封装]
categories: Dynamic
---

```javascript
Object.create = null;

function create(obj) {
  if (typeof obj != "object") {
    throw TypeError("输入值必须为对象！")
  }
  var proto = new Object();
  if (typeof Object.create === "function") {
    proto = Object.create(obj);
  } else {
    function temp() {};
    temp.prototype = obj;
    proto = new temp();
    temp.prototype = null; //清除不用的引用
  }
  if (arguments.length > 1) {
    var Properties = arguments[1];
    var hasOwn = Object.prototype.hasOwnProperty;
    for (var key in Properties) {
      if (hasOwn.call(Properties, key)) { //这个hasOwn用的特别的巧妙
        proto[key] = Properties[key]["value"];
      }
    }
  }
  return proto;
}
```