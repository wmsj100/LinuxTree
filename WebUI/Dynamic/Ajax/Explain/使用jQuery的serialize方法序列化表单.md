---
title: 使用jQuery的serialize方法序列化表单
date: 2016-07-09
tags: [Ajax,jQuery]
categories: Dynamic
---

我自己之前封装过一个关于表单的序列化函数，但那个函数一直没有弄明白，只是抄着`尼古拉丝`的过来。
`jQuery`自己的封装就有这个函数，用着就比较方便了。
`$("#form1").serialize()`

```javascript
    $("#send").click(function(){
        $.post("10_02.php", $("#form1").serialize(), function(data,textStatus){
            console.log(data, textStatus)
        })
    })
```

省去了一个一个输入表单对应的内容。否则就得像这样进行操作。

```javascript
    $("#send").click(function(){
        $.post("10_02.php", {
            usename: $("#usename").val(),
            content: $("#content").val()
        }, function(data,textStatus){
            console.log(data, textStatus)
        })
    });
```

如果表单内容简单还好，如果表单比较复杂，那么就很容易出错来。

---

- `serializeArray` -- 将表单序列化为`JSON`格式对象。

```javascript
$(":checkbox").serializeArray();
{name: "color",value: "red"};
{name: "color",value: "blue"};
{name: "color",value: "green"};
{name: "color",value: "yellow"};
```

---

- `$.param()` -- 它是`jQuery`方法的核心，可以使对象或数组按照`key/value`进行序列化。

```javascript
    var obj = [
        {
            name: "color",
            value: "red"
        }, {
            name: "color",
            value: "blue"
        }, {
            name: "color",
            value: "green"
        }, {
            name: "color",
            value: "yellow"
        }
    ];
    $.param(obj); // "color=red&color=blue&color=green&color=yellow"
```


