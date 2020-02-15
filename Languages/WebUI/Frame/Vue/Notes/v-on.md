---
title: v-on
date: 2020-02-15 22:11:42
modify: 
tags: [Notes]
categories: Vue
author: wmsj100
email: wmsj100@hotmail.com
---

# v-on

## 概要

- 事件绑定

## 绑定方式

- `@click="greet"` 只是调用方法，方法可以获取到`event`，指向当前点击tag
- `@click="greet('hi')` 传参，可以通过`greet: function(msg){}` 中获取到传入的参数
- `@click="greet('hi', $event)` 通过传入参数`$event`来获取原始DOM事件

## 事件修饰符

- 之前写页面对于点击事件处理的很粗糙，其实很多点击事件是不需要传播的，很确定就是要点击来触发事件，不需要扩散到顶部
- `stop`: `@click.stop` 阻止单击事件继续传播
- `prevent`: `<form @submit.prevent="onSubmit">` 提交事件不再重载页面
- `self`: `<div v-on:click.self="doT">` 只有当前元素触发函数

```html
<div v-on:click.self="clickDiv">
	<button class="btn btn-danger" v-on:click.stop="clickBtn">test click</button>
</div>
```
- `enter` `<input v-on:keyup.enter='submit'>` 输入框只有按下enter键才触发方法submit， event.key==Enter

## v-on优点

- 轻松定位htm代码对应的方法
- 无须在js里手动绑定事件，viewmodel代码是非常纯粹的代码逻辑，和dom完全解耦，更易于测试
- 当一个viewmodel被销毁时，所有的事件处理器都会被自动删除，无须担心如何清理

## 参考

- [v-on](https://cn.vuejs.org/v2/guide/events.html)
