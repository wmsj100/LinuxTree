---
title: Date 类型
date: 2016-04-30
tags: [时间,JavaScript]
categories: Dynamic
---

要创建一个日期对象，使用 new 操作符和 Date 构造函数即可，如下所示。`var now = new Date();` 

在调用 Date 构造函数而不传递参数的情况下，新创建的对象自动获得当前日期和时间。如果想根据特定的日期和时间创建日期对象，必须传入表示该日期的毫秒数（即从 UTC 时间 1970 年 1 月 1 日午夜起至该日期止经过的毫秒数）。为了简化这一计算过程ECMAScript 提供了两个方法： Date.parse()和 Date.UTC() 。

其中， Date.parse() 方法接收一个表示日期的字符串参数，然后尝试根据这个字符串返回相应日期的毫秒数。

```javascript
Date.parse("2016-05-01")
1262304000000
```

Date.UTC() 方法同样也返回表示日期的毫秒数，但它与Date.parse() 在构建值时使用不同的信息。 Date.UTC() 的参数分别是年份、基于 0 的月份（一月是 0，二月是 1，以此类推）、月中的哪一天（1 到 31）、小时数（0 到 23）、分钟、秒以及毫秒数。在这些参数中，只有前两个参数（年和月）是必需的。如果没有提供月中的天数，则假设天数为 1；如果省略其他参数，则统统假设为 0。以下是两个使用 Date.UTC() 方法的例子：

```
// GMT 时间 2000 年 1 月 1 日午夜零时
var y2k = new Date(Date.UTC(2000, 0));
// GMT 时间 2005 年 5 月 5 日下午 5:55:55
var allFives = new Date(Date.UTC(2005, 4, 5, 17, 55, 55));
```

ECMAScript 5 添加了 Data.now() 方法，返回表示调用这个方法时的日期和时间的毫秒数。这个方法简化了使用 Data 对象分析代码的工作。

```javascript
//取得开始时间
var start = Date.now();
//调用函数
doSomething();
//取得停止时间
var stop = Date.now(),
result = stop – start;
```

支持 Data.now() 方法的浏览器包括 IE9+、Firefox 3+、Safari 3+、Opera 10.5 和 Chrome。在不支
持它的浏览器中，使用+操作符把 Data 对象转换成字符串，也可以达到同样的目的。

```javascript
//取得开始时间
var start = +new Date();
//调用函数
doSomething();
//取得停止时间
var stop = +new Date(),
result = stop - start;
```

```javascript
var date1 = new Date(2007, 0, 1); //"January 1, 2007"
var date2 = new Date(2007, 1, 1); //"February 1, 2007"
alert(date1 < date2); //true
alert(date1 > date2); //false
```





