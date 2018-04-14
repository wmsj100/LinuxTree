---
title: 关于立即执行函数SetTimeout的误区
date: 2016-07-23
tags: ["Javascript"]
categories: Dynamic
---
https://segmentfault.com/q/1010000006056646
代码1：
for (var i = 0; i < 5; i++) {
setTimeout((function(){

console.log("delayer:" + i);
})(),0);
console.log(i);
}

问题：
代码1:setTimeout(立即执行函数,0)循环里面不是有console.log(i),为什么不是先执行console.log(i)而是先执行setTimeout(立即执行函数,0)

答：
这样的立即执行函数，直接运行了，这后面的console.log和setTimeout有什么关系了。。

调用setTimout的时候，相当于调用立刻执行函数返回的undefinde