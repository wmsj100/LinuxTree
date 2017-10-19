---
title: jQuery事件代理
date: 2016-07-05
tags: [jQuery]
categories: Dynamic
---

事件绑定使用`on`，解绑使用`off`,也可以使用事件代理形式，其中`on`接受3个参数，分别为`事件类型，接受响应的目标元素， 响应函数。`

```javascript
$("body").on("click", ".p3", function(e) {
    console.log(e.target);
});
```

创建了一个绑定在`body`上面的函数，但是只有通过`.p3`触发的事件才会触发函数。

```javascript
function fn() {
    $("div").toggle();
}

$("#bind").on("click", function() {
    $("body").one("click", "#theone", fn).find("#theone").text("show");
});
$("#unbind").on("click", function() {
    $("body").off("click", "#theone", fn).find("#theone").text("hidden");
})
```

这个函数有以下一个问题，首先我如何避免重复绑定事件。
解除事件时候，是没有问题的，
关于重复绑定事件，我暂时先不想管，