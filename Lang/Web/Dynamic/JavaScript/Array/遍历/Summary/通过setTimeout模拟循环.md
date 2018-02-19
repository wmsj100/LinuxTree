---
title: 通过setTimeout模拟循环
date: 2016-06-12
tags: [Array]
categories: Dynamic
---

```javascript
var a = [2,1,3,4,23,4];
function copyLoop(arr,process,callback){
    var newArr = arr.concat();  //获取克隆数据
    setTimeout(function(){
        process(newArr.shift());
        if(newArr.length){
            setTimeout(arguments.callee,25);
        }else{
            callback();
        }
        },25);
}
function process(num){
    document.body.innerHTML += num + "<br>";
}
function callback(){
    document.body.innerHTML += "over";
}
copyLoop(a,process,callback);
```
