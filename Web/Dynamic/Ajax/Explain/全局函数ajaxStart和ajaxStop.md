---
title: 全局函数ajaxStart和ajaxStop
date: 2016-07-09
tags: [Ajax,jQuery]
categories: Dynamic
---

对于页面的`ajax`请求，会在`ajax`执行前触发`ajaxStart`,当`ajax`数据接收完成之后会触发`ajaxStop`.
这俩个方法是全局的，只要页面有`ajax`在执行就会触发这俩个方法，
通常这俩个方法会绑定到`document`上面，

```html
<button>click</button>
<p class="res"></p>

<script>
    $("button").click(function(){
        $.get("10_01.js",function(){
            console.log(info);
        })
    });
    $(document).ajaxStart(function(){
        $(".res").text("hello world");
    });
    $(document).ajaxStop(function(){
        $(".res").text("end");
    });
</script>
```


