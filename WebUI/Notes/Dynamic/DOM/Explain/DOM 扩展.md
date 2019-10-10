---
title: DOM 扩展
date: 2016-05-07
tags: [DOM,Book]
categories: Dynamic
---

## 11.1 选择符 API

众多 JavaScript 库中最常用的一项功能，就是根据 CSS 选择符选择与某个模式匹配的 DOM 元素。实际上，jQuery（www.jquery.com）的核心就是通过 CSS 选择符查询 DOM 文档取得元素的引用，从而抛开了 getElementById() 和 getElementsByTagName() 。

Selectors API Level 1的核心是两个方法： querySelector() 和 querySelectorAll() 。在兼容的浏览器中，可以通过 Document 及 Element 类型的实例调用它们。

### 11.1.1  querySelector() 方法

querySelector() 方法接收一个 CSS 选择符，返回与该模式匹配的第一个元素，如果没有找到匹配的元素，返回 null 。

通过 Document 类型调用 querySelector() 方法时，会在文档元素的范围内查找匹配的元素。而通过 Element 类型调用 querySelector() 方法时，只会在该元素后代元素的范围内查找匹配的元素。

```javascript
<p>
	<span class="p">hello</span>
</p>
<div class="p">world</div>
---
var a = document.querySelector("p");
document.querySelector(".p")	//<span class="p">
a.querySelector(".p")	//<span class="p">
a.querySelector(".p") === document.querySelector(".p")	//true
```

CSS 选择符可以简单也可以复杂，视情况而定。如果传入了不被支持的选择符， querySelector()会抛出错误。

### 11.1.2  querySelectorAll() 方法

querySelectorAll() 方法接收的参数与 querySelector() 方法一样，都是一个 CSS 选择符，但返回的是所有匹配的元素而不仅仅是一个元素。这个方法返回的是一个 NodeList 的实例。

具体来说，返回的值实际上是带有所有属性和方法的 NodeList ，而其底层实现则类似于一组元素的快照，而非不断对文档进行搜索的动态查询。这样实现可以避免使用 NodeList 对象通常会引起的大多数性能问题。

只要传给 querySelectorAll() 方法的 CSS 选择符有效，该方法都会返回一个 NodeList 对象，而不管找到多少匹配的元素。如果没有找到匹配的元素， NodeList 就是空的。

与 querySelector() 类似，能够调用 querySelectorAll() 方法的类型包括 Document 、DocumentFragment 和 Element 。

```javascript
//取得某<div>中的所有<em>元素（类似于 getElementsByTagName("em")）
var ems = document.getElementById("myDiv").querySelectorAll("em");
//取得类为"selected"的所有元素
var selecteds = document.querySelectorAll(".selected");
//取得所有<p>元素中的所有<strong>元素
var strongs = document.querySelectorAll("p strong");
```

### 11.1.3  matchesSelector() 方法

## 11.2 元素遍历

对于元素间的空格，IE9及之前版本不会返回文本节点，而其他所有浏览器都会返回文本节点。这样，就导致了在使用 childNodes 和 firstChild 等属性时的行为不一致。为了弥补这一差异，而同时又保持 DOM规范不变，Element Traversal规范（www.w3.org/TR/ElementTraversal/）新定义了一组属性。

Element Traversal API 为 DOM 元素添加了以下 5 个属性。
 childElementCount ：返回子元素（不包括文本节点和注释）的个数。
 firstElementChild ：指向第一个子元素； firstChild 的元素版。
 lastElementChild ：指向最后一个子元素； lastChild 的元素版。
 previousElementSibling ：指向前一个同辈元素； previousSibling 的元素版。
 nextElementSibling ：指向后一个同辈元素； nextSibling 的元素版。

支持的浏览器为 DOM 元素添加了这些属性，利用这些元素不必担心空白文本节点，从而可以更方便地查找 DOM元素了。

## 11.3 HTML5

 HTML5 规范则围绕如何使用新增标记定义了大量 JavaScript API。其中一些 API 与 DOM 重叠，定义了浏览器应该支持的 DOM扩展。

### 11.3.1 与类相关的扩充

#### 1.  getElementsByClassName() 方法

HTML5 添加的 getElementsByClassName() 方法是最受人欢迎的一个方法，可以通过 document对象及所有 HTML 元素调用该方法。这个方法最早出现在 JavaScript 库中，是通过既有的 DOM 功能实现的，而原生的实现具有极大的性能优势。

