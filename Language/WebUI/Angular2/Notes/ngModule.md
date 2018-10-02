---
title: 模块
date: 2018-07-15 18:01:55	
modify: 
tag: [basic]
categories: Angular 
author: wmsj100
mail: wmsj100@hotmail.com
---

# 模块

## 疑问
- 为什么需要一个新的模块系统? 只用`ES6/TypeScript`的模块还不够吗?
- 现在所有的组件都在`app.module.ts`中声明,我认为这不是一个好的方式,组件应该要做到只对某些模块可见,而不是全局可见,这样就可以避免名称冲突.这种思路要怎么实现?

## 概述
- 每个组件都必须在某些`NgModule`中声明过
- 任何组件都只能从属于一个`NgModule`
- 通常会把很多组件一起放进一个`NgModule`中


## 参考
- []()
