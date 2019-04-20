---
title: goTop
date: 2016-07-11
tags: [Model,Package]
categories: Frame
---

```less
html,body,div,p,ul,ol,li{
    padding: 0;
    margin: 0;
}

#go_top{
    @color: #E74C3C;
    @bgColor: #fff;
    @borderWidth: 2px;
    
    border: solid 2px @color;
  color: @color;
  border-radius: 5px;
  padding: 5px 10px;
  width: 50px;
  font-size: 18px;
    font-weight: bold;
    cursor: pointer;
    bottom: 10px;
    right: 10px;
    opacity: 0.5;
    &:hover{
        color: @bgColor;
        background-color: @color;
        opacity: 1;
    }
}
```

```javascript
require.config({
    paths: {
        jquery: "js/lib/jquery-1.12.4"
    }
});

define(["jquery"], function($) {
    $(function() {
        // 创建节点，设置id和position属性
        var $goTop = $("<div/>").attr("id", "go_top").css("position", "fixed").appendTo("body"),
            $span = $("<span/>").attr("class", "go_top_text").text("GoTop").appendTo($goTop),
            scrollTop = 0;

        function check() {
            scrollTop = $(window).scrollTop(); // 获取此刻页面的偏移距离
            scrollTop > 200 ? $goTop.show() : $goTop.hide(); // 3元判断
        }

        check();    // 在页面加载完成之后就检查一次位置，确定是否显示。

        $(window).scroll(function() {   
            check();
        });

        $goTop.click(function() {
            $(window).scrollTop(0);
            $(this).hide();
        });
    })


});
```

