---
title: 数据架构
date: 2018-07-15 18:24:08	
modify: 
tag: [data]
categories: Angular 
author: wmsj100
mail: wmsj100@hotmail.com
---

# 数据架构

## 概述
- 管理数据可以说是编写可维护应用最棘手的方面之一,有很多种方式可以将数据应用到应用中
	- `AJAX HTTP`
	- `Websocket`
	- `indexdb`
	- `LocalStorage`
	- `Service Worker`

- 数据架构涉及的问题如下:
	- 如何将所有不同的数据源聚合成一个完整的体系?
	- 如何防止意想不到的副作用导致bug?
	- 如何更好的构建代码以使其更容易维护并让新来的团队成员更容易上手?
	- 当数据发生变化时,如何让应用尽快做出反应?
- 目前,数据架构领域常见的理念
	- `MVW` `Model-View-Whatever` 双向数据绑定,是`AngularJs`中默认架构的一个术语,`$scope`提供数据双向绑定,整个应用都共用同样的数据结构,某个区域的一个变化会传达至该应用的其余部分
	- `Flux` 单向数据流 在`Flux`中,`Store`负责存储数据,`View`负责渲染`Store`中的数据,`Action`负责改变`Store`中的数据.虽然设置`Flux`有些繁琐,但是因为数据只在一个方向上流动,所以很容易推断
	- `Observable` 可观察对象 `observable`给我们提供了数据流,我们订阅数据流然后执行操作对变化作出反应.`RxJS`是当下最流行的响应式`JS`库,

## Angular数据架构
- `Angular`在数据架构上很灵活,它没有规定具体的技术栈,而是力图让你无论选择何种数据架构都能很容易使用

## 参考
- []()
