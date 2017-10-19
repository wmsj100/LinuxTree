---
title: setTimeout死循环
date: 2016-3-25 15:15:27
tags: [函数,时间]
categories: Dynamic
---
---
<!-- more -->
```javascript
var t = true;
setTimeout(function(){
  t = false;
},1000);
while(t){ };
alert("end");
```

函数解析：

- 首先定义t=true，然后执行到setTimeout，但是这个函数是延迟1s执行的，所以直接跳过这个函数，开始执行while函数，但是while是个无限循环的函数，空值，就像下面这个一样：

```javascript
t = true;
while (t) {}	//浏览器会一直进行计算，直至内存耗尽；
console.log(1);
```

- 所以即便是过了1秒，因为while函数还在执行，所以setTimeout函数就需要一直等待，所以alert函数也不会执行，
- 所以这个就是个无限循环函数。