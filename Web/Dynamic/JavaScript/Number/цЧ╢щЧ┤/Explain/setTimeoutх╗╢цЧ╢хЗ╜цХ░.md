---
title: setTimeout延时函数
date: 2016-04-21
tags: [JavaScript,函数,时间]
categories: Dynamic
---

`setTimeout`不是说持续时间段内发生的函数就不执行了，而是说再延时结束之后，期间发生的过程会马上执行，所以下面这个函数就不会是我期望的效果

```javascript
$(window).on("scroll", function() {
    setTimeout(function(){
        scrollTop = $(window).scrollTop();
        console.log(scrollTop);
        },1000);
    });
```

它不是说过1s之后才输出一次，而是过1s之后会瞬间输出期间发生的所有次数，

`setTimeout`第一个参数可以是字符串或者是函数。但是传递字符串可能导致性能损失。
第二个参数`毫秒数`表示过多长时间把当前任务添加到任务队列，如果任务队列为空，那么会立即指向任务，但是如果任务队列不为空，那么就要等待前面的任务都指向完毕之后在执行当前任务。