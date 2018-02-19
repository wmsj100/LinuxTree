---
title: 匿名函数与this
date: 2016-06-22
tags: [Function]
categories: Dynamic
---

匿名函数的执行环境具有全局性，`this`通常指向`window`。

```javascript
    var name = "wmsj";
    var obj = {
        name: "nicholas",
        getName: function(){
            return function(){
                return this.name;
            }();
        }
    }
    obj.getName();
```

关于自执行函数，可以使用`fn()`也可以使用`(fn)()`;

每个函数被调用过程中都会自动获取俩个特殊变量`this`、`arguments`。内部函数访问这俩个变量时只会搜索到其活动对象，不会搜索外层函数。而匿名函数是具有全局性的，所以此时`this`指向`window`。
但是可以把外层函数的`this`保存到一个变量，然后传递给`闭包`的`匿名函数`，这样就可以访问外层函数的`this`了

```javascript
    var name = "wmsj";
    var obj = {
        name: "nicholas",
        getName: function(){
            var me = this;
            return function(){
                return me.name;
            }();
        }
    }
    obj.getName();  //"nicholas"
```

`arguments`也是这样的，需要通过变量来传递外层函数的`arguments`

```javascript
    var name = "wmsj";
    var obj = {
        name: "nicholas",
        getName: function(num){
            var me = this;
            var args = arguments;
            return function(){
                console.log(args)
                return me.name;
            }();
        }
    }
    obj.getName(10);    //10
```

`this`的值也可能会意外的被改变

```javascript
    var name = "wmsj";
    var obj = {
        name: "nicholas",
        getName: function(){
                return this.name;
            }
        }
    obj.getName();  //"nicholas";
    (obj.getName)();    //"nicholas";
    (obj.getName = obj.getName)();  //"wmsj"
```


