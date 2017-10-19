---
title: 关于CSS的snipppet调用方法
date: 2016-07-03
tags: [CSS,LESS]
categories: Static
---

我之前写了一个`less`的`clearfix`的`snippet`，但是我想要调用的时候，发现怎么都无法触发，以为是不行，刚刚发现需要在`css`或者`less`文件中的模块内部调用。

```less
p{
    clear
}
<!--  -->
p{
    .clearfix {
        display: block;
        zoom: 1;
        &:after {
            content: "";
            display: block;
            clear: both;
            font-size: 0;
            height: 0;
            visibility: hidden;
        }
    }
}
```

在`p`内部只需要输入`clear`，然后按下`tab`切换就可以调出来了。