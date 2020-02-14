---
title: basic
date: 2019-10-10 15:06:22 Thursday
modify: 2020-02-12 10:21:21 
tag: [basic,note]
categories: Vue
author: wmsj100
mail: wmsj100@hotmail.com
---

# basic

## 概述

- 基础知识

## 用法

- vue中俩个特定简写
	- `v-bind` ==> `:`
	- `v-on` ==> `@`

## 计算属性

- `computed` 计算属性，用于进行计算，
- 多用于一个值依赖于另一个值，当另一个值变动时候，该值会自动变动。
- 下面例子中就是计算属性对比方法和监听
```html
<div id="app8">
	<a v-bind:href="url">{{ url }}</a>
	<a :href="url1">{{ url1 }}</a>
	<div>
		<p>{{ message }}</p>
		<p>{{ reverseMsg }}</p>
		<p>{{ reverseFn() }}</p>
		<p>{{ reverseVal }}</p>
	</div>
</div>

<script>
	var app8 = new Vue({
		el: '#app8',
		data: {
			url: 'https://www.wmsj100.com',
			url1: 'https://www.adfwmsj100.com',
			message: 'hello world',
			reverseVal: this.message,
		},
		methods: {
			reverseFn: function(){
				return this.message.split('').reverse().join('')
			}
		},
		watch: {
			message: function(val){
				console.log('val is changed')
				this.reverseVal = val.split('').reverse().join('')
			}
		},
		computed: {
			reverseMsg: function(){
				return this.message.split('').reverse().join('')
			}
		}
	})
</script>
```
- 计算属性VS方法
	- 计算属性是基于它们的响应式依赖进行缓存的，只有在相关响应式依赖发生变化时它们才会重新求值。
	- 方法每次触发重新渲染都会重新进行计算，如果计算性能开销比较大，计算属性的缓存优势更加明显
- 计算属性VS监听： 监听容易被滥用，使用计算属性是更好的选择
