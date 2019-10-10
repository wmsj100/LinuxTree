---
title: 关于深度复制clone
date: 2016-07-12
tags: [jQuery]
categories: Dynamic
---

正常情况下,可以通过`clone(true)`来复制节点并且包含节点绑定的事件.
但是这个节点必须是使用`jQuery`的方法绑定的事件,如果是通过`js`绑定的事件,那么就无法复制事件.

```html
<div class="wrap1">
    <div class="wrap">
        <h3>hello world</h3>
    </div>
</div>

<script>
    var wrap = document.querySelector(".wrap");
    wrap.onclick = function(){
        console.log(this.innerHTML);
    }
</script>
```

上面这个方法就无法达到预期的效果,点击没有效果.

但是对于下面的,通过`jQuery`绑定的事件就可以.

```javascript
$(".wrap").click(function(){
    console.log($(this).html());
})
$(".wrap").clone(true).appendTo("body");
```

所以以后,当使用`jQuery`库时候,就不要使用原生`js`的方法.因为原生`js`无法复制节点的事件.