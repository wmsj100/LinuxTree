---
title: 原生JS监听窗口变化
date: 2016-05-16
tags: [JavaScript,DOM]
categories: Dynamic
---

`window.onscroll = function(){ }` --监听窗口滚动

`window.onresize = function(){ }` -- 监听窗口尺寸变化

`window.innerWidth / window.innerHeight` -- 获得窗口尺寸，包括滚动条

`document.body.offsetWidth` --获取窗口尺寸，不包括滚动条

`document.body.clientWidth` -- 获取窗口尺寸，不包括滚动条，不包括`margin`；

`document.documentElement.clientWidth` -- 获取窗口尺寸，不包括滚动条，包括`margin`