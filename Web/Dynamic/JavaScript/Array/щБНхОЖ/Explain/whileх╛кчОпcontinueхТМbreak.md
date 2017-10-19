---
title: while循环continue和break
date: 2016-06-08
tags: [遍历,Array,JavaScript]
categories: Dynamic
---

`while`循环的条件判断是在内部进行的，如下

```javascript
var i = 0;
while(i<10){
    console.log(i);
    i++;
}
```
但是如果把`i++`给遗忘了，那么这时候`while`就会进入无限循环，因为虽然有结束条件，但是`i=0`，所以页面知道卡死状态。

当然了，如果进行`break`，或者是`continue`时候也是一样的。

```javascript
var i = 0;
while(i<10){
    if(i === 3){
        continue;
    }
    console.log(i);
    i++;
}
```

上面这个判断看似没有问题，但是其实页面会进入无限循环，直到卡死状态。
刚开始会输出1，2，然后当`i=3`的时候，进入`if`条件判断，所以跳过这一次循环，但是此时`i`依然是3，没有递增，所以下一次还会进入`if`条件判断，依然会跳过，就这样一直进行跳过和判断，直到页面卡死，
所以需要给if条件添加一个条件，在跳过的时候`i++`，这样下次判断`i`的时候i就是4了。

```javascript
var i = 0;
while(i<10){
    if(i === 3){
        i++;
        continue;
    }
    console.log(i);
    i++;
}

//或者是
var i = 0;
while(i<10){
    i++;
    if(i === 3){
        continue;
    }
    console.log(i);
}
//但是这样会影响到i的输出值，所以还是上面的好。
```
