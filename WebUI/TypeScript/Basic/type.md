---
title: 类型别名 
date: 2018-06-23 23:11:50	
modify: 2018-06-23 23:11:53	
tag: [type]
categories: TypeScript
author: wmsj100
mail: wmsj100@hotmail.com
---

# 类型别名

## 概述
- 类型别名用来给类型起个新名字, 常用于联合类型.
```ts
type Name = string;
type NameFun = () => string;
function getName(n: Name | NameFun): Name{
    if(typeof n === 'string'){
        return n;
    } else {
        return n();
    }
}
```

## 参考
- [类型别名](https://ts.xcatliu.com/advanced/type-aliases.html)
