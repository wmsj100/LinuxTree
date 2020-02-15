---
title: component
date: 2020-02-15 23:15:47
modify: 
tags: [Notes]
categories: Vue
author: wmsj100
email: wmsj100@hotmail.com
---

# component

## 概要

- 组件是vue的核心，
- 组件是可复用的vue实例，
- 组件可以进行任意次数的复用

## 使用

- `Vue.component('my-tag', {})` 这样的方式定义组件,这样定义的组件是全局注册，
	- 全局组件可以被使用于其被注册后的任意新创建的vue根实例
- `new Vue({el: '#app1'})` 这样的方式进行组件调用
- 如下面的例子，组件的data必须是一个函数，因此每个实例可以维护一份被返回对象的独立拷贝，而不会互相干扰。

```html
<div id="app1">
	<button-my></button-my>
</div>
<div id="app2">
	<button-my></button-my>
</div>

<script>
	Vue.component('button-my', {
		data: function(){
			return {count: 0}
		},
		template: '<button class="btn btn-danger" v-on:click="count++">{{ count }}</button>'
	});

	new Vue({el: '#app1'});
	new Vue({el: '#app2'});
</script>
```

## 组件v-for

- 在组件中使用for循环
- 在组件中传递传递数据需要通过`props`注册属性，通过这些属性可以传递值。
```html
<div id="app3">
	<blog-post v-for="post in posts" v-bind:key="post.id" v-bind:title="post.title"></blog-post>
</div>
<script>
	Vue.component('blog-post', {
		props: ['title'],
		template: '<h1> {{ title }}</h1>'
	});
	new Vue({
		el: '#app3',
		data: {
			posts: [
				{id: 1, title: 'one blog'},
				{id: 2, title: 'two blog'},
				{id: 3, title: 'three blog'},
				{id: 4, title: 'four blog'},
			],
		}
	});
</script>
```

## 参考

