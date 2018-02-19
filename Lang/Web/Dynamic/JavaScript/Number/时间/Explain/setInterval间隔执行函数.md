---
title: setInterval间隔执行函数
date: 2016-06-22
tags: [Number]
categories: Dynamic
---

间歇调用和超时调用类似，只不过它是按照指定的时间间隔执行代码，直至间歇调用被取消或者页面被卸载。
因为间歇调用可能会出现前面函数没有执行完成，后面函数又开始调用的情景，所以最好不要使用间歇调用。

```javascript
    var num = 0,
            clock,
            max = 10;
    function increateNum(){
        num++;
        console.log(num);
        if(num === max){
            clearInterval(clock);
        }
    }
    clock = setInterval(increateNum,500);
```

使用延时函数实现同样效果

```javascript
    function fn1(){
        num++;
        console.log(num);
        if(num < max){
            setTimeout(arguments.callee,500);
        }else{
            clearTimeout(clock);
        }
    }
    clock = setTimeout(fn1,500);
```

