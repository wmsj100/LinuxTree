---
title: jQuery基础知识
date: 2016-4-9 22:50:33
tags: [jQuery]
categories: Dynamic
---

1. 说说库和框架的区别？

         库指的是封装了一些函数，可以很方便的拿来即可使用，是通用性质的，像jQuery就是一个库；而框架指的是高度集成的一个流程，是具有针对性的，比如针对与前端后台通讯的框架；

         一个库可能在任何场景都能找到切入点，但是框架有很大的局限性，知识针对很明确的问题提出的解决流程；

2. jQuery能做什么？

   首先`jQuery`是一个JavaScript`库，可以进行文档遍历、DOM操作、事件处理、动画效果、ajax等，并且是这些操作更加容易，而且还做了跨浏览器的兼容，这就免去了烦人的兼容问题，从而更加专注于代码的功能实现；

3. jquery 对象和 DOM 原生对象有什么区别？如何转化？

   jQuery操作对象是在DOM原生对象上面进行了封装和加工，有专属于自己的属性，比DOM原生对象操作更便捷。

   ```javascript
   <div id="index">目录</div>
   var index=document.querySelector("#index");
   //这是元素DOM对象
   var $index=$("#index");
   //这是jQuery对象；
   $(index)=>这样就把元素DOM转换为jQuery对象；
   $index[0]/$index.get()=>这样就把jQuery对象转换为DOM原生对象；
   ```

4. jquery中如何绑定事件？ `bind` 、 `unbind`、 `delegate`、 `live`、 `on` 、 `off` 都有什么作用？推荐使用哪种？使用`on`绑定事件使用事件代理的写法？

   - bind-用于绑定事件

     ```javascript
     $(".p1").bind("click",function(){
         		console.log("aaa");
         	})
     ```

   - unbind-用于解绑元素绑定的事件，不推荐使用

     ```
     $(".p1").unbind()	//解绑p1绑定的所有事件
     ```

   - delegate-是早期的事件代理函数，现在推荐使用`on`;

     ```javascript
     $(".p1").delegate("p","click",function(){
         		console.log($(this).text());
         	})
     //可以在点击p1的子元素p时候输出文本；
     ```

   - live-和delegate功能类似，而且在早期版本更推荐使用delegate替代live进行事件代理的操作

     ```
     $(".p2").live("click",function(){
         		console.log("hello");
         	})
     ```

   - on-提供了绑定事件的所有功能，可以替代早期的`bind`,`delegate`，新版本推荐使用；

     ```javascript
     $(".p1").on("click","p",function(){
         		console.log($(this).text());
         	})
     ```

   - off-用于移除通过`on`绑定的事件

     ```javascript
     $(".p1").off();
     ```

5. jquery 如何展示/隐藏元素？

   可以通过`hide / show / toggle / slideUp / slideDown / fadeIn / fadeOut / fadeToggle / slideToggle`进行控制元素的显示和隐藏；[example](https://github.com/wmsj100/test/blob/wmsj100/jquery/0409/task 25-05.html)

   ![](http://wmsj100.github.io/webFile/img/2016/April/0409/01.gif)

6. jquery 动画如何使用？

   jquery动画通过函数`animate({cssStyle},time)`来实现：[example](https://github.com/wmsj100/test/blob/wmsj100/jquery/0409/task 25-6.html)

   ![](http://wmsj100.github.io/webFile/img/2016/April/0409/02.gif)

7. 如何设置和获取元素内部 HTML 内容？如何设置和获取元素内部文本？

   ![](http://wmsj100.github.io/webFile/img/2016/April/0409/03.gif)

   ```html
   <div class="temp">
   	<h1>hello <i>world</i><br></h1>
   	<input type="text">
   </div>
   <button class="html">html</button>
   <button class="text">text</button>
   <script>
   $(".html").on("click", function() {
   	$("input").val($("h1").html());
   });
   $("input").on("keyup", function() {
   	$("h1").html($(this).val());
   });
   $(".text").on("click", function() {
   	$("input").val($("h1").text());
   })
   ```


1. 如何设置和获取表单用户输入或者选择的内容？如何设置和获取元素属性？

     通过`$("input").val()`可以得到用户的输入，通过`$("input:checked")`得到用户选择的标签，通过`$( "input" ).attr()`来查看和设置属性；如下图即代码[example](https://github.com/wmsj100/test/blob/wmsj100/jquery/0409/task 25-08.html)

     ![](http://wmsj100.github.io/webFile/img/2016/April/0409/04.gif)

### 代码

[task 25-1](https://github.com/wmsj100/test/blob/wmsj100/jquery/0409/task 25-1.html)

[task 25-2](http://www.erheizi.com/jirengu/task 25/task 25-2.html)

[task 25-3](http://www.erheizi.com/jirengu/task 25/task 25-3.html)