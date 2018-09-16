---
title: 基础
date: 2018-07-17 23:34:37	
modify: 
tag: [basic]
categories: RxJS 
author: wmsj100
mail: wmsj100@hotmail.com
---

# 基础

## 概述
- `Observables`传递值可以是同步的也可以是异步的
- `Observable`和函数的区别是,它可以随着时间的推移返回多个值,这是函数做不到的.
- `observable.subscribe()`的意思是"给我任意数量的值,无论是同步还是异步"
- `Observab`的核心关注点:
	- `create` 创建
	- `subscribe` 订阅
	- 执行
		- `next`: 发送一个值,比如数值/字符串/对象等,最常见的类型,表示传递给观察者的实际数据;
		- `error`: 发送一个`js`错误或异常
		- `complete`: 不再发送任何值
		- 备注: `error`和`complete`只会执行其中一个,而且只执行一次.
	- `unsubscribe` 定义的事件需要使用这个方法进行清理,也可以在`create`内部创建同名的清理函数.
	- `observable.subscribe(x => console.log(x)).unsubscribe();`

## 观察者`Observer`
- 观察者是有`Observable`发送的值的消费者,它只是一组回调函数的集合,每个回调函数对应一种`Observable`发送的通知类型`next, error, complete`,下面是一个典型的观察者对象
	
	```ts
	var observer = {
		next: x => console.log(x),
		error: err => console.error(err),
		complete: () => console.log('complete')
	};
	```
- 观察者的三个对象是可选的,也可以只提供一个回调函数作为参数,而不需要附加到观察者对象上;
- `observable.subscribe(x => console.log(x))`
- `rxjs`内部会创建一个观察者对象并使用第一个回调函数参数作为`next`的处理方法.
- 三种类型的回调函数都可以直接作为参数来提供;

## `Subscription`订阅
- `Subscription`是表示可清理资源的对象,它有一个重要的方法`unsubscribe`,不需要任何参数,只用来清理`Subscription`占用的资源;
- 订阅还可以多个合并在一起`add`,这样调用一个`unsubscribe`就可以取消多个订阅.

	```ts
	  unsubscribeDemo1() {
		const observable1 = Observable.create((observer) => {
		  let i = 0;
		  setInterval(() => {
			observer.next(i++);
		  }, 400);
		}).subscribe(x => console.log('name1: ', x));
		const observable2 = Observable.create((observer) => {
		  let i = 0;
		  setInterval(() => {
			observer.next(i++);
		  }, 300);
		}).subscribe(x => console.log('name2: ', x));
		observable1.add(observable2);
		setTimeout(() => {
		  observable1.unsubscribe();
		}, 1000);
	  }
	```

## `Subject`主体
- 一种特殊类型的`Observable`,允许将值多播给多个观察者,所以`Subject`是多播的.
- 而普通的`Subject`是单播的.
- 对于`Subject`可以提供一个观察者并使用`subscribe`方法就可以开始正常接收值.
- 从观察者角度而言,它无法判断`Observable`执行是来自普通的`Observable`还是`Subject`.
- `Subject`有如下方法的对象`next(v), error(e), complete()`.
- 要给`Subject`提供新值,只要调用`next(thevalue)`,它会将值多播给已经注册监听该`Subject`的观察者.
- 因为`Subject`是观察者,意味着可以把`Subject`作为参数传给任何`Observable`的`subscribe`方法.

## `ReplaySubject`
- 它可以发送旧值给新的订阅者,但它还可以记录`Observable`执行的一部分.
- 它记录`Observable`执行中的多个值,并将其回放给新的订阅者.
- `const subject = new ReplaySubject(3)` 表示为新的订阅者缓冲3个值

## 范例
- 调用`RxJS`模块

	```ts
	import { Component, OnInit } from '@angular/core';
	import { Observable, Subscription, fromEvent } from 'rxjs';

	@Component({
	  selector: 'app-rxjs',
	  templateUrl: './rxjs.component.html',
	  styleUrls: ['./rxjs.component.css']
	})
	export class RxjsComponent implements OnInit {
	  button;

	  constructor() { }
	  ngOnInit() {
		this.button = document.querySelector('button');
		fromEvent(this.button, 'click').subscribe(() => console.log('clicked'));
	  }

	}
	```

## 参考
- []()
