---
title: Boolean 布尔类型
date: 2016-04-30
tags: [布尔,JavaScript]
categories: Dynamic
---

```javascript
var a = new Boolean(false);
var b = a && true;
var c = false;
var d = c && true;
console.log(b); //true;
console.log(d); //false;
console.log(typeof(a));	//object;
console.log(typeof(c));	//boolean;
console.log(a instanceof Boolean);	//true;
console.log(c instanceof Boolean);	//false;
```

在这个例子中，我们使用 false 值创建了一个 Boolean 对象。然后，将这个对象与基本类型值 true构成了逻辑与表达式。在布尔运算中， false && true 等于 false 。可是，示例中的这行代码是对falseObject 而不是对它的值（ false ）进行求值。前面讨论过，布尔表达式中的所有对象都会被转换为 true ，因此 falseObject 对象在布尔表达式中代表的是 true 。结果， true && true 当然就等于 true 了。

理解基本类型的布尔值与 Boolean 对象之间的区别非常重要——当然，我们的建议是永远不要使用 Boolean 对象。

