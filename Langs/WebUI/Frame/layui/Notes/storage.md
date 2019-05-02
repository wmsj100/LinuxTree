---
title: 存储
date: 2018-05-04 22:37:24 Fri
modify: 2018-05-04 22:37:24 Fri
tag: [layui]
categories: Web
author: wmsj100
mail: wmsj100@hotmail.com
---

# 存储

## 概述
- 对于临时存储的值一般都是存储在变量中；
- 但是对于通过点击事件(提交表单，打开弹框)这些操作要获取值肯定不能通过存储在变量中的值，因为此时变量怎么获取，
- 这种情况下我以前从来没有思考过，因为之前使用`tinyUI`时候框架有封装`API`，直接调用就可以了，但是现在我需要自己实现时候就需要思考了。
- 这时候肯定就想到了要使用`cookie`插件来实现这个存储过程。
- 但是看到`layui`的`API`时候，感觉它提供的方法更加好，因为这种操作更像是操作数据库的表。

## API
- localStorage 持久化存储，数据会永久存储，除非物理删除，和`cookie`类似
	- layui.data('test', {key: 'nickname', value: 'xianxin'});
	- layui.data('test', {key: 'nickname', remove: true}); 删除test表的nickname字段
	- layui.data('test', null); 删除test表
- sessionStorage 会话性存储，页面关闭后就失效，这个可以用来临时存储数据；
	- layui.sessionData(table, setting) 和上面的操作类似
