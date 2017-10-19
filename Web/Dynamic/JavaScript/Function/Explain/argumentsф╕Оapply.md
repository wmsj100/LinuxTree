---
title: arguments与apply
date: 2016-05-20
tags: [Function]
categories: Dynamic
---

### arguments

- `arguments` -- 包含了函数运行时候的所有参数，只能在函数内部起作用。
- `arguments` -- 除了可以读取参数之外还可以为参数赋值，但是严格模式不允许

```javascript
    function fn(a, b) {
        arguments[0] = 3;
        arguments[1] = 4;
        return a + b;
    }
    fn(1, 1); //7;
```

- `arguments.length` -- 读取调用函数时候传入的参数数量。
- `arguments` -- 是类数组，可以把它转换为数组，然后使用数组的方式。通常转换方式有俩种，即`遍历填充空数组`、`slice`；

- `arguments.callee` -- 获取对应的原函数

```javascript
    function fn(a,b){
        console.log(arguments.callee === fn);
    }
    fn();   //true
```

---


```javascript
function join() {
	return Array.prototype.join.apply(arguments);
}
```

```javascript
function join() {
	var str = "";
	for (var i = 0; i < arguments.length; i++) {
		str += "," + arguments[i];
	}
	return str.substr(1);
}
```

获取`arguments`的遍历数组，通常使用`slice`或者`遍历`

```javascript
    function fn(a, b) {
        var arr = Array.prototype.slice.apply(arguments);
        console.log(arr);
        return arr;
    }

    function fn2(a, b) {
        var arr = [];
        var i = arguments.length;
        while (i--) {
            arr.push(arguments[i]);
        }
        return arr.reverse();
    }
```
