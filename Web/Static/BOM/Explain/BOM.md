---
title: BOM
date: 2016-05-05
tags: [BOM]
categories: Dynamic
---

## 8.1  window 对象

BOM 的核心对象是 window ，它表示浏览器的一个实例。在浏览器中， window 对象有双重角色，它既是通过 JavaScript 访问浏览器窗口的一个接口，又是 ECMAScript 规定的 Global 对象。这意味着在网页中定义的任何一个对象、变量和函数，都以 window 作为其 Global 对象，因此有权访问parseInt() 等方法。

### 8.1.1 全局作用域

由于 window 对象同时扮演着 ECMAScript中 Global 对象的角色，因此所有在全局作用域中声明的变量、函数都会变成 window 对象的属性和方法。

抛开全局变量会成为 window 对象的属性不谈，定义全局变量与在 window 对象上直接定义属性还是有一点差别：全局变量不能通过 delete 操作符删除，而直接在 window 对象上的定义的属性可以。

```javascript
var age = 29;
window.color = "red";
//在 IE < 9 时抛出错误，在其他所有浏览器中都返回 false
delete window.age;
//在 IE < 9 时抛出错误，在其他所有浏览器中都返回 true
delete window.color; //returns true
alert(window.age); //29
alert(window.color); //undefined
```

刚才使用 var 语句添加的 window 属性有一个名为 [[Configurable]] 的特性，这个特性的值被设置为 false ，因此这样定义的属性不可以通过 delete 操作符删除。IE8及更早版本在遇到使用 delete删除 window 属性的语句时，不管该属性最初是如何创建的，都会抛出错误，以示警告。IE9 及更高版本不会抛出错误。

另外，还要记住一件事：尝试访问未声明的变量会抛出错误，但是通过查询 window 对象，可以知道某个可能未声明的变量是否存在。例如：

```javascript
//这里会抛出错误，因为 oldValue 未定义
var newValue = oldValue;
//这里不会抛出错误，因为这是一次属性查询
//newValue 的值是 undefined
var newValue = window.oldValue;
```

### 8.1.2 窗口关系及框架

### 8.1.3 窗口位置

只有火狐浏览器的位置查询是通过`screenX, screenY` ,其它浏览器是通过`screenLeft , screenTop` 来查看窗口距离屏幕边距的距离。下面的代码可以通用

```javascript
var leftPos = (typeof window.screenLeft == "number") ? screenLeft : screenX;
var topPos = (typeof window.screenTop == "number") ? screenTop : screenY;
```

这个例子运用二元操作符首先确定 screenLeft 和 screenTop 属性是否存在，如果是（在 IE、Safari、Opera 和 Chrome 中），则取得这两个属性的值。如果不存在（在 Firefox 中），则取得 screenX和 screenY 的值。

使用 moveTo()和 moveBy() 方法倒是有可能将窗口精确地移动到一个新位置。这两个方法都接收两个参数，其中moveTo() 接收的是新位置的 x 和 y 坐标值，而 moveBy() 接收的是在水平和垂直方向上移动的像素数。需要注意的是，这两个方法一般都会被浏览器禁用；

### 8.1.4 窗口大小

兼容性获取浏览器窗口大小；

```javascript
var pageWidth = window.innerWidth;
var pageHeight = window.innerHeight;
if (typeof pageWidth !== "number") {
	if (typeof document.compatMode === "CSS1compat") {
		pageWidth = document.documentElement.clientWidth;
		pageHeight = document.documentElement.clientHeight;
	} else {
		pageWidth = document.body.clientWidth;
		pageHeight = document.body.clientHeight;
	}
}
```

在以上代码中，我们首先将 window.innerWidth 和 window.innerHeight 的值分别赋给了
pageWidth 和 pageHeight 。然后检查 pageWidth 中保存的是不是一个数值；如果不是，则通过检查
document.compatMode （这个属性将在第 10 章全面讨论）来确定页面是否处于标准模式。如果是，则分别使用 document.documentElement.clientWidth 和 document.documentElement.clientHeight 的值。否则，就使用document.body.clientWidth 和 document.body.clientHeight 的值。

### 8.1.5 导航和打开窗口

因为现在浏览器一般都会默认屏蔽弹出窗口，所以可以通过一下代码来监测弹出窗口

```javascript
var a = window.open("http://www.baidu.com", "wmsj");
if (a == null) {
	alert("the window wad blocked!")
}
```

