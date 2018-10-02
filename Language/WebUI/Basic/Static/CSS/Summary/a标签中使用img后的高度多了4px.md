---
title: a标签中使用img后的高度多了4px
date: 2016-05-25
tags: [CSS]
categories: Static
---

前两天，在做一个网站的时候，发现a标签中使用img后的高度多了4px，各种纠结。

最后，仔细分析，终于找到原因了，因为img是行内元素，默认display: inline; 它与文本的默认行为类似，下边缘是与基线（baseline）对齐，而不是紧贴容器下边缘。将displayp设置为block即可消除4px的BUG。

既然原因找到了，那么，解决方案肯定不止这一种啦！

如下：

    1.将图像定义成block (display:block)
    2.给父级设置固定高度，然后overflow:hidden
    3.设置font-size:0;
    4.设置 img 的 vertical-align: bottom;
    5.设置 img 的 margin-bottom: -4px;

就是这样，以后可以根据具体使用场景来确定最优方案了。
我比较喜欢第4个，给图片设置对齐方式，感觉影响是最小的。
