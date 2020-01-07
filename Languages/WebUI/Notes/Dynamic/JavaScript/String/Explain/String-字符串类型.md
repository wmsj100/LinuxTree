---
title: String 字符串类型
date: 2016-05-01
tags: [字符串,JavaScript]
categories: Dynamic
---

String 类型的每个实例都有一个 length 属性，表示字符串中包含多个字符。

## 字符方法

两个用于访问字符串中特定字符的方法是： charAt() 和 charCodeAt() 。这两个方法都接收一个参数，即基于 0 的字符置。其中， charAt() 方法以单字符字符串的形式返回给定位置的那个字符；如果你想得到的不是字符而是字符编码，那么就要像下面这样使用 charCodeAt() 了

```javascript
a="hello world"
a.charAt(1)	//"e"
a.charCodeAt(1)	//101
```

ECMAScript 5还定义了另一个访问个别字符的方法。在支持此方法的浏览器中，可以使用方括号加数字索引来访问字符串中的特定字符，如下面的例子所示

```javascript
var stringValue = "hello world";
alert(stringValue[1]); //"e"
```

## 字符串操作方法

 `concat() ` 用于将一或多个字符串拼接起来，返回拼接得到的新字符串。`concat()` 方法可以接受任意多个参数，也就是说可以通过它拼接任意多个字符串。`concat()` 不会改变原字符串；

```javascript
var stringValue = "hello ";
var result = stringValue.concat("world", "!");
```

虽然 `concat()`  是专门用来拼接字符串的方法，但实践中使用更多的还是加号操作符（+）。而且，使用加号操作符在大多数情况下都比使用` concat()` 方法要简便易行（特别是在拼接多个字符串的情况下）。

ECMAScript还提供了三个基于子字符串创建新字符串的方法： slice() 、 substr() 和 substring() 。这三个方法都会返回被操作字符串的一个子字符串，而且也都接受一或两个参数。第一个参数指定子字符串的开始位置，第二个参数（在指定的情况下）表示子字符串到哪里结束。具体来说， slice() 和substring() 的第二个参数指定的是子字符串最后一个字符后面的位置。而 substr() 的第二个参数指

定的则是返回的字符个数。如果没有给这些方法传递第二个参数，则将字符串的长度作为结束位置。与concat() 方法一样， slice() 、 substr() 和 substring() 也不会修改字符串本身的值——它们只是返回一个基本类型的字符串值，对原始字符串没有任何影响。

## 3. 字符串位置方法

有两个可以从字符串中查找子字符串的方法： indexOf() 和 lastIndexOf() 。这两个方法都是从一个字符串中搜索给定的子字符串，然后返子字符串的位置（如果没有找到该子字符串，则返回 -1 ）。这两个方法的区别在于： indexOf() 方法从字符串的开头向后搜索子字符串，而 lastIndexOf() 方法是从字符串的末尾向前搜索子字符串。

```javascript
var stringValue = "hello world";
alert(stringValue.indexOf("o")); //4
alert(stringValue.lastIndexOf("o")); //7
```

这两个方法都可以接收可选的第二个参数，表示从字符串中的哪个位置开始搜索。换句话说，indexOf() 会从该参数指定的位置向后搜索，忽略该位置之前的所有字符；而 lastIndexOf() 则会从指定的位置向前搜索，忽略该位置之后的所有字符。看下面的例子。

```javascript
var stringValue = "hello world";
alert(stringValue.indexOf("o", 6)); //7
alert(stringValue.lastIndexOf("o", 6)); //4
```

## 4.  trim() 方法

ECMAScript 5 为所有字符串定义了 trim() 方法。这个方法会创建一个字符串的副本，删除前置及后缀的所有空格，然后返回结果。

```javascript
var stringValue = " hello world ";
var trimmedStringValue = stringValue.trim();
alert(stringValue); //" hello world "
alert(trimmedStringValue); //"hello world"
```

## 6. 字符串的模式匹配方法

String 类型定义了几个用于在字符串中匹配模式的方法。第一个方法就是 match() ，在字符串上调用这个方法，本质上与调用 RegExp 的 exec() 方法相同。 match() 方法只接受一个参数，要么是一个正则表达式，要么是一个 RegExp 对象。

替换字符串--`replace(/.at/g,"wmsj");

```javascript
function htmlEscape(text){
return text.replace(/[<>"&]/g, function(match, pos, originalText){
switch(match){
case "<":
return "&lt;";
case ">":
return "&gt;";
case "&":
return "&amp;";
case "\"":
return "&quot;";
}
});
}
alert(htmlEscape("<p class=\"greeting\">Hello world!</p>"));
//&lt;p class=&quot;greeting&quot;&gt;Hello world!&lt;/p&gt;
```

最后一个与模式匹配有关的方法是 split() ，这个方法可以基于指定的分隔符将一个字符串分割成多个子字符串，并将结果放在一个数组中。分隔符可以是字符串，也可以是一个 RegExp 对象（这个方法不会将字符串看成正则表达式）。 split() 方法可以接受可选的第二个参数，用于指定数组的大小，

 fromCharCode() 方法-

```javascript
String.fromCharCode(104, 101, 108, 108, 111)
//"hello";
```







