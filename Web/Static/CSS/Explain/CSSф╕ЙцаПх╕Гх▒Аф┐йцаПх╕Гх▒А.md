---
title: CSS三栏布局俩栏布局
date: 2016-03-24 12:18:58
tags: [CSS,效果]
categories: Static
---
### 问题
1. 负边距在让元素产生偏移时和position：relative有什么区别？
- 对元素使用负边距会影响后面元素的文档流，因为元素的真实位置发生了变动；
  <!-- more -->
- position：relative只是相对自己之前的位置发生偏移，但是元素在文档流中的位置没有发生变化，不会影响到后面的元素排版。
1. 使用负margin形成三栏布局有什么条件？
- 三栏内容全部浮动，然后利用clear或者BFC对父容器撑开高度；
- 分别对每个侧边栏使用负margin，其中左侧的margin：-100%；右侧margin：width；
- 需要知道俩个侧边栏的宽度width，然后针对每个侧边栏的宽度在父容器上使用相应的padding值来为侧边栏空出位置。
- 分别对每个侧边栏使用position：relative；然后利用left进行位置偏移。
1. 圣杯布局的原理是怎样的？简述实现圣杯布局的步骤
- 圣杯布局是利用了给浮动元素设置负margin从而实现垂直方向的偏移，然后利用position定位来对侧边栏进行位置调整；
- 首先需要将三栏块元素全部float，然后分别对每个侧边栏的浮动元素添加合适的负margin，然后对父容器进行padding值的设置，最后利用position：relative进行位置的偏移；
- 或者是对父元素进行相对定位，然后分别给每个侧边栏设置绝对定位；[example](http://js.jirengu.com/jusegeqaqu/1/edit?html,css,output)
  ![圣杯布局](http://upload-images.jianshu.io/upload_images/1606281-70553698aab6e425.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
1. 双飞翼布局的原理？实现步骤？
- 双飞翼的布局和圣杯有很多相似处，区别在于双飞翼的侧边栏没有使用position定位，而是在内容栏内部新建了一个子元素div，通过对它设置左右margin值来达到双飞翼的效果。
- 具体实现步骤如下：
- 先写出html部分：
```
<div class="main">
  <div class="content">
    <div class="content-show">asd</div>
  </div>
  <div class="side-left">asd</div>
  <div class="side-right">asd</div>
</div>
```
- 然后分别对content、side-left、side-right进行float；
- 分别对侧边栏进行负margin偏移；
- 最后设置content-show的作用margin值，效果如下：
  [example](http://js.jirengu.com/wugoloqaga/1/edit?html,css,output)
  ![双飞翼布局](http://upload-images.jianshu.io/upload_images/1606281-c4e4c542ee6c41ee.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
### 代码
1. 使用圣杯布局实现如下三栏布局（俩侧固定宽度200px，中间自适应）
   [task 12-1](http://book.jirengu.com/jirengu-inc/jrg-tehui2/homework/%E7%8E%8B%E6%B5%A9/12-%E4%BB%BB%E5%8A%A1-12/task 12-1.html)
   ![圣杯三栏布局](http://upload-images.jianshu.io/upload_images/1606281-880bae45818f6b74.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
2. 使用圣杯布局思路实现如下俩栏布局：
   [task 12-2](http://book.jirengu.com/jirengu-inc/jrg-tehui2/homework/%E7%8E%8B%E6%B5%A9/12-%E4%BB%BB%E5%8A%A1-12/task 12-2.html)
   ![圣杯俩栏布局](http://upload-images.jianshu.io/upload_images/1606281-7c15f207128cff16.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
3. 使用双飞翼布局实现如下三栏布局（俩侧固定固定200px，中间自适应）：
   [task 12-3](http://book.jirengu.com/jirengu-inc/jrg-tehui2/homework/%E7%8E%8B%E6%B5%A9/12-%E4%BB%BB%E5%8A%A1-12/task 12-3.html)
   ![双飞翼三栏布局](http://upload-images.jianshu.io/upload_images/1606281-e1e62667ec62d1cb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
4. 使用双飞翼布局思路实现俩栏布局：
   [task 12-4](http://book.jirengu.com/jirengu-inc/jrg-tehui2/homework/%E7%8E%8B%E6%B5%A9/12-%E4%BB%BB%E5%8A%A1-12/task 12-4.html)
   ![双飞翼俩栏布局](http://upload-images.jianshu.io/upload_images/1606281-1452cfdbc835e3c4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
