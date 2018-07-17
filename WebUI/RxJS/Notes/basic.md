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
