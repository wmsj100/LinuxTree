---
title: JS函数复制
date: 2016-03-24 12:18:58
tags: [复制]
categories: Dynamic
---
> 有俩种赋值过程，基础类型复制和引用类型复制；
> 对象和数值通吃；
---
<!-- more -->
```
 function cloneObj(obj) {
        //此处相当于var obj = a;复制了a的指针；
        var str = {};
        //创建一个空对象，等同于str=new Object();
        if (obj instanceof Array) {
            str = [];
            //判断如果obj为数组，就创建空数组；
        }
        for (var key in obj) {
            if (typeof obj[key] === "object") {
                //判断obj元素是不是对象，
                str[key] = cloneObj(obj[key]);
                //此处复制的是cloneObj中参数obj的内部元素；
            } else {
                str[key] = obj[key];
                //如果参数不是对象，直接赋值；
            }
        }
        return str;
    }

    var a = ["name", 123, null, undefined, true, ["name", "wmsj"], {
        "name": "wmsj",
        "hello": "world",
        "num": [1, 2, 3]
    }];
    var b = cloneObj(a);
    //["name", 123, Object, undefined, true, Array[2], Object]
    //b[5][1]="hao"		
    //此时就只有b改变了，a没有变。
```
### 简单类型赋值：
1. 直接赋值：
```
function cloneObj(obj){
    	var val=obj;
    	return val;
    }    
    var a=["name","wmsj","hello"];
    var b=cloneObj(a);
    console.log(b);
```
1. slice方式：
```
function cloneObj(obj){
    	var val=obj.slice(0);
    	return val;
    }    
    var a=["name","wmsj","hello"];
    var b=cloneObj(a);
    console.log(b);
```
3. concat方式：
```
function cloneObj(obj){
    	var val=[];
    	val=obj.concat();
    	return val;
    }    
    var a=["name","wmsj","hello"];
    var b=cloneObj(a);
    console.log(b);
```
4. for循环赋值；
```
function cloneObj(obj){
    	var val=[];
    	for(var i=0;i<obj.length;i++){
    		val[i]=obj[i]
    	}
    	
    	return val;
    }    
    var a=["name","wmsj","hello"];
    var b=cloneObj(a);
    console.log(b);
```
> #### 这些方式都可以复制基础类型，但是碰到引用类型时候就歇菜了，改变一个值，同时也会改变另一个值；
### 深度复制：
通过——arguments.callee()——来复制当前的函数的参数；
```
var a=["name","hello",{"name":"wmsj","hello":"world","num":[1,2,3]}];
    var b=cloneObj(a);
    function cloneObj(obj){
    	var str={};
    	if(obj instanceof Array){
    		str=[];
    	}
    	for(var key in obj){
    		str[key]=typeof obj[key]==="object"? arguments.callee(obj[key]):obj[key];
    	}
    	return str;
    }
```
