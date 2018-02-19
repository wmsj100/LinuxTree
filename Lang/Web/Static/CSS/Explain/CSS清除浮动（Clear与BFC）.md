---
title: CSS清除浮动（Clear与BFC）
date: 2016-03-24 12:18:58
tags: [CSS,浮动]
categories: Static
---
在CSS布局中float属性经常会被用到，但使用float属性后会使其在普通流中脱离父容器，让人很苦恼。

```css
.clearfix:after{
        content: "";
        display: block;
        clear: both;
        height: 0;
    }
    .clearfix{
        zoom: 1;
    }
```
像上面这个`clearfix`就成为了通用的清除浮动的样式；

<!-- more -->
1. 浮动带来布局的便利，却也带来了新问题；
```
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Clear float</title>
    <style type="text/css">
        .container{
            margin: 30px auto;
            width:600px;
            height: 300px;
        }
        .p{
            border:solid 3px #a33;
        }
        .c{
            width: 100px;
            height: 100px;
            background-color: #060;
            margin: 10px;
            float: left;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="p">
            <div class="c"></div>
            <div class="c"></div>
            <div class="c"></div>
        </div>
    </div>
</body>
</html>
```
我们希望看到的效果是这样的：
![Paste_Image.png](http://upload-images.jianshu.io/upload_images/1606281-822f644efd14133a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
但结果却是这样的：
![Paste_Image.png](http://upload-images.jianshu.io/upload_images/1606281-8ec3abab233b8df1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
父容器并没有把浮动元素包围起来，俗称塌陷，为了消除这种现象，我们需要一些清除浮动的技巧。

1. 如何清除浮动
   清除浮动一般有俩种思路：
   - 利用clear属性，清除浮动；
   - 使父容器形成BFC；
     分别看一下：

2.1 利用clear属性清除浮动；
clear属性是一个什么东东呢？clear属性规定元素的那一侧不允许其他浮动元素，修改一下刚才的代码：
```
<div class="p">
    <div class="c"></div>
    <div class="c" style="clear:left;"></div>
    <div class="c"></div>
```
![Paste_Image.png](http://upload-images.jianshu.io/upload_images/1606281-2ee9f06b0609c109.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
第二个div添加了clear：left属性后，其左侧的div（第一个div）不再浮动，我们可以利用这点在父容器的最后添加一个空的div，设置属性clear：left，这样就可以达到我们的目的了。

2.1.1 添加空的div清理浮动
对我们刚才代码稍作修改
```
<div class="p">
    <div class="c"></div>
    <div class="c"></div>
    <div class="c"></div>
    <div style="clear:left;"></div>
</div>
```
也就是在父容器的最后添加`<div style="clear:both"></div>`看看效果
![Paste_Image.png](http://upload-images.jianshu.io/upload_images/1606281-2178eaf1c3958055.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
果真好使了，有些同学看了后可能感觉奇怪，为什么想上一个例子修改第二个div`<div style="clear:left" class="c"></div>`没有变成这样的效果
![Paste_Image.png](http://upload-images.jianshu.io/upload_images/1606281-eb600398894598f1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
说一下自己的拙见，clear：left属性只是消除其左侧div浮动对自己造成的影响，而不会改变左侧div甚至于父容器的表现，在父容器看来，三个div都还是浮动的，所以高度依旧是塌陷。但是我们在最后添加了一个非浮动的div，由于它有clear：left属性，所以它会按照左侧div不浮动来定位自己，也就是定位到下一行，而父容器看到有一个非浮动，普通流的子元素，会将其包围，这样造成了顺便也把三个浮动元素也包裹起来的效果，高度不再塌陷。

2.1.2 使用CSS插入效果
上面的做法浏览器兼容性不错，但是有个很大的问题就是向页面添加了内容来改变效果的目的，也就是数据和表现混淆，既然是变现，看看怎么使用CSS来解决这一问题。根本的做法还是向父容器的最后追加元素，但我们可以利用CSS的：after伪元素来做此事。
添加一个floatfix
```
.floatfix::after{
  content: ".";
  display:block;
  height:0;
  visibility:hidden;
  clear:left;
}
```
对父容器添加此类
```
<div class="p floatfix">
  <div class="c">1</div>
  <div class="c">2</div>
  <div class="c">3</div>
</div>
```
这样我们就可以看到正确效果了
![Paste_Image.png](http://upload-images.jianshu.io/upload_images/1606281-10c41d0fe4abb309.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

2.1.3 大师手笔
nicolas Gallagher在[A new micro clearfix hack](http://nicolasgallagher.com/micro-clearfix-hack/)中提供了一种看起来更清爽的做法；
```
.floatfix::after{
  content: "";
  display:table;
  clear:both;
}
```

2.2 使父容器形成BFC
BFC有三个特性：
- BFC会阻止外边距（margin-top、margin-bottom)折叠;
  - 按照BFC的定义，只有同属于一个BFC时，俩个元素才有可能发生垂直Margin的重叠，这个包括相邻元素、嵌套元素，只要它们之间没有阻挡（例如边框、非空内容、padding；）就会发生margin重叠。
  - 因此要解决margin重叠问题，只要让它们不在同一个BFC就行了，但是对于俩个相邻的元素来说，意义不大，没有必要给它们加个外壳，但是对于嵌套元素来说就很有必要了，只要把父元素设置为BFC就可以了。这样子元素的margin就不会和父元素的margin发生重叠了。
- BFC不会重叠浮动元素；
- BFC可以包含浮动；

我们可以利用BFC的第三条特性来”清除浮动“，这里其实说清除浮动已经不再合适，应该说包含浮动。也就是说只要父容器形成BFC就可以，简单看看如何形成BFC
- float为left | right；
- overflow为 hidden | auto | scroll；
- display为 table-cell | table-caption | inline-block;
- position为 absolute | fixed;
  我们可以对父容器添加这些属性来形成BFC达到”清除浮动“的效果

2.2.1 利用float来使父容器形成BFC
```
<div class="p" style="float:left;">
    <div class="c">1</div>
    <div class="c">2</div>
    <div class="c">3</div>
```
![Paste_Image.png](http://upload-images.jianshu.io/upload_images/1606281-0af8c139d703c1a1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
我们可以看到父容器高度没有塌陷，但是长度变短了，因为div应用float后会根据内容来改变长度，这个在很多时候有用。

2.2.2 使用BFC的其他局限
上面提到使用BFC使用float的时候会使父容器的长度缩短，而且还有一个重要缺陷——父容器float解决了其塌陷问题，那么父容器的父容器怎么办？难道要全部使用float吗（确实有这种布局方式）。BFC的几种布局方式都有自己的问题，overflow会影响滚动条和绝对定位的元素；position会改变元素的定位方式，这是我们不希望的，display这几种凡是依然没有解决低版本IE问题……

2.2.3 haslayout
我们知道在IE6、7内有个hasLayout的概念，很多bug正式由hasLayout导致的，当元素的hasLayout属性值为false的时候，元素的尺寸和位置由最近拥有布局的祖先元素控制。当元素的hasLayout属性值为true的时候会达到和BFC类似的效果，元素负责本身及其子元素的尺寸设置和定位。我们可以利用这点儿在IE6、7下完成清浮动，先看看怎么使元素hasLayout为true
**position**: absolute 
**float**: left|right
**display**: inline-block
**width**: 除 “auto” 外的任意值
**height**: 除 “auto” 外的任意值
**zoom**: 除 “normal” 外的任意值
**writing-mode**: tb-rl

在IE7中使用**overflow**: hidden|scroll|auto 也可以使hasLayout为true

3 一个相对靠谱的解决方案
- 在IE+、现代浏览器上使用伪元素；
- 在IE6、7使用haslayout;
```
.floatfix{
    *zoom:1;
}
.floatfix:after{
    content:"";
    display:table;
    clear:both;
}
```
参考文献——[CSS清浮动处理（Clear与BFC）](http://www.cnblogs.com/dolphinX/p/3508869.html)
