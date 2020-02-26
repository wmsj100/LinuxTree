---
title: 对象
date: 2018-08-01 23:36:45	
modify: 
tag: [object]
categories: TypeScript
author: wmsj100
mail: wmsj100@hotmail.com
---

# 对象参数

## 概述
- `object`表示非基元素类型的类型
- 即不为`number, string, boolean, symbol, undefined`

## 范例
```ts
function create(data:object):void;
create({a:1}); //ok
create(null); //ok
create(32); //error
```

## 参考
- []()
