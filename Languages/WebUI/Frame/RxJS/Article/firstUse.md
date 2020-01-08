---
title: 第一次使用
date: 2018-07-26 00:34:36	
modify: 
tag: [article]
categories: RxJS
author: wmsj100
mail: wmsj100@hotmail.com
---

# 第一次使用

## 概述
- 今天在做环境创建和修改的校验时候我就考虑到如果要依靠传统的做法就必须要在`dom`上写很多`blur`,`keyup`事件,还要统一的一个校验方法,
- 说到统一的校验这个我遗漏了,明天要记得补上
- 对于同一校验我想到一个方法,就是只查询有`require`属性或参数的不能为空的校验,这些校验通过就校验ok
- 我今天的做法是不修改`dom`,而是利用`rxjs`的事件广播先创建订阅,然后通过`dom`的`id`的事件来触发校验
- 用法也是很简单的,就是教程最开始的几个例子,但是效果确实很震撼的,知道要深入研究一下这个框架了.
- 这就是学习的动力

## 参考
- []()