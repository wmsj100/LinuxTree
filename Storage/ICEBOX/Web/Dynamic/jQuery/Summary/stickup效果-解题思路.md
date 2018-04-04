---
title: stickup效果-解题思路
date: 2016-4-19 10:06:36
tags: [jQuery,效果]
categories: Dynamic
---

1. 首先我无法处理clone出来的`.nav`，因为它和页面之前的`.nav`无法区分开了，我也没办法单独提取，`$static = $(".nav1").eq(0),`这种是没用的，

2. ```javascript
   $up = $static.after($static.clone())
   					 .css({"position": "fixed", "top": 0, "width": $width, "margin": 0})
   $static = $(".nav1").eq(0),					 
   ```

   上面的结果就是`$up === $static`,因为它们选择的都是页面的第一个元素。

3. 我这样考虑，既然无法区分开来，那我为什么不把clone出来的元素单独放置到一个div里面呢。这样我选择就不会这么困难了。

4. 这个思路是正确的，效果完美[预览](http://wmsj100.github.io/GrowUp/html/jirengu/task28/task 28-2.html)

5. 现在有一个新问题，那就是我的页面不能缩放，缩放就会位置错乱。但是她的就没问题，这是我需要思考的。

6. 修改了一下，但是新问题是我滚动页面时候浮动条会消失，所以我打算在创建一个父元素把clone元素进行包裹。

7. 我把这个包裹起来看DOM的时候是没问题的，因为所有的clone元素都被很好的包裹了，不会乱，但是问题还是没用解决，我忘记了for循环的目的，一个作业不能拖得时间太长。这样就会忘记一些函数的作业。