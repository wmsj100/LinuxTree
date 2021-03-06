---
title: 基础概念 
date: 2018-07-01 11:52:14	
modify: 2018-07-08 12:49:29	
tag: [basic]
categories: Angular2 
author: wmsj100
mail: wmsj100@hotmail.com
---

# 基础概念

## 表达模块`FormModule`
- `ngModel`
	- 在`html`的`dom`结构上使用`[]`表示把等号后面当成表达式来解析而不是当成字符串.
		- `<input [ngModel]="username">`
	- `[]`方括号的含义是单向数据绑定,表示给`model`赋值会设置到`input`
	- `[()]` 双向数据绑定,`input`中的值的改变会映射到`model`上.

## 生成模块和服务
- `ng generate component login` ==> `ng g c login`
- `ng genereate serve auth` ==> `ng g s auth`

## 注入service服务
- 创建服务 `ng g s auth`;
- 在`app.module.ts`中会自动注入生成的服务,
	- 在`providers`中注入服务
	- `{ provide: 'auth', useClass: AuthService }`
- 在要调用服务的模块中引入`auth`	
	- `constructor(@Inject('auth') private auth) { }`

## *ngIf
- `*ngIf="usernameRef.errors?.required"` 表示如果`errors`为空的时候就不调用后面的值,如果不为空,就调用后面的值,
- 如果不这样写会调用.

## 流程
- Angular有一个强大的概念`模块`,但引导一个`Angular`应用时,并不是直接引导一个组件,而是创建了一个`NgModule`,它指向了你要加载的组件.
- 要想在模板中使用组件,必须现在`NgModule`中声明它.

## 组件
- `Angular`应用是由组件构成的,可以将组件理解为一种教浏览器认识新`HTML`标签的方式.

## 应用
- 一个`Angular`应用其实就是一颗由组件构成的树
- 这棵树的根节点,最顶层的组件就是应用本身.它会在浏览器启动(引导)应用时候被渲染.
- 组件的一个很棒的特性就是可组合,可以基于小组件构建成大组件.
- 应用只是一个会渲染其他组件的组件而已.
- 由于组件是以树型结构组织起来的,每当组件被渲染时,它都会递归地渲染下级组件.

## 参考
- []()
