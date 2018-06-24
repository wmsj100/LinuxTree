---
title: Number类型
date: 2016-06-18
tags: [Number]
categories: Dynamic
---

`number` -- 类型也是重写了`toStrint`/ `valueOf`/ `toLocalString`;
`toString` -- 可以传入数值参数,把数字转换为对应进制的字符串值;

```javascript
var a = 1234;
a.toString(2);  //"10011010010"
```

`toFixed` -- 把数字转换为字符串,可以传入参数说明小数的位数;如果数值本身小数位数比参数的值大,那么就会进行四舍五入;这个特性使得它多用于处理货币,标准最多支持的小数位数是`20`,但浏览器可能支持更多.

```javascript
var a = 1234;
a.toFixed(2);   //"1234.00"
var b = 12.1234;
b.toFixed(2);   //12.12
```

`toExponential` -- 使用科学计数法表示数值,参数为小数位数;
`toPrecision` -- 更智能化的科学计数法,会自动判断要使用那种方式合理的展示数值;

```javascript
var a=1234;
1234
a.toExponential(2);
"1.23e+3"
a.toPrecision(2);
"1.2e+3"
a.toFixed(2);
"1234.00"
```

不建议直接实例化`Number`,因为判断值类型时候会有问题,

对于基本类型值,都直接使用字面量形式创建值,而不是使用实例化.