---
title: undefined解释
date: 2016-3-25 23:24:28
tags: [函数,undefined,作用域]
categories: Dynamic
---

- undefined是可以被赋值的，当undefined不在全局作用域的时候，所以此时如果通过undefined来进行筛选数据就很容易出错，例如：
  <!-- more -->
```javascript
(function(){
	var undefined=3;
	console.log(undefined);
}())	//3
```

所以有时候就会看到void（）函数的出现，它是任何值都会返回参数undefined，所以可以通过这样的判断来查看undefined是否被赋值。

```javascript
void(0)===undefined
true
```

经过这样的判断就可以放心大胆的使用undefined。