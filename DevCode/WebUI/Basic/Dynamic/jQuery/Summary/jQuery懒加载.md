---
title: jQuery懒加载
date: 2016-04-23
tags: [jQuery,效果]
categories: Dynamic
---

## 问答

1. 如何判断一个元素是否出现在窗口可视范围（浏览器的上边缘和下边缘之间，肉眼可视）。写一个函数 `isVisible`实现

   ```javascript
   isVisible($("div"));
   function isVisible($node) {
     $node.each(function() {
       var top = $(this).offset().top,
         height = $(window).height(),
         scrollTop = $(window).scrollTop();
       if (top < height + scrollTop && top > scrollTop) {
         console.log($(this).text());
       }
     });
   }
   ```

2. 当窗口滚动时，判断一个元素是不是出现在窗口可视范围。每次出现都在控制台打印 `true` ,用代码实现

   ```javascript
   var clock;
   $(window).on("scroll", function() {
     if (clock) {
       clearTimeout(clock);
     }
     clock = setTimeout(function() {
       isVisible($("div"));
     }, 500)
   })

   function isVisible($node) {
     $node.each(function() {
       var top = $(this).offset().top,
         height = $(window).height(),
         scrollTop = $(window).scrollTop();
       if (top < height + scrollTop && top > scrollTop) {
         console.log(true);
       }
     });
   }
   ```

3. 当窗口滚动时，判断一个元素是不是出现在窗口可视范围。在元素第一次出现时在控制台打印 true，以后再次出现不做任何处理。用代码实现

   ```javascript
   var clock;
   $(window).on("scroll", function() {
     if (clock) {
       clearTimeout(clock);
     }
     clock = setTimeout(function() {
       isVisible($("div"));
     }, 500)
   })

   function isVisible($node) {
     $node.each(function() {
       var current = $(this);
       var top = current.offset().top,
         height = $(window).height(),
         scrollTop = $(window).scrollTop();
       if (top < height + scrollTop && top > scrollTop) {
         showNode(current);
       }
     });
   }

   function showNode(cur) {
     if (cur.attr("data-show")) {
       return;
     }
     cur.attr("data-show", true);
     console.log(cur.attr("data-show"))
   }
   ```

4. 图片懒加载的原理是什么？

   - 正常图片加载是通过给`img`标签的`src`赋值来实现的，当浏览器读取到`src`的时候就会加载图片，但是如果图片过多这样就需要大量的时间和性能来加载全部图片，而实际上没必要一次就把全部图片加载完成，懒加载就是解决性能问题而出现的。
   - 懒加载是通过判断图片是否显示然后从存储图片位置信息的属性中提取值，再赋值给`src`,然后图片就会加载，而没有显示的图片因为`src`值为空，或者是为了避免图片丑陋问题`src`的值是一个模板图片。这样的话，图片就会按需加载了。

## 代码

[task 29-1](http://www.erheizi.com/jirengu/task 29/task 29-1/task 29-1.html) [github](https://github.com/wmsj100/GrowUp/blob/gh-pages/html/jirengu/task29/task 29-1/task 29-1.html)

[task 29-2懒加载-监听父元素](http://www.erheizi.com/jirengu/task 29/task 29-2/task 29-2-lazy-listen-parent/02.html) [github](https://github.com/wmsj100/GrowUp/blob/gh-pages/html/jirengu/task29/task 29-2/task 29-2-lazy-listen-parent/02.html)

[task 29-2懒加载-监听子元素](http://www.erheizi.com/jirengu/task 29/task 29-2-lazy-listen-son/02.html) [github](https://github.com/wmsj100/GrowUp/blob/gh-pages/html/jirengu/task29/task 29-2/task 29-2-lazy-listen-son/02.html)[]

[task 29-3懒加载-无限加载](http://www.erheizi.com/jirengu/task 29/task 29-3/task 29-3.html) [github](https://github.com/wmsj100/GrowUp/blob/gh-pages/html/jirengu/task29/task 29-3/task 29-3.html)

