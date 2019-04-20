---
title: jQuery与Ajax的应用
date: 2016-07-08
tags: [Ajax,jQuery]
categories: Dynamic
---

`jQuery`中`$.ajax()`是最底层的方法。第二层是`load, $.get(), $.post()`方法，第三层是`$.getScrip(), $.getJSON()`.

---

### load -- 传递静态文件

`load()` -- 最简单使用频率也挺高。就是载入远程的`HTML`代码并插入`DOM`中。
`load(url [data] [callback])`


`$("#resText").load("10_01.html .para")`; -- 在`url`链接的末尾可以通过空格来分割一个参数， 对接受的`html`进行过滤插入。
如果没有参数会把整个页面，包括除`html`根标签之外的所有标签引入到`#resText`节点内部。

如果`load`没有传递参数，则默认为`get`请求方式。
`$("#resText").load("10_01.html .para", function(){})`
如果`load`有传递参数，则自动转换为`post`方式。
`$("#resText").load("10_01.html .para", {name: "wmsj", age: "12"}, function(){})`

对于回调函数，接受3个参数，分别是:
- `responseText` -- 返回的内容
- `textStatus` -- 请求状态
- `XMLHttpRequest` -- xml对象。

--- 

### `$.get()` and `$.post()`

- `$.get(url, [data], function(data, textStatus){})` -- 回调函数接受俩个参数，
- `data` -- 表示请求返回的内容，可以是`html, json, xml`
- `textStatus` -- 请求状态：`success, error, notmodified, timeout`;
- 只有当请求状态是`success`时候才会执行回调函数。

```javascript
    $("#send").click(function() {
        $.get("10_02.php", {
            name: $("#usename").val(),
            cont: $("#content").val()
        }, function(data, textStatus) {
            $("#resText").append(data);
            // console.log(data);
            console.log(textStatus);
        })
    });
```

如果需要后台返回的数据是`json`格式的，那么就需要给回调函数传递第四个参数`json`。

```javascript
    $("#send").click(function() {
        $.get("10_02.php", {
            name: $("#usename").val(),
            cont: $("#content").val()
        }, function(data, textStatus) {
            console.log(data);
            var name = data.name,
                    age = data.age,
                    cont = data.comment;
            $("#resText").append("<p>" + name + ";" + age + ";" + comment + "</p>");
        }, "json");
    });
```

- `post`的使用方式和`get`完全相同。只是把`get`换为`post`。

- `$.getScript()` -- 动态获取脚本。 其实触发的也是`ajax`的`get`方法。
- 接受俩个参数，第一个是要加载的脚本的地址，第二个是当脚本成功加载后执行的函数。
- `getJSON()` -- 获取`json`，

- `$("form1").serialize()` -- 可以使表单序列化，把表单的内容转换为字符串形式。