---
title: contains也可以通过拼装字符串接受变量
date: 2016-07-07
tags: [jQuery]
categories: Dynamic
---

一般来说，`contains`只是包含文本字符串进行内容筛选的，但是也可以接受变量，只不过需要进行字符串的拼接

[效果](http://jsbin.com/zapeqoq/6/edit?html,output)

```javascript
$("input.search").keyup(function(){
        var val = $(this).val();
        console.log(val);
        $("tbody tr").hide().filter(":contains(" + val + ")").show();
    });
```

上面这个是一个表格的搜索框内容实例，其中`contains`接受的就是通过字符串拼接的一个变量`val`。
**如果直接输入`:contains(val)`-- 这样是以字符串`val`进行内容匹配的。**
这一点需要切记。