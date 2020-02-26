---
title: CSS字体图标-雪碧图
date: 2016-03-24 12:18:58
tags: [CSS,效果]
categories: Static
---
### 问题
- CSS Sprite（雪碧图）指的是什么？有什么作用
- CSS Sprite——有人叫它CSS精灵，是一种图片拼合技术，该方法是将小图标和背景图片合并到一张图片，然后利用CSS的背景定位来显示需要的图片部分。
  <!-- more -->
- 它的使用可以极大的减少网站的HTTP请求数据，而且因为图标是集中在一张图片上，所以也会使图标加载速度会很快，而且所有图片集中一张图片的大小小于所有图标单个放置的大小，这样可以提高网站性能。
- 但是它有一个显著的缺点就是如果要修改一个图标的外形和尺寸，那么所有的图标都需要重新定位，这无形中增加了CSS的维护难度和页面代码的复杂程度。而且如果是这个整张图片过大，也会占用大量的内存，提高计算机的功耗。
- img标签和CSS背景使用图片在什么场景上，有何区别？
- img标签——多用于图片内容经常变更的场景，而且引用图片地址时候使用的是——src；
- background-image——多用于图片内容不会经常改变的场景，比如文字前面的ICON图标，引用图片地址是使用的是——url；
- 由于浏览器加载页面时候是先解析内容的，所以通过CSS的background-image
- title和alt属性分别有什么作用？
- title用于为元素提供额外说明信息；
- alt属性用来指定替换文字，只能在img、area、input元素中，用于网页中图片无法正常显示时给用户提供的文字说明使其了解图片的信息。alt是替代图片作用而不是提供额外的说明。而且alt的使用还具有搜索引擎优化效果，因为搜索引擎无法直接读取图片，alt可以提供文字信息有利于搜索引擎对图片内容的收录。
- background：url（abc.png）0 0 no-repeat；这句话是什么意思？
- 背景图片引用的地址是页面目录下的abc.png图片，图片的偏移为0，不重复。
- background-size有什么作用？兼容性如何？常用的值是？
- 它的作用主要用于调整背景图片的尺寸，兼容性如下图所示：
  ![background-size兼容性](http://upload-images.jianshu.io/upload_images/1606281-963018b25adab1e2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 常用的值有以下几类：
  - auto——原始图片大小；
  - length——根据给定长度值调整背景图片大小；
  - percentage——根据给定的百分比调整图片大小；
  - contain——按比例调整背景图片，使得其图片宽高比自适应整个元素的背景区域的宽高比，因此假如背景图片过大，而背景区域的整体宽高比不能恰好包含背景图片的话，那么其背景区域会出现空白，这个值多用于响应式页面；
  - cover——按比例调整背景图片，这个值的属性和contain正好相反，背景图会按照比例填充背景区域，如果背景图片过大且不能正好按照宽高比包含背景区域，那么背景图片就会被裁减显示不全；[参考文献](http://sentsin.com/web/939.html)
- 如何让一个div水平居中？如何让图片水平居中？
- div水平居中——通过设置div的左右margin为auto即可；
- 图片水平居中——因为img为行内元素，可以为其父元素设置text-align：center，来让其水平居中；或者通过设置其作用padding值来达到视觉上的水平居中，但这样的方式对于响应式页面兼容性不好。
- 如何设置元素透明？兼容性？
- 通过css样式添加opacity的值来进行透明度的调整，但是对于IE8以及更早的版本不支持该标签，需要用filter来替换，如下：
```
div{
    opacity:0.5;
    filter:Alpah(opacity=50)/*IE8及之前版本*/
}
```
- opacity和rgba都能设置透明，有什么区别？
    俩者都可以设置透明但还是有区别的，如下：
- rgba只能作用于颜色或背景色，并不能使设置的颜色透明化；
- opacity作用于元素以及元素内部的所有元素的透明度；
   俩者的兼容性都需要IE8以上版本的支持。[参考文献](http://blog.csdn.net/q285661571/article/details/7536490)

### 代码题
- 使用CSS Sprite 把如下6张图标图片合并成一张图片，做出如下效果？
   [task 9-1](http://book.jirengu.com/jirengu-inc/jrg-tehui2/homework/%E7%8E%8B%E6%B5%A9/%E4%BB%BB%E5%8A%A1-9/task 9-1.html)
  ![雪碧图](http://upload-images.jianshu.io/upload_images/1606281-d4f98a4402e20831.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 使用字体图标实现上例效果
  [Base64样式](http://book.jirengu.com/jirengu-inc/jrg-tehui2/homework/%E7%8E%8B%E6%B5%A9/%E4%BB%BB%E5%8A%A1-9/task 9-2.html)
  [字体图标](http://book.jirengu.com/jirengu-inc/jrg-tehui2/homework/%E7%8E%8B%E6%B5%A9/%E4%BB%BB%E5%8A%A1-9/task 9-2_2.html)
  ![png-base64](http://upload-images.jianshu.io/upload_images/1606281-020eb12b5359e132.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 使用CSS border实现如下三角形
  [task 9-3](http://book.jirengu.com/jirengu-inc/jrg-tehui2/homework/%E7%8E%8B%E6%B5%A9/%E4%BB%BB%E5%8A%A1-9/task 9-3.html)
  ![border](http://upload-images.jianshu.io/upload_images/1606281-40822f54ea7b777a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
