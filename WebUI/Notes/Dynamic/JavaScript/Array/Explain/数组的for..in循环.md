---
title: 数组的for in循环
date: 2016-06-08
tags: [Array]
categories: Dynamic
---

`in`运算符检查某个键名是否存在，适用于对象，也适用于数组。

```javascript
var a = [1,2,3,4];
2 in a; //true;
"2" in a;   //true;
5 in a; //true;
```
由于键名都是字符串，所以数值2会自动转换为字符串。

```javascript
    var a = [1, 2, 3, 4];
    for (var i in a) {
        console.log(a[i])
    }
```

对于数组使用`for in`循环需要注意的是数组内部的属性也会被遍历，如下

```javascript
var a = [1, 2, 3, 4];
    a["age"] = 10;
    a["name"] = "wmsj";
    for (var i in a) {
        console.log(i,a[i]) 
    }
```

但是使用`for length`或者是`forEach`就没有这个问题。所以除非是确定数组内部没有绑定属性，否则不建议对数组使用`for in`循环。

还有一直`while`循环，它的逆序遍历比较巧妙，方法是阮一峰想到的。
逆序循环的性能优化是编程语言的常识，并不是阮一峰想到的。

```javascript
    var i = a.length;
    while(i--){
        console.log(i,a[i]);
    }
```
进行`while`判断的时候`i=4`，然后调用的时候`i`已经变为`3`了。当`i = 0`的时候，`while`判断为`false`。退出循环。
