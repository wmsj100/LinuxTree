---
title: CSS 有序列表ol 无序列表ul
date: 2016-03-24 12:18:58
tags: [CSS,名词]
categories: Static
---
### 一、问答
---
1. 有序列表、无序列表、自定义列表如何使用？写个简单的例子。三者在语义上有什么区别？使用场景是什么？能否嵌套？
- 有序列表：列表前面有数字、字母或其他阿拉伯字符的表示序列的字符，属于块级元素，能够继续嵌套各种形式的标签：
  <!-- more -->
- 无序列表：列表前面是实心圆的、空心圆点、方块、或者自定义图片……总之就是无法区分列表顺序的排序方式，无序列表也可以不限制数量和形式的继续嵌套其他标签：
- 钩子方式：在IE6时代，人们为了实现自定义图标列表，进行了很多尝试，有的大神就使用了钩子方式，在列表-li-俩测添加空的div，通过设置border各边的样式或宽度也可以实现很多图标，当然这些空的div是没有语义化的，只是为了在不引入图片的情况下实现自定义样式，可以参考：
- 其实通过样式控制可以很明显的看出，无序列表和有序列表的边界是很模糊的，可以使用有序列表（ol）来实现无序列表的所有样式，反之亦可，只是为了语义化的需要，如果涉及到排序时候，还是建议使用有序列表。不涉及排序时候，使用无序列表。
- 自定义列表：多用于一个图片，然后下面有几行说明文字，或者是有很多个列表，每个列表都有相应的说明，而且很多情况下用自定义列表（dl）比有序/无序列表更有利于简化代码：
### 下面是一些常见的列表样式：
![常见列表样式](http://upload-images.jianshu.io/upload_images/1606281-a70dc5fcfc1eacc1.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

1. 如何去除列表前面的点或者数字？
   设置`list-style`属性值为`none`即可，样式如下图：
   ![list-style:none](http://upload-images.jianshu.io/upload_images/1606281-6ce7a03f51db0497.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
2. class和id有什么区别？什么时候用class什么时候用id？
- class和id都属于CSS选择器，区别在于class可以被多次使用，而id只能在一个页面中使用一次。
- class适用于使用频率高的标签样式，而id适用于重要的用于区别于其它标签且位于嵌套位置顶层的标签使用。
1. 块级元素、行内元素是什么？有什么区别？分别对应那些常用标签？
- 块级元素的行为表现：
  - 块级元素占据父元素的整个空间；
  - 浏览器会在块级元素前后另起一个新行；
  - 块级元素可以包含块级元素和行内元素；
  - 块级元素可以设置width、height、margin、padding，且水平垂直方向都有效；
  - 常见的块级元素标签：div\ p\ table\ thead \caption\tbody \ tfoot \ tr \ th \td \ form\ fieldset \ legend\ frameset \hr \ h1~h6\ ul \ol \li \dl \dt \dd 。
- 行内元素的行为表现：
  - 行内元素的宽度有内容大小决定；
  - 行内元素只能设置水平方向的width、margin、padding；
  - 行内元素的垂直方向设置的padding、margin在视觉上是无效果的，但是如果给行内元素添加背景色，背景色在垂直方向的padding和margin是生效的；
  - 行内元素只能包含行内元素，不能包含块级元素；
  - 常见的行内元素标签：a \ img \br \input \em \strong \label \select \ q\ span\ sub\ sup\ textarea\ button。
1. display:block、display:inline、display:inline-block分别有什么作用？
- display:block——把行内元素转换为块级元素；
- display:inline——把块级元素转换为行内元素；
- display:inline-block——把块级/行内元素转换为行内元素，但是拥有块级元素的垂直方向height、margin、padding大小可调节。
1. 下面代码的作用？
```
<div id="header">
    	
    </div>
    <div id="content">
    	<div class="main"></div>
    	<div class="aside"></div>
    </div>
    <div id="footer">
    	
    </div>
```
是页面HTML、CSS代码语义化，提高代码的可读性和对页面的理解性，更方便团队协作时候代码的识别度。
1. 如何理解HTML、CSS语义化？
- HTML语义化：指的是页面标签的使用，即使在没有CSS样式的视觉表现时候也可以通过HTML代码很轻松的理解页面的布局和表现；可以很高效的和搜索引擎沟通，能够被网络爬虫抓取更多关联内容；可以在特殊设备（盲人屏幕阅读器、语音设备、移动设备……）很好的理解；可以是团队在协作时候无障碍的阅读代码。
- CSS语义化：指的是在对样式命名时候，一定要有目的的、简洁的、一目了然的、约定俗成的命名方式，让人看到名称就能想到表达的是什么。
1. form表单有什么作用？有哪些常用的input标签，分别有什么作用？
- form表单常用于收集访客的填写的表单并提交到后台然后可能还会返回一个结果。
- 常用的input标签有以下几个：
  - type="text"——文字输入框
  - type="password" ——密码输入框
  - type="radio" ——单选
  - type="checkbox"——多选
  - type="button" ——按钮
  - type="submit"——提交按钮
  - type=”reset"——重置页面
     -type="hidden" ——隐藏数据，提交时候同样会传给服务器
1. post和get方式的区别？
   post和get都可以用于提交表单，但是俩者还是有区别的。
- post常用于更新后台资源，是以密文的形式提交，从页面上看不见提交的内容，而且也不会显示在输入栏显示，更不会留下什么提交记录，最重要的区别是post不限制提交信息的大小，所说的限制也只是服务器自己的限制。
- get常用于查找后台资源，是以明文的形式提交表单的，即所提交信息会出现在输入栏中，从而在浏览器的浏览记录中可以找寻到提交链接，从而可以提取出敏感信息，没有安全保障，更重要的是它有大小限制，默认小于1K，所以不适合用于提交大量文本，常用的场景是搜索关键字。
1. 在input里，name有什么用？
   input是用于收集访客的信息，而收集的方式就是以表格或者数组的形式提交到后台，而name就是提交数据时候相应的input的属性名，而访客输入的值--value--就是属性值。如果没有name，提交数据时候会直接忽视该栏input的内容。
2. <button>提交</button>、<a href="#" class="btn">提交</a>、<input type="submit" vlaue="提交">三者有什么区别？
- <button>提交</button>：这就是一个单纯的按钮，这种形式是配合JavaScript进行功能绑定用的。
- <a class="btn" href="#">提交</a>：这是把链接用CSS的样式表现为按钮形式，但作用还是一个链接。
- <input type="submit" value="提交">：这是一个专门用来表单提交的语义化的按钮，是为了把表单提交到后台进行数据交换使用的。
- 总结来说，这三者只是样式上一样，但功能是不一样的，第一个是为了JS绑定事件，第二种是一个链接，只是为了页面样式化成按钮形式；第三个是单纯的提交数据功能。
10. radio如何分组？
    radio的分组是通过name的值来分组的，相同name值的为一组。
20. placeholder属性有什么作用？
    这个属性是在访客进行表单输入时候起提示作用的，可以避免对表单的理解错误。
30. type=hidden隐藏域有什么作用？举例说明
    这个属性有很多作用，比如客户修改数据时候进行的验证功能，通过JS调用到被hidden的value值进行验证，防止恶意攻击。还可以通过这个属性进行数据的缓存，因为是不可见的，所以客户是无法察觉，但通过这个缓存可以极大的提高网页的交互性能。还可以进行很多交互方面的功能，但基本都是配合JS来实现功能的。
---
### 代码
1. 写出导航栏，文字默认颜色#444，可点，鼠标放置文字变为red。[第一题](http://book.jirengu.com/jirengu-inc/jrg-tehui2/homework/%E7%8E%8B%E6%B5%A9/%E4%BB%BB%E5%8A%A1-7/task 7-1.html)
   ![导航栏](http://upload-images.jianshu.io/upload_images/1606281-eb0c0706bbd2b91e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
2. 写出如下form表单，性别和取向是单选，爱好是多选。[第二题](http://book.jirengu.com/jirengu-inc/jrg-tehui2/homework/%E7%8E%8B%E6%B5%A9/%E4%BB%BB%E5%8A%A1-7/task 7-2.html)
   ![表单](http://upload-images.jianshu.io/upload_images/1606281-c052d8b37c85515b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
