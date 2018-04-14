---
title: 通过r.js进行代码发布
date: 2016-07-17
tags: [Models, jQuery,Frame,Public]
categories: Frame
---
模块化我使用的是`requirejs`，
压缩，使用的是`r.js`
我首先是通过`volo`初始化一个页面模块，
然后切换到`tools`目录，进行命令
` r.js -o build.js`
这样就可以把所有的js文件压缩为一个文件。