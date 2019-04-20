---
title: less入门教程
date: 2016-06-21
tags: [CSS,LESS]
categories: Static
---

http://www.w3cplus.com/css/less
- 首先需要引入`less`脚本，然后修改`css`的`link`内容。

```html
<link rel="stylesheet/less" href="10.css">
<script src="../less.js"></script>
```

- less的变量前面多用`@`，

```css
@color: red;
h3{
    color: @color;
}
```

- less支持变量

```css
@color: #5b83ad;
@highlight: "color";
h3{
    color: @@hightlight;
}
```

less中的变量实际上就是常量，因为它们只能被定义一次。

```css
@color: #5b83ad;
@highlight: "color";
@color: #696969;
h3{
    color: @@hightlight;
}
```

后者会覆盖前者；

### Mixins -- 混入

```css
.roundedCorners(@radius: 5px) {
    -webkit-border-radius: @radius;
    -moz-border-radius: @radius;
    border-radius: @radius;
}
h3{
    border: solid 1px red;
    .roundedCorners;
}
p{
    border: solid 1px red;
    .roundedCorners;
}
```

参数在设置时候可以设置一个默认值，但在调用的时候可以输入新值。

```css
.roundedCorners(@radius:5px) {
    -webkit-border-radius: @radius;
    -moz-border-radius: @radius;
    border-radius: @radius;
}
h3{
    border: solid 1px red;
    .roundedCorners(10px);
}
p{
    border: solid 1px red;
    .roundedCorners(3px);
}
```

`arguments`可以替代参数的输入

```css
.boxShadow(@x:0,@y:0,@blur:0,@color: #fff) {
    -webkit-box-shadow: @arguments;
    box-shadow: @arguments;
}
.h3{
    .boxShadow;
}
```

### Nested Rules

```html
    <style>
        #header{
            display: inline-block;
            float: left;
            h1 {
                font-size: 26px;
                font-weight: bold;
                a {
                    text-decoration: none;
                    color: #f36;
                    &:hover {
                        text-decoration: underline;
                        color: #63f;
                    }
                }
            }
            p {
                font-size: 12px;
            }
        }
    </style>

    <div id="header">
        <h1><a href="#">hello world</a></h1>
        <p>hello wrold</p>
    </div>
```

这个嵌套模仿`DOM`的结构，`&`表示同一个元素或者此元素的伪类。没有`&`表示后代元素

### 4.Functions & Options

`Options` -- 主要是针对颜色、尺寸、变量进行加减乘除四则运算

- 同一单位的四则运算

```css
@base: 5%;
@filter: @base*2;
@other: @base + @filter;
#header {
    color: #888/2;
    height: 100%/2 + @other;
}
```

`less`代码不能有空格；否则运算时候会报错。
- 不同单位的四则运算

```css
@var: 15px+5;
#header {
    height: @var+5*20;
    width: (@var + 5)*20;
}
```

`Functions` -- 具有多种颜色变换的功能。
- `lighten(@color,10%)` -- 颜色变浅；
- `darken(@color,10%)` -- 颜色变深；
- `saturate(@color,10%)` -- 饱和度加； 
- `desaturate(@color,10%)` -- 饱和度减；
- `fadein(@color,10%)` -- 透明度减 
- `fadeout(@color,10%)` -- 透明度加；
- `spin(@color,10)` -- 色相加度； 
- `spin(@color,-10)` -- 色相减度； 

```css
@base: #f04615;
#header{
    color: @base;
    background-color: fadein(@base,50%);
    h1{
        color: lighten(@base, 20%);
        background-color: lighten(fadeout(@base, 20%), 5%);
        a {
            color: darken(@base, 50%);
            background-color: spin(@base, 10);
            &:hover {
                color: saturate(@base, 30%);
                background-color: fadein(spin(@base, -5), 20%);
            }
        }
    }
    p{
        color: desaturate(@base, 60%);
    }
}
```

### 5. Namespaces 命名空间

这个就是如果有一个模块样式(部分)一样，就可以进行这样的引用。**但是这个最好是进行`class`引用，如果直接引用标签`p`就会出现警告。**

```css
#header{
    .wrap {
        display: block;
        border: solid 1px red;
        background-color: gray;
        &:hover {
            background-color: white;
        }
    }
    .p1{
        color: red;
        font-size: 14px;
    }
}
h3{
    #header > .wrap;
    #header > .p1;
}
```

### 6. scope 变量范围

变量有作用域，和js的原型链变量搜索类似，先从自身查找，然后上升到父元素，最后是全局。

```css
@var: red;
.wrap{
    @var: purple;
    color: @var;
}
.p1{
    color: @var;
}
```

变量不必在使用前申明，所以下面的代码也是可行的。

```css
@var: red;
h3{
    color: @var;
    @var: green;
}
p{
    color: @var;
}
```

### 7. comments 注释

可以采用单行注释(//...),
多行注释(/*....*/);
也可以采用css的注释方法(/*.....*);

### 8. import 引入外置`less/css`文件

02.less

```css
@var: red;
p{
    color: green;
}
```

```css
@import "02.less";
h3{
    color: @var;
}
```



