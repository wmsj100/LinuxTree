---
title: 创建随机数 
date: 2018-07-01 18:41:00	
modify: 
tag: [summary]
categories: Angular2
author: wmsj100
mail: wmsj100@hotmail.com
---

# 创建随机数

## 概述
- 如何创建随机数,之前的方式
	- `let value = Math.random() + Date.now();` 通过随机数和时间字符串;
- 引入`angular2`的`UUID`
	- ` npm i --save angular2-uuid`
	- `import { UUID } from 'angular2-uuid';`
	- `let id = UUID.UUID(); // "142a170a-654d-5b8c-5ccc-3b4b6e8ca7fa"`

## 参考
- [创建随机数](https://www.jianshu.com/p/86c6249a2069)
