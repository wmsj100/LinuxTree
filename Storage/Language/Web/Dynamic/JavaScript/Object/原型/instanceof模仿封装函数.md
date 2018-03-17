---
title: instanceof模仿封装函数
date: 2016-05-28
tags: [Object,原型]
categories: Dynamic
---

- 这个函数封装的有问题，只能判断一次，因为函数是直接通过重新赋值原型来实现的原型判断，这样就切断了函数和原型之间的连接
- 比如先判断`instance(a, Person)`，然后再判断`instance(a, Object)`，重新会过头来判断`instance(a, Person)`就会发现输出了`false`

```javascript
function Person(name) {
    this.name = name;
}
Person.prototype.say = function() {
    console.log(this.name);
}
var a = new Person("wmsj");
var b = 0;
console.log(instance(a, Person)); //true
console.log(instance(a, Object)); //true
console.log(instance(a, Array)); //false
console.log(instance(b, Number)); //true
function instance(obj, func) {
    do {
        if (obj.__proto__ === func.prototype) {
            return true;
        }
        if (!obj.__proto__) {
            return false;
        }
    }
    while (obj.__proto__ = obj.__proto__.__proto__);
    return false;
}
```
