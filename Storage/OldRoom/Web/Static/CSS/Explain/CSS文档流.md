---
title: CSS文档流
date: 2016-03-24 12:18:58
tags: [CSS]
categories: Static
---
### 问答
- 文档流的概念指什么？有哪种方式可以让元素脱离文档流？

- 文档流指的是在没有浮动和定位的时候，元素按照自然的方式，从左到右，从上倒下布局。
  <!-- more -->

- 脱离文档流的方式有——浮动（float）、绝对定位（absolute）、固定定位（fix）；

- 通过设置标签的display属性值可以改变元素的文档流方式，但是不会脱离文档流；

- 有几种定位方式，分别是如何实现定位的，使用场景如何？

- absolute——生成绝对定位元素，相对于static定位以外的第一个父元素进行定位，该定位会脱离文本流，多用于特殊位置的页面布局，比如页面左侧的用户头像：
  ![头像](http://upload-images.jianshu.io/upload_images/1606281-ccf0ca0b8106f7ef.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

- fixed——生成绝对定位元素，相对于浏览器窗口进行定位，该定位方式也会脱离文档流，多用于广告或者顶部导航栏的布局：
  ![导航栏](http://upload-images.jianshu.io/upload_images/1606281-adb17a53c3eb2e84.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

- relative——生产相对定位，相对于其正常位置进行定位，该定位不会脱离文档流，相对定位和绝对定位的使用场景差不多，但是因为相对定位可以作为其他定位方式的参考，所以使用的更加广泛。

- static——正常文本流定位，是默认的定位方式，大部分的页面都是按照这样的定位方式进行基础布局。

- inherit——规定应该从父元素继承position属性的值，这是所有CSS都会默认具有的继承属性。

- absolute、relative、fixed偏移的参考点分别是什么？

- absolute——参考点是父元素中除了默认文档流外的最靠近的定位元素，如果所有的父元素都没有符合的定位方式，那么就以浏览器页面边界为定位参考点。

- relative——参考点是定位元素本身；

- fixed——定位参考点是浏览器窗口；

- z-index有什么作用？如何使用？

- z-index用于调整层叠定位元素的可见优先级，只能用于定位元素中。(position: absolute, relative, fixed)

- position：relative和负margin都可以使元素位置发生偏移？二者有什么区别？

- 二者最大的区别就是前者不会对文档流产生影响，而后者会对文档流中的页面布局产生影响。前者无论如何定位，元素所占区域大小不变，而后者随着margin的值的变化，元素所占页面的区域也在变化。

- position:relative可以调整定位元素的z-index层级，而负margin不能；

- position：relative主要配合绝对定位对页面进行版块布局方面的定位，而负margin主要用于小的细节方面的位置调整。

- 如何让一个固定宽高的元素在页面上垂直居中水平居中？
  有俩种方式，table-cell、absolute；

- table-cell方式：

  ```css
  .p1{
    border:solid 1px;
    width:100px;
    height:100px;
    display:table-cell;
    text-align:center;
    vertical-align:middle;
  }
  .p2{
    width:50px;
    height:50px;
    background:red;
    display:inline-block;
    
  }
  ```

  [table-cell](http://js.jirengu.com/dijeqiwaru/1/edit?html,css,output)
  ![table-cell](http://upload-images.jianshu.io/upload_images/1606281-5fe210c01fdfb0ce.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

- absolute方式：

  ```css
  .p1{
    width:100px;
    height:100px;
    border:solid 1px;
    position:relative;
  }
  .p2{
    width:50px;
    height:50px;
    background:red;
    position:absolute;
    top:50%;
    left:50%;
    margin-top:-25px;
    margin-left:-25px;
  }
  ```

  [absolute/负margin方法](http://js.jirengu.com/qahopiteci/1/edit)
  ![absolute或者负margin](http://upload-images.jianshu.io/upload_images/1606281-411d1892bf3aa046.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

- 浮动元素有什么特征？对其他浮动元素、普通元素、文字有什么影响？

- 浮动元素可以作用移动，直至它的外边缘遇到包含框或者另一个浮动框的边缘。

- 浮动元素不属于文档的普通流，当一个元素浮动后，不会影响到块级元素的布局而只会影响到内联框的排列，文档中的普通流就会表现的和浮动框不存在一样，当浮动框的高度超出文档框的时候，文档框/包含框并不会自动升高来闭合浮动框，所以就会造成高度塌陷的情况。
  [高度塌陷](http://js.jirengu.com/yalidigiza/1/edit?html,css,output)
  ![高度塌陷](http://upload-images.jianshu.io/upload_images/1606281-dcc529f830c7a593.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

- 当一个元素浮动之后，其他浮动元素（假如浮动方式相同，都是左浮动）会紧挨着浮动元素表现出行内元素的特性，浮动元素的高度会收缩。
  [浮动后](http://js.jirengu.com/qututuxoru/1/edit?html,css,output)
  ![未浮动前](http://upload-images.jianshu.io/upload_images/1606281-d404514918787f5f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
  ![浮动后](http://upload-images.jianshu.io/upload_images/1606281-ceb5e0e2a359f30c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

- 如果浮动元素后面是块级元素，那么块级元素就会被浮动元素本身覆盖，使其不可见，或者显示不完整。
  [浮动遮盖](http://js.jirengu.com/gugepoxoqa/1/edit)
  ![浮动后遮盖了div.p2](http://upload-images.jianshu.io/upload_images/1606281-ca4fb3ad8a9fa469.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

- 如果浮动元素后面是包含文字的块级元素，则文字会被挤到第三个文档流中，并且与第三个文档流中的文字重叠。
  [文字重叠](http://js.jirengu.com/gugepoxoqa/1/edit)
  ![文字重叠](http://upload-images.jianshu.io/upload_images/1606281-aa43b18e8aae24ad.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
> [查看文献](http://www.jb51.net/css/67471.html)
- 清除浮动指的是什么？如何清除浮动？
- 清除浮动——指的是清除由于浮动元素对自身造成的影响，也就是说清除这个操作必须是使用在由浮动造成影响的元素上，如果是使用在其他元素上面是没有任何效果的。
  ![浮动1](http://upload-images.jianshu.io/upload_images/1606281-21dd891094869bee.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
  此时div.p2受到了影响，被div.p1给覆盖了，所以如果在受影响的p2上面清除浮动，p2就可以显示出来，
  ![.p2 clear:left;](http://upload-images.jianshu.io/upload_images/1606281-548940756c9bffd1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
  但是如果在没有收到影响的p3上面清除浮动，是没有任何效果的。
  ![p3 clear：left](http://upload-images.jianshu.io/upload_images/1606281-a45025f732fb828c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
  [JS Bin 代码](http://js.jirengu.com/soyevixose/1/edit?html,css,output)
- 清除浮动的方式有3种值：
  - clear：left——清除元素左边的浮动元素；
  - clear：right——清除元素右边的浮动元素；
  - clear：both——清除元素左右俩边的浮动元素；
> 所谓的清除浮动并不是把浮动元素清除掉了，而是把块元素向下移动，使其在水平方向上面没有浮动元素。清除浮动操作只能在块级元素上面使用，在行内元素上面使用是没有效果的。如下：
> ![span clear:both](http://upload-images.jianshu.io/upload_images/1606281-7e4fb2b86a3abb4b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
> 清除浮动——[参考文献](http://www.jb51.net/css/67471.html)
### 代码
- 写出如下俩栏布局，其中中间区块宽度900px，居中，左侧边栏宽度200px，右侧边栏宽![高度塌陷](http://upload-images.jianshu.io/upload_images/1606281-dcc529f830c7a593.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)度700px；
  [task 10-1](http://book.jirengu.com/jirengu-inc/jrg-tehui2/homework/%E7%8E%8B%E6%B5%A9/%E4%BB%BB%E5%8A%A1-10/task 10-1.html)
  ![task 10-1](http://upload-images.jianshu.io/upload_images/1606281-162c803a85d8a133.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 不使用背景图片实现如下效果
  [task 10-2](http://book.jirengu.com/jirengu-inc/jrg-tehui2/homework/%E7%8E%8B%E6%B5%A9/%E4%BB%BB%E5%8A%A1-10/task 10-2_2.html)
  ![task 10-2](http://upload-images.jianshu.io/upload_images/1606281-4b5c217ac9d29595.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
