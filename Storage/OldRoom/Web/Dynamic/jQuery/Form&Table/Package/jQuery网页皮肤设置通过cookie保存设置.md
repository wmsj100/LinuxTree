---
title: jQuery网页皮肤设置通过cookie保存设置
date: 2016-07-07
tags: [jQuery]
categories: Dynamic
---

这个是通过给`css`的`link`链接添加`id=cssfile`，这样就可以通过选择器`$("#cssfile")`来选择到引用样式表的链接了。`$("#cssfile").attr("href")`,这样就可以通过按钮来确定要获取和设置的样式表。

因为这样的设置当刷新页面时候就无效了，所以需要把参数保存到cookie中，所以就使用了`jQuery`的`cookie`插件。

```skin_1.css
h3{
    background-color: yellow;
    color: #fff;
}
```

```skin_2.css
h3{
    background-color: blue;
    color: #fff;
}
```

```skin_3.css
h3{
    background-color: green;
    color: #fff;
}
```

```html
<style>
    ul{
    list-style-type: none;
    overflow: hidden;
}
li{
    float: left;
}
h3{
    display: block;
}
.selected{
    background-color: pink;
}
</style>

<button id="skin_1">btn1</button>
<button id="skin_2">btn2</button>
<button id="skin_3">btn3</button>

<h3>hello world</h3>

<script>
    $("button").click(function() {
        switchSkin(this.id);
    });
    var cookie = $.cookie("mycss"); // 刷新页面时候确定是否存在cookie。
    if (cookie) {
        switchSkin(cookie);
    }

    function switchSkin(skinName) {
        $("#" + skinName).addClass("selected").siblings().removeClass("selected");
        $("#cssfile").attr("href", "css/" + skinName + ".css");
        $.cookie("mycss", skinName);
    }
</script>
```