如果窗口被屏蔽，就弹出警告框。

### 8.1.6 间歇调用和超时调用

```javascript
//不建议传递字符串！
setTimeout("alert('Hello world!') ", 1000);
//推荐的调用方式
setTimeout(function() {
alert("Hello world!");
}, 1000);
```

虽然这两种调用方式都没有问题，但由于传递字符串可能导致性能损失，因此不建议以字符串作为第一个参数。

第二个参数是一个表示等待多长时间的毫秒数，但经过该时间后指定的代码不一定会执行。
JavaScript 是一个单线程序的解释器，因此一定时间内只能执行一段代码。为了控制要执行的代码，就有一个 JavaScript 任务队列。这些任务会按照将它们添加到队列的顺序执行。 setTimeout() 的第二个参数告诉 JavaScript 再过多长时间把当前任务添加到队列中。如果队列是空的，那么添加的代码会立即执行；如果队列不是空的，那么它就要等前面的代码执行完了以后再立即执行。

调用 setTimeout() 之后，该方法会返回一个数值 ID，表示超时调用。这个超时调用 ID 是计划执行代码的唯一标识符，可以通过它来取消超时调用。要取消尚未执行的超时调用计划，可以调用clearTimeout() 方法并将相应的超时调用 ID 作为参数传递给它，如下所示。

```javascript
//设置超时调用
var timeoutId = setTimeout(function() {
alert("Hello world!");
}, 1000);
//注意：把它取消
clearTimeout(timeoutId);
```

只要是在指定的时间尚未过去之前调用 clearTimeout() ，就可以完全取消超时调用。前面的代码在设置超时调用之后马上又调用了 clearTimeout() ，结果就跟什么也没有发生一样。

调用 setInterval() 方法同样也会返回一个间歇调用 ID，该 ID 可用于在将来某个时刻取消间歇调用。要取消尚未执行的间歇调用，可以使用 clearInterval() 方法并传入相应的间歇调用 ID。取消间歇调用的重要性要远远高于取消超时调用，因为在不加干涉的情况下，间歇调用将会一直执行到页面卸载。

```javascript
var num = 0;
var max = 10;
var intervalId = null;	//先重置变量，
function incrementNumber() {
  num++;
  //如果执行次数达到了 max 设定的值，则取消后续尚未执行的调用
  if (num == max) {
  	clearInterval(intervalId);
  	alert("Done");
  }
}
intervalId = setInterval(incrementNumber, 500);
```

使用`setTimeout` 函数来模拟`setInterval`效果

```javascript
var num = 0,
	max = 10,
	timeoutId = null;

function timeoutFunc() {
	num++;
	console.log(num);
	if (num < max) {
		timeoutId = setTimeout(timeoutFunc, 500);
	} else {
		clearTimeout(timeoutId);
		console.log("it's over");
		timeoutId = null;
	}
}
timeoutId = setTimeout(timeoutFunc, 500);
```

一般认为，使用超时调用来模拟间歇调用的是一种最佳模式。在开发环境下，很少使用真正的间歇调用，原因是后一个间歇调用可能会在前一个间歇调用结束之前启动。而像前面示例中那样使用超时调用，则完全可以避免这一点。所以，最好不要使用间歇调用。

### 8.1.7 系统对话框

浏览器通过 alert() 、 confirm() 和 prompt() 方法可以调用系统对话框向用户显示消息。系统对话框与在浏览器中显示的网页没有关系，也不包含 HTML。它们的外观由操作系统及（或）浏览器设置决定，而不是由 CSS 决定。此外，通过这几个方法打开的对话框都是同步和模态的。也就是说，显示这些对话框的时候代码会停止执行，而关掉这些对话框后代码又会恢复执行。

为了确定用户是单击了 OK 还是 Cancel，可以检查 confirm() 方法返回的布尔值： true 表示单击了 OK， false 表示单击了 Cancel 或单击了右上角的 X 按钮。确认对话框的典型用法如下。

```javascript
if (confirm("are you sure?")) {
	console.log("hello wmsj100");
} else {
	console.log("fuck!!!")
}
```

如果用户单击了 OK 按钮，则 prompt() 返回文本输入域的值；如果用户单击了 Cancel 或没有单击OK 而是通过其他方式关闭了对话框，则该方法返回 null 。下面是一个例子。

