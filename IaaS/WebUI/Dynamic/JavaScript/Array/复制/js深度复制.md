---
title: js深度复制
date: 2016-03-24 12:18:58
tags: [复制]
categories: Dynamic
---
---
<!-- more -->
```
(function () {  
            //深复制对象方法  
            var cloneObj = function (obj) {  
                var newO = {};  
  
                if (obj instanceof Array) {  
                    newO = [];  
                }  
                for (var key in obj) {  
                    var val = obj[key];  
                    newO[key] = typeof val === 'object' ? arguments.callee(val) : val;  
                }  
                return newO;  
            };  
  
            //测试  
            var a = {a:{a:123}},  
                    b = cloneObj(a);  
  
            b.a.a = 456;  
            alert(a.a.a);  
        })();  
```
