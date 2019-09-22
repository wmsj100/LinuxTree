---
title: 类
date: 2018-07-10 22:34:35	
modify: 
tag: [class]
categories: Angular 
author: wmsj100
mail: wmsj100@hotmail.com
---

# 类

## 概述
- 如果是数据结构类型的,不要再组件内部定义,放到专门的文件中,
	```ts
	class Product {
		constructor(
		public sku: string,
		public name: string,
		public imageUrl: string,
		public department: string[],
		public price: number) {
		}
	}
	```
- 上面定义了一个类,直接在构造函数内部声明

## 参考
- []()
