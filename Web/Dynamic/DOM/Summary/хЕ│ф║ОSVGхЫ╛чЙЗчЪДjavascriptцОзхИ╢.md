---
title: 关于SVG图片的javascript控制
date: 2016-05-30
tags: [SVG]
categories: Dynamic
---

我想知道`SVG`图片是怎么引入的,可是每个人都讳莫如深,感觉这不是个事,好像每个人都应该会,可是我就是不知道该怎么通过`js`控制,然后百度了一下午也没有结果,最后还是回归到最初,因为本来就是页面上面引入的节点,既然和`iframe`类似,也有属于自己的空间,那么就都可以通过`contentDocument`获取元素的空间.然后通过`querySelector`获取`path`的`class`和通过`setAttribute`设置`fill`.直接上码
```html
<object class="svg" data="img/icon/close.svg" type="image/svg+xml">Your browser does not support SVGs</object>
```

```javascript
window.onload = function() {
var b = document.querySelector(".svg");
var c = b.contentDocument.querySelector(".svg1");
c.setAttribute("fill", "red");
}
```

因为`SVG`图片加载是需要时间的,类似`ajax`,所以对于这个图片的操作需要等待图片加载完成,即可以通过`onload`命令,这是最省事的,当然了也可以设置循环检测值,
获取值只需要`querySelector`获取`path`里面的`class`值`svg1`,然后设置

检测`SVG`图片是否加载完成,
```javascript
    var clock = 0;
    clock = setInterval(function() {
        var b = document.querySelector(".svg");
        var c = b.contentDocument.querySelector("svg");
        if (c) {
            console.log(c);
            console.log(clock);
            clearInterval(clock);
        }
    }, 10);
```

我一直想要封装到一个函数内部,因为我感觉之前就就是这么做的,但是不成功,还是放到俩个函数里面吧,放到一个函数可能是因为封装性好看,但是俩个函数也没有多大影响,

```javascript
var clock = 0;
data();
var b = document.querySelector(".svg");

function data() {
    clock = setInterval(check, 10);
}

function check() {
    var c = b.contentDocument.querySelector("svg");
    if (c) {
        console.log(c);
        console.log(clock);
        clearInterval(clock);
        //return; //这个没有必要,可以删除
    }
}
```

说到使用技巧,因为我的`SVG`图片基本都是从阿里的图库http://www.iconfont.cn/下载的,所以它的格式应该基本是确定的,可以优化内容,
```xml
<![CDATA[

]]>`
```
这里面包裹的是`style`内容,暂时感觉没用.
`path`是路径的数据,里面的`fill`是颜色填充,可以删除,然后通过`js`动态添加属性到`svg`的属性里面,因为关于尺寸的属性也是在那里面的.

其实从使用`SVG`开始就是恶魔的开始，因为不管是操作还是遍历里面的内容，感觉都是很不方便的，而且我觉得性能也不一定会有多好，而如果使用`字体图标`就完全没有这方面的考虑了。首先不需要考虑图片的加载问题，其次图标的大小尺寸也完全不用考虑了，而且不管是用过`css`还是`JS`操作性都是极好的。为了身心健康，远离`SVG`；