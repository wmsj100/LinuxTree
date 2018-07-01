---
title: 学习代码 
date: 2018-07-01 16:56:23	
modify: 
tag: [study]
categories: Angular2 
author: wmsj100
mail: wmsj100@hotmail.com
---

# 学习代码

## 概述
- `login.component.ts`
	```ts
	import { Component, OnInit, Inject } from '@angular/core';

	@Component({
	  selector: 'app-login',
	  templateUrl: './login.component.html',
	  styleUrls: ['./login.component.css']
	})
	export class LoginComponent implements OnInit {
	  username = 'wmsj100';
	  password = 'hello123';
	  constructor(@Inject('auth') private auth) { }

	  ngOnInit() {
	  }


	  onSubmit(formVal) {
		const state = this.auth.loginWithCredentials(formVal.login.username, formVal.login.password);
		console.log(state);
	  }
	}
	```
- `login.component.html`
	```html
	<div>
	  <form #formRef="ngForm" (ngSubmit)="onSubmit(formRef.value)">
		<fieldset ngModelGroup="login">
		  <input name="username" required class="ng-pristine ng-invalid ng-touched"  #usernameRef="ngModel" [(ngModel)]="username" minlength="3" type="text">
		  <div *ngIf="usernameRef.errors?.required">this is required</div>
		  <div *ngIf="usernameRef.errors?.minlength">Should be at least 3</div>
		  <input name="password" required #passwordRef="ngModel" [(ngModel)]="password" type="password">
		  <div *ngIf="passwordRef.errors?.required">this is required</div>

		  <button type="submit">Login</button>
		</fieldset>
	  </form>
	</div>
	```
- `login.component.css`
	```ts
	input.ng-invalid {
	  border: 3px solid red;
	}

	input.ng-valid {
	  border: 3px solid green;
	}
	```

## 参考
- [学习angular2](https://segmentfault.com/a/1190000008213984)
