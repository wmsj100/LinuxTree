---
title: window.close-关闭窗口
date: 2016-05-16
tags: [DOM,JavaScript]
categories: Dynamic
---

该方法只能由 [window.open](https://developer.mozilla.org/zh-cn/DOM/window.open) 方法打开的窗口的window对象来调用.如果一个窗口不是由脚本打开的,调用该方法时,JavaScript控制台会出现下面的错误: "`不能使用``脚本``关闭一个不是由脚本打开的窗口".`

直接使用`window.close()` 谷歌会报错，而火狐会直接关闭窗口。