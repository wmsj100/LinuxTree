---
title: template
date: 2019-10-10 15:07:11 Thursday
modify:
tag: [template]
categories: Vue
author: wmsj100
mail: wmsj100@hotmail.com
---

# template

## 概述

## 用法

- `v-once` 只有第一次镜像渲染，之后就不再改变
- `v-html` 通常渲染为普通文本，添加该标签后就按照HTML进行渲染
- `v-bind` 可以进行特性绑定，例如
	- `<button v-bind:disabled="status">button</button>`

## 指令

- `v-` 带有这个前缀，预期是单个js表达式`for/if/bind`
- 携带参数的指令
	- 一些指令能够接收一个参数，使用冒号分隔
	- v-bind:href="url"
	- `v-on`用来监听DOM事件
	- `<a v-on:click="domSomething">...</a>`
	- `v-bind[someArr]="value"` 通过中括号包裹的是动态参数，真正的值是data总的`someArr`值

## 修饰符

- 以`.`指明的特殊后缀
- `<div v-on:submit:prevent="onSubmit"></div>` 指明使用`event.preventDefault()`

## 缩写
- `:` ==> `v-bind`
	- `<a v-bind:href="url">url</a>`
	- `<a :href="url">url</a>`
- `@` ==> `v-on`
	- `<h3 v-on:click="dosmt">click</h3>`
	- `<h3 @click="dosmt">click</h3>`

## v-if or v-show

- v-if是真正的条件渲染，因为它会确保在切换过程中条件块内的事件监听和子组件适当被销毁和重建。
- v-if 也是惰性的，如果初始条件为假，则什么也不做，知道条件第一次变为真时才开始渲染
- v-show简单很多，就是通过切换display:none，切换css的样式，DOM块始终会渲染
- v-if有很高的切换开销，v-show有很高的初始化渲染开销。
- 如果是频繁切换，则使用v-show，如果运行条件少，就使用v-if

## 范例

## 参考
- [指令](https://cn.vuejs.org/v2/guide/syntax.html)
