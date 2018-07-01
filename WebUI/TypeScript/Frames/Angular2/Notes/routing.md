---
title: 路由 
date: 2018-07-01 17:07:01	
modify: 
tag: [route]
categories: Angular2 
author: wmsj100
mail: wmsj100@hotmail.com
---

# 路由

## 概述
- 现在前端的发展趋势是`SPA(Simple Page Application)`
- 通过试图切换来展示不同内容

## 解析
- 在`app.module.ts`中引入`RouterModule`
	- `import { RouterModule } from '@angular/router';`
- 配置路由
	```ts
	RouterModule.forRoot([
      {
        path: 'login',
        component: LoginComponent
      }
    ])
	```
- 属性解析
	- path: 路由器会用它来匹配路由中指定的路径和浏览器地址中的当前路径
	- component: 导航到此路由时,路由器需要创建的组件`LoginComponent`
	- redirecTo: 重定向到某个`path`,比如用户输入不存在的路径时重定向到首页
	- pathMatch: 路径的字符匹配策略
	- children: 子路由数组
- 创建插头`outlet`来装载组件
	- 在`app.component.html`中插入`<router-outlet></router-outlet>`
- 定义重定向路径
	```ts
	import { Routes, RouterModule } from '@angular/router';
	import { LoginComponent } from './login/login.component';

	export const routes: Routes = [
		{
			path: '',
			redirectTo: 'login',
			pathMatch: 'full'
		},
		{
			path: 'login',
			component: LoginComponent
		}
	];

	export const routing = RouterModule.forRoot(routes);
	```

## 技巧
- 定义路由文件时候出错后重新修改了文件,但是无论清除缓存刷新页面还是关闭浏览器重新开启,都不能使修改后的路由文件生效,这时候重启服务`ng serve`就可以
- 其他类似情况也可以通过这种方式来避免


## 参考
- [Angular2学习三](https://www.jianshu.com/p/86c6249a2069)
