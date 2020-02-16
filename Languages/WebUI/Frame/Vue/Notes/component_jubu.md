---
title: 局部组件
date: 2020-02-16 10:52:12
modify: 
tags: [Notes]
categories: Vue
author: wmsj100
email: wmsj100@hotmail.com
---

# 局部组件

## 概要

- 通过`Vue.component`注册的组件是全局组件，
- 全局组件往往不够理想，假如一个组件已经不再使用，当通过webpack进行构建系统时，哪些不再使用的全局组件仍然会被包含在最终的构建结果中，这就造成了下载的js无谓增加体积。

## 参考

