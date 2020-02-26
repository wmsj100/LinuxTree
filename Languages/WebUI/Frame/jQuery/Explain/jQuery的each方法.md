---
title: jQuery的each方法
date: 2016-07-08
tags: [jQuery]
categories: Dynamic
---

`jQuery`中的`each`有俩个使用场景，一个是对前面的选择器筛选出的集合，对集合中的每个元素进行操作就可以使用`each`

`$("ul li").each(function(){console.log($(this).text())})`

`jQuery`中的另一个`each`使用场景是对数组和对象的遍历操作,这时候`each`是全局函数

```javascript
    var a = {
        name: "wmsj",
        age: 10
    }
    $.each(a, function(index, item){
        console.log(item);
    })
```


