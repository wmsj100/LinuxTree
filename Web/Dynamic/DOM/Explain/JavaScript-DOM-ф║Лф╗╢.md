---
title: JavaScript-DOM-事件
date: 2016-3-31 21:04:38
tags: [JavaScript,DOM]
categories: Dynamic
---

#### preventDefault -阻止默认事件（跳转）

把a链接设置为按钮的时候，因为a链接默认的属性，页面会进行跳转，即便链接地址为`#`还是会调到页面顶部，所以此时就需要取消a链接的默认事情属性。
<!-- more -->

```html
<a href="http://www.baidu.com" id="btn">点我</a>
<script>
    var btn = document.querySelector("#btn");
    btn.addEventListener("click", function(e) {
    	console.log("wmsj");
    	console.log(e);
    	e.preventDefault();
    })
</script>
```

通过给事件`e`添加属性`preventDefault()`这样点击a链接页面就不会进行跳转啦。

#### Propagation -阻止冒泡传递

```html
<div id="wrap">
	<a href="http://www.baidu.com" id="btn">点我</a>
</div>
<script>
    var btn = document.querySelector("#btn");
    btn.addEventListener("click", function(e) {
    	console.log("wmsj");
    	console.log(e);
    	e.preventDefault();
    	e.stopPropagation();
    });
    document.querySelector('#wrap').addEventListener("click",function(e){
    	console.log("hello world");
    })
</script>
```

默认情况下，事件会冒泡到div上面，但是因为添加了stopPropagation事件，即阻止了事件的传递，所以div上的事件是不会被触发的。

```
console.log(this.innerText)
//获取当前点击对象的文本内容
console.log(e.target)
//获取e的
```

#### onclick获取事件过程

```javascript
<input type="button" value="点击" id="btn">
  ---
var btn=document.getElementById("btn"); 
    btn.onclick=function(){
    	var e=window.event; 
    	console.log(e);
    	console.log("hello wmsj")
    }
//通过window.event来获得事件
```

#### 事件代理

```html
<ul id="wrap">
	<li><span class="d">item1</span></li>
	<li><span class="d">item2</span></li>
	<li><span class="d">item3</span></li>
</ul>
<button class="btn">添加</butt</button>
```

```javascript
var wrap=document.querySelector("#wrap");
    for(var i=0;i<wrap.children.length;i++){
    	var list=document.querySelectorAll(".d")[i];
    	list.addEventListener("click",function(){
    	console.log(this.innerText);
    },false);
    };
    var btn=document.querySelector(".btn");
    btn.addEventListener("click",function(){
    	var span=document.createElement("span");
    	span.setAttribute("class","d");
    	span.appendChild(document.createTextNode("item"));
    	var list=document.createElement("li");
    	list.appendChild(span);
    	wrap.appendChild(list);
    	list.addEventListener("click",function(){
    		console.log(this.innerText);
    	},false)
    },false)
```

如果把事件绑定到子元素上面，那么每添加一个事件就需要重复的申明，如果一个事件上面绑定的函数特别多，这样的方式就不现实了，无法满足需求了。

#### 把事件绑定到父元素上面

>  target 事件属性可返回事件的目标节点（触发该事件的节点），如生成事件的元素、文档或窗口。

```javascript
<button class="btn">添加</butt</button>
    <script>
    var wrap=document.querySelector("#wrap");
    wrap.addEventListener("click",function(e){
    	console.log(e.target,e.target.innerHTML);
    },false);
    var btn=document.querySelector(".btn");
    btn.addEventListener("click",function(){
    	var span=document.createElement("span");
    	span.setAttribute("class","d");
    	span.innerHTML="item";
    	var list=document.createElement("li");
    	list.appendChild(span);
    	wrap.appendChild(list);
    })
```

![](/file/img/tool/April/0401/01.gif)

事件监听——当点击目标的时候，目标没有绑定事件，就向上级元素（父元素）查找。因为不管点击任何元素，都会跑到父元素了。

---

如果给ul添加一个链接，但是点击链接的时候，再控制台输出——“this is a link”



像这个需求，如果还是按照上面的方法做的话，因为它没有对子元素进行区分，所以所有的元素都会弹出一样的内容，效果如下：

![](/file/img/tool/April/0401/02.gif)

所以这就需要在父元素上对接收到的事件进行区分了。

通过对子元素的class\或者id区分,并且使用`preventDefault`禁用a的跳转；

父元素绑定的函数如下，子元素和上面的一样。

```javascript
var wrap=document.querySelector("#wrap");
    wrap.addEventListener("click",function(e){
    	if(e.target.className==="d"){
    		console.log(e.target,e.target.innerHTML);
    	}
    	if(e.target.className==="link"){
    		console.log("this is a link");
    	}
    },false);
```

![](/file/img/tool/April/0401/02.gif)

记住，读取`class`时候，需要使用`className`.