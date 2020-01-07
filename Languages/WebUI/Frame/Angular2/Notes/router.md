---
title: 路由
date: 2018-07-14 20:53:57	
modify: 
tag: [router]
categories: Angular
author: wmsj100
mail: wmsj100@hotmail.com
---

# 路由

## 概述
- 路由的原理是通过锚点`#`来对页面进行定位,这样的路由文件也可以保存为书签,也可以前进后退.
- `HTML5`支持通过`js`来操作历史纪录,所以支持没有锚点的路由
- `Angular`默认支持`HTML5`无锚点路由方式

## 使用
- `import { Routes, RouterModule } from '@angular/router';` 调用前需要引入这俩个模块
- 定义路由配置:
	```ts
	export const routes: Routes = [
	  { path: '', redirectTo: 'home', pathMatch: 'full' },
	  { path: 'home', component: HomeComponent },
	  { path: 'about', component: AboutComponent },
	  { path: 'contact', component: ContactComponent },
	  { path: 'contactus', redirectTo: 'contact' },
	];
	@NgModule({
	  declarations: [
		AppComponent,
		HomeComponent,
		AboutComponent,
		ContactComponent,
	  ],
	  imports: [
		BrowserModule,
		FormsModule,
		ReactiveFormsModule,
		HttpModule,
		RouterModule.forRoot(routes)
	  ],
	  providers: [
		{ provide: LocationStrategy, useClass: HashLocationStrategy }
	  ],
	  bootstrap: [AppComponent],

	})
	class AppModule { }

	platformBrowserDynamic().bootstrapModule(AppModule).catch((err: any) => console.log(err));
	```

- 使用`<router-outlet>`来调用`RouterOutlet`指令
- 开发单页面绝对要杜绝的是页面重载
	```html
	<div>
	  <nav>
		<a href="">Navigation:</a>
		<ul>
		  <li>
			<a [routerLink]="['home']">Home</a>
		  </li>
		  <li>
			<a [routerLink]="['about']">About</a>
		  </li>
		  <li>
			<a [routerLink]="['contact']">Contact Us</a>
		  </li>
		</ul>
	  </nav>
	  <router-outlet></router-outlet>
	</div>
	```
- `http://localhost:4200/#/home` 通过页面地址调用

## 路由策略
- 定位策略:
- `Angular`默认策略为`PathLocationStrategy`,即`HTML5`路由,路由路径为常规路径
- `HashLocationStrategy`为锚点策略
- 如果在路由模式下直接刷新页面,向服务器索要的就不是根`URL`,而是`/about`等,因为服务器没有对应的页面,所以它会返回`404`
- 因此必须配置服务器将所有不存在的路由重定向到根`URL`

## 路由参数
- 在路径后面的参数前面添加冒号,类似`/route/:param`
- 获取参数需要引入`ActivatedRoute`
	```ts
	import { Component, OnInit } from '@angular/core';
	import {ActivatedRoute} from '@angular/router';

	@Component({
	  selector: 'app-artist',
	  templateUrl: './artist.component.html',
	  styleUrls: ['./artist.component.css']
	})
	export class ArtistComponent implements OnInit {
	  id: string;
	  constructor(
		private route: ActivatedRoute
	  ) {
		route.params.subscribe(params => {
		  this.id = params['id'];
		});
	  }

	  ngOnInit() {
	  }

	}
	```
## 参考
- []()
