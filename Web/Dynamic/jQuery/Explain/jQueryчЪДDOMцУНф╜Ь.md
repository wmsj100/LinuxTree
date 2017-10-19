---
title: jQuery的DOM操作
date: 2016-07-04
tags: [jQuery]
categories: Dynamic
---

`DOM`操作包括3个方面 -- `DOM核心`, `HTML-DOM`, `CSS-DOM`;
- `DOM核心`
    - `document.getElementsByTagName("form")`;--获取表单 
    - var img = document.getElementsByTagName("img");--获取图片 
    - `img.getAttribute("src")` -- 获取图片的地址
- `HTML-DOM` -- 出现的更早，而且代码通常更短，
    + `document.forms` -- 获取表单
    + `var img = document.images` -- 获取图片
    + `img.src` -- 获取图片的地址
- `CSS-DOM` -- 获取设置style对象的各种属性。

---

- `attr` -- 查找并设置元素的属性
- `$("<li/>")` -- jQuery的工厂函数`$(html)`可以创建`html`节点。
- `append` -- 作为子节点插入
- 创建文本节点的方法,下面俩个方法是等效的。
    + `$("<li>hello</li>")`
    + `$("<li/>").text("hello")`
- 创建属性，下面的俩个方法是等效的,使用下面的会感觉更加的清晰
    + `$('<li title="sss">hello</li>')` => `<li title="sss">hello</li>`
    + `$("<li/>").text("hello").attr("title","sss")` 
---

- 插入节点
    + `append` -- `$("div").append(a)` -- 在目标元素的子节点末尾插入元素。
    + `appendTo` -- `a.appendTo($("div"))` -- 将元素插入目标元素的子节点末尾
    + `prepend` -- `$("div").prepend(a)` -- 在目标元素的头部插入元素
    + `prependTo` -- `a.prependTo($("div"))` -- 将元素插入目标元素的头部
    + `after` -- `$("div").after(a)` -- 在目标元素的后面插入元素
    + `insertAfter` -- `a.insertAfter($("div"))` --把元素插入目标元素后面
    + `before` -- `$("div").before(a)` -- 在目标元素前面插入元素
    + `insertBefore` -- `a.insertBefore($("div"))` 把元素插入目标元素前面
    **`append`可以接受`id, class, label`等名称，也可以接受`$("ul")`等jQuery对象，如下这俩个是等效的。**
        * `appendTo($("ul"))` === `appendTo("ul")`；
    所以建议还是以代码少为优，使用名称。
- 删除节点
    + `remove` -- 删除节点同时删除节点的事件可以传入参数对前面的集合进行过滤
        * `$("div>:visible").remove("span")` -- 删除`div`的所有可见子元素中的`span`元素。
        * `$("ul li").remove()` -- 这样会删除所有的选中元素。
    + `detach` -- 删除节点但是节点会保存节点绑定的事件，也可以接受参数进一步筛选
    + `empty` -- 会清空选择对象的内容，
- 复制节点
    + `clone(true)` -- 复制节点，可以接受参数`true`，表示可以同时复制节点的事件，即便没有参数，这个复制也会把节点的所有子节点都复制，和`JS`的`clone`还是有区别的。
- 替换节点 `replaceWith, replaceAll`
    + `replaceWith` -- `$("ul").replaceWith("<h3>sss</h3>")` 
    + `replaceAll` -- `$("<h3>sss</h3>").replaceAll("ul")` 是前者的逆序操作
- 包裹节点 `wrap, wrapAll, wrapInner`
    + `wrap` 让元素被某个节点包裹，每个元素都会进行单独包裹

```html
<li>
    <span>hello world</span>
    <span>hello world</span>
    <span>hello world</span>
</li>

<script>
    $("ul>li:eq(1) span").wrap("<strong></strong>");
</script>
<li>
    <strong><span>hello world</span></strong>
    <strong><span>hello world</span></strong>
    <strong><span>hello world</span></strong>
</li>
```

    +  `wrapAll` -- 所有被选择元素被包裹在一个节点内部

