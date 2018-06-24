---
title: javascript加载伪类样式 :after
date: 2016-05-12
tags: [CSS,JavaScript]
categories: Dynamic
---

对于清除浮动通常在父元素上面添加伪类`:after` 然后添加元素，但是对于这个操作如何在`js` 中进行呢，因为`js` 中对于样式的操作都是通过`style` 这个接口，而伪类是没有明确父元素的，或者说这个无法通过`style` 的方法加载，怎么办呢/

大神的办法是通过动态加载样式表来实现的，[http://stackoverflow.com/questions/21032481/change-the-style-of-before-and-after-pseudo-elements](http://stackoverflow.com/questions/21032481/change-the-style-of-before-and-after-pseudo-elements)

```javascript
var styleAfter = document.createElement("style");
styleAfter.innerHTML = '#carousel .wrap-link:after{content: ""; display: block; clear: both; } ';
document.head.appendChild(styleAfter);
```

创建了一个标签`style` ，放置到`head` 的末尾，然后通过`innerHTML` 写入样式的内容，超级好用。