---
title: CSS多个类并列和出现多个id
date: 2016-06-16
tags: [CSS]
categories: Static
---

如果想要同时选择多个`class`属性，比如

```html
    <style>
        .p1{
            color: red;
        }
        .p2{
            background-color: yellow;
        }
        .p1.p2{
            border: solid 1px green;
        }
        #w1{
            font-size: 32px;
        }
    </style>

     <p class="p1 p2" id="w1">hello world</p>
    <p class="p1" id="w1">hello world</p>
    <p class="p2">hello world</p>
```

对于同时具备`p1 p2`的元素设置样式时候，可以这样选择`.p1.p2`或者是`.p2.p1`顺序是没有关系的，

对于一个页面出现多个相同的`id`值，这些`id`值的样式会共享，即在样式表的显示效果上，`id`和`class`是没有区别的，他俩的区别表现在`JS`的选择中。

浏览器不会检测`HTML`中`id`的唯一性，

对于同一个类型的标签，同一个`id`值只能出现一次；

```html
<style>
    #important{
    color: red;
}
</style>

<p class="important">hello</p>
<span class="important">hello</span>
<div class="important">hello</div>
```

上面这些都是可以的。

css选择器是区分大小写的。

### 字串属性值选择器

`*="hh"` -- 只要字符串中包含即被选择
`^="wmsj"` -- 只要以`wmsj`开头的会被选中
`$="wmsj"` -- 只要以`wmsj`结尾的会被选择

```html
<style>
    a[href*="hei"] {
        color: yellow;
    }
    a[href^="s"] {
        color: green;
    }
    a[href$="d"] {
        color: red;
    }
</style>

<a href="erheizi">erheizi</a>
<a href="ss">ss</a>
<a href="dd">as</a>
<a href="heiss">as</a>
```


### 部分选择器

`[title~="link"]`这个选择器比较好用，其实就像是`class`中的`.p1`选择器，只不过这个使用范围更广。

```html
<style>
a[class~="p3"]{
        background-color: purple;
    }
    a[title~="link"]{
        font-size: 24px;
    }
</style>

<a class="p1 p2 p3" title="link erheizi" href="erheizi">erheizi</a>
<a class="p1 p2 p4" title="link" href="ss">ss</a>
```

### 特定属性选择类型

`lang|="en"` -- 这个通用可以运用于所有的元素，匹配`lang` = "en"或者是`lang = en-?`这类型元素 [jsBin效果](http://jsbin.com/kafuxay/1/edit?html,css,output)

```html
<style>
    img[src|="erheizi"] {
        border: solid 1px red;
    }
    img[src$="-3"] {
        padding: 10px;
    }
</style>

<img src="erheizi" alt="erheizi">
<img src="aa" alt="aa">
<img src="erheizi-2" alt="erheizi-2">
<img src="erheizi-3" alt="erheizi-2">
```


### 兄弟选择器

`+` -- 选择同一个父元素下面的兄弟元素，这个还是和第一个元素有关系的，
`h1 + p` -- 选中`p`选手
`li + li` -- 选中第二个li及之后的li元素

### 伪类

对于链接，为了确保起见，所有的链接都使用伪类`a:link`,访问过得链接使用`a:visited`,这样做可以防止链接应用到目标锚上面，如下：

```html
<style>
    a:link{
        color: blue;
    }
    a:visited{
        color: green;
    }
</style>
<a href="#">sd</a>
<a href="#">sdf</a>
<a>ads</a>  //这是一个目标锚
```

### 动态伪类
`hover/ visited/ focus`;动态伪类可以运用到任何元素

```html
<style>
a:link,a:visited{
        font-size: 18px;
    }
    a:hover{
        font-size: 24px;
    }
</style>
<a href="#">sdf</a>
```

对于这样的预想，当鼠标`hover`时候会改变尺寸，但是当a链接尺寸改变时候就会造成后面的元素位置改变，需要全部重排版和重绘，只是因为一个效果而造成的性能问题是得不偿失的。可以把a设置为绝对定位，脱离文档流来避免重排版。

### CSS 层叠样式表

html>body table tr[id="totals"] td ul > li{color: red;}
对于上面的选择器特殊值为 1+1+1+1+10+1+1+1 = 17；

内联样式表： 1000，
id：100；
class： 10；
label： 1；
*： 0；

`!important` -- 重要性声明，位置在结束符`;`之前；

```html
<style>
    p{
        color: pink !important;
    }
</style>
<p style="color: red">hello world</p>
```

最后文字显示为`pink`；

继承完全没有特殊性，连`0`都不是，而通配符`*`的特殊性是`0`，所以通配符的优先级要高于继承的值。

```html
<style>
    *{
        color: pink;
    }
    p{
        color: green;
    }
</style>
<p>hello <em>world</em></p>
```
<style>
    a:link{
        color: gray;
    }
    a:visited{
        color: green;
    }
    a:hover{
        color: purple;
    }
    a:active{
        color: red;
    }
</style>
<a href="www.erheizi.com">erheizi</a>
```
