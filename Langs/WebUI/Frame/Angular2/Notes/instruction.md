---
title: 指令
date: 2018-07-10 22:39:50	
modify: 
tag: [instruction]
categories: Angular
author: wmsj100
mail: wmsj100@hotmail.com
---

# 指令

## 概述
- 指令分为内置指令和自定义指令

## 内置指令
- `ngSwitch`
	```ts
	<div [ngSwitch]="value">
	  <div *ngSwitchCase="'a'">a</div>
	  <div *ngSwitchCase="'b'">b</div>
	  <div *ngSwitchCase="'c'">c</div>
	  <div *ngSwitchDefault>others</div>
	</div>
	```
	- 也可以为不同的元素声明同样的`*ngSwitchCase`值,这样可以多次匹配同一个值.
- `ngStyle` 给`DOM`设定特定的`css`属性,最简单的用法就是`[style.<cssproperty>]="value"`
	- `<div [style.background-color]="'yellow'"></div>`
	- 通过`ngStyle`通过键值对来设置多个属性
	- `<div [ngStyle]="{color: 'color'}"`

- `ngNonBindable` - 告诉`Angular`不要编译或绑定页面某个特殊部分.
- `Angular`的核心指令很少,可以通过组合这些简单的指令来创建五花八门的应用.

## 参考
- []()
