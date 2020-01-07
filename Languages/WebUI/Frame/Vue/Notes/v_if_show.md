---
title: v-if/v-show
date: 2019-10-11 07:57:38 Friday
modify:
tag: [basic]
categories: Vue
author: wmsj100
mail: wmsj100@hotmail.com
---

# v-if/v-show

## 概述

- 俩个命令都是切换，但`v-if`是真正的条件渲染，在切换过程总条件块内的事件监听和子组件适当被销毁和重建
- `v-show`只是通过css样式来控制显式，DOM是会被渲染的
- `v-if`可以使用`template`标签来控制，`v-show`不可以

## 参考
- [v-if/v-show](https://cn.vuejs.org/v2/guide/conditional.html#v-if-%E4%B8%8E-v-for-%E4%B8%80%E8%B5%B7%E4%BD%BF%E7%94%A8)
