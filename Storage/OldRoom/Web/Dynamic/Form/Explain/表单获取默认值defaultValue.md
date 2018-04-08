---
title: 表单获取默认值defaultValue
date: 2016-07-04
tags: [jQuery]
categories: Dynamic
---

对于表单的文本框，如果想要判断值是否改变，可以通过`defaultValue`来获取值。

```html
<input type="text" value="表单获取默认值defaultValue">

<script>
    var form = $("input:last");
    var val = form.val();
    if(val === form[0].defaultValue){
        console.log("没有改变")
    }
</script>
```


