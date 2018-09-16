---
title: Number 数值类型
date: 2016-04-30
tags: [数值,JavaScript]
categories: Dynamic
---

可以为 toString() 方法传递一个表示基数的参数

```javascript
var num = 10;
alert(num.toString()); //"10"
alert(num.toString(2)); //"1010"
alert(num.toString(8)); //"12"
alert(num.toString(10)); //"10"
alert(num.toString(16)); //"a"
```

 toFixed() 方法会按照指定的小数位返回数值的字符串表示:

```javascript
var num = 10;
var num1 = 10.005;
num.toFixed(2);	//"10.00";
num1.toFixed(2);	//"10.01";
```

` toPrecision()`  会根据要处理的数值决定到底是调用` toFixed() ` 还是调用 `toExponential() ` 。
而这三个方法都可以通过向上或向下舍入，做到以最准确的形式来表示带有正确小数位的值。

```javascript
var num = 99;
alert(num.toPrecision(1)); //"1e+2"
alert(num.toPrecision(2)); //"99"
alert(num.toPrecision(3)); //"99.0"
```

