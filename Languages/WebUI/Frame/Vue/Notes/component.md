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

## 组件写复杂模板

- 复杂模板可以用'`'包裹，
- 多个属性可以绑定到一个属性进行传递，
- 绑定的属性prop是在当前标签上传输下去的，定义模板时候只是申明了哪些属性是允许传递数据的
```html
<div id="app4">
	<my-blog v-for="post in posts" v-bind:key="post.id" v-bind:post="post"></my-blog>
</div>
<script>
	Vue.component('my-blog', {
		props: ['post'],
		template: `
		<div>
		<p>{{ post.title }}</p>
		<p>{{ post.content }}</p>
		</div>
		`
	});
	new Vue({el: '#app1'});
	new Vue({el: '#app2'});

	new Vue({
		el: '#app4',
		data: {
			posts: [
				{id: 1, content: 'this is content',  title: 'one blog'},
				{id: 2, content: 'this is content',  title: 'two blog'},
				{id: 3, content: 'this is content',  title: 'three blog'},
				{id: 4, content: 'this is content',  title: 'four blog'},
			],
		}
	});
```

## 组件事件联动

- 可以在自定义组件调用时候添加自定义事件进行绑定，
- 子组件内部通过`v-on:click="$emit('enlarge-text')"`这样来实现实现组件内触发父组件事件触发
- 对于组件自定义事件监听的属性名必须符合h5标准，只能是中横线模式，不能是驼峰，也不能有大写，
- 如果写做`v-on:enlargeText='enlarge'`这样子组件调用这个方法就会报错，不生效。
```html
<div id="app4" :style="{fontSize: postFontSize + 'em'}">
	<my-blog v-for="post in posts" v-bind:key="post.id" v-on:enlarge-text="enlarge" v-bind:post="post"></my-blog>
</div>
<script>
	Vue.component('my-blog', {
		props: ['post'],
		template: `
		<div>
		<p>{{ post.title }}</p>
		<p>{{ post.content }}</p>
		<button class="btn btn-warning" v-on:click="$emit('enlarge-text')" >large text</button>
		</div>
		`
	});

	new Vue({
		el: '#app4',
		data: {
			postFontSize: 1,
			posts: [
				{id: 1, content: 'this is content',  title: 'one blog'},
				{id: 2, content: 'this is content',  title: 'two blog'},
				{id: 3, content: 'this is content',  title: 'three blog'},
				{id: 4, content: 'this is content',  title: 'four blog'},
			],
		},
		methods: {
			enlarge: function(){
				this.postFontSize += 0.1;
			}
		}
	});
</script>
```

## v-model组件

- 子组件内部的input如果想要和父组件的变量联用，需要满足下面条件
	- 子组件的input必须将`value`属性绑定到名为`value`的prop上
	- input事件被触发时，将新的值通过自定义的`input`事件抛出
	- `v-on:input="$emit('input', $event.target.value)"`
```html
<div id="app4">
	<p>{{ searchTxt }}</p>
	<custom-input v-model="searchTxt"></custom-input>
</div>
<script>
	Vue.component('custom-input', {
		props: ['value'],
		template: `
		<input type="" v-bind:value="value" v-on:input="$emit('input', $event.target.value)">
		`
	});

	new Vue({
		el: '#app4',
		data: {
			searchTxt: 'wmsj',
		},
	});
</script>
```

## 参考

