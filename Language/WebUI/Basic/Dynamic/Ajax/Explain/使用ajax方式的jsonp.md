---
title: 使用ajax方式的jsonp
date: 2016-07-08
tags: [Ajax,jQuery]
categories: Dynamic
---

关于`jsonp`，通常就是动态创建一个`script`，然后在`src`中绑定一个回调函数的名称，但是，因为不知道什么时候`script`加载完成，或者是获取数据完成，

`jQuery`做的更远，它通过自己的计算得出一个回调函数的名字，然后去访问目标链接，也会动态创建一个`script`，但是在获取了数据之后就会把这个`script`移除，

`jQuery`的`jsonp`方式和获取`json`的方式一样，都是使用`$.getJSON()`,只是多了一个回调函数，但是不需要给起名字，只需要一个`?`，它会自己计算一个函数名字出来。

```javascript
    $("#send").click(function(){
        $.getJSON("http://platform.sina.com.cn/slide/album_tech?app_key=1271687855&num=5&page=1&jsoncallback=?", function(data){
            var html = "";
            $.each(data.data, function(index, item){
                html += "<p>" + item["name"] + "</p> "
                            + "<img src=" + item["img_url"] + "><br>";
            });
            $("#resText").html(html);
            console.log(data.data)
        });
    });
```

请注意看回调函数`&callback=?`，`jQuery`会自己计算出正确的函数名。以执行后面的回调函数，虽然回调函数是一个匿名函数。