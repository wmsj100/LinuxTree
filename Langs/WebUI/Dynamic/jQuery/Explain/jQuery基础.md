---
title: jQuery基础
date: 2016-07-03
tags: [jQuery]
categories: Dynamic
---

- 对于同一个对象的不超过3个操作的，可以直接写成一行。
- 如果超过3个操作的，建议每行写一个操作。
- 对于多个对象的操作，可以每个对象写一行。
- 如果获取的是`jQuery`对象，在前面加`$`.

---

- $a.get(0) = dom
- $a[0] = dom
- $(dom) = jQuery

- `jQuery.noConflict()` -- 移交`$`操作符。
- `$j = jQuery.noConflict()` -- 把`$j`设置为`jQuery`的操作符。

--- 

命名冲突时候

```javascript
jQuery.noConflict();
        jQuery(function($){
            $(".wrap").click(function(){
                console.log("sss");
            })
        });
```

```javascript
jQuery.noConflict();
(function($) {
            $(function() {
                $(".wrap").click(function() {
                    console.log("sss");
                })
            })
        })(jQuery);
```

判断所选元素是否存在，因为`jQuery`获取的是对象，即便页面没有此元素，也不会报错

```javascript
var a = $(".wrap2");
if(a.length >= 1){
    console.log("这个元素存在");
}
if(a[0]){
    console.log("存在")
}
```

因为`jQuery`选择的元素是以数组的形式出现的，所以可以判断数组的长度。

$("span, #two") 可以这样选择多个对象。

$(".one + div") 等同于 $(".one").next("div");

### 选择器分类

