---
title: 未能加载类型“WebApplication1.WebForm1”
date: 2016-09-07
tags: [ASP.NET]
categories: Language
---

这个问题是因为添加网站时候设置的‘物理路径’没有指向项目的根目录下，也就是说添加网站，物理路径必须是项目的文件目录，右侧的面板展开就是项目的文件结构，
然后再设置网站的`.NET`版本为`4.0`,这样就可以了。