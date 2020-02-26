---
title: JS选择器
date: 2016-4-3 00:03:51
tags: [JavaScript,选择器,事件,DOM]
categories: Dynamic
---
### 问答
阻止冒泡、阻止捕获、阻止事件

1. dom对象的`innerText`和`innerHTML`有什么区别？

   - innertext——获取的是标签内部的文本内容
   - innerHTML——获取的是标签内部的所有内容
     <!-- more -->
     ```html
     <a href="#"><span>hello world</span></a>
     ```

   ```javascript
   console.log(document.querySelector("a").innerHTML);
   //<span>hello world</span>
   console.log(document.querySelector("a").innerText);
   //hello world
   ```

2. `elem.children`和`elem.childNodes`的区别？

   - elem.children——获取的是html标签节点
   - elem.childNodes——获取的是元素内部所有的内容，包括换行和不在标签内部的文本

   ```html
   <a href="#">
       "hello world"
       <span>hello world</span>

       <span>wmsj</span>

   </a>
   ```

   ```javascript
   var a=document.querySelector("a");
   console.log(a.children);
   //[span, span]
   //只获取了内部的html标签——2个span
   console.log(a.childNodes);
   //[text, span, text, span, text]
   //获取了内部的所有标签，包括换行和文本
   //换行也被标记为了文本[text];
   ```

