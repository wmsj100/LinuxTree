---
title: 函数的apply与call
date: 2016-06-18
tags: [Function]
categories: Dynamic
---

```javascript
    function sum(num1, num2) {
        return num1 + num2;
    }

    function applySum1(num1, num2) {
        return sum.apply(this, arguments);
    }

    function applySum2(num1, num2) {
        return sum.apply(this, [num1, num2]);
    }
    applySum1(10,20);   //30
    applySum2(10,203);  //213
```

因为函数`applySum1` 和 `applySum2`都是在全局环境中调用的,所以俩个`this`都指向`window`;

`call`和`apply`的真正作用是可以扩展函数赖以运行的作用域;

```javascript
    var color = 'red';
    var o = {"color": "blue"};
    function say(){
        return this.color;
    }
    say();  //"red"
say.call(o);    //"blue"
```

`bind` -- 创建函数的实例,

```javascript
var a = say.bind(o);
a();    "blue"
```

