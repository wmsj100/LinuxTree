---
title: 无法识别的属性“targetFramework”
date: 2016-09-07
tags: [ASP.NET]
categories: Language
---

参考文献：
http://blog.csdn.net/jiankunking/article/details/50547601

对于提示`无法识别的属性“targetFramework”。请注意属性名称区分大小写。`
这个需要修改默认的应用池的`.net`版本从`2.0` => `4.0`;
然后转到自己的网站，修改右侧的‘高级属性’中的‘应用程序池’的内容选择`ASP.NET v4.0`;