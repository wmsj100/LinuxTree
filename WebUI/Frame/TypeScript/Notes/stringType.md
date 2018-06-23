---
title: 字符串类型 
date: 2018-06-23 23:15:47	
modify: 2018-06-23 23:15:49	
tag: [string]
categories: TypeScript
author: wmsj100
mail: wmsj100@hotmail.com
---

# 字符串

## 概述
- 字符串字面量类型用来约束取值只能是某几个值中的一个;

```ts
type EventNames = 'click' | 'scroll' | 'mousemove';
function handleEvent(ele: Element, event: EventNames){
    //
}

handleEvent(document.getElementById('hello'), 'scroll');
```
- 上例中定义了一个字符串字面量类型,它只能取三种类型中的一种,否则编译器会报错.

## 参考
- [字符串字面量](https://ts.xcatliu.com/advanced/string-literal-types.html)
