---
title: jQuery代码收集
date: 2016-07-04
tags: [jQuery]
categories: Dynamic
---

`$("ul li:eq(1)").text()` -- 获取ul中的第二个`li`元素的文本内容。

`$("ul li:gt(5):not(:last)")` -- 获取`ul`中的下标大于`6`但是不包含最后一项的所有`li`节点。

`$("div>:visible")` -- 选择`div`的所有可见直接子元素。

`$("div>:visible").not("span[title]")` -- 选择`div`的所有可见子元素中`span`不包含`title`的集合

`$("div>:visible").filter("span[title]")` -- 选择`div`的所有可见子元素中`span`包含`title`的集合。

`$("div>:visible").remove("span[title]")` -- 选择`div`的所有可见子元素，并且删除包含`title`的`span`元素，然后返回剩余的内容。删除的是前面筛选出来的元素，只能是操作同级元素，而不能在remove里面添加一个子元素的过滤来删除子元素。

```javascript
$("ul li").click(function(){
        $(this).clone(true).appendTo($("ul"));
        // 克隆一个元素，并且克隆出来的元素也绑定了事件
    });
```

通过`clone`来克隆一个列表`li`并且复制绑定的事件，

`$(":radio:checked")` -- 获取单选框的选中对象。

`$(":radio").val(["02"]); ` -- 选中单选框中值为`value = "02"`的选项。

`$(":checkbox").val(["1","3"])` -- 选中多选框中值为`value = "1"`和`value = "2"`的选项

`$("select:first").val("2")` -- 选中下拉菜单中`value = "2"`的选项。

`$("select:first").children()` -- 获取第一个下来列表框的所有选项

`$("div").css({"font-size":"20px","background-color":"red"})` ===
`$("div").css({fontSize:"20px",backgroundColor:"red"})`
都可以设置字体和背景颜色，写法可以是`CSS`方法，也可以是`JS`驼峰写法。
建议都带上引号。

`$("h3").css("opacity",0.5)` -- 设置字体的透明度

`$("p").next().is(":visible")` -- 判断`p`元素的下一个元素是否显示，返回布尔值。

`is` 方法就是用来进行判断的。

- `toggle` - 可以用来切换元素的显示状态。`$("p").toggle()` 
- `toggle` 可以用来模拟`click`事件，但是现在已经被废弃了。

---

`return false` -- 同时阻止`stopPropagation, preventDefault`俩个事件。但是这个事件在`ie8`不能使用，谨慎使用。对于版本`jQuery1.x以下都可以`

`bind` -- 对于函数绑定也不建议使用，通过`on`来替换

- `$("input").on("mouseover mouseout",function(){$(this).toggleClass("over"); })` -- 一次绑定多个事件

- `$("p").parents("div")` -- 可以找到父元素为`div`的元素集合。

- `$("textarea").height($("textarea").height() + 50)` -- 这个也是可以实现叠加。

- `.height()`和`css("height")`的区别如下，都可以达到通用的效果

- [多行文本框操作](http://jsbin.com/kotezot/3/edit?html,js,output)

```javascript
    $(".bigger").click(function() {
        var cmtHeight = $("#comment").height();
        if (cmtHeight < 300) {
            $("#comment").height(cmtHeight + 50)
        }
    });

    $(".smaller").click(function() {
        var cmtHeight = $("#comment").height();
        if (cmtHeight > 50) {
            $("#comment").css("height", cmtHeight - 50);
        }
    });

    $(".down").click(function() {
    if (!$("#comment").is(":animated")) {
        $("#comment").animate({
            "scrollTop": "+=50px"
        }, 100);
    }
    });

    $(".up").click(function() {
        if (!$("#comment").is(":animated")) {
            $("#comment").animate({
                "scrollTop": "-=50px"
            }, 100);
        }
    });
```

- `this.checked` -- 原生JS的方法。

对于多选框的判断，我的代码和高手的代码的区别如下：
我觉得从性能或者是代码数量来考虑，都是他的好，而且感觉代码的易读性很好。

```javascript
$(":checkbox").each(function(){
    if(this.checked){
        str += this.value + " \n";
    }
});

<!-- 在第一次筛选多选框时候就直接进行选项的筛选 -->
// 因为经过第一步的过滤之后，进行each遍历的数量就少了。
$(":checkbox:checked").each(function(){
    str += this.value + " \n";
})
```

- `$("div:first>:nth-child(even)")` -- 选中第一个`div`元素的后代元素中下标为偶数的所有子元素。 -- 对于`nth-child`要好好挖掘

- `$("tr:first").hasClass("selected")` -- 判断第一个`tr`是否含有`selected`的class。返回布尔值。

- `$("tr:first").addClass("selected")` === 
`$("tr:first")["addClass"]("selected")`
所以基于上面的特性可以通过一个3元运算来进行基于当前状态的切换操作

```javascript
$("tbody").on("click", "tr", function() {
    var hasClass = $(this).hasClass("selected");
    $(this)[hasClass ? "removeClass" : "addClass"]("selected").find(":checkbox").prop("checked", !hasClass);
});
```

- `has()` -- 接受选择器类型的参数，`$("tr").has("td")` 选择拥有`td`的`tr`，这样就把`thead`中的`tr`过滤了。

- `$(":checkbox:not(:last):checked").length,`
