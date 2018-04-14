---
title: CSS-BFC-边距合并
date: 2016-03-24 12:18:58
tags: [CSS]
categories: Static
---
### 问题
- 在什么场景下会出现外边距合并？如何合并？如何不让相邻元素外边距合并？
- 在俩个盒模型都处于同一个BFC（块级格式上下文）时候，元素的上下margin会合并；
  <!-- more -->
- margin合并时候保留margin值大的一个，如果俩个margin值相等，则取任一个值为合并后的margin；
- 让俩个盒模型不要处于同一个BFC中即可，可以对一个盒模型增加父容器，并且给父容器添加样式`overflow:hidden/auto/scroll`
  [jsbin演示](http://js.jirengu.com/?html,css,output)
  ![margin重叠](http://upload-images.jianshu.io/upload_images/1606281-3b6aa3a8ea9aebc1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
  ![margin没有重叠](http://upload-images.jianshu.io/upload_images/1606281-c728ef0a18ad2507.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 去除inline-block内缝隙有哪几种方式？
- 把设置inline-block元素的标签放置在一行，并且删除标签之间的空格；
- 把设置inline-block元素的结束标签折行，但是结束标签和下一个元素的开始标签之间不能有空格；
- 给设置inline-block的元素添加负margin属性；
- 给设置inline-block元素的父元素设置font-size=0；然后给该元素添加字体大小设置；
  [@example](http://js.jirengu.com/favanakami/1/edit?html,css,output)
  ![去除inline-block缝隙](http://upload-images.jianshu.io/upload_images/1606281-e8f430cfcde598a6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 父元素使用overflow：hidden |auto撑开高度的原理是什么？
- BFC（块级格式上下文）用于对块级元素排版，默认情况下只有根元素（body）一个BFC，但是如果一个块级元素设置了float：left |right；overflow：hidden |auto |scroll；position：absolute |fixed样式，就会为这个元素生成一个独立的块级格式上下文，新开辟的BFC就像一个小宇宙，使这个块级元素内部的排版完全独立隔绝；
- 独立的块级格式上下文可以包裹浮动流，全部浮动子元素也不会引起父容器高度塌陷，也就是说包含块会把浮动元素的高度也计算在内，所以不用清除浮动来撑开高度；
- 因为块级格式上下文区域内部不会对外部排版造成影响，而现在因为浮动是父容器高度塌陷，进而影响了外部布局。所以BFC就给内部的浮动元素撑开了空间，保证不影响外部的排版。
- 正常父元素包含浮动元素，父元素的高度确实为0，但是父元素overflow：hidden后，首先会计算height：auto的真实高度，由于触发了BFC，需要包含子元素，所以高度不是0，而是子元素高度。这是overflow：hidden才起到隐藏作用，不过父元素高度足够大，所以子元素没有被隐藏。总之，是先计算真实高度，再去隐藏。如果是先直接隐藏了，再去计算高度也就没有意义了。
- BFC是什么，如何形成BFC，有什么作用？
- BFC——块级格式化上下文，它是一个独立的块级渲染区域，只有Block-level Box参与，该区域拥有一套渲染规则来约束块级盒子的布局，且与区域外部无关；
- CSS2.1中规定满足下列CSS声明之一的元素便会生成BFC：
  - float的值不为none；
  - overflow的值不为visible；
  - display的值为inline-block、table-cell、table-caption；
  - position的值为absolute或fixed；
- BFC常见的作用是防止margin重叠、清除浮动造成的父容器高度塌陷和页面布局；
- 浮动导致的父容器高度塌陷指的是什么？为什么会产生？有几种解决方法？
- 浮动导致父容器高度塌陷指的是父容器的高度height=0，塌陷成一条border线；
- 产生塌陷的原因是对元素进行浮动之后，元素会脱离标准文档流，而父容器由于内部元素的脱离成为了空集，因为没有子元素撑开高度，所以就会塌陷。
- 常见的解决方式有几下几种：
  - 通过为父容器设置：overflow：hidden，把父容器转换为BFC来撑开高度；
  - 为父容器指定一个合适的高度值来撑开高度；
  - 为父容器的最后一个子元素后边添加一个空的div，并且为该div设置clear：both；
  - 使用css伪类操作：
```
.parent::after{
  content: "";
  display: block;
  height: 0;
  visibility: hidden;
  clear: both;
}
```
    或者是更为简洁的方式：
```
.parent::after{
  content: "";
  display: table;
  clear: both;
}
```
- 以下代码每一行的作用是什么？为什么会产生作用？和BFC撑开空间有什么区别？
```
.clearfix:after{   /* 给class属性值为clearfix的元素后面添加伪类 */
		content: "";  /* 伪类的内容为空 */
		display: block;  /* 转换为块级元素 */
		clear: both;  /* 清除浮动方式为俩边 */
	}
	.clearfix{
		*zoom: 1;   /* ------兼容IE6、7-- */
	}
```

### 代码
1. 实现如下效果的导航条？
   [task 11-1](http://book.jirengu.com/jirengu-inc/jrg-tehui2/homework/%E7%8E%8B%E6%B5%A9/%E4%BB%BB%E5%8A%A1-11/task 11-1.html)
   ![导航条](http://upload-images.jianshu.io/upload_images/1606281-fee6a0328ee9655e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
2. 利用BFC原理实现下图俩栏布局？
   [task 11-2](http://book.jirengu.com/jirengu-inc/jrg-tehui2/homework/%E7%8E%8B%E6%B5%A9/%E4%BB%BB%E5%8A%A1-11/task 11-2.html)
   ![俩栏布局](http://upload-images.jianshu.io/upload_images/1606281-2f7612134247a195.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
