---
title: end返回上一个选择器
date: 2016-07-07
tags: [jQuery]
categories: Dynamic
---

`end`方法会返回选择器链条的上一个选择集。
`end`方法也可以连续使用以此来进行选择器的回溯

看下面这个超级牛逼的链条

```javascript
$("tbody").on("click", "tr", function(){
    $(this).siblings().removeClass("selected")
            .find(":radio:checked").prop("checked", false)
            .end()
            .end()
            .addClass("selected")
            .find(":radio").prop("checked",true);
});
```

