---
title: RegExp 类型
date: 2016-04-30
tags: [正则,JavaScript]
categories: Dynamic
---

与其他语言中的正则表达式类似，模式中使用的所有元字符都必须转义。正则表达式中的元字符包括：`( [ { \ ^ $ | ) ? * + .]}` 

```javascript
/*
* 匹配第一个"bat"或"cat"，不区分大小写
*/
var pattern1 = /[bc]at/i;
/*
* 与 pattern1 相同，只不过是使用构造函数创建的
*/
var pattern2 = new RegExp("[bc]at", "i");
```

```javascript
var text = "mom and dad and baby";
var pattern = /mom( and dad( and baby)?)?/gi;
var matches = pattern.exec(text);
alert(matches.index); // 0
alert(matches.input); // "mom and dad and baby"
alert(matches[0]); // "mom and dad and baby"
alert(matches[1]); // " and dad and baby"
alert(matches[2]); // " and baby"
```

对于 exec() 方法而言，即使在模式中设置了全局标志（ g ），它每次也只会返回一个匹配项。在不设置全局标志的情况下，在同一个字符串上多次调用 exec() 将始终返回第一个匹配项的信息。而在设置全局标志的情况下，每次调用 exec() 则都会在字符串中继续查找新匹配项，如下面的例子所示。

```javascript
var text = "cat, bat, sat, fat";
var pattern1 = /.at/;
var matches = pattern1.exec(text);
alert(matches.index); //0
alert(matches[0]); //cat
alert(pattern1.lastIndex); //0
matches = pattern1.exec(text);
alert(matches.index); //0
alert(matches[0]); //cat
alert(pattern1.lastIndex); //0
var pattern2 = /.at/g;
var matches = pattern2.exec(text);
alert(matches.index); //0
alert(matches[0]); //cat
alert(pattern2.lastIndex); //3
matches = pattern2.exec(text);
alert(matches.index); //5
alert(matches[0]); //bat
alert(pattern2.lastIndex); //8
```

这个例子中的第一个模式 pattern1 不是全局模式，因此每次调用 exec() 返回的都是第一个匹配项（ "cat" ）。而第二个模式 pattern2 是全局模式，因此每次调用 exec() 都会返回字符串中的下一个匹配项，直至搜索到字符串末尾为止。此外，还应该注意模式的lastIndex 属性的变化情况。在全局匹配模式下， lastIndex 的值在每次调用 exec() 后都会增加，而在非全局模式下则始终保持不变。

*使用exec进行正则还是很不方便的，不如使用match好用* 

正则表达式的第二个方法是 test() ，它接受一个字符串参数。在模式与该参数匹配的情况下返回true ；否则，返回 false 。在只想知道目标字符串与某个模式是否匹配，但不需要知道其文本内容的情况下，使用这个方法非常方便。因此， test() 方法经常被用在 if 语句中，

