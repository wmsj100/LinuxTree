---
title: jQuery基础知识解析
date: 2016-06-20
tags: [jQuery]
categories: Dynamic
---

`jQuery`和`DOM`的互相转换：
- `jQuery` => `DOM` -- var a = $a[0] / var a = $a.get(0);
- `DOM` => `jQuery` -- var $a = $(a);

```javascript
        var $cr = $("#cr");
        $cr.click(function(){
            if($cr[0].checked){
                console.log("hello");
            };
        });
//同样效果的jquery代码
        var $cr = $("#cr");
        $cr.click(function(){
            if($cr.is(":checked")){
                console.log("hello jj")
            };
        });
```

`is(":checked")` -- 是`jQuery`的方法，判断`jQuery`方法是否被选中。

`jQuery.noConflict()` -- 把`$`控制权交出去。
`var _ = jQuery.noConflict()` -- 创建自定义快捷方式`_`。