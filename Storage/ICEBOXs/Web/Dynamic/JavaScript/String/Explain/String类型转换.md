---
title: String类型转换
date: 2016-04-28
tags: [字符串,JavaScript]
categories: Dynamic
---

# String类型转换

## 字符串特点

ECMAScript 中的字符串是不可变的，也就是说，字符串一旦创建，它们的值就不能改变。要改变某个变量保存的字符串，首先要销毁原来的字符串，然后再用另一个包含新值的字符串填充该变量，

```javascript
var lang = "Java";
lang = lang + "Script";
```

以上示例中的变量 lang 开始时包含字符串 "Java" 。而第二行代码把 lang 的值重新定义为 "Java"
与 "Script" 的组合，即 "JavaScript" 。实现这个操作的过程如下：首先创建一个能容纳 10 个字符的
新字符串，然后在这个字符串中填充 "Java" 和 "Script" ，最后一步是销毁原来的字符串 "Java" 和字符串 "Script" ，因为这两个字符串已经没用了。这个过程是在后台发生的，而这也是在某些旧版本的浏览器（例如版本低于 1.0 的 Firefox、IE6 等）中拼接字符串时速度很慢的原因所在。但这些浏览器后来的版本已经解决了这个低效率问题。

## 转换为字符串

要把一个值转换为一个字符串有两种方式。第一种是使用几乎每个值都有的 toString() 方法（第5 章将讨论这个方法的特点）。这个方法唯一要做的就是返回相应值的字符串表现。来看下面的例子：

```javascript
var age = 11;
var ageAsString = age.toString(); // 字符串"11"
var found = true;
var foundAsString = found.toString(); // 字符串"true"
```

​	数值、布尔值、对象和字符串值（没错，每个字符串也都有一个 toString() 方法，该方法返回字符串的一个副本）都有 toString() 方法。但 null 和 undefined 值没有这个方法。
​	多数情况下，调用 toString() 方法不必传递参数。但是，在调用数值的 toString() 方法时，可以传递一个参数：输出数值的基数。默认情况下， toString() 方法以十进制格式返回数值的字符串表示。而通过传递基数， toString() 可以输出以二进制、八进制、十六进制，乃至其他任意有效进制格式表示的字符串值。下面给出几个例子：
```javascript
var num = 10;
alert(num.toString()); // "10"
alert(num.toString(2)); // "1010"
alert(num.toString(8)); // "12"
alert(num.toString(10)); // "10"
alert(num.toString(16)); // "a"
```

​	通过这个例子可以看出，通过指定基数， toString() 方法会改变输出的值。而数值 10 根据基数的不同，可以在输出时被转换为不同的数值格式。注意，默认的（没有参数的）输出值与指定基数 10 时
的输出值相同。

在不知道要转换的值是不是 null 或 undefined 的情况下，还可以使用转型函数 String() ，这个函数能够将任何类型的值转换为字符串。 String() 函数遵循下列转换规则：
  如果值有 toString() 方法，则调用该方法（没有参数）并返回相应的结果；
  如果值是 null ，则返回 "null" ；
  如果值是 undefined ，则返回 "undefined" 。

```javascript
String(null)	//"null"
String(undefined)	//"undefined"
String(true)	//"true"
```

​	这里先后转换了 4 个值：数值、布尔值、 null 和 undefined 。数值和布尔值的转换结果与调用toString() 方法得到的结果相同。因为 null 和 undefined 没有 toString() 方法，所以 String()函数就返回了这两个值的字面量。

​	要把某个值转换为字符串，可以使用加号操作符和一个字符串("")加在一起。

```javascript
23+""	//"23"
```











