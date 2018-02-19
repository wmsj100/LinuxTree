---
title: jQuery的链式调用
date: 2016-07-16
tags: [jQuery]
categories: Dynamic
---

如果想要通过`jQuery`动态创建`DOM`节点，那么可以使用链式调用，
正常情况下，我想到的是这样的。

最传统的创建`DOM`的方法是拼接字符串。这样会很容易陷入单引号和双引号的战争中，而且特别容易出错。对于复杂的`DOM`结构不建议使用。
而且字符串的拼接很耗性能，

```javascript
html += "<li class='paging active' data-page=" + i + ">" +
     "<a class='active' href='?page=" + i + "'>" + i + " </li>";
```

使用`jQuery`方法

```javascript
$wrap.append("<li>").addClass("paging").data("page", i)
    .append("<a>").addClass("active").attr("href", "?page" + i);
```

但是仔细看上面的这个链式表达式，渲染出来后会看到所有的`class`都加到来`$wrap`上面，
所以不能从顶层到底层这样传递，
一个好的方式是对于每个节点进行分割。

```javascript
$link = $("<a>").addClass("active").attr("href", "?page" + i).text(i);
$list = $("<li>").addClass("paging active").data("page", i).append($link);
$wrap.append($list);
```

我还是对链式传递还不死心，又尝试从底层回溯到顶层

```javascript
$("<span>").html("&raquo").appendTo("<li>").addClass("next").appendTo($wrap);
```

但是不识别中间的`li`节点，所以还是按照上面的分开的好。
