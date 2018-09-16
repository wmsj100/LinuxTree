---
title: jQuery表单多选框的bug以及解决办法attr  prop
date: 2016-07-06
tags: [jQuery]
categories: Dynamic
---

`jQuery`提供了新的方法`prop`来操作属性值,他返回的都是布尔值，在进行布尔值赋值或者是只是添加一个属性名称就会生效的情况下使用`prop`替代`attr`.

在设置值时候完全用`prop`替代`attr`。后者只是在用于查询`css`样式时候用。


`jQuery`的选择可以通过设置`attr`来选择。但是这个如果是在代码中设置一次性的改变是没问题的，如果是通过按钮来进行多次的切换操作的话就不行了。会出问题，只有第一次会正确显示，之后只会改变`DOM`,但是却不会显示被勾选的效果，而且通过`is(":checked")`竟然显示的是错误。

```javascript
        $(".btn2").click(function(){
            $(":checkbox:eq(1)").attr("checked", true);
        });
```

上面的代码只有第一次会生效，之后就只是改变dom，但是通过js查看没有任何效果，都是false。
这种情况就使用JS的原生方法- `this.checked` 通过返回的值来查看是否选中。
对于多个选项，如果是一次性的改变，那么通过代码可以很容易改变，但是如果不是一次性的操作，那么最好使用`each`进行遍历，并且通过原生JS来改变显示状况，如下。

```html
<form method="post" action="">
   你爱好的运动是？
   <br/>
    <input type="checkbox" name="items" value="足球"/>足球
    <input type="checkbox" name="items" value="篮球"/>篮球
    <input type="checkbox" name="items" value="羽毛球"/>羽毛球
    <input type="checkbox" name="items" value="乒乓球"/>乒乓球
   <br/>
    <input type="button" id="CheckedAll" value="全　选"/>
    <input type="button" id="CheckedNo" value="全不选"/>
    <input type="button" id="CheckedRev" value="反　选"/> 

    <input type="button" id="send" value="提　交"/> 
</form>

<script>
    $("#CheckedAll").click(function(){
    $("[name=items]:checkbox").each(function(){
        this.checked = true;
    })
});

$("#CheckedNo").click(function(){
    $("[name=items]:checkbox").attr("checked", false);  
    // 对于全部取消勾选，可以使用attr进行统一改变。
});

$("#CheckedRev").click(function(){
    $(":checkbox").each(function(){
        this.checked = !this.checked;   // 让自己的值取反。
    });
});
</script>
```

