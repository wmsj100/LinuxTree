---
title: JS的基础类型与引用类型
date: 2016-03-24 12:18:58
tags: [JavaScript]
categories: Dynamic
---
- 俩种类型：
 1. ECMAScript变量包含俩种不同类型的值：基本类型值、引用类型值；
 2. 基本类型值——指的是保存在栈内存中的简单数据段；
 <!-- more -->
 3. 引用类型值——指的是那些保存在栈内存中的对象，意思是，变量中保存的实际上只是一个指针，这个指针执行内存中的另一个位置，由该位置保存对象；
- 俩种访问方式：
 4. 基本类型值——按值访问，操作的是他们实际保存的值；
 5. 引用类型值——按引用访问，当查询时，我们需要先从栈中读取内存地址，然后再顺藤摸瓜找到保存在堆内存中的值；
![俩种类型的机制](http://upload-images.jianshu.io/upload_images/1606281-36d3fb294215aa72.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 俩种类型复制
 1. 基本类型变量的复制：从一个变量向另一个变量复制时，会在栈中创建一个新值，然后把值复制到为新变量分配的位置上。
![基本类型的复制过程](http://upload-images.jianshu.io/upload_images/1606281-4a1c8af02da4012c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
 2. 引用类型变量的复制：复制的是存储在栈中的指针，将指针复制到栈中为新变量分配的空间中，而这个指针副本和原指针执行存储在堆中的同一个对象；
 3. 复制操作结束后，俩个变量实际上将引用同一个对象；因此改变其中一个，将影响另一个；
![引用类型值复制过程](http://upload-images.jianshu.io/upload_images/1606281-30f206c8090f9fcc.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![Paste_Image.png](http://upload-images.jianshu.io/upload_images/1606281-e6b6bc9fe3995ccf.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
参考文献——[http://blog.sina.com.cn/s/blog_6fd4b3c10101d0va.html](http://blog.sina.com.cn/s/blog_6fd4b3c10101d0va.html)