- 基础选择器 id(#), class(.), 通配符("*"), 节点选择器("span"),
- 层叠选择器 后代选择器("div span"), 直接后代选择器("div > span"), 紧邻的下一个 $("#a").next(), 后面的所有元素 **$("#a").nextAll()**.
- 过滤选择器 基本过滤选择器
    + 基本过滤选择器 
        * `$("p:first")` -- 选择第一个
        * `$("p:last")` -- 选择最后一个
        * `$("p:not(.para2)")` -- 选择除`para2`之外的所有元素
        * `$("p:even")` -- 选择索引是偶数的所有元素
        * `$("p:odd")` -- 选择索引是奇数的所有元素
        * `$("p:eq(2)")` -- 选择索引等于`2`的元素
        * `$("p:gt(2)")` -- 选择索引大于`2`的所有元素，不包括2
        * `$("p:lt(2)")` -- 选择索引小于`2`的所有元素，不包括2
        * `$(":header")` -- 选择所有的标题元素
        * `$("p:animated")` -- 选择所有正在执行动画的元素
        * `$(":focus")` -- 选择获取焦点的元素
    + 内容过滤器
        * `$("p:empty, div:empty")` -- 选择空节点，折行都算作是文本节点，不为空
        * `$("p:parent")` -- 选择不是空节点的p节点，折行也算是内容
        * `$("p:contains(ld2)")` -- 选择包含文本`ld2`的节点
        * `$("p:has(span)")` -- 选择包含`span`的所有p节点。
        * `$("p:hidden")` -- 选择所有p节点中`display = none`的节点
        * `$("p:visible")` -- 选择所有p节点中`display != none`的节点
    + 属性过滤选择器
        * `$("p[class]")` -- 选择包含`class`属性的节点
        * `$("p[class=p2]")` -- 选择`class=p2`的节点
        * `$("p[class!=p2]")` -- 选择`class != p2`的所有节点
        * `$("p[class^=p2]")` -- 选择`class`值以`p2`开头的节点，`class= "p2", class = "p2p1", class = "p2-p1", class = "p2 p1"`这些都会被选择.只要是开头有`p2`这个值就可以。
        * `$("p[class$=p2]")` -- 选择`class`值以`p2`结尾的节点，`class="p2", class = "p1 p2", class = "p1p2", class = "p1-p2"`所有`class`只要是以`p2`结尾的值节点都会被选择/
        * `$("p[class*=p2]")` -- 选择`class`值包含`p2`的所有节点，`calss = "p2", class = "p1 p2", class = "p1p2", class = "p1-p2", class = "p1 p2 p3", class = "p1p2 p3", class = "p1 p2-p1", class = "p2-p1", class = "p2p1"`所有只要是包含`p2`，不管`p2`是以前缀或后缀或中间，或是字符串的一部分，只要是出现`p2`这个值，都会被选择。
        * `$("p[class|=p2]")` -- 选择`class`值为`p2`或者是以`p2`为前缀的节点，`class = "p2", class = "p2-p1"`，这些节点都会被选择。
        * `$("p[class~=p2]")` -- 选择`class`包含`p2`的所有节点，但是`p2`必须为独立的值，不能是以前缀的形式，或者是`p2`必须是被空格分割的值，`class = "p1 p2 p3", class = "p1 p2", class = "p2 p1",`，但是不包含`class = p2-p1`.
        * `$("p[class][id]")` -- 选择`p`元素中同时拥有`class`和`id`属性的节点。
    + 子元素过滤选择器
        * `$("ul :first-child")` -- 选择所有后代的第一个子元素，包括直接和后代
        * `$("ul > :first-child")` -- 选择`ul`的第一个直接子元素.
        * `$("ul li:first-child")` -- 判断`ul`的第一个子元素是不是`li`，如果是，则选中，如果不是，则返回一个空数组。
        * `$("ul li:nth-child(1)")` -- 选择所有后代元素中第1个子元素是`li`的节点，如果不是，则返回空数组，这个等同于`:first-child`.
        * `$("ul :nth-child(7)")` -- 选择所有后代元素中第7个子元素，
        * `$("ul>:nth-child(1)")` -- 选择直接后代元素的第一个子元素，等同于`>:first-child`,
        * `$("ul>li:nth-child(1)")` -- 判断直接后代元素的第一个子元素是不是`li`，如果是，则返回这个元素，如果不是，则返回空数组。
        * `$("ul>:nth-child(even)")` -- 选择后代元素中索引为偶数的直接子元素。
        * `$("ul>:nth-child(odd)")` -- 选择后代元素中索引为奇数的直接子元素
        * `$("ul>:nth-child(3n)")` -- 选择直接后代元素中索引是`3`的倍数的节点。
    + 表单对象属性过滤选择器
        * `$("form :enabled")` -- 选择表单中所有未被禁用的元素
        * `$("form :disabled")` -- 选择表单中所有被禁用的元素
        * `$("form :checked")` -- 选择表单中所有被选择的元素，包括`单选，多选，下拉菜单`。
        * `$("form input:checked")` -- 选择表单中所有被选择的单选或多选按钮元素
        * `$("form :selected")` -- 选择表单中所有被选择的下拉菜单元素。
        * `$("form input[type=radio]")` -- 选择所有的单选按钮
    + 表单选择器
        * `$("form :input")` -- 选择表单中所有的`input, textarea, select, button`.
        * `$("form :text")` -- 选择表单的所有单行文本框
        * `$("form :password")` -- 选择表单中的密码框
        * `$("form :radio")` -- 选择单选按钮
        * `$("form :checkbox")` -- 选择多选按钮
        * `$("form :submit")` -- 选择`submit`按钮
        * `$("form :reset")` -- 选择`reset`按钮
        * `$("form :button")` -- 选择`button`按钮

`.val` -- 可以设置选择的input文本框的值 === `value`
`$("table tr:nth-child(odd)").css("background-color","gray");` ===
`$("table tr:even").css("background-color","gray")`

`$("form :checkbox:checked").length` -- 获取表单的多选按钮的勾选数量

```javascript
    $("form .sum").click(function(){
        var cons = $("form :checkbox:checked").length;
        console.log(cons);
    });

    $("form input[type=checkbox]:checked") ===
    $("form :checkbox:checked") === 
    $("form input[name=duoxuan]:checked")
```

- 对于特殊字符`., #, (, [`这些字符需要进行转义`\\`.

```html
<h3 id="q#e">hello world</h3>
<h3 id="q[1]">hello world</h3>

<script>
    $("#q\\#e");
    $("#q\\[1\\]");
</script>
```


`$("ul>li:lt(5):not(:first)")` -- 选择器可以像这样连用，选择索引值小于5，并且不包含第一个值。
`$("ul li").filter(":contains(佳能),:contains(三星),:contains(柯达)").removeClass("promoted");`
filter是一个筛选器，会对元素自身进行筛选，而上面的元素自身就是指`$("ul li")`

- `$(node).height()` - 获取高度，返回数值，`100`;
- `$(node).css("height")` -- 获取高度，返回字符串；`100px`;

- `$(node).offset()` -- 获取元素在当前视窗的相对偏移，返回一个对象，包含`left, top`.
- `$(node).position()` -- 获取元素相对于祖先元素中设置有`relative, absolute`的偏移值，返回一个对象，包含top。left

```javascript
$("div").offset();  //Object {top: 18.71875, left: 8}
$("div").offset().left; //8
$("div").offset().top;  //18
```


