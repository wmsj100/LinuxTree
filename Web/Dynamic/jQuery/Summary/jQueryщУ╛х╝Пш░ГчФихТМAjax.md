---
title: jQuery链式调用和Ajax
date: 2016-4-12 22:00:28
tags: [jQuery,Ajax]
categories: Dynamic
---

### 问答

1. Jquery 中， $(document).ready()是什么意思？还有其他什么写法或者替代方法？

   `$(docment).ready(function(){})`的意思是等页面全部加载完成之后再执行`jquery`;

   可以直接用一个匿名函数来申明`$(function(){})`,效果是一样的。

2. $node.html()和$node.text()的区别?

   `node.html()`--可以查看或者修改`node`节点内部的HTML;

   `node.text()`--可以查看或者修改`node`节点的文本内容;

   ```javascript
   <div class="wrap"><p class="item">item 1</p></div>
   ------
   $(".wrap").html();
   //"<p class="item">item 1</p>"
   $(".wrap").text();
   //"item 1"
   ```

3. $.extend 的作用和用法?

   `$.extend`--用于合并对象值，有3中合并模式

   - 浅拷贝模式--何必俩个对象的值，如果有同名属性，简单的用后者覆盖前者；

     ```javascript
     var defaults = {
     	name: "wmsj",
     	age: "20",
     	ability: {
     		eat: "less",
     		do :"more.."
     	}
     };
     var options = {
     	name: "wmsj100",
     	sex: "male",
     	ability: {
     		write: "good",
     		eat: "more",
     	}
     };
     $.extend(defaults, options);
     //{name: "wmsj100", age: "20", ability: {eat:"more",write:"good"}, sex: "male"}
     ```


- 深拷贝模式--对于对象内部的数组、对象的属性和值也进行覆盖和合并；

  ```javascript
  //对象属性和值同上；
  $.extend(true,defaults, options);
  //{name: "wmsj100", age: "20", ability: {do:"more",eat:"more",write:"good"}, sex: "male"}
  ```

- `jQuery`插件开发模式--有一个系统默认值，有一个新创建的值，不改变系统默认值，输出值是俩者的深度合并值；

  ```javascript
  //对象属性和值同上；
  var settings = {};
  settings = $.extend(true, {}, defaults, options);
  console.log(settings);
  //{name: "wmsj100", age: "20", ability: {do:"more",eat:"more",write:"good"}, sex: "male"}
  ```

1. JQuery 的链式调用是什么？

   链式调用--通过对象上的方法，最后在`return this`,把对象再返回来，对象就可以继续调用方法了，这就是链式调用。

   链式调用的优点：

   - 让调用过程更加接近自然语言，使代码的读和写都变得更加简单；
   - 减少了不必要的代码量；

