---
title: DOM扩展解析
date: 2016-06-24
tags: [DOM]
categories: Dynamic
---

- `jQuery`的核心就是根据`CSS`选择符查询`DOM`文档取得元素的引用。

- 选择元素尽可能使用`querySelector`/ `querySelectorAll`,这是原生扩展，`ie8+`支持。

- 元素遍历`firstElementChild, lastElementChild, previousElementSibling, nextElementSibling`这些是`DOM`扩展，需要`ie9+`的支持。

- `getElementsByClassName`这还是`HTML5`的规范，可以通过`document`或者`html`元素调用该方法。需要`ie9+`支持。

- `classList`是新扩展的`DOM`属性选择器，需要`ie10+`支持，对于`class`的操作简单到极致；
- `a.classList.add("aa")` -- 增加`class`值`aa`，如果已经存在就不操作
- `a.classList.remove("aa")` -- 删除`class`值`aa`，如果不存在就不处理
- `a.classList.contains("aa")` -- 确认`class`是否包含`aa`，是就返回`true`,否则返回`false`;
- `a.classList.toggle("aa")` -- 如果`aa`已经存在，则删除，否则就添加。

- 焦点管理`document.activeElement`/ `document.hasFocus`，没有兼容性问题；
- `document.activeElement` -- 返回现在焦点停留的元素标签；
- `document.hasFocus()` -- 如果焦点在页面上则返回`true`,否则返回`false`；

- `readyState` -- 指示文档是否加载完成的一个指示器，有俩个参数`complete` and `loading`.没有兼容性问题。仅仅是一个标签，省去了`onload`的判断。

- `document.compatMode`判断页面的模式，
- `CSS1compat` -- 标准模式
- `BackCompat` -- 混杂模式

- `document.charset` -- 查看页面的编码方式`UTF-8`;

- `dataset`可以访问以`data`开头的自定义属性集，可以直接读写自定义属性。
- `a.dataset.name = "wmsj"` -- 添加自定义属性`data-name`;
- `a.dataset.name` => `wmsj`;
- 但是这个有兼容性问题，因为`ie9`都不支持，可以使用`a.setAttribute("data-name","wmsj")`进行替代。

- `innerHTML`-- 这还是`H5`的标准。这个需要注意，检测代码，最好不要使用。
- `outerHTML` -- 这个会替换内部元素和元素本身。
- 使用`innerHTML`或者`outerHTML`会导致内存占用问题，因为通过这样把元素从`DOM`树替换，元素身上绑定的事件并没有随着删除，元素只是不在`DOM`树中，但是依然在内存中，所以元素身上绑定的事件也依然是有效的，只是不会被触发了。这样的操作多了之后就会导致大量的内存占用问题。
- 每调用一次`innerHTML`就会创建一个`HTML`解析器，对于大量的代码操作，使用这个会比操作`DOM`性能好。

- `scrollIntoView` -- 页面自动滚动，可以传参，但是也没必要，就是让元素出现在视口中。如果元素设置了`a.focus()`，在刷新页面时候也会自动出现在视口中。
- 这个方法也没有兼容性问题。

- `children` - 获取子元素集合，不包含文本节点，可以替代`childNodes`，没有兼容性问题。

- `contains` -- 判断节点是不是元素的后代，这个感觉挺好用的，而且没有兼容性问题

```html
<div class="wrap">
    <p><span>hello world</span></p>
</div>

<script>
    var a = document.querySelector(".wrap");
    var b = document.querySelector("p");
    var c = document.querySelector("span");
    a.contains(b);  //true
    a.contains(c);  //true
</script>
```

- `innerText`使用也没有兼容性问题。