---
title: Infinity解析
date: 2016-06-08
tags: [Number]
categories: Dynamic
---

`Infinity` -- 表示无群大，出现的场景是要么数值超出了JS的表示范围，要么是一个非零数除以0；

```javascript
Math.pow(2,10000);  //Infinity;
2/0;    //Infinity;
-2/-0;  //Infinity;
0/0;    //NaN;
```

`-Infinity` -- 表示无群小，出现的场景是要么数值超出了JS的数值下限，要么是非零除以`-0`，
因为JS的小数位数是有极限数量的，如下`Math.pow(0.2,10000)` => `0`;

```javascript
2/-0;   //-Infinity;
```

数值正向溢出和负向溢出和被`0`除，JS都不会报错。而是返回`Infinity`；

`Infinity`大于一切数值，除了`NaN`；`-Infinity`小于一切数值，除了`NaN`；`Infinity`和`NaN`比较总是返回`false`；

```javascript
Infinity > NaN; //false;
Infinity < NaN; //false;
-Infinity > NaN;    //false;
-Infinity < NaN;    //false;
```

`Infinity`的四则运算规则；

```javascript
5 + Infinity;   //Infinity
5 - Infinity;   //-Infinity;
5 * Infinity;   //Infinity;
5 / Infinity;   //0;
```

`Infinity`加上或乘以`Infinity`的值还是`Infinity`,减去或除以的值为`NaN`；

```javascript
Infinity + Infinity;    //Infinity
Infinity * Infinity;    //Infinity
Infinity - Infinity;    //NaN;
Infinity / Infinity;    //NaN;
```

`isFinite` -- 用于检查某个值是不是正常值，而不是检查是不是`Infinity`；

```javascript
isFinite(Infinity); //false
isFinite(NaN);  //false
isFinite(null); //true
isFinite(undefined);    //false
```