2. JQuery ajax 中缓存怎样控制?

   `ajax`在发送的数据请求成功后，会把请求的`URL`和请求的数据缓存在浏览器中，当下次如果请求的还是相同的`URL`,浏览器就会直接从本地服务器中提取数据，不会访问服务器，这样可以减少服务器的请求量，提高网页性能。

   `jQuery.ajax`的缓存机制只对`GET`和`HEAD`(不常见)有效，如果是GET请求，默认会缓存页面，可以通过修改传递方式为`POST`,或者设置属性`cache=false`，这样在提交请求的时候，浏览器会自动在`URL`后面添加时间戳，`http://www.erheizi.com/jirengu/task 26/test/01.php?val=wmsj&_=1460476123169`所以每次的`URL`是不同的，浏览器就不会访问缓存而直接访问服务器。

   > 我虽然使用了`get`请求方式，而且也设置了`cache=true`但是我每次提交的时候，`URL`都是一样的，浏览器访问的却是服务器，而不是本地缓存，访问状态都是`200`,而不是我期望的`304`，不知道为什么？[example](http://www.erheizi.com/jirengu/task 26/test/task 26.html)

3. jquery 中 data 函数的作用

   `.data()`--允许我们在DOM元素上附加任意类型的数据，避免了循环引用的内存泄漏风险。可以在一个元素上设置不同的值，并获取数据。

   如果传入的参数只有`key`,jQuery将在元素的属性中搜索，将驼峰式字符串转换为中横线字符串，然后在结果前面加上`data-`,例如`lastValue`转化为`data-last-value`;

   如果传入的参数是`key，value`形式，那么将给元素添加属性`key`,并且设置值为`value`;

   [example](http://www.erheizi.com/jirengu/task 26/task/task 26-wt6.html)

### 代码

1. 写出以下功能对应的 Jq 方法：

   1. 给元素 $node 添加 class `active`;

      ```javascript
      $(node).attr("class","active");
      $(node).addClass("active");
      ```

      给元素 $noed 删除 class `active`

      ```javascript
      //$(node).attr("class","");
      $(node).removeAttr("active");
      $(node).removeClass("active");
      ```

   2. 展示元素$node;

      ```javascript
      $(node).slideDown();
      $(node).fadeIn();
      ```

      隐藏元素$node

      ```javascript
      $(node).slideUp();
      $(node).fadeOut();
      ```

      切换状态

      ```
      $(node).toggle();
      $(node).slideToggle();
      $(node).fadeToggle();
      ```

   3. 获取元素$node 的 属性: id、src、title， 修改以上属性

      ```javascript
      $node.attr("id");
      $node.attr("id","temp");
      $node.attr("src");
      $node.attr("src","http");
      $node.attr("title");
      $node.attr("title","hello");
      ```

   4. 给$node 添加自定义属性`data-src`

      ```javascript
      $node.attr("data-src","aaa");
      $node.data("src","aaa");
      ```

   5. 在$ct 内部最开头添加元素$node

      ```javascript
      $ct.prepend(node);
      $node.prependTo(ct);
      $ct.children().first().before(node);
      $ct.children().eq(0).before(node); 
      ```

   6. 在$ct 内部最末尾添加元素$node

      ```
      $ct.append(node);
      $node.appendTo(ct);
      $ct.children().last().after(node);
      $ct.children().eq($ct.children().length-1).after(node);
      ```

   7. 删除$node

      ```
      $node.remove();
      ```

   8. 把$ct里内容清空

      ```
      $ct.empty();
      $ct.html("");
      $ct.text("");
      ```

   9. 在$ct 里设置 html`"<div class="btn"></div>"`

      ```
      $ct.html("<div class="btn"></div>");
      $ct.empty().append("<div class="btn"></div>");
      $ct.empty().prepend("<div class="btn"></div>");
      ```

   10. 获取、设置$node 的宽度、高度(分别不包括内边距、包括内边距、包括边框、包括外边距)

       ```
       $node.height();	
       //获取高度值
       $node.height(30)	
       //设置高度为10px，px可有可无
       $node.innerHeight();	
       //获取高度，包含padding值；
       $node.innerHeight(30)
       //设置高度为30px，包含padding值；
       $node.outerHeight();
       //获取高度，包含padding和border;
       $node.outerHeight(30);
       //设置高度为30px，包含padding和border；
       $node.outerHeight(true);
       //获取高度，包含padding、border、margin
       //外边距无法设置
       ```

   11. 获取窗口滚动条垂直滚动距离

       ```
       $node.scrollTop();
       ```

   12. 获取$node 到根节点水平、垂直偏移距离

       ```
       $node.offset()	//获取偏移距离
       $node.offset({top: 10, left: 20});
       //把node节点转换为`relative`，然后按照目标值重新进行定位。
       ```

   13. 修改$node 的样式，字体颜色设置红色，字体大小设置14px

       ```
       $node.css({"color": "red", "font-size": 14});
       ```

   14. 遍历节点，把每个节点里面的文本内容重复一遍

       ```
       $node.clone().text();
       ```

   15. 从$ct 里查找 class 为 `.item`的子元素

       ```
       $ct.find(".item")
       ```

   16. 获取$ct 里面的所有孩子

       ```
       $ct.children();
       ```

   17. 对于$node，向上找到 class 为’.ct’的父亲，在从该父亲找到’.panel’的孩子

       ```
       $node.parents(".ct").find(".panel");
       ```

   18. 获取选择元素的数量

       ```
       $node.length;
       ```

   19. 获取当前元素在兄弟中的排行

       ```
       $node.index();
       ```

2. 简单实现以下操作

   [task 26-2-1](http://www.erheizi.com/jirengu/task 26/task/task 26-2-1.html)

   [task 26-2-2](http://www.erheizi.com/jirengu/task 26/task/task 26-2-2.html)

   [task 26-2-3](http://www.erheizi.com/jirengu/task 26/task/task 26-2-3.html)

   [task 26-2-4](http://www.erheizi.com/jirengu/task 26/task/task 26-2-4.html)

   [task 26-5](http://www.erheizi.com/jirengu/task 26/task/task 26-2-5.html)

   [task 25-6](http://www.erheizi.com/jirengu/task 26/task/task 26-3.html)

3. [task 26-3](http://www.erheizi.com/jirengu/task 26/task/task 26-3.html)