HTML5 新增了一种操作类名的方式，可以让操作更简单也更安全，那就是为所有元素添加classList 属性。这个 classList 属性是新集合类型 DOMTokenList 的实例。与其他 DOM 集合类似，DOMTokenList 有一个表示自己包含多少元素的 length 属性，而要取得每个元素可以使用 item() 方法，也可以使用方括号语法。此外，这个新类型还定义如下方法。

 add(value) ：将给定的字符串值添加到列表中。如果值已经存在，就不添加了。
 contains(value) ：表示列表中是否存在给定的值，如果存在则返回 true ，否则返回 false 。
 remove(value) ：从列表中删除给定的字符串。
 toggle(value) ：如果列表中已经存在给定的值，删除它；如果列表中没有给定的值，添加它。

这样，前面那么多行代码用下面这一行代码就可以代替了：
div.classList.remove("user");
以上代码能够确保其他类名不受此次修改的影响。其他方法也能极大地减少类似基本操作的复杂性，如下面的例子所示。

```javascript
//删除"disabled"类
div.classList.remove("disabled");
//添加"current"类
div.classList.add("current");
//切换"user"类
div.classList.toggle("user");
//确定元素中是否包含既定的类名
if (div.classList.contains("bd") && !div.classList.contains("disabled")){
//执行操作
)
//迭代类名
for (var i=0, len=div.classList.length; i < len; i++){
doSomething(div.classList[i]);
}
```
有了 classList 属性，除非你需要全部删除所有类名，或者完全重写元素的 class 属性，否则也就用不到 className 属性了。支持 classList 属性的浏览器有 Firefox 3.6+和 Chrome。

### 11.3.2 焦点管理

HTML5 也添加了辅助管理 DOM 焦点的功能。首先就是 document.activeElement 属性，这个属性始终会引用 DOM 中当前获得了焦点的元素。元素获得焦点的方式有页面加载、用户输入（通常是通过按 Tab 键）和在代码中调用 focus() 方法。来看几个例子。

```javascript
var button = document.getElementById("myButton");
button.focus();
alert(document.activeElement === button); //true
```

默认情况下，文档刚刚加载完成时， document.activeElement 中保存的是 document.body 元素的引用。文档加载期间， document.activeElement 的值为 null 。

另外就是新增了 document.hasFocus() 方法，这个方法用于确定文档是否获得了焦点。

### 11.3.3  HTMLDocument 的变化

#### 1.  readyState 属性

 Document 的 readyState 属性有两个可能的值：
 loading ，正在加载文档；
 complete ，已经加载完文档。

使用 document.readyState 的最恰当方式，就是通过它来实现一个指示文档已经加载完成的指示器。在这个属性得到广泛支持之前，要实现这样一个指示器，必须借助 onload 事件处理程序设置一个标签，表明文档已经加载完毕。 document.readyState 属性的基本用法如下。

```javascript
if (document.readyState == "complete"){
//执行操作
}
```

#### 2. 兼容模式

自从 IE6 开始区分渲染页面的模式是标准的还是混杂的，检测页面的兼容模式就成为浏览器的必要功能。IE 为此给 document 添加了一个名为 compatMode 的属性，这个属性就是为了告诉开发人员浏览器采用了哪种渲染模式。就像下面例子中所展示的那样，在标准模式下， document.compatMode 的值等于 "CSS1Compat" ，而在混杂模式下， document.compatMode 的值等于 "BackCompat" 。

#### 3.  head 属性

作为对 document.body 引用文档的 <body> 元素的补充，HTML5 新增了 document.head 属性，引用文档的 <head> 元素。要引用文档的 <head> 元素，可以结合使用这个属性和另一种后备方法。

```javascript
var head = document.head || document.getElementsByTagName("head")[0];
```

### 11.3.4 字符集属性

HTML5 新增了几个与文档字符集有关的属性。其中， charset 属性表示文档中实际使用的字符集，也可以用来指定新字符集。默认情况下，这个属性的值为 "UTF-16" ，但可以通过 <meta> 元素、响应头部或直接设置 charset 属性修改这个值。

### 11.3.5 自定义数据属性

HTML5规定可以为元素添加非标准的属性，但要添加前缀 data- ，目的是为元素提供与渲染无关的信息，或者提供语义信息。这些属性可以任意添加、随便命名，只要以 data- 开头即可。来看一个例子。

