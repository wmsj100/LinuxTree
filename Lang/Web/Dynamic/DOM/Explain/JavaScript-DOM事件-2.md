---
title: JavaScript-DOM事件-2
date: 2016-3-31 17:40:32
tags: [JavaScript,DOM]
categories: Dynamic
---

#### 内置事件

- 事件的绑定方式和script的写入方式是一样的，可以写在标签上面，head里面，js脚本里面，但是特别不建议写在标签里面，因为修改太不方便了，
  <!-- more -->
  ```javascript
  <input type="button" value="button" onclick="alert('hello')">
  //点击button，就会弹出窗口
  ```


- 而且一般js脚本是放在页面底部的，如果js脚本还没有加载，然后去点击按钮，肯定会报错的。

---

#### 绑定事件监听函数

选择元素的时候建议使用querySelector，而不是使用class，因为class选中的是一个数组，使用class的时候必须用中括号指定

```html
<input type="button" value="button" class="click">
<script>
    var btn=document.getElementsByClassName("click");
    	btn.onclick=function(){
    		console.log("click me ....")
    	}
    </script>
```

如果不在class后面指定数组下标的话，点击按钮是没有反应的，

```html
<input type="button" value="button" class="click">
<script>
var btn=document.getElementsByClassName("click")[0];
    	btn.onclick=function(){
    		console.log("click me ....")
    	}
</script>	//"click me ..."
```

如果使用querySelector的话，就省去了很多麻烦，而且代码会短一些。 

```html
<input type="button" value="button" class="click">
<script>
	var btn=document.querySelector(".click");
    	btn.onclick=function(){
    		console.log("click me ....")
    	}
</script>	//"click me ..."
```

如果再监听函数中添加——`this`,指的是绑定函数的标签内容。

在上面函数console.log("click me...")上面添加下面的函数

```javascript
console.log(this);
//<input type="button" value="button" class="click">
//就会输出函数的绑定标签
console.log(this.innerText);
//click me ....
//就会输出函数绑定标签的文本内容。

```

#### 事件冒泡流畅

```html
	<div id="tmp">
		<input type="button" value="button" class="click">
        ----------------------------------------
	</div>
    <script>
    	var btn=document.querySelector(".click");
    	btn.onclick=function(){
    		console.log(this);
    		// console.log(this.innerText);
    		console.log("click me ....");
    	}
    	var tmp=document.querySelector("#tmp");
    	tmp.onclick=function(){
    		console.log(this);
    		console.log("tmp click...");
    	}
    </script>
//<input type="button" value="button" class="click">
//click me ....
//<div id="tmp">…</div>
//tmp click...
```

从上面的流程中可以看到事件是先反馈到出发点`button`上面，然后又继续反馈到包裹的`div`上面。

因为事件也是一个参数，所以通过给函数传递一个参数，来查看事件，

```javascript
btn.onclick=function(e){console.log(e);}
//MouseEvent {isTrusted: true, screenX: 41, screenY: 102, clientX: 41, clientY: 17…}
```

#### addEventListener-事件冒泡

这是DOM2的操作方法，它的好处是可以对于一个标签同时绑定多个监听函数，而如果是上面的方法，就只能绑定一个函数，因为后面的会覆盖前面的。

```javascript
document.querySelector("#tmp").addEventListener("click",function(){
    		console.log(this);
    		console.log("tmp click...");
    	});
```

#### addEventListener-事件捕获

```javascript
<div id="tmp">
		<input type="button" value="button" class="click">
	</div>
    <script>
    	document.querySelector(".click").addEventListener("click",function(){
    		// console.log(this.innerText);
    		console.log("click me ....");
    	},true);
    	document.querySelector("#tmp").addEventListener("click",function(){
    		console.log("tmp click...one");
    	},true);
    	document.querySelector("#tmp").addEventListener("click",function(){
    		console.log("hello wmsj100--two");
    	},true);
    	document.querySelector("#tmp").addEventListener("click",function(){
    		console.log("this is the third!");
    	},true);
    </script>
```

> addEventListener默认的方式`false`是事件冒泡，我们可以修改为`true`把模式修改为事件捕获，即
>
> `addEventListener("click" , function(){} , true)`
>
> 所以上面的时间传递顺序就是从最外面的div开始接收事件，因为addEventlistener可以同时绑定多个事件，因为我绑定了3个事件，所以那3个事件顺序发生，然后再传递到内部的button事件。

- 事件捕获就是从浏览器捕获对象的时候开始监听事件，而事件冒泡是指事件捕获的时候不做出反应，等全部捕获完成之后才去监听事件，然后就是从里往外的顺序。


- 通过addEventListener可以自己控制事件的发生是再捕获阶段还是再冒泡阶段。

> 判断不需要针对浏览器，比如说if(IE),而是针对某个方法是否存在，针对方法去选择。