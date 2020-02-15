---
title: v-for
date: 2020-02-15 19:00:01
modify: 
tags: [Notes]
categories: Vue
author: wmsj100
email: wmsj100@hotmail.com
---

# v-for

## 概要

- 循环遍历，可以遍历数组，也可以是对象

## 数组

- `v-for='item in list'`
- `v-for='(item, index) in list'`

## 对象

- `v-for='value in obj'`
- `v-for='(value, key) in obj'`

## 维护状态

- v-for渲染列表，默认是就地更新策略，如果只是元素的顺序变更，vue是不会更新dom的，
- 为了提高重用和重新排序现有元素，需要给for循环指定一个key值。
```html
<div id="app2">
	<ul>
		<li v-for="(item,index) in items" v-bind:key="index">
			<span>{{ index }},{{ item }}</span>
		</li>
	</ul>
	<ul>
		<li v-for="(value,name) in obj" v-bind:key="name">
			<span>{{ name }} is {{ value }}</span>
		</li>
	</ul>
</div>
```

## 数组更新

- vue对于数组的更新进行了包裹，比如常见的数组操作方法都支持
- push/pop/shift/unshift/splice/sort/reverse
- 通过上面的方法对vue的数组的操作，页面都可以动态感知到
- 下面的俩种对数组的更新方法vue无法感知，
	- 直接通过索引赋值更新
	- 直接修改数组的长度
- 针对上面vue提供的解决方法
	- Vue.set(app.items, indexOfItem, newValue)
	- app.$set(app.items, indexOfItem, newValue)
	- app.items.splice(newLength)
- 对于嵌套

## 数组排序

- 如果是要对数组进行过滤或者排序，建议使用计算属性
- 使用计算属性可以提升性能
```html
<ul>
	<li v-for="(item,index) in items" v-bind:key="index">
		<span>{{ index }},{{ item }}</span>
	</li>
</ul>
<ul>
	<li v-for="(item,index) in sortItem" v-bind:key="index">
		<span>{{ index }},{{ item }}</span>
	</li>
</ul>

<script>
var app2 = new Vue({
	'el': '#app2',
	'data': {
		items: ['python', 'html', 'shell', 'django'],
		obj: {
			'name': 'wmsj100', 
			'age': 32,
			'sex': 'male',
		}
	},
	computed: {
		'sortItem': function(){
			return this.items.filter(function(val){
				return val.startsWith('s')
			})
		}
	}
})
</script>
```

- 如果是不适用计算属性来更新的，可以通过方法来间接实现
```html
<ul>
	<li v-for="(num,index) in obj2.nums" v-bind:key="index">{{ num }}</li>
</ul>
<ul>
	<li v-for="(num,index) in filterNum(obj2.nums)" v-bind:key="index">{{ num }}</li>
</ul>

<script>
	methods: {
		filterNum: function(tar_list){
			return tar_list.filter(function(num){
				return num%2 == 0;
			})
		}
	}
</script>
```

## 对象更新

- 同样由于js的限制，如果直接操作对象，vue也是无法直接感知的，
- vue提供的操作方法和数组类似
	- app2.$set(app2.obj, 'addr', 'qiaotou')
	- Vue.set(app2.obj, 'dizhi', 'qiaotou')
- 一次性赋值多个属性
	- Object.assign(a, {name:'wms', age: 32}) 这是原始的js扩展对象的方法
	- app2.obj = Object.assign({}, app2.obj, {name: 'wmsj100', age:32}) 
	- 上面是vue提供的更新属性的方法

## template

- v-for也可以像v-if一样作用于template标签

## 组件

- v-for可以用于组件component,当用于组件时，key必须指定。


## 总结

- **其实对于上面的问题只有在更新当前数组或对象时候才会出行，如果是重新赋值就没有这样的问题**
- 我再想当初用angular时候有没有这样的问题，
- 既然这是js的问题，那么应该所有的语言都有这样的问题吧，都应该是类似处理方式吧
- 可能angular的处理方法更加底层。

## 参考