```javascript
var result = prompt("are you sure!", "yes");
if (result !== null) {
	console.log("wahahaha " + result);
} else {
	console.log(result + " Ao my gold !!!");
}
```

如果当前脚本在执行过程中会打开两个或多个对话框，那么从第二个对话框开始，每个对话框中都会显示一个复选框，以便用户阻止后续的对话框显示，除非用户刷新页面.

还有两个可以通过 JavaScript 打开的对话框，即“查找”和“打印”。这两个对话框都是异步显示的，能够将控制权立即交还给脚本。这两个对话框与用户通过浏览器菜单的“查找”和“打印”命令打开的对话框相同。而在 JavaScript 中则可以像下面这样通过 window 对象的 find() 和 print() 方法打开它们。

```javascript
//显示“打印”对话框
window.print();
//显示“查找”对话框
window.find();
```

## 8.2  location 对象

location 是最有用的 BOM对象之一，它提供了与当前窗口中加载的文档有关的信息，还提供了一些导航功能。事实上， location 对象是很特别的一个对象，因为它既是 window 对象的属性，也是document 对象的属性；换句话说， window.location 和 document.location 引用的是同一个对象。location 对象的用处不只表现在它保存着当前文档的信息，还表现在它将 URL 解析为独立的片段，让
开发人员可以通过不同的属性访问这些片段。

```javascript
window.location == document.location	//true
```

|  属 性 名   |                   例 子                    | 说 明                           |
| :------: | :--------------------------------------: | :---------------------------- |
|   hash   |                "#content"                | 返回URL中的hash（#号后跟零或多个字符），如果URL |
|   host   |            "www.wrox.com:80"             | 返回服务器名称和端口号（如果有）              |
| hostname |              "www.wrox.com"              | 返回不带端口号的服务器名称                 |
|   href   | "http://localhost/php/test/book/bom.html?a=1" | 返回当前加载页面的完整URL。而location对象的   |
| pathname |        "/php/test/book/bom.html"         | 返回URL中的目录和（或）文件名              |
|   port   |                  "8080"                  | 返回URL中指定的端口号。如果URL中不包含端口号，则   |
| protocol |                 "http:"                  | 返回页面使用的协议。通常是http:或https:     |
|  search  |             "?q=javascript"              | 返回URL的查询字符串。这个字符串以问号开头        |

### 8.2.1 查询字符串参数

使用 location 对象可以通过很多方式来改变浏览器的位置。首先，也是最常用的方式，就是使用
assign() 方法并为其传递一个 URL，如下所示。

```javascript
location.assign("http://www.wrox.com");
```

这样，就可以立即打开新 URL 并在浏览器的历史记录中生成一条记录。如果是将 location.href或 window.location 设置为一个 URL 值，也会以该值调用 assign() 方法。例如，下列两行代码与显式调用 assign() 方法的效果完全一样。

```javascript
window.location = "http://www.wrox.com";
location.href = "http://www.wrox.com";
```

在这些改变浏览器位置的方法中，最常用的是设置 location.href 属性。

另外，修改 location 对象的其他属性也可以改变当前加载的页面。下面的例子展示了通过将 hash 、search 、 hostname 、 pathname 和 port 属性设置为新值来改变 URL。

```javascript
//假设初始 URL 为 http://www.wrox.com/WileyCDA/
//将 URL 修改为"http://www.wrox.com/WileyCDA/#section1"
location.hash = "#section1";
//将 URL 修改为"http://www.wrox.com/WileyCDA/?q=javascript"
location.search = "?q=javascript";
//将 URL 修改为"http://www.yahoo.com/WileyCDA/"
location.hostname = "www.yahoo.com";
//将 URL 修改为"http://www.yahoo.com/mydir/"
location.pathname = "mydir";
//将 URL 修改为"http://www.yahoo.com:8080/WileyCDA/"
location.port = 8080;
```

每次修改 location 的属性（ hash 除外），页面都会以新 URL 重新加载。

当通过上述任何一种方式修改 URL 之后，浏览器的历史记录中就会生成一条新记录，因此用户通过单击“后退”按钮都会导航到前一个页面。要禁用这种行为，可以使用 replace() 方法。这个方法只接受一个参数，即要导航到的 URL；结果虽然会导致浏览器位置改变，但不会在历史记录中生成新记录。在调用 replace() 方法之后，用户不能回到前一个页面，

```javascript
setTimeout(function () {
location.replace("http://www.wrox.com/");
}, 1000);
```

