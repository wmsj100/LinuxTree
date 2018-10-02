---
title: 使用jQuery动态创建JS文件
date: 2016-07-08
tags: [Ajax,jQuery]
categories: Dynamic
---

动态创建`JS`脚本文件的方法：

- 常规方法

```javascript
var script = document.createElement("script");
script.src = "01.js";
document.head.appendChild(script);
```

- `jQuery`方法

```javascript
    $("<script/>").attr("src", "01.js").appendTo("head");
    $("<script src='01.js'><\/script>").appendTo("head");
```

上面俩个方法都可以，但是第二个记得需要转义。

上面这些方法都可以实现动态加载脚本，但是我无法知道`JS`脚本什么时候加载完成了，对于依赖于这个脚本的函数我该怎么去运行，
一个丑陋的方法就是，设置一个循环，一直去监听这个文件，直到获取到文件，然后才开始执行后面的函数。
因为循环过程中会阻断后面函数的执行。所以上面这种方法还是

- `jQuery - $.getScript()` -- 方法 

```javascript
    $("#send").click(function(){
        $.getScript("../lib/jquery.color.js", function(){
            console.log("ss");
            $("#content").animate({"backgroundColor": "yellow"},1000)
                        .animate({"backgroundColor": "blue"},1000);
        });
    });
```

上面这个是通过动态加载一个`jQuery`的`color`动画插件。等加载完成之后会给目标添加一个颜色动画。

- `jQuery - $.getJSON()` -- 加载`json`文件
当涉及到读取`json`时候，就可以使用这个方法，并且配合`each`进行`data`遍历，
`$.getJSON`方法接受俩个参数，第一个是目标`json`的地址，第二个是当`json`文件加载成功之后的回调函数，回调函数可以接受一个参数`data`，对`json`文件进行处理。

```javascript
    $("#send").click(function() {
        $.getJSON("10_01.json", function(data) {
            console.log(data)
            var html = "";
            $.each(data.value, function(index, item) {
                html += '<div class="comment"><h6>' + item['name'] 
                            + '</h6><p class="para">' + item["value"] 
                            + "</p></div>";
                $("#resText").html(html);
            })
        })
    })
```

对于表格使用`ajax`，就不会使用表格的默认提交方式`submit`。