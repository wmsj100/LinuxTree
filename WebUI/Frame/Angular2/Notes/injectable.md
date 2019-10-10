---
title: 依赖注入
date: 2018-07-15 10:42:46	
modify: 
tag: [inject]
categories: Angular
author: wmsj100
mail: wmsj100@hotmail.com
---

# 依赖注入

## 概述
- 要注册一个依赖,就得找到一些东西作为那个依赖的标识.
- 这个标识被称为依赖的令牌.
- 如果要注册某个`API`的`uRL`,就可以用字符串`API_URL`作为令牌
- 要注册一个类,就可以使用这个类本身作为它的令牌

## 构成
- 依赖注入包括三个部分,
- 提供者: 负责把一个令牌映射到一个依赖的列表,
- 注入器: 负责持有一组绑定,当外界要求创建依赖时,解析这些依赖并注入它们.
- 依赖: 被用于注入的对象

## 用途
- 与依赖注入打交道时,最常见的情况是提供一个服务或值,它将在整个应用中保持一致.
- 我们的应用中,99%的场景可能都属于这种情况.

## 别名和工厂函数
- `{ provide: 'ApiServiceAlias', useClass: ApiService },` 把服务`ApiService`设置为别名`ApiServiceAlias`;

	```ts
	{
		  provide: 'SizeService', useFactory: (viewport: any) => {
			return viewport.determineService();
		},
		  deps: [ViewPortService]
		},
	```
- 这样就把服务注入了注入器中了,使用时需要按照下面这样调用就可以了.

	```ts
	constructor(
		@Inject('ApiServiceAlias') private aliasService: any,
		@Inject('SizeService') private sizeService: any
	  ) {
	  }
	invokeApi(): void {
		this.aliasService.get();
		this.sizeService.run();
	  }

	```
- 已经注入过的服务,在组件中调用时候不需要再次注入服务文件,只需要在组件的构造函数中调用就可以,`@Inject('ApiServiceAlias') private aliasService: any,`
- 这样的构造函数的特点是工厂函数只会被执行一次,也就是在应用启动时候,如果遇到类似要随着浏览器窗口宽度变化要调用不同服务的场景就不合适了.

### 组件内的工厂函数
- 把要调用的服务在组件内注入,这样的工厂函数是随需创建的,比如调整浏览器宽度,不需要重新刷新页面点击按钮就会重新执行工厂函数,可以完美解决上面的问题;

	```ts
	import { Component, OnInit, ReflectiveInjector, Inject } from '@angular/core';
	  userInjectors(): void {
		const injector: any = ReflectiveInjector.resolveAndCreate([ViewPortService, {
		  provide: 'OtherSizeService',
		  useFactory: (viewport: any) => {
			return viewport.determineService();
		  },
		  deps: [ViewPortService]
		}]);
		const sizeService: any = injector.get('OtherSizeService');
		sizeService.run();
	  }
	```

## 替换值
- 使用依赖注入的另一个理由是在运行期间改变被注入对象的硬编码值,
- 适用于单元测试或集成测试.
- 比如在开发环境下运行该应用,可能会接触与生存环境下不同的API服务器.
- 这时候要允许调用者定义或改写API的URL

	```ts
	export const API_URL = 'API_URL';

	export class ApiService {
		constructor(@Inject(API_URL) private apiUrl: string) { }

		get(): void {
			console.log(`Calling ${this.apiUrl}/endpoint...`);
		}
	}

	const isProduction = false;
	{ provide: API_URL, useValue: isProduction ? 'https://production-api.sample.com' : 'http://dev-api.sample.com' }
	```
- 通过设置`app.moudle.ts`内的`isProduction`的布尔值来确认`API_URL`的值,这样就可以在开发环境和生产环境分别设置不同的值.
