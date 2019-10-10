---
title: addEventListener的event事件类型
date: 2016-4-2 18:34:30
tags: [DOM,事件,函数]
categories: Dynamic
---

addEventListener的事件类型不只是`click`,html事件中的enent在DOM2中都可以使用，只需要把前面的`on`去掉就行。
<!-- more -->
| 属性                                       | 此事件发生在何时...        |
| ---------------------------------------- | ------------------ |
| [onabort](http://www.w3school.com.cn/jsref/event_onabort.asp) | 图像的加载被中断。          |
| [onblur](http://www.w3school.com.cn/jsref/event_onblur.asp) | 元素失去焦点。            |
| [onchange](http://www.w3school.com.cn/jsref/event_onchange.asp) | 域的内容被改变。           |
| [onclick](http://www.w3school.com.cn/jsref/event_onclick.asp) | 当用户点击某个对象时调用的事件句柄。 |
| [ondblclick](http://www.w3school.com.cn/jsref/event_ondblclick.asp) | 当用户双击某个对象时调用的事件句柄。 |
| [onerror](http://www.w3school.com.cn/jsref/event_onerror.asp) | 在加载文档或图像时发生错误。     |
| [onfocus](http://www.w3school.com.cn/jsref/event_onfocus.asp) | 元素获得焦点。            |
| [onkeydown](http://www.w3school.com.cn/jsref/event_onkeydown.asp) | 某个键盘按键被按下。         |
| [onkeypress](http://www.w3school.com.cn/jsref/event_onkeypress.asp) | 某个键盘按键被按下并松开。      |
| [onkeyup](http://www.w3school.com.cn/jsref/event_onkeyup.asp) | 某个键盘按键被松开。         |
| [onload](http://www.w3school.com.cn/jsref/event_onload.asp) | 一张页面或一幅图像完成加载。     |
| [onmousedown](http://www.w3school.com.cn/jsref/event_onmousedown.asp) | 鼠标按钮被按下。           |
| [onmousemove](http://www.w3school.com.cn/jsref/event_onmousemove.asp) | 鼠标被移动。             |
| [onmouseout](http://www.w3school.com.cn/jsref/event_onmouseout.asp) | 鼠标从某元素移开。          |
| [onmouseover](http://www.w3school.com.cn/jsref/event_onmouseover.asp) | 鼠标移到某元素之上。         |
| [onmouseup](http://www.w3school.com.cn/jsref/event_onmouseup.asp) | 鼠标按键被松开。           |
| [onreset](http://www.w3school.com.cn/jsref/event_onreset.asp) | 重置按钮被点击。           |
| [onresize](http://www.w3school.com.cn/jsref/event_onresize.asp) | 窗口或框架被重新调整大小。      |
| [onselect](http://www.w3school.com.cn/jsref/event_onselect.asp) | 文本被选中。             |
| [onsubmit](http://www.w3school.com.cn/jsref/event_onsubmit.asp) | 确认按钮被点击。           |
| [onunload](http://www.w3school.com.cn/jsref/event_onunload.asp) | 用户退出页面。            |

```html
<div class="box">asdf</div>
    <img src="http://wmsj100.github.io/webFile/img/ICON/03.jpg" alt="">
```

```javascript
var img=document.querySelector("img");
    	var box=document.querySelector(".box");
    	box.addEventListener("mouseover",function(){
    		img.style.opacity=0.3;
    	})
    	box.addEventListener("mouseout",function(){
    		img.style.opacity=1;
    	})
```

![](/file/img/tool/April/0402/06.gif)