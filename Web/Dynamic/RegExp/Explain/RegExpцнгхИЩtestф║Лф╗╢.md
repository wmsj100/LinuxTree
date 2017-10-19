---
title: RegExp正则test事件
date: 2016-4-1 16:26:02
tags: [正则,事件]
categories: Dynamic
---

正则的test可以匹配字符串和数组；
<!-- more -->

字符串的正则：String or string
```javascript
var a="abcd";
/c/g.test(a)	//true;
a.match(/c/g)	//["c"]
a.replace(/ab/g,"dd")	//'ddcd'
```

数组的正则： Array or array

```javascript
var b=[1,2,3];
/2/g.test(b)	//true;
b.match(/2/g)	
//false b.match is not a function(…)
b.replace(4,/2/g)	
//false b.match is not a function(…)
```

match , replace , search ——这些都是字符串的属性。