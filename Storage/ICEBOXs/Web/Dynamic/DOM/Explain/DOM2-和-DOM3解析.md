---
title: DOM2-和-DOM3解析
date: 2016-06-24
tags: [DOM]
categories: Dynamic
---

- `document.importNode(node,true)` -- 可以向不同文档(深度)复制节点，如果使用`appendChild`就会报错，因为后者只能在同一个文档进行操作。

- `defaultView` -- 指向窗口或框架的拥有者。

- `isEqualNode`和`isSameNode`类似，都是比较来个节点，并且返回布尔值。
- `isSameNode` -- 只有俩个节点引用的是一个对象时候才会返回`true`；
- `isEqualNode` -- 俩个节点的内容和属性相同就返回`true`；

```javascript
    var div1 = document.createElement("div");
    div1.setAttribute("data-name", "wmsj");
    var div2 = document.createElement("div");
    div2.setAttribute("data-name", "wmsj");
    div1.isEqualNode(div2); //true
    div1.isSameNode(div2);  //false
```

---

### `style` 样式设置

- `a.style.float = "right"` -- 可以直接设置浮动，没有兼容性问题。
- `a.style.cssText` -- 返回样式设置列表，可以读写，如果是写入，则会覆盖之前所有的样式，之前的样式会丢失。
- `cssText` - 只能获取元素的行内样式，通过`style`标签设置的样式，或者是继承的样式都无法通过`a.style.cssText`获取。
- `a.style.removeProperty("color")` -- 从a元素删除`color`样式。
- `a.style.length` -- 获取`cssText`的数组长度。
- `a.style.removeProperty("color")` -- 移除`color`颜色设置，使用继承样式。
- `document.defaultView.getComputedStyle(a,null).width` -- 获取`a`的宽度。这样以后的尺寸就可以通过这个函数获取，尺寸就可以放到`css`中了，没必要在JS中，这样就可以是`css`显示代码脱离`JS`。
- `a.currentStyle.width`--这是`ie`获取显示宽度的方法。
- 计算的样式的只读的。

- `offsetLeft, offsetTop`获取的是相对父元素的偏移量，但是因为一般元素都是被包含在`div`内部，而`div.offsetParent` => `body`，所以元素直接调用相对自己的偏移值就是需要的值。

- `clientWidth, clientHeight` -- 获取客户区大小，指的是元素的内容宽度加上左右内边距`padding-left, padding-right`.这个属性常用于获取可视窗口但是不包含滚动条时候
- `document.body.clientWidth` -- 获取的是不包含滚动条的窗口宽度。
- `document.documentElement.clientWidth` -- 和上面是一样的。 

- `document.body.scrollHeight` -- 当出现滚动条时候，获取页面的总高度。
- `document.body.scrollTop` -- 获取页面的垂直滚动距离，可以写入值，然后页面就掉到相应的距离。
