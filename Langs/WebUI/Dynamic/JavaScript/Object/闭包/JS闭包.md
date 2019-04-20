---
title: JS闭包
date: 2016-3-26 16:20:19
tags: [JavaScript,闭包,术语]
categories: Dynamic
---

#### 什么是闭包？由什么作用

参考文献-[JavaScript闭包 取for循环i ](http://blog.csdn.net/nx8823520/article/details/6858126)

闭包——就是函数内部的函数，它由俩部分组成，函数，以及创建该函数时的环境；环境由闭包创建时在作用域中任何局部变量组成。
<!-- more -->
闭包的作用：闭包可以读取函数内部的局部变量并且把值保存在内存中，从而可以从外部访问这些局部变量。

#### setTimeout 0由什么作用

setTimeout设置延迟为0表示该函数在最后运行，而且是前面函数执行完成之后马上执行。

#### 下面的代码输出多少？修改代码让`fnArr[i]()` 输出 i。使用**两种以上的**方法

```javascript
 var fnArr = [];
    for (var i = 0; i < 10; i ++) {
        fnArr[i] =  function(){
            return i;
        };
    }
    console.log( fnArr[3]() );  //
```

- 通过闭包返回一个函数：

```javascript
    var fnArr = [];
    for (var i = 0; i < 10; i++) {
        fnArr[i] = (function(num) {
            return function() {
                return num;
            }
        }(i))
    }	//通过自执行函数来形成闭包
    console.log(fnArr[5]());	//5
```

- 通过闭包返回一个函数的局部变量：

```javascript
 var fnArr = [];
    for (var i = 0; i < 10; i ++) {
    	(function(){
    		var temp=i;	//定义局部变量；
    		fnArr[i]=function(){
    			return temp;
    		}
    	}())
    }
    console.log( fnArr[3]() );  //
```

- 通过给函数的属性赋值：

```javascript
 var fnArr = [];
    for (var i = 0; i < 10; i ++) {
        (fnArr[i] =  function f(){
            return f.i;
        }).i=i;
    }
    console.log( fnArr[3]() );
```

- 通过数组push方法：

```javascript
var fnArr = [];
        for (var i = 0; i < 10; i++) {
            fnArr.push(i);
        }
        console.log(fnArr[3]);	//3
```

#### 使用闭包封装一个汽车对象，可以通过如下方式获取汽车状态
```javascript
var Car = //todo;
Car.setSpeed(30);
Car.getSpeed(); //30
Car.accelerate();
Car.getSpeed(); //40;
Car.decelerate();
Car.decelerate();
Car.getSpeed(); //20
Car.getStatus(); // 'running';
Car.decelerate(); 
Car.decelerate();
Car.getStatus();  //'stop';
//Car.speed;  //error
```

代码如下：

```javascript
var Car = (function() {
    var speed = 0;

    function setSpeed(num) {
        speed = num;
    }

    function getSpeed() {
        return speed;
    }

    function accelerate() {
        speed += 10;
    }

    function decelerate() {
        speed -= 10;
    }

    function getStatus() {
        var status;
        if (speed > 0) {
            status = "running";
            return status;
        } else {
            status = "stop";
            return status;
        }
    }
    return {
        'setSpeed': setSpeed,
        'getSpeed': getSpeed,
        'accelerate': accelerate,
        'decelerate': decelerate,
        'getStatus': getStatus,
        'speed': 'error' //这个没有意义吧
    }
}())
Car.setSpeed(30);
Car.getSpeed(); //30
Car.accelerate();
Car.getSpeed(); //40;
Car.decelerate();
Car.decelerate();
Car.getSpeed(); //20
Car.getStatus(); // 'running';
Car.decelerate();
Car.decelerate();
Car.getStatus(); //'stop';
Car.speed; //error	//这个没有意义吧
```

#### 写一个函数使用`setTimeout`模拟`setInterval`的功能

```javascript
var num=0;
function count(){
setTimeout(function(){
	num+=1;
	console.log(num);
	count();
},1000)	
}//每隔1s数字num加1，模拟的时自动计数
```

#### 写一个函数，计算setTimeout最小时间粒度

```javascript
function minTime() {
    var start = Date.now();
    console.log('start-time', start);
    var num = 0;
    (function count() {
        var plus = setTimeout(function() {
            num += 1;
            console.log(1);
            count();

        }, 0);
        if (num === 1000) {
            clearTimeout(plus);
            var end = Date.now();
            console.log('end-time', end);
            var space = (end - start) / 1000;
            console.log(space);
        }
    }())
}
minTime() //4.878
```

#### 下面这段代码输出结果是? 为什么?

```javascript
var a = 1;
setTimeout(function(){
    a = 2;
    console.log(a);	//2-最后显示
}, 0);
var a ;
console.log(a);	//1
a = 3;
console.log(a);	//3
```

解析如下：

```javascript
var a = 1;
var a ;
console.log(a);	//1
a = 3;
console.log(a);	//3
setTimeout(function(){
    a = 2;
    console.log(a);	//2-最后显示
}, 0);	//延时为0时候，函数会最后执行。
```

#### 下面这段代码输出结果是? 为什么?

```javascript
var flag = true;
setTimeout(function(){
    flag = false;
},0)
while(flag){}
console.log(flag);
```

解析如下：

```javascript
var flag = true;
while (flag) {}	
//因为flag=true，条件为真，所以while循环会一直无限循环；
console.log(flag);	//不会进行到这一步
setTimeout(function() {
    flag = false;
}, 0)	
//setTimeout函数最后执行，而while在一直循环，不会结束
//所以延时函数也不会被执行，
```

#### 下面这段代码输出？如何输出`delayer: 0, delayer:1...`

```javascript
for(var i=0;i<5;i++){
    setTimeout(function(){
         console.log('delayer:' + i );
    }, 0);
    console.log(i);
}
```

代码如下：

```javascript
for(var i=0;i<5;i++){
    setTimeout((function(){
         console.log('delayer:' + i );
    }()), 0);
    console.log(i);
}//只是让setTimeout的函数变为自执行函数就输出了。
```

加一层闭包，i以函数形式传递给内层

```javascript
for(var i=0;i<5;i++){
(function(tags){
	    setTimeout(function(){
         console.log('delayer:' + tags );
    }, 0);
}(i));
  console.log(i);	//0 1 2 3 4
}//delayer:0 delayer:1 delayer:2 delayer:3 delayer:4
```

加一层闭包，i以函数内局部变量传递给内层

```javascript
    for (var i = 0; i < 5; i++) {
        (function() {
            var temp = i;	//定义局部变量
            setTimeout(function() {
                console.log('delayer:' + temp);
            }, 0);
        }());
      console.log(i);	0 1 2 3 4
    }	//delayer:0 delayer:1 delayer:2 delayer:3 delayer:4
```

