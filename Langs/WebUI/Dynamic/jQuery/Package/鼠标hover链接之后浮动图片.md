---
title: 鼠标hover链接之后浮动图片
date: 2016-07-04
tags: [jQuery]
categories: Dynamic
---

[效果](http://jsbin.com/noxodus/1)

```html
<a href="#" class="tooltip" title="link-1">
    <img src="http://a4.att.hudong.com/57/93/01300000010387121627936773175.jpg" alt="">
</a>
<a href="#" class="tooltip" title="link-2">
    <img src="http://a2.att.hudong.com/33/92/01300000010387121627921091284.jpg" alt="">
</a>
```

```less
.dropStyle {
    html, body, h1, h2, h3, div, p, ul, ol, dl, dt, li {
        margin: 0;
        padding: 0;
    }
    a{
        text-decoration: none;
        color: #333;
        &:hover {
            color: #E74C3C;
        }
        img{
            width: 60px;
        }
    }
}

/*----------------------  ------------------------------------*/
body {
    .dropStyle;
}
@borderColor: #ccc;
@fontColor: #999;
@padding: 5px 10px;
@borderRadius: 3px;

.toolTipBox {
    position: absolute;
    border: solid 1px @borderColor;
    padding: @padding;
    border-radius: @borderRadius;
    color: @borderColor;
}
```

```javascript
function setLinkTitle() {

    var useOffset = {
            left: 20,
            top: 10
        };

    $("a.tooltip").mouseover(function(e) {
        var $src = $(this).find("img").attr("src"),
            alt = this.title,
            img = '<img src="' + $src + '"' + 'alt="' + this.title + '">',
            span = this.title ? "<br><span>" + this.title + "</span>" : "",
            cont = '<div class="toolTipBox">' + img + span + "</div>",
            $box = $(cont);
        $("body").append($box);
        $box.css({
            "left": e.clientX + useOffset.left + "px",
            "top": e.clientY + useOffset.top + "px"
        }).show("fast");
        $(this).removeAttr("title");

    }).mousemove(function(e) {
        $(".toolTipBox").css({
            "left": e.clientX + useOffset.left + "px",
            "top": e.clientY + useOffset.top + "px"
        });

    }).mouseout(function(e) {
        this.title = $(".toolTipBox").find("img").attr("alt");
        $(".toolTipBox").remove();
    });
}
```