如果将这个页面加载到浏览器中，浏览器就会在 1 秒钟后重新定向到 www.wrox.com。然后，“后退”按钮将处于禁用状态，如果不重新输入完整的 URL，则无法返回示例页面。

与位置有关的最后一个方法是 reload() ，作用是重新加载当前显示的页面。如果调用 reload()时不传递任何参数，页面就会以最有效的方式重新加载。也就是说，如果页面自上次请求以来并没有改变过，页面就会从浏览器缓存中重新加载。如果要强制从服务器重新加载，则需要像下面这样为该方法传递参数 true 。

```javascript
location.reload(); //重新加载（有可能从缓存中加载）
location.reload(true); //重新加载（从服务器重新加载）
```

位于 reload() 调用之后的代码可能会也可能不会执行，这要取决于网络延迟或系统资源等因素。为此，最好将 reload() 放在代码的最后一行。

## 8.3  navigator 对象

最早由 Netscape Navigator 2.0引入的 navigator 对象，现在已经成为识别客户端浏览器的事实标准。常用的属性如下：

```javascript
navigator.cookieEnabled	//表示cookie是否启用 true
navigator.javaEnabled()	//表示当前浏览器中是否启用了Java	 true
navigator.language	//浏览器的主语言 "zh-CN"
navigator.onLine	//表示浏览器是否连接到了因特网 false
navigator.platform	//"Win32"
navigator.plugins	//浏览器中安装的插件信息的数组
navigator.userAgent	//浏览器的用户代理字符串
```

### 8.3.1 检测插件

检测浏览器中是否安装了特定的插件是一种最常见的检测例程。

一般来说， name 属性中会包含检测插件必需的所有信息，但有时候也不完全如此。在检测插件时，需要像下面这样循环迭代每个插件并将插件的 name 与给定的名字进行比较。

```javascript
//检测插件（在 IE 中无效）
function hasPlugin(name){
name = name.toLowerCase();
for (var i=0; i < navigator.plugins.length; i++){
if (navigator. plugins [i].name.toLowerCase().indexOf(name) > -1){
return true;
}
}
return false;
}
//检测 Flash
alert(hasPlugin("Flash"));
//检测 QuickTime
alert(hasPlugin("QuickTime"));
```

## 8.5  history 对象

history 对象保存着用户上网的历史记录，从窗口被打开的那一刻算起。因为 history 是 window对象的属性，因此每个浏览器窗口、每个标签页乃至每个框架，都有自己的 history 对象与特定的window 对象关联。出于安全方面的考虑，开发人员无法得知用户浏览过的 URL。不过，借由用户访问过的页面列表，同样可以在不知道实际 URL 的情况下实现后退和前进。

```javascript
//后退一页
history.go(-1);
//前进一页
history.go(1);
//前进两页
history.go(2);
```

## 8.6 小结

浏览器对象模型（BOM）以 window 对象为依托，表示浏览器窗口以及页面可见区域。同时， window对象还是 ECMAScript 中的 Global 对象，因而所有全局变量和函数都是它的属性，且所有原生的构造函数及其他函数也都存在于它的命名空间下。本章讨论了下列 BOM 的组成部分。
  在使用框架时，每个框架都有自己的 window 对象以及所有原生构造函数及其他函数的副本。每个框架都保存在 frames 集合中，可以通过位置或通过名称来访问。
  有一些窗口指针，可以用来引用其他框架，包括父框架。
 top 对象始终指向最外围的框架，也就是整个浏览器窗口。
 parent 对象表示包含当前框架的框架，而 self 对象则回指 window 。
  使用 location 对象可以通过编程方式来访问浏览器的导航系统。设置相应的属性，可以逐段或整体性地修改浏览器的 URL。
  调用 replace() 方法可以导航到一个新 URL，同时该 URL 会替换浏览器历史记录中当前显示的页面。
 navigator 对象提供了与浏览器有关的信息。到底提供哪些信息，很大程度上取决于用户的浏览器；不过，也有一些公共的属性（如 userAgent ）存在于所有浏览器中。
BOM 中还有两个对象： screen 和 history ，但它们的功能有限。 screen 对象中保存着与客户端显示器有关的信息，这些信息一般只用于站点分析。 history 对象为访问浏览器的历史记录开了一个小缝隙，开发人员可以据此判断历史记录的数量，也可以在历史记录中向后或向前导航到任意页面

