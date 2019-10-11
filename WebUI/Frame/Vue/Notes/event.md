---
title: 事件
date: 2019-10-11 09:53:35 Friday
modify:
tag: [basic]
categories: Vue
author: wmsj100
mail: wmsj100@hotmail.com
---

# 事件

## 概述

- 事件包括点击事件
- 还有子组件来触发父组件的特点事件

## 用法

- `$emit` 子组件来继承父组件事件
- `v-on:click="clickBtn('hello', $event)` 通过`$event`来传入event事件

## 事件修饰符

- `.stop` 阻止单击事件继续传播
- `.prevent` 阻止提交事件不再重载页面，用于`form`表单
- `.self` 只有点击自己才触发
- `.once` 只触发一次
- `v-on:click.self.once='clickDiv'` 事件修饰符可以连用

## 按键修饰符

- `v-on:keyup.enter='keyupFn'` 只有在按下`Enter`键时才会触发
- 支持的按键修饰符如下：
	- `enter`
	- `tab`
	- `delete`
	- `esc`
	- `space`
	- `up`
	- `down`
	- `left`
	- `right`

## 系统修饰键

- 支持的系统修饰键如下
	- `ctrl`
	- `shift`
	- `alt`
	- `meta`
- `v-on:keyup.shift.67='clickC'` 只有按下`shift+c`才会触发

## 鼠标事件

- `v-on:click.left="leftClick"` 只响应鼠标的左键点击

## 范例

## 参考
- [组件](https://cn.vuejs.org/v2/guide/list.html)
