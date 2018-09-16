---
title: trim删除字符串前面和后面的空格
date: 2016-06-19
tags: [String]
categories: Dynamic
---

`trim` -- 原生的字符串方法，可以删除字符串的前面和后面的空格，但是需要IE9以上版本支持，自己用正则模仿一个方法。

```javascript
var a = a=" as d f  ";
var reg = /\S+[\w|\W].*\S+/;
a.match(reg).toString();
a="  s!@ #$^8 s d  ";
a.match(reg).toString();    //"s!@ #$^8 s d"
a.trim();   //"s!@ #$^8 s d"
```

