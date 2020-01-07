---
title: 计算属性和侦听器
date: 2019-10-10 15:31:43 Thursday
modify:
tag: [basic]
categories: Vue
author: wmsj100
mail: wmsj100@hotmail.com
---

# 计算属性和侦听器

## 概述

- 模板内的表达式非常便利，但是大量使用会导致模板过重且难以维护，
- 对于任何复杂的逻辑，都应该使用**计算属性**

## 用法

- 计算属性是有缓存的，如果依赖值不变，就不需要进行重复计算，而方法是每次都需要计算的，如下范例1
- 从angular转过来的容易滥用`watch`，其实好多可以通过**计算属性**来实现，如下范例2
- 通常`computed`只有`getter`,也可以使用`setter`
	```js
	computed: {
		total: {
			get: function(){
				return this.first + this.last;
			},
			set: function(value){
				var names = value.split(' ');
				this.first = names[0];
				this.last = names[1];
			}
		}
	}
	```

## 范例

- template1
```html
<!DOCTYPE html>
<html>
	<head>
        <meta charset="utf-8" />
		<title>Compute_Watch</title>
		<script src="js/vue.js"></script>
	</head>
	<body>
		<div id="app1">
			<p>{{ message }}</p>
			<p>{{ reverseMsg }}</p>
		</div>

		<script>
			var app = new Vue({
				el: '#app1',
				data: { message: 'hello' },
				computed: {
					reverseMsg: function(){
						return this.message.split('').reverse().join('');
					}
				}
			})
		</script>
	</body>
</html>
```

- template2
```html
<!DOCTYPE html>
<html>
	<head>
        <meta charset="utf-8" />
		<title>Compute_Watch</title>
		<script src="js/vue.js"></script>
	</head>
	<body>
		<div id="app2">
			<p>{{ fullName }}</p>
			<p>{{ total }}</p>
			<input type="" v-model="first">
			<input type="" v-model="last">
		</div>

		<script>
			var app2 = new Vue({
				el: '#app2',
				data: {
					first: 'wang',
					last: 'hao',
					fullName: 'wang hao',
				},
				watch: {
					first: function(){
						this.fullName = this.first + this.last;
					},
					last: function(){
						this.fullName = this.first + this.last;
					}
				},
				computed: {
					total: function(){
						return this.first + this.last;
					}
				}

			})
		</script>
	</body>
</html>
```

## 参考
- []()