3. 查询元素有几种常见的方法？

   1. `document.getElementById("id")`——查找`id`属性标签
   2. `document.getElementsByClassName("class")——查找`class`属性标签，这样查找到的是一个数组，需要通过下标来查找具体是那个标签。
   3. `document.getElementsByTagName("tag")`——查找标签属性，和`class`类似，这样查找到的也是一个数组。
   4. `document.querySelector("name")`——查找`name`属性的标签，其中`name`可以是`id` ,`className`, `tagName`。如果查找的内容有多个，那么它只找寻到第一个。
   5. `document.querySelectorAll("name")`——查找`name`属性的标签，它获取的是一个数组，其中`name`可以是`id`, `className` ,`tagName` .
   6. 通过上面查找获得数组之后开可以继续进行精确查找：
      - `innerHTML`——获取标签内部所有的内容，包括文本和换行，返回字符串；
      - `innerText`——只获取标签内部所有的文本内容，返回字符串；
      - `firstChild`——获取标签内部第一个元素，可以是文本或者换行；
      - `lastChild`——获取标签内部最后一个元素，可以是文本或者换行；
      - `childNodes[n]`——获取标签内部第`n`个元素内容，包括文本和换行；
      - `children`——获取标签内部的`html`标签元素；
      - `[n]`——直接在获取的数组后面输入元素的排序也可以；

4. 如何创建一个元素？如何给元素设置属性？

   1. `document.createElement`——用来创建元素，
      - 使用`appendChild`或者`insertBefore`来选择在父元素的那个位置插入元素，
      - 使用`document.createTextNode`来为创建的元素生成文本内容；
      - 使用`innerHTML`来为元素创建标签和内容，这样会覆盖元素之前的内容
      - 使用`innerText`为元素添加文本，同样这样的设置会重置元素的文本；
   2. `document.createAttribute`——用来创建元素属性，
      - 使用`nodeValue`来为创建的属性赋值；
      - 使用`setAttributeNode`来把创建的属性添加到节点上面；
   3. `node.setAttribute("className","value")`——直接给节点赋值，这样比较方便，建议这样的操作，
   4. `node.getAttribute("name")`——可以查看元素属性名`name`的值。

5. 元素的添加、删除？

   1. 元素的添加：

      - `parentNode . appendChild ( childNode )`——在父元素的最后添加子元素

      > 如果添加的子元素`childNode`已经存在于父元素`parentNode`中，那么就会先把之前的子节点删除，然后重新在父元素的最后添加子元素，在重新给父元素内容排序时候可以这样使用。

      - `parentNode.insertBefore (newChild , oldChild )`——在父元素的`oldChild`前面添加`newChild` ，也可不把`oldChild`替换为`firstChild`/`lastChild`

   2. 元素的删除：

      - `parentNode . removeChild ( childNode )`——从父元素中删除子元素
      - `parentNode . replaceChild (newNode , oldNode )`——把父元素中的`oldNode`替换为`newNode`;这样算是变相的删除吧。

6. DOM0 事件和DOM2级在事件监听使用方式上有什么区别？

   1. DOM0事件是直接把事件绑定在节点上面，而且一个节点只能绑定一个事件，如果遇到多事件的场景就无能为力了。

      ```javascript
      var btn = document.querySelector (" .btn ");
      btn.onclick = function(){ console.log ( " hello world " ) }
      //"hello world"
      ```

   2. DOM2事件是通过添加事件监听来把事件绑定到节点上面，而且理论上可以无限制的给节点绑定事件。而且还可以控制事件执行的时间是在事件捕获阶段还是在事件冒泡阶段。

      ```html
      <p>
        <button class="btn">click</button>
      </p>
      ```

      - 事件在冒泡阶段执行(父元素在最后执行)

      ```javascript
      var wrap = document.querySelector("p");
      wrap.addEventListener("click", function() {
      console.log("this is parent....")
      }, false);
      var btn = document.querySelector(".btn");
      btn.addEventListener("click", function() {
      console.log("child.....this is");
      }, false);
      btn.addEventListener("click", function() {
      console.log("wa, come here......");
      }, false);
      //child.....this is
      //wa, come here......
      //this is parent....
      ```

      - 事件在捕获阶段执行，(父元素在最开始执行)

      ```javascript
      var wrap = document.querySelector("p");
      wrap.addEventListener("click", function() {
      console.log("this is parent....")
      }, true);
      var btn = document.querySelector(".btn");
      btn.addEventListener("click", function() {
      console.log("child.....this is");
      }, false);
      btn.addEventListener("click", function() {
      console.log("wa, come here......");
      }, false);
      //this is parent....
      //child.....this is
      //wa, come here......
      ```

7. `attachEvent`与`addEventListener`的区别？

   1. `attachEvent`——这是IE特有的事件，在IE9之前的版本只支持这个事件，IE9及以后的版本同时支持俩个事件。
      1. 它针对的事件动作前面需要添加--`on`;
      2. 它绑定的函数只有俩个参数，`node.attachEvent ("onclick" , function(){})`;
      3. 如果绑定多个事件，事件执行的顺序是不确定的，
      4. 它绑定的函数内部的this指代的是全局，不是正则执行的节点范围，可以通过`window.event`把this限制在正在执行的函数内部。
      5. 它不能控制事件的执行事件，只能再冒泡阶段执行；
   2. `addEventListener`——这是现代浏览器支持的事件模式，是推荐标准
      1. 它执行事件的当作前面不需要添加--`on`;
      2. 它绑定的函数又3个参数，`node.addEventListener ( "click" , function(){},boolean);`
      3. 如果绑定多个事件，`boolean`值为`true`的优先执行，并且是安装位置的先后顺序执行，`boolean`值为`false`的事件后执行，执行时候也是按照事件的写入顺序执行。
      4. 它绑定的函数内部的this指代的就是绑定函数的节点内容，可以通过`console.log(this)`来查看节点，或者`console.log ( this.innerText )`来获取节点的文本。
      5. 通过控制`boolean`来控制事件的执行时间，当为`boolean=true`时，事件在捕获阶段执行，当`boolean=false`事件在冒泡阶段执行。

8. 解释IE事件冒泡和DOM2事件传播机制？

   1. IE事件冒泡——以`onclick`事件为例，当用户触发点击事件时，开始进入事件捕获阶段，IE不支持在捕获阶段执行事件，然后事件找到目标节点开始进入冒泡阶段。事件先从子节点开始执行，然后上传到父节点，如果父节点也绑定了事件，那么再执行父节点的事件，以此一级一级往上传递事件。
   2. DOM2事件——以`click`事件为例，当用户触发点击事件时，事件开始捕获，从祖先节点一级一级下探，直到找到目标节点，如果在这个阶段父节点设置了事件，并且类型时捕获执行事件，那么父节点就会先执行，然后到的目标节点，触发目标节点的事件，开始进入冒泡阶段，然后事件再一级一级向上扩展，依次触发冒泡事件。

9. 如何阻止事件冒泡？ 如何阻止默认事件？

   1. `preventDefault( )`事件用于阻止默认事件的执行，比如阻止a链接的跳转：

      ```javascript
      <p>
        <a href="http://www.baidu.com">链接</a>
      </p>
      ```

      ```javascript
      var wrap = document.querySelector("p");
      wrap.addEventListener("click", function() {
      console.log("this is parent....")
      // console.log(this)
      }, false);
      var link=document.querySelector("a");
      link.addEventListener("click",function(e){
      console.log("not a link...");
      e.preventDefault();
      },false);
      //
      ```

      ![](http://wmsj100.github.io/webFile/img/0402/02.gif)

   2. `stopPropagation()`事件用于阻止事件的冒泡，父节点的事件就不会被执行：

      ```javascript
      var wrap = document.querySelector("p");
      wrap.addEventListener("click", function() {
      console.log("this is parent....")
      // console.log(this)
      }, false);
      var link=document.querySelector("a");
      link.addEventListener("click",function(e){
      console.log("not a link...");
      e.preventDefault();
      e.stopPropagation();
      },false);
      ```

      ![](http://wmsj100.github.io/webFile/img/0402/03.gif)


---

### 代码
[task 22-1](http://book.jirengu.com/jirengu-inc/jrg-tehui2/homework/%E7%8E%8B%E6%B5%A9/task22/task 22-1.html)
[task 22-2](http://book.jirengu.com/jirengu-inc/jrg-tehui2/homework/%E7%8E%8B%E6%B5%A9/task22/task 22-2.html)
[task 22-3](http://book.jirengu.com/jirengu-inc/jrg-tehui2/homework/%E7%8E%8B%E6%B5%A9/task22/task 22-3.html)
[task 22-4](http://book.jirengu.com/jirengu-inc/jrg-tehui2/homework/%E7%8E%8B%E6%B5%A9/task22/task 22-4.html)
[task 22-5](http://book.jirengu.com/jirengu-inc/jrg-tehui2/homework/%E7%8E%8B%E6%B5%A9/task22/task 22-5.html)
