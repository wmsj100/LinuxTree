---
title: Web基础知识-1
date: 2016-03-24 12:18:58
tags: [CSS,名词]
categories: Static
---
### 一、样式有几种引入方式？link和@import有什么区别？
1. 样式有3种引入方式：
- 外部样式（外联式Linking）：是将网页链接到外部样式表
  <!-- more -->
  ``` <link rel="stylesheet" type="text/css" href="index.css"> ```
- 内部样式（嵌入式Embedding）：在网页上创建嵌入的样式表
````
 <style rel="stylesheet" type="text/css">
      p{
            color:red;
        }
        </style> 
````
- 内联样式（内联式Inline）：应用内联样式到网页元素
``` 
<p style="color:red; font-siez:14px;">Hello World!</p>
```
1. link和@import有什么区别？
- 本质上，这俩种方式都属于外联式Linking，都是为了引入CSS文件，但还是存在细微差别。
  - 差别1：link标签除了可以加载css外，还可以定义RSS，定义rel连接属性等，而@import就只能加载CSS。
  - 差别2：加载优先级。当一个页面被加载时，link引用的CSS会同时被加载，而@import引用的CSS会等到页面全部下载完之后再被加载。所以有时在浏览@import加载的样式页面时开始会没有样式（也就是会出现闪烁，这种情况会出现在网速比较慢的时候）。
  - 差别3：兼容性的差异。由于@import是CSS2.1提出的，所以老版本的浏览器不支持，@import只有在IE5以上的版本才能识别，而link无此顾虑。
  - 差别4：使用DOM控制样式时差别。当使用JavaScript控制样式时只能使用link标签，因为@import不是DOM可以控制的。
  - 差别5：@import可以在CSS中再次引入样式表，虽然这样做有利于修改和扩展，不过这样做有一个缺点，会对网站服务器产生过多的HTTP请求，以前是一个文件，现在确实俩个或更多文件了，服务器的压力增大，浏览量大的网站还是谨慎使用。（确实，在浏览量大的网站中首页或栏目首页等项目都会直接把CSS或JS直接写在HTML中，而不是用link或者@import外置引用。
---
### 二、文件路径 ../main.css、./main.css、main.css有什么区别？
- ../main.css是上一级文件夹中名为main.css的文件
- ./main.css是当前目录中名为main.css的文件
- main.css相当于 ./main.css的简写，也是指当前目录中的文件
---
### 三、console.log是做什么用的？
- 调试代码
- 让程序员更好的知晓在页面渲染时候代码的进程
- 彪悍的输出记录功能，可以从自己的页面上调用，也最快的方式转存尽可能多的信息到控制台上，从而更加醒目的让人意识到JS下一步需要做什么。
- 相比alert的优点是：
- console.log能看到结构性的东西，如果是alert，弹出一个对象就是『object object』，但是console能看到对象的内容。
- console不会打断你页面的操作，如果用alert弹出内容，那么页面就死了，但是console输入内容之后页面还是可以操作的。
- console的内容非常丰富，可以在控制台输入console进行查看。
---
### 四、text-align:justify是什么意思？
- 这个属性值是文本俩端对齐的意思。
- 对齐的内容可以是纯文本，纯英文，以及中英文混排，都可以实现完美的俩端对齐。
---
### 五、px、em、rem分别是什么？有什么区别？如何使用？
- px像素（pixel）相对长度单位。像素px是相对于显示器的分辨率而言的。
- px特点：
  - IE无法调整那些使用px作为单位的字体大小；
  - Firefox能够调整px和em、rem，但是96%以上的中国网民使用IE或者IE内核的浏览器。
- px使用：
  - 任意浏览器的默认字体都是16px，chrome的最小字体大小是12px。
- em是相对长度单位。相对于当前对象内文本的尺寸，如果当前文本为设置尺寸，则向上查询并继承尺寸，如果都没有设置尺寸，则相对于浏览器的默认字体尺寸（16px）。
- em特点：
  - em的值并不是固定的；
  - em会继承父级元素的字体大小。
- em使用：
  - 任意浏览器的默认字体大小都是16px，所以未调整的浏览器都符合1em=16px；
  - 那么12px=0.75em，10px=0.625em；
  - 为了简化font-size的换算，需要在CSS中的body选择器中声明font-size=62.5%，这就使em的值变为16px*0.625=10px,这样12px=1.2em，10px=1em，也就是说只需要将原来的px值除以10，然后换上em作为单位就行了。
- rem（root em）是相对于HTML根节点的单位。
- rem特点：
  - rem是CSS3新增的一个相对单位；
  - 这个单位和em的区别是rem仍然是相对单位，但只是相对于HTML根节点的；
  - 这个单位可谓是集相对大小和绝对大小的优点于一身，通过它既可以做到只修改根节点大小就可以成比例的调整所以的字体，有可以避免字体大小逐层复合的连锁反应。
  - 目前，除了IE8及更早的版本外，所有的浏览器均已支持rem，应对方法也很简单，就是多写一个绝对单位的声明，这些浏览器会忽略rem设定的字体大小。
- 选择使用什么单位主要是看项目的客户群，如果客户都似乎使用新版浏览器，那么就放心大胆的使用rem，如果要考虑兼容性，那就是要px，或者俩者同时使用。
---
### 六、对chrome审查元素的功能做个简单的截图介绍。

![elements](http://upload-images.jianshu.io/upload_images/1606281-8b03cf5e1c86fcd3.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![network简单介绍](http://upload-images.jianshu.io/upload_images/1606281-1c1a6e4836b4b1fa.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![resources介绍](http://upload-images.jianshu.io/upload_images/1606281-bb07526771203599.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![Audits优化建议](http://upload-images.jianshu.io/upload_images/1606281-b9ed7e652d1fae07.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![Timeline内存优化](http://upload-images.jianshu.io/upload_images/1606281-291c4b8c1e08a768.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