```
<div id="myDiv" data-appId="12345" data-myname="Nicholas"></div>
```

添加了自定义属性之后，可以通过元素的 dataset 属性来访问自定义属性的值。 dataset 属性的值是 DOMStringMap 的一个实例，也就是一个名值对儿的映射。在这个映射中，每个 data-name 形式的属性都会有一个对应的属性，只不过属性名没有 data- 前缀（比如，自定义属性是 data-myname ，那映射中对应的属性就是 myname ）。还是看一个例子吧。

```javascript
<p class="para" data-name="wmsj" data-id="p1">这是一个网页</p>	
---
var a = document.querySelector("p");
a.dataset	//DOMStringMap { id: "p1", name: "wmsj" }
a.dataset.id	//"p1";
a.dataset.id="hello"	//"hello"
a.dataset	//DOMStringMap { id: "hello", name: "wmsj" }
```

如果需要给元素添加一些不可见的数据以便进行其他处理，那就要用到自定义数据属性。在跟踪链接或混搭应用中，通过自定义数据属性能方便地知道点击来自页面中的哪个部分。

### 11.3.6 插入标记

虽然 DOM 为操作节点提供了细致入微的控制手段，但在需要给文档插入大量新 HTML 标记的情况下，通过 DOM 操作仍然非常麻烦，因为不仅要创建一系列 DOM 节点，而且还要小心地按照正确的顺序把它们连接起来。相对而言，使用插入标记的技术，直接插入 HTML 字符串不仅更简单，速度也更快。以下与插入标记相关的 DOM 扩展已经纳入了 HTML5 规范。

#### 1.  innerHTML 属性

使用 innerHTML 属性也有一些限制。比如，在大多数浏览器中，通过 innerHTML 插入 <script>元素并不会执行其中的脚本。



大多数浏览器都支持以直观的方式通过 innerHTML 插入 <style> 元素，例如：

```javascript
<p class="para" data-name="wmsj" data-id="p1">这是一个网页</p>	
<div>hello world</div>
---
var a = document.querySelector("p");
a.innerHTML="<style>body{color: red;}</style>"
//p中的文字就消失了，被style标签填充了。
a.innerHTML	//"<style>body{color: red;}</style>"
```

#### 2.  outerHTML 属性

在读模式下， outerHTML 返回调用它的元素及所有子节点的 HTML 标签。在写模式下， outerHTML会根据指定的 HTML 字符串创建新的 DOM子树，然后用这个 DOM 子树完全替换调用元素。

具体使用的限制和`innterHTML` 是类似的，不能写入js脚本，但是可以写入style样式表；

#### 3.  insertAdjacentHTML() 方法

插入标记的最后一个新增方式是 insertAdjacentHTML() 方法。这个方法最早也是在IE中出现的，它接收两个参数：插入位置和要插入的 HTML 文本。第一个参数必须是下列值之一：

 "beforebegin" ，在当前元素之前插入一个紧邻的同辈元素；
 "afterbegin" ，在当前元素之下插入一个新的子元素或在第一个子元素之前再插入新的子元素；
 "beforeend" ，在当前元素之下插入一个新的子元素或在最后一个子元素之后再插入新的子元素；
 "afterend" ，在当前元素之后插入一个紧邻的同辈元素。

```javascript
<p class="para" data-name="wmsj" data-id="p1">这是一个网页</p>	
<div>hello world</div>
---
var a = document.querySelector("p");
a.insertAdjacentHTML("beforebegin", "<p>这是前面的同辈元素</p>")
a.insertAdjacentHTML("afterend", "<p>这是后面的同辈元素</p>");
a.insertAdjacentHTML("afterbegin", "<p>这是第一个子元素</p>");
a.insertAdjacentHTML("beforeend", "<p>这是最后一个子元素</p>");
```

#### 4. 内存与性能问题

使用本节介绍的方法替换子节点可能会导致浏览器的内存占用问题，尤其是在 IE 中，问题更加明显。在删除带有事件处理程序或引用了其他 JavaScript 对象子树时，就有可能导致内存占用问题。假设某个元素有一个事件处理程序（或者引用了一个 JavaScript 对象作为属性），在使用前述某个属性将该元素从文档树中删除后，元素与事件处理程序（或 JavaScript 对象）之间的绑定关系在内存中并没有一并删除。如果这种情况频繁出现，页面占用的内存数量就会明显增加。因此，在使用 innerHTML 、outerHTML 属性和 insertAdjacentHTML() 方法时，最好先手工删除要被替换的元素的所有事件处理程序和 JavaScript 对象属性

