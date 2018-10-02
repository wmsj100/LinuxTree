---
title: 正则-replace
date: 2016-4-1 23:50:20
tags: [正则,函数]
categories: Dynamic
---

```javascript
a="1 2 3"	
a.replace(/1/g,"")	//" 2 3"
a	//"1 2 3"
a.replace(/"1"/g,"")	//"1 2 3"
a.replace(1,"")	//" 2 3"
a.replace("1","")	//" 2 3"
```
<!-- more -->
- 通过replace是不会改变原字符串的，因为字符串是只读的，不可以被改写，要改变字符串，只能通过重新赋值的方法。
- 从上面可以看到正则是不能添加变量，如果要添加变量，只能是再构造函数中；

```javascript
var exp=new RegExp(/a/g);
str=str.replace(exp," ");
//这样a就是被当作变量传递进来的。
```

```javascript
a=a.replace("1","")	//" 2 3"
a	//" 2 3"
```