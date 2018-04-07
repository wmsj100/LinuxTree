---
title: 关于模块ajax地址的引用
date: 2016-07-19
tags: [Models, jQuery]
categories: Frame
---

睡梦中忽然意识到我的模块不能支持本地模式，因为是通过`jsonp`的`ajax`方式获取的数据，但是能通过这个方式获取那么就可以通过`json`获取，因为`jQuery`对这俩个方式的数据获取是一样的，都是通过`$.getJSON()`,所以我只需要自己手写一个`json`文件，就像之前的那样。通过这个文件来创建`DOM`，所以我的模块封装是没有问题的。