使用这几个属性——特别是使用 innerHTML ，仍然还是可以为我们提供很多便利的。一般来说，在插入大量新 HTML 标记时，使用 innerHTML 属性与通过多次 DOM 操作先创建节点再指定它们之间的关系相比，效率要高得多。这是因为在设置 innerHTML 或 outerHTML 时，就会创建一个 HTML解析器。这个解析器是在浏览器级别的代码（通常是 C++编写的）基础上运行的，因此比执行 JavaScript快得多。不可避免地，创建和销毁 HTML 解析器也会带来性能损失，所以最好能够将设置 innerHTML或 outerHTML 的次数控制在合理的范围内。

### 11.3.7  scrollIntoView() 方法

如何滚动页面也是 DOM 规范没有解决的一个问题。为了解决这个问题，浏览器实现了一些方法，
以方便开发人员更好地控制页面滚动。在各种专有方法中，HTML5 最终选择了 scrollIntoView() 作
为标准方法。

scrollIntoView() 可以在所有 HTML 元素上调用，通过滚动浏览器窗口或某个容器元素，调用
元素就可以出现在视口中。如果给这个方法传入 true 作为参数，或者不传入任何参数，那么窗口滚动
之后会让调用元素的顶部与视口顶部尽可能平齐。如果传入 false 作为参数，调用元素会尽可能全部
出现在视口中，（可能的话，调用元素的底部会与视口顶部平齐。）不过顶部不一定平齐，

```javascript
var a = document.querySelector("div");
a.scrollIntoView(false);
```

## 11.4 专有扩展

### 11.4.2  children 属性

这个属性是 HTMLCollection 的实例，只包含元素中同样还是元素的子节点。除此之外，children 属性与 childNodes 没有什么区别，即在元素只包含元素子节点时，这两个属性的值相同。

contains()---在实际开发中，经常需要知道某个节点是不是另一个节点的后代。

```javascript
<p class="para" data-name="wmsj" data-id="p1">
	<span>这是一个网页</span>
</p
---
var a = document.querySelector("p");
a.contains(document.querySelector("span")); //true
```

实际上， innerText 与 textContent 返回的内容并不完全一样。比如，
innerText 会忽略行内的样式和脚本，而 textContent 则会像返回其他文本一样返
回行内的样式和脚本代码。避免跨浏览器兼容问题的最佳途径，就是从不包含行内样
式或行内脚本的 DOM 子树副本或 DOM 片段中读取文本。

#### 2.  outerText 属性

除了作用范围扩大到了包含调用它的节点之外， outerText 与 innerText 基本上没有多大区别。在读取文本值时， outerText 与 innerText 的结果完全一样。但在写模式下， outerText 就完全不同了： outerText 不只是替换调用它的元素的子节点，而是会替换整个元素（包括子节点）。

支持 outerText 属性的浏览器有 IE4+、Safari 3+、Opera 8+和 Chrome。由于这个属性会导致调用它的元素不存在，因此并不常用。我们也建议读者尽可能不要使用这个属性。

### 11.4.5 滚动

## 11.5 小结

虽然 DOM 为与 XML 及 HTML 文档交互制定了一系列核心 API，但仍然有几个规范对标准的 DOM进行了扩展。这些扩展中有很多原来是浏览器专有的，但后来成为了事实标准，于是其他浏览器也都提供了相同的实现。本章介绍的三个这方面的规范如下。
  Selectors API，定义了两个方法，让开发人员能够基于 CSS 选择符从 DOM中取得元素，这两个方法是 querySelector() 和 querySelectorAll() 。
  Element Traversal，为 DOM 元素定义了额外的属性，让开发人员能够更方便地从一个元素跳到另一个元素。之所以会出现这个扩展，是因为浏览器处理 DOM 元素间空白符的方式不一样。
  HTML5，为标准的 DOM 定义了很多扩展功能。其中包括在 innerHTML 属性这样的事实标准基础上提供的标准定义，以及为管理焦点、设置字符集、滚动页面而规定的扩展 API。虽然目前 DOM扩展的数量还不多，但随着 Web 技术的发展，相信一定还会涌现出更多扩展来。很多浏览器都在试验专有的扩展，而这些扩展一旦获得认可，就能成为“伪”标准，甚至会被收录到规范的更新版本中。