```html
<li>
    <span>hello world</span>
    <span>hello world</span>
    <span>hello world</span>
</li>

<script>
    $("ul>li:eq(1) span").wrapAll("<strong></strong>");
</script>

<li>
    <strong>
        <span>hello world</span>
        <span>hello world</span>
        <span>hello world</span>
    </strong>  
</li>
```

    + `wrapInner` -- 被选择元素内部被节点包裹

```html
<li>
    <span>hello world</span>
    <span>hello world</span>
    <span>hello world</span>
</li>

<script>
    $("ul>li:eq(1) span").wrapInner("<strong></strong>");
</script>

<li>
    <span><strong>hello world</strong></span>
    <span><strong>hello world</strong></span>
    <span><strong>hello world</strong></span>
</li>
```

---

### 属性操作 `attr, removeAttr`

- `attr` -- `$("h3").attr("title","hello")` -- 传入一个参数时候，可以查看`title`属性，如果传入俩个参数，就可以设置`title`属性， 
- `removeAttr` -- `removeAttr("disabled")`
- 也可以同时设置多个属性，以键值对的形式导入 
`$("h3").attr({"title":"hello","name":"biaoti", "data-age": 23})`;
- 追加样式，- addClass
    + `$("h3").addClass("p1")` -- 追加一个样式
    + `$("h3").addClass("p2 p4 p6")` -- 追加多个样式
    + `$("h3").removeClass("p1 p3 p6")` -- 移除多个样式
- 样式切换 - `toggleClass`
- 判断是否含有样式 - `hasClass` -- 这个方法调用的其实是`is`方法
    + `$("h3").hasClass("wmsj")` -- 判断是否含有`wmsj`。
    + `$("h3").is(".wmsj")` -- 判断是否
- 设置`HTML`内容 - `$("p").html()`
- `$("p").text()` -- 查看和设置节点的文本内容。

- 查看和设置文本框的内容 -- `val`，但是也可以设置表单中的单选框，多选框，下拉菜单的选中值，
- 也就是说，`val`不仅仅是用来设置查看`input`的值，还是可以操作`radio, checkbox, select`的选择值。设置选项时候，需要把值放到中括号中。

```javascript
`$(":radio").val(["02"]); ` //-- 选中单选框中值为`value = "02"`的选项。

`$(":checkbox").val(["1","3"])` //-- 选中多选框中值为`value = "1"`和`value = "2"`的选项

`$("select:first").val("2")` //-- 选中下拉菜单中`value = "2"`的选项。
```

- `children` -- 获取元素的所有子元素。
- `next` -- 获取下一个同辈元素
- `prev` -- 获取上一个同辈元素
- `siblings` -- 获取所有的同辈元素，不管是之前还是之后。

- `closest` -- 获取离目标最近的值,这个目标必须是在自己的`dom`链条上可以查找到，只会向上查找，也就是说，目标元素必须是当前元素的父元素。

```html
<div>
    <p><span><strong>hello</strong></span></p>
</div>

<script>
    $("strong:first").click(function(){
        $(this).closest("div").css("color","red");  // 点击，给父元素的`div`
    })
</script>
```

- `parent, parents, closest`这三个还是很相似的，都是对父级元素的查找，
    + `parent` -- 查找直接父元素，即上一级，
    + `parents` -- 返回所有的父元素，包括祖先元素，这个不实用
    + `closest` -- 返回父元素中离目标元素最近的元素。

---

### CSS-DOM

- `css` -- 设置和获取通过外置或者是内置样式表添加的样式。
- 这个方法只能获取已经设置的值，如果没有设置，则返回`undefined`
- 对于这个方法内部的写法，可以使用`css`写法(必须带引号)，也可以用驼峰写法。

```javascript
$("div").css({"font-size":"20px","background-color":"red"});
$("div").css({fontSize:"20px",backgroundColor:"red"});
```

上面的俩种写法都是正确的，但是建议总是带上引号。

- 我费尽心思封装的那个获取样式尺寸的函数现在看好像是没什么意义了，因为`jQuery`封装的比我的好。有助于我理解这个函数吧。

- `$(window).scrollTop()` -- 获取页面垂直方向的滚动距离
- `$("body").scrollTop()` === 
  `$(document).scrollTop()` ===
  `$(window).scrollTop()`   //都可以获取页面的滚动距离


