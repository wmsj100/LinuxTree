---
title: 关于json文件访问失败
date: 2016-09-12
tags: [ASP.NET]
categories: Language
---

http://www.cnblogs.com/feigao/p/5058708.html

如果通过`asp.net`访问`json`文件获取失败，那么需要把`.json`文件后缀添加到支持页面。

在`iis`的`huntaotao`主页的`IIS`的`MIME类型`，
关联扩展名：*.json
内容类型(MIME)：application/x-javascript