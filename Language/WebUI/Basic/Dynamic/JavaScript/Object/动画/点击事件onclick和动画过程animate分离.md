---
title: 点击事件onclick和动画过程animate分离
date: 2016-05-25
tags: [动画,DOM,JavaScript]
categories: Dynamic
---

通过jQuery绑定的`click`事件内部的`animate`如果有其它对象调用的话，那么最好把这个内部的`animate`对象提取出去，外部直接调用这个`animate`，而不是调用`click`，因为如果调用`click`事件的话，是没有效果的，
这个问题在轮播插件通过`bullet`按钮触发`arrow`点击过程中出现的，
其实点击`bullet`需要的不是触发`点击arrow`，而是触发`listwarp`的动画效果，我太执迷于触发这个点击过程了，所以就掉坑了。