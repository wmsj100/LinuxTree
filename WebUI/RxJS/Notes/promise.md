---
title: observable vs promise
date: 2018-07-21 10:00:55	
modify: 
tag: [basic]
categories: RxJS 
author: wmsj100
mail: wmsj100@hotmail.com
---

# Observable vs Promise

## Observable
- `Observable`异步是push推动
```ts
let stream$ = Rx.Observable.from([1,2,3])
.map(v => v)
.filter(v => true)
.subscribe(
    v => { console.log( v) },
    e => { console.log( e ) },
    () => { console.log('complete') }
```
let stream$ = Rx.Observable.from([1,2,3])
.map(v => v)
.filter(v => true)
.subscribe(
    v => { console.log( v) },
    e => { console.log( e ) },
    () => { console.log('complete') }
);
```

## Promise
- 缺陷:
	- 不能生产多个值
	- 不能重试
	- 不能真正玩转其它异步思想
- `promise` 是pull推动
```ts
let promise = new Promise((resolve, reject) => {
    setTimeout(() => {
        resolve([1,2,3]);
    }, 3000);
});
promise.then((value) => {
    console.log(value);
}, null, () => {
    console.log('complete');
});
```

## 参考
- []()
