---
title: ngModel报错
date: 2018-07-01 12:57:42	
modify: 
tag: [error]
categories: Angular2 
author: wmsj100
mail: wmsj100@hotmail.com
---

# ngModel报错

## `Can't bind to 'ngModel' since it isn't a known property of 'input'...`
- 如果出现上面的报错,说明是`ngModel`模块调用有问题,这个模块需要依赖`FormsModule`
- 在`app.module.ts`中引入`FormsModule`
	```ts
	import { FormsModule } from '@angular/forms';

	imports: [
		BrowserModule,
	    FormsModule,
	  ],
	```
- 再次调用就ok了


## 参考
- [ngModel报错解决](https://blog.csdn.net/h363659487/article/details/78619225)
