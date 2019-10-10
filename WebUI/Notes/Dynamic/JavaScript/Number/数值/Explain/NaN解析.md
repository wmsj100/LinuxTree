---
title: NaN解析
date: 2016-06-08
tags: [Number]
categories: Dynamic
---

`NaN` -- 表示非数字，主要出现在将字符串解析成数字的场合。
`NaN` -- 表示一种特殊的数值，依然属于`Number` `typeof NaN` => `Number`;
`NaN` -- 不等于任何值，包括自己；   `NaN === NaN` => `false`;

由于数组的indexOf方法，内部使用的是严格相等运算符，所以该方法对NaN不成立。
`[NaN].indexOf(NaN)` => `-1`;

`NaN`与任何数(包括自己)的运算都是`NaN`。

`isNaN()` -- 只对数值有效，如果传入一个非数字，首先会进行数值转换，转换为数字，然后进行判断，所以如果传入的是一个字符串，进行转换的时候变为`NaN`，然后进行判断，就会返回`true`。

```javascript
isNaN({});  //true;
isNaN([]);  //false;
isNaN([1,2]);   //true;
isNaN([2]);     //false;
isNaN(['2']);     //false;
```

判断一个数值是不是`NaN`的有效方法
```javascript
    function myIsNaN1(val){
        return typeof val === "number" && isNaN(val) === true;
    }

    function myIsNaN2(val){
        return val !== val;
    }
```

上面的俩个函数都可以进行判断，但是第二个更简洁一些。