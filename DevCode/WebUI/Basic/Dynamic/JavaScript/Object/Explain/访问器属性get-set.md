---
title: 访问器属性get-set
date: 2016-16-20
tags: [Object]
categories: Dynamic
---

访问器属性有`get, set`，`get`是读取属性时候触发的条件，`set`是写入属性时候触发的条件。

```javascript
        var info = {
            _year: 2004,
            edit: 1
        };
        Object.defineProperty(info, "year", {

            get: function() {
                return this._year;
            },

            set: function(year) {
                
                if (year > this._year) {
                    this.edit += year - this._year;
                    this._year = year;
                }
            }
        });
        info.year = 2006;
        info.edit = 3;
        info;   //Object {_year: 2006, edit: 3}
```

这是访问器属性的常见方法，即设置一个属性会导致其它属性变化。

在这个标准之前有俩个非标准的方法，`__defineGetter__`, `__defineSetter__`;

```javascript
    var info = {
            _year: 2004,
            edit: 1
        };
    info.__defineGetter__("year",function(){
            return this._year;
        });
        info.__defineSetter__("year",function(year){
            if (year > this._year) {
                    this.edit += year - this._year;
                    this._year = year;
                }
        });
        info.year = 2006;
        info.edit = 3;
        info;   //Object {_year: 2006, edit: 3}
```

`get`和`set`可以单独设置，如果值设置`get`表示属性是只读的，不能写入，反之则表示属性是只写的，如果读取不会返回值。

### 同时设置多个属性

属性这时候只有俩个参数，属性的对象和要添加和修改的属性对象集合。

```javascript
    var info = {};

    Object.defineProperties(info, {
        _year: {
            writable: true,
            value: 2004
        },
        edit: {
            writable: true,
            value: 1
        },
        year: {
            get: function() {
                return this._year;
            },
            set: function(year) {
                if (year > this._year) {
                    this.edit += year - this._year;
                    this._year = year;
                }
            }
        }
    });

    info.year = 2006;
    info.edit = 3;
    info;   //Object {_year: 2006, edit: 3}
```

### 读取属性的特性 -- `Object.getOwnPropertyDescriptor`

这个方法接收俩个参数，要读取的属性的对象名称和要读取的属性；

```javascript
    a=Object.getOwnPropertyDescriptor(info,"_year");
    Object {value: 2006, writable: true, enumerable: false, configurable: false}
    b=Object.getOwnPropertyDescriptor(info,"edit");
    Object {value: 3, writable: true, enumerable: false, configurable: false}
    c=Object.getOwnPropertyDescriptor(info,"year");
    Object {enumerable: false, configurable: false}
```

对于直接通过字面量的形式创建的对象也可以访问其属性的特性

```javascript
    var people = {
        name: "wmsj",
        age: 10
    }
    a = Object.getOwnPropertyDescriptor(people, "name");
    Object {value: "wmsj", writable: true, enumerable: true, configurable: true}
```

通过实例无法查看原型的属性特征，必须通过实例的`__proto__`来查看

```javascript
Object.getOwnPropertyDescriptor(a,"name")
undefined
Object.getOwnPropertyDescriptor(a.__proto__,"name")
Object {value: "wmsj", writable: true, enumerable: true, configurable: true}
```


