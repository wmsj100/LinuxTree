---
title: DOM
date: 2016-05-05
tags: [DOM,Book]
categories: Dynamic
---

DOM（文档对象模型）是针对 HTML 和 XML 文档的一个 API（应用程序编程接口）。DOM 描绘了一个层次化的节点树，允许开发人员添加、移除和修改页面的某一部分。DOM 脱胎于Netscape 及微软公司创始的 DHTML（动态 HTML），但现在它已经成为表现和操作页面标记的真正的跨平台、语言中立的方式。
1998 年 10 月 DOM１级规范成为 W3C 的推荐标准，为基本的文档结构及查询提供了接口。本章主要讨论与浏览器中的 HTML 页面相关的 DOM1 级的特性和应用，以及 JavaScript 对 DOM1 级的实现。IE、Firefox、Safari、Chrome 和 Opera 都非常完善地实现了 DOM。

## 10.1 节点层次

DOM 可以将任何 HTML 或 XML 文档描绘成一个由多层节点构成的结构。节点分为几种不同的类型，每种类型分别表示文档中不同的信息及（或）标记。每个节点都拥有各自的特点、数据和方法，另外也与其他节点存在某种关系。节点之间的关系构成了层次，而所有页面标记则表现为一个以特定节点为根节点的树形结构。

文档节点是每个文档的根节点。在这个例子中，文档节点只有一个子节点，即 <html> 元素，我们称之为文档元素。文档元素是文档的最外层元素，文档中的其他所有元素都包含在文档元素中。每个文档只能有一个文档元素。在 HTML 页面中，文档元素始终都是 <html> 元素。在 XML 中，没有预定义的元素，因此任何元素都可能成为文档元素。

每一段标记都可以通过树中的一个节点来表示：HTML 元素通过元素节点表示，特性（attribute）通过特性节点表示，文档类型通过文档类型节点表示，而注释则通过注释节点表示。总共有 12 种节点类型，这些类型都继承自一个基类型。

### 10.1.1  Node 类型

每个节点都有一个 nodeType 属性，用于表明节点的类型。节点类型由在 Node 类型中定义的下列12 个数值常量来表示，任何节点类型必居其一：

```
 Node.ELEMENT_NODE (1)；
 Node.ATTRIBUTE_NODE (2)；
 Node.TEXT_NODE (3)；
 Node.CDATA_SECTION_NODE (4)；
 Node.ENTITY_REFERENCE_NODE (5)；
 Node.ENTITY_NODE (6)；
 Node.PROCESSING_INSTRUCTION_NODE (7)；
 Node.COMMENT_NODE (8)；
 Node.DOCUMENT_NODE (9)；
 Node.DOCUMENT_TYPE_NODE (10)；
 Node.DOCUMENT_FRAGMENT_NODE (11)；
 Node.NOTATION_NODE (12)。
```

通过比较上面这些常量，可以很容易地确定节点的类型，例如：

```javascript
<p>hello world</p>
---
var a = document.querySelector("p");
if (a.nodeType === Node.ELEMENT_NODE) {
	console.log(a + " is an element")
}	//[object HTMLParagraphElement] is an element
```

这个例子比较了 someNode.nodeType 与 Node.ELEMENT_NODE 常量。如果二者相等，则意味着someNode 确实是一个元素。然而，由于 IE 没有公开 Node 类型的构造函数，因此上面的代码在 IE 中会导致错误。为了确保跨浏览器兼容，最好还是将 nodeType 属性与数字值进行比较，如下所示：

```javascript
if (someNode.nodeType == 1){ // 适用于所有浏览器
alert("Node is an element.");
}
```

并不是所有节点类型都受到 Web 浏览器的支持。开发人员最常用的就是元素和文本节点。

#### 1 nodeName 和 nodeValue 属性

要了解节点的具体信息，可以使用 nodeName 和 nodeValue 这两个属性。这两个属性的值完全取决于节点的类型。在使用这两个值以前，最好是像下面这样先检测一下节点的类型。

```javascript
if (a.nodeType === 1) {
	name = a.nodeName;	//"p"
	value = a.nodeValue;	//null
}
```

在这个例子中，首先检查节点类型，看它是不是一个元素。如果是，则取得并保存 nodeName 的值。对于元素节点， nodeName 中保存的始终都是元素的标签名，而 nodeValue 的值则始终为 null 。

#### 2 节点关系

```javascript
<div class="div1">
	<p>
		<span>hello world</span>
	</p>
	<p>
		<button>click</button>
	</p>
</div>
---
var div1 = document.querySelector("div");
console.log(div1.childNodes);
console.log(div1.childNodes.length);
console.log(div1.childNodes.item(1));
console.log(div1.childNodes[1]);
```

每个节点都有一个 childNodes 属性，其中保存着一个 NodeList 对象。 NodeList 是一种类数组对象，用于保存一组有序的节点，可以通过位置来访问这些节点。请注意，虽然可以通过方括号语法来访问 NodeList 的值，而且这个对象也有 length 属性，但它并不是 Array 的实例。 NodeList 对象的独特之处在于，它实际上是基于 DOM 结构动态执行查询的结果，因此 DOM 结构的变化能够自动反映在 NodeList 对象中。我们常说， NodeList 是有生命、有呼吸的对象，而不是在我们第一次访问它们的某个瞬间拍摄下来的一张快照。
下面的例子展示了如何访问保存在 NodeList 中的节点——可以通过方括号，也可以使用 item()方法。

```javascript
var firstChild = someNode.childNodes[0];
var secondChild = someNode.childNodes.item(1);
var count = someNode.childNodes.length;
```

无论使用方括号还是使用 item() 方法都没有问题，但使用方括号语法看起来与访问数组相似，因此颇受一些开发人员的青睐。

另外，要注意 length 属性表示的是访问 NodeList 的那一刻，其中包含的节点数量。我们在本书前面介绍过，对 arguments 对象使用 Array.prototype.slice() 方法可以将其转换为数组。而采用同样的方法，也可以将 NodeList 对象转换为数组。来看下面的例子：

```javascript
//在 IE8 及之前版本中无效
var arrayOfNodes = Array.prototype.slice.call(someNode.childNodes,0);
var div1 = document.querySelector("div");
var arrayOfNodes = Array.prototype.slice.call(div1.childNodes, 0);
```

```javascript
function convertToArray(nodes){
var array = null;
try {
array = Array.prototype.slice.call(nodes, 0); //针对非 IE 浏览器
} catch (ex) {
array = new Array();
for (var i=0, len=nodes.length; i < len; i++){
  //这里只是获取最开始的一个快照
array.push(nodes[i]);
}
}
return array;
}
```

这个 convertToArray() 函数首先尝试了创建数组的最简单方式。如果导致了错误（说明是在IE8 及更早版本中），则通过 try-catch 块来捕获错误，然后手动创建数组。这是另一种检测怪癖的形式。

每个节点都有一个 parentNode 属性，该属性指向文档树中的父节点。包含在 childNodes 列表中的所有节点都具有相同的父节点，因此它们的 parentNode 属性都指向同一个节点。此外，包含在childNodes 列表中的每个节点相互之间都是同胞节点。通过使用列表中每个节点的 previousSibling和 nextSibling 属性，可以访问同一列表中的其他节点。列表中第一个节点的 previousSibling 属性值为 null ，而列表中最后一个节点的 nextSibling 属性的值同样也为 null ，

```javascript
if (someNode.nextSibling === null){
alert("Last node in the parent’s childNodes list.");
} else if (someNode.previousSibling === null){
alert("First node in the parent’s childNodes list.");
}
```

父节点与其第一个和最后一个子节点之间也存在特殊关系。父节点的 firstChild 和 lastChild属性分别指向其 childNodes 列表中的第一个和最后一个节点。其中， someNode.firstChild 的值始 终 等 于 someNode.childNodes[0] ， 而 someNode.lastChild 的 值 始 终 等 于 someNode.childNodes [someNode.childNodes.length-1] 。在只有一个子节点的情况下， firstChild 和lastChild 指向同一个节点。如果没有子节点，那么 firstChild 和 lastChild 的值均为 null 。

```javascript
div1.childNodes[0] === div1.firstChild	//true
div1.childNodes[div1.childNodes.length-1] === div1.lastChild //true
```

![](http://wmsj100.github.io/webFile/2016/May/2016-05-06/000034.png)

 hasChildNodes() 也是一个非常有用的方法，这个方法在节点包含一或多个子节点的情况下返回 true ；应该说，这是比查询 childNodes列表的 length 属性更简单的方法。

```javascript
<span></span>
var a = document.querySelector("span");
---
a.hasChildNodes()	//false
a.childNodes.length	//0
```

所有节点都有的最后一个属性是 ownerDocument ，该属性指向表示整个文档的文档节点。这种关系表示的是任何节点都属于它所在的文档，任何节点都不能同时存在于两个或更多个文档中。通过这个属性，我们可以不必在节点层次中通过层层回溯到达顶端，而是可以直接访问文档节点。

```javascript
a.ownerDocument
HTMLDocument → file:///E:/wamp/www/PHP/test/book/dom01.html
```

虽然所有节点类型都继承自 Node ，但并不是每种节点都有子节点。

#### 3. 操作节点

因为关系指针都是只读的，所以 DOM 提供了一些操作节点的方法。其中，最常用的方法是appendChild() ，用于向 childNodes 列表的末尾添加一个节点。添加节点后， childNodes 的新增节点、父节点及以前的最后一个子节点的关系指针都会相应地得到更新。更新完成后， appendChild()返回新增的节点。

 appendChild() 时传入了父节点的第一个子节点，那么该节点就会成为父节点的最后一个子节点，

```javascript
//someNode 有多个子节点
var returnedNode = someNode.appendChild(someNode.firstChild);
alert(returnedNode == someNode.firstChild); //false
alert(returnedNode == someNode.lastChild); //true
```

如果需要把节点放在 childNodes 列表中某个特定的位置上，而不是放在末尾，那么可以使用insertBefore() 方法。这个方法接受两个参数：要插入的节点和作为参照的节点。插入节点后，被插入的节点会变成参照节点的前一个同胞节点（ previousSibling ），同时被方法返回。如果参照节点是null ，则 insertBefore() 与 appendChild() 执行相同的操作，

```javascript
//插入后成为最后一个子节点
returnedNode = someNode.insertBefore(newNode, null);
alert(newNode == someNode.lastChild); //true
//插入后成为第一个子节点
var returnedNode = someNode.insertBefore(newNode, someNode.firstChild);
alert(returnedNode == newNode); //true
alert(newNode == someNode.firstChild); //true
//插入到最后一个子节点前面
returnedNode = someNode.insertBefore(newNode, someNode.lastChild);
alert(newNode == someNode.childNodes[someNode.childNodes.length-2]); //true
```

 replaceChild() 方法接受的两个参数是：要插入的节点和要替换的节点。要替换的节点将由这个方法返回并从文档树中被移除，同时由要插入的节点占据其位置。

在使用 replaceChild() 插入一个节点时，该节点的所有关系指针都会从被它替换的节点复制过来。尽管从技术上讲，被替换的节点仍然还在文档中，但它在文档中已经没有了自己的位置。

如果只想移除而非替换节点，可以使用 removeChild() 方法。这个方法接受一个参数，即要移除的节点。被移除的节点将成为方法的返回值，

与使用 replaceChild() 方法一样，通过 removeChild() 移除的节点仍然为文档所有，只不过在文档中已经没有了自己的位置。

#### 4. 其他方法

有两个方法是所有类型的节点都有的。第一个就是 cloneNode() ，用于创建调用这个方法的节点的一个完全相同的副本。 cloneNode() 方法接受一个布尔值参数，表示是否执行深复制。在参数为 true的情况下，执行深复制，也就是复制节点及其整个子节点树；在参数为 false 的情况下，执行浅复制，即只复制节点本身。复制后返回的节点副本属于文档所有，但并没有为它指定父节点。因此，这个节点副本就成为了一个“孤儿”，除非通过 appendChild() 、 insertBefore() 或 replaceChild() 将它添加到文档中。

```javascript
<ul>
<li>item 1</li>
<li>item 2</li>
<li>item 3</li>
</ul>
---
var a = document.querySelector("ul");
var b = a.cloneNode()
b.childNodes.length	//0
var c = a.cloneNode(true)
c.childNodes.length	//7
```

cloneNode() 方法不会复制添加到 DOM 节点中的 JavaScript 属性，例如事件处
理程序等。这个方法只复制特性、（在明确指定的情况下也复制）子节点，其他一切
都不会复制。IE 在此存在一个 bug，即它会复制事件处理程序，所以我们建议在复制之前最好先移除事件处理程序。

我们要介绍的最后一个方法是 normalize() ，这个方法唯一的作用就是处理文档树中的文本节点。由于解析器的实现或 DOM 操作等原因，可能会出现文本节点不包含文本，或者接连出现两个文本节点的情况。当在某个节点上调用这个方法时，就会在该节点的后代节点中查找上述两种情况。如果找到了空文本节点，则删除它；如果找到相邻的文本节点，则将它们合并为一个文本节点。

### 10.1.2  Document 类型 

JavaScript 通过 Document 类型表示文档。在浏览器中， document 对象是 HTMLDocument （继承自 Document 类型）的一个实例，表示整个 HTML 页面。而且， *document 对象是 window 对象的一个属性*，因此可以将其作为全局对象来访问。 Document 节点具有下列特征：

 nodeType 的值为 9；
 nodeName 的值为 "#document" ；
 nodeValue 的值为 null ；
 parentNode 的值为 null ；
 ownerDocument 的值为  null ；
  其子节点可能是一个 DocumentType （最多一个）、 Element （最多一个）、 ProcessingInstruction或 Comment 。

Document 类型可以表示 HTML 页面或者其他基于 XML 的文档。不过，最常见的应用还是作为HTMLDocument 实例的 document 对象。通过这个文档对象，不仅可以取得与页面有关的信息，而且还能操作页面的外观及其底层结构。

在 Firefox、Safari、Chrome 和 Opera 中，可以通过脚本访问 Document 类型的构
造函数和原型。但在所有浏览器中都可以访问 HTMLDocument 类型的构造函数和原型，

```javascript
HTMLDocument.prototype	//可以查看document的原型上面绑定的属性
HTMLDocument.prototype.querySelector	//function querySelector()
document instanceof HTMLDocument	//true
```

#### 1. 文档的子节点

虽然 DOM 标准规定 Document 节点的子节点可以是 DocumentType 、 Element 、 ProcessingInstruction 或 Comment ，但还有两个内置的访问其子节点的快捷方式。第一个就是 documentElement属性，该属性始终指向 HTML 页面中的 <html> 元素。另一个就是通过 childNodes 列表访问文档元素，但通过 documentElement 属性则能更快捷、更直接地访问该元素。

```javascript
document.children
//HTMLCollection [ <html> ]
document.children[0]
//<html lang="en">
document.childNodes[1]
//<html lang="en">
document.documentElement
//<html lang="en">
document.lastChild
//<html lang="en">
document.firstChild.nextSibling
//<html lang="en">
document.documentElement== document.childNodes[1]
//true
document.documentElement=== document.childNodes[1]
//true
document.lastChild === document.documentElement
//true
//你妹，这个方法是不是无穷无尽了
```

作为 HTMLDocument 的实例， document 对象还有一个 body 属性，直接指向 <body> 元素。因为开发人员经常要使用这个元素，所以 document.body 在 JavaScript代码中出现的频率非常高，其用法如下。

```javascript
var body = document.body; //取得对<body>的引用
```

所有浏览器都支持 document.documentElement 和 document.body 属性。

Document 另一个可能的子节点是 DocumentType 。通常将 <!DOCTYPE> 标签看成一个与文档其他部分不同的实体，可以通过 doctype 属性（在浏览器中是 document.doctype ）来访问它的信息。

```javascript
var doctype = document.doctype; //取得对<!DOCTYPE>的引用
```

多数情况下，我们都用不着在 document 对象上调用 appendChild() 、 removeChild() 和replaceChild() 方法，因为文档类型（如果存在的话）是只读的，而且它只能有一个元素子节点（该节点通常早就已经存在了）。

#### 2. 文档信息

作为 HTMLDocument 的一个实例， document 对象还有一些标准的 Document 对象所没有的属性。

```javascript
Document instanceof Object
//true
Document instanceof HTMLDocument
//false
//Document不是HTMLDocument的实例
document instanceof HTMLDocument
//true
//所以document是HTMLDocument的实例
document instanceof Object
//true
HTMLDocument.prototype.querySelector == Document.prototype.querySelector
//true
//俩者原型的属性引用的函数是相同的。
```

这些属性提供了 document 对象所表现的网页的一些信息。其中第一个属性就是 title ，包含着<title> 元素中的文本——显示在浏览器窗口的标题栏或标签页上。通过这个属性可以取得当前页面的标题，也可以修改当前页面的标题并反映在浏览器的标题栏中。修改 title 属性的值不会改变 <title>元素。来看下面的例子。

```javascript
//取得文档标题
var originalTitle = document.title;
//设置文档标题
document.title = "New page title";
```

接下来要介绍的 3 个属性都与对网页的请求有关，它们是 URL 、 domain 和 referrer 。 URL 属性中包含页面完整的 URL（即地址栏中显示的 URL）， domain 属性中只包含页面的域名，而 referrer属性中则保存着链接到当前页面的那个页面的 URL。(通过a链接跳转过来)在没有来源页面的情况下， referrer 属性中可能会包含空字符串。所有这些信息都存在于请求的 HTTP 头部，

当页面中包含来自其他子域的框架或内嵌框架时，能够设置 document.domain 就非常方便了。由于 跨 域 安 全 限 制 ， 来 自 不 同 子 域 的 页 面 无 法 通 过 JavaScript 通 信 。 而 通 过 将 每 个 页 面 的document.domain 设置为相同的值，这些页面就可以互相访问对方包含的 JavaScript 对象了。

浏览器对 domain 属性还有一个限制，即如果域名一开始是“松散的”（loose），那么不能将它再设置为“紧绷的”（tight）。换句话说，在将 document.domain 设置为 "wrox.com" 之后，就不能再将其设置回 "p2p.wrox.com" ，否则将会导致错误，只能升级到更上一级的父域名，而不能是降级到子域名。

#### 3. 查找元素

如果页面中多个元素的 ID 值相同， getElementById() 只返回文档中第一次出现的元素。

与 NodeList 对象类似，可以使用方括号语法或 item() 方法来访问 HTMLCollection 对象中的项。

```javascript
<p>heool 1</p>
<p>heool 2</p>
---
var a = document.querySelectorAll("p");
a[1].innerHTML	//"heool 2"
a.item(0).innerText	//"heool 1"
```

第三个方法，也是只有 HTMLDocument 类型才有的方法，是 getElementsByName() 。顾名思义，这个方法会返回带有给定 name 特性的所有元素。最常使用 getElementsByName() 方法的情况是取得单选按钮；为了确保发送给浏览器的值正确无误，所有单选按钮必须具有相同的 name 特性，

```javascript
<fieldset>
<legend>Which color do you prefer?</legend>
<ul>
<li><input type="radio" value="red" name="color" id="colorRed">
<label for="colorRed">Red</label></li>
<li><input type="radio" value="green" name="color" id="colorGreen">
<label for="colorGreen">Green</label></li>
<li><input type="radio" value="blue" name="color" id="colorBlue">
<label for="colorBlue">Blue</label></li>
</ul>
</fieldset>
var radios = document.getElementsByName("color");
```

其中所有单选按钮的 name 特性值都是 "color" ，但它们的 ID 可以不同。ID 的
作用在于将 <label> 元素应用到每个单选按钮，而 name 特性则用以确保三个值中只有一个被发送给浏览器。这样，我们就可以使用如下代码取得所有单选按钮：

#### 4. 特殊集合

不太常用，直接跳过；

#### 5. DOM 一致性检测

由于 DOM 分为多个级别，也包含多个部分，因此检测浏览器实现了 DOM 的哪些部分就十分必要了。 document.implementation 属性就是为此提供相应信息和功能的对象，与浏览器对 DOM 的实现直接对应。DOM1 级只为 document.implementation 规定了一个方法，即 hasFeature() 。这个方法接受两个参数：要检测的 DOM 功能的名称及版本号。如果浏览器支持给定名称和版本的功能，则该方法返回 true ，

```javascript
var hasXmlDom = document.implementation.hasFeature("XML", "1.0");
// true
document.implementation.hasFeature("Views","2.0")	//true
document.implementation.hasFeature("Events","3.0")	//true
document.implementation.hasFeature("MouseEvents","3.0")	//true
```

尽管使用 hasFeature() 确实方便，但也有缺点。因为实现者可以自行决定是否与 DOM 规范的不同部分保持一致。事实上，要想让 hasFearture() 方法针对所有值都返回 true 很容易，但返回 true有时候也不意味着实现与规范一致。例如，Safari 2.x 及更早版本会在没有完全实现某些 DOM 功能的情况下也返回 true 。为此，我们建议多数情况下，在使用 DOM 的某些特殊的功能之前，最好除了检测hasFeature() 之外，还同时使用能力检测。

#### 6. 文档写入

有一个 document 对象的功能已经存在很多年了，那就是将输出流写入到网页中的能力。这个能力体现在下列 4 个方法中： write() 、 writeln() 、 open() 和 close() 。其中， write() 和 writeln()方法都接受一个字符串参数，即要写入到输出流中的文本。 write() 会原样写入，而 writeln() 则会在字符串的末尾添加一个换行符（ \n ）。在页面被加载的过程中，可以使用这两个方法向页面中动态地加入内容，

如果使用`document.write()` 的内容里面包含`</script>` 则需要进行转义，否则就被理解为结束字符。

```javascript
document.write('<script>console.log("hello")<\/script>');
```

通过`document.write()` 写入的脚本也会被执行，

```javascript
document.write("<script>var a = \"sss\"<\/script>")
a	//"sss"
```

如果在文档加载结束后再调用 document.write() ，那么输出的内容将会重写整个页面，

方法 open() 和 close() 分别用于打开和关闭网页的输出流。如果是在页面加载期间使用 write()或 writeln() 方法，则不需要用到这两个方法。

### 10.1.3  Element 类型

要访问元素的标签名，可以使用 nodeName 属性，也可以使用 tagName 属性；这两个属性会返回相同的值

```javascript
<h3 id="whh">hello world</h3>
var a = document.getElementById("whh");
a.nodeName	//"H3"
a.tagName	//"H3"
//在 HTML 中，标签名始终都以全部大写表示；
```

这里的元素标签名是 h3 ，它拥有一个值为 "whh" 的 ID。可是， a.tagName 实际上输出的是"H3" 而非 "h3" 。在 HTML 中，标签名始终都以全部大写表示；而在 XML（有时候也包括 XHTML）中，标签名则始终会与源代码中的保持一致。假如你不确定自己的脚本将会在 HTML 还是 XML 文档中执行，最好是在比较之前将标签名转换为相同的大小写形式，

```javascript
if (element.tagName == "div"){ //不能这样比较，很容易出错！
//在此执行某些操作
}
if (element.tagName.toLowerCase() == "div"){ //这样最好（适用于任何文档）
//在此执行某些操作
}
```

#### 1. HTML 元素

所有 HTML 元素都由 HTMLElement 类型表示，不是直接通过这个类型，也是通过它的子类型来表示。 HTMLElement 类型直接继承自 Element 并添加了一些属性。添加的这些属性分别对应于每个HTML元素中都存在的下列标准特性。

 id ，元素在文档中的唯一标识符。
 title ，有关元素的附加说明信息，一般通过工具提示条显示出来。
 lang ，元素内容的语言代码，很少使用。
 dir ，语言的方向，值为 "ltr" （left-to-right，从左至右）或 "rtl" （right-to-left，从右至左），也很少使用。
 className ，与元素的 class 特性对应，即为元素指定的CSS类。没有将这个属性命名为 class ，是因为 class 是 ECMAScript 的保留字上述这些属性都可以用来取得或修改相应的特性值。

```javascript
<h3 id="whh" class="class1" title="this is a title" lang="ch" dir="ltr">hello world</h3>
a.id	//"whh"
a.className	//"class1"
a.lang	//"ch"
a.dir	//"ltr"
a.title	//"this is a title"
```

当然，像下面这样通过为每个属性赋予新的值，也可以修改对应的每个特性：

```javascript
a.id="qqq"	//"qqq"
a.className="www"	//"www"
a.title="ooo"	//"ooo"
a.lang="en"	//"en"
a.dir="rtl"	//"rtl"
a
//<h3 lang="en" dir="rtl" title="ooo" class="www" id="qqq">
```

这个貌似比较牛掰

#### 2. 取得特性

每个元素都有一或多个特性，这些特性的用途是给出相应元素或其内容的附加信息。操作特性的DOM 方法主要有三个，分别是 getAttribute() 、 setAttribute() 和 removeAttribute() 。这三个方法可以针对任何特性使用，包括那些以 HTMLElement 类型属性的形式定义的特性。

```javascript
a.getAttribute("id")	//"whh"
a.getAttribute("title")	//"this is a title"
a.getAttribute("class")	//"class1"
a.getAttribute("lll")	//null
```

传递给 getAttribute() 的特性名与实际的特性名相同。因此要想得到 class 特性值，应
该传入 "class" 而不是 "className "，后者只有在通过对象属性访问特性时才用。如果给定名称的特性不存在， getAttribute() 返回 null 。

通过 getAttribute() 方法也可以取得自定义特性（即标准 HTML 语言中没有的特性）的值，

```javascript
a.setAttribute("data-bg-color","red")	//undefined
a
//<h3 lang="ch" dir="ltr" title="this is a title" class="class1" id="whh" data-bg-color="red">
a.getAttribute("bg-color")	//"red"
```

先通过`setAttribute()` 方法添加自定义属性，然后就可以通过`getAttribute()` 访问自定义属性。

另外也要注意，根据 HTML5 规范，自定义特性应该加上 data- 前缀以便验证。

#### 3. 设置特性

与 getAttribute() 对应的方法是 setAttribute() ，这个方法接受两个参数：要设置的特性名和值。如果特性已经存在， setAttribute() 会以指定的值替换现有的值；如果特性不存在， setAttribute()则创建该属性并设置相应的值。

通过 setAttribute() 方法既可以操作 HTML 特性也可以操作自定义特性。通过这个方法设置的特性名会被统一转换为小写形式，即 "ID" 最终会变成 "id" 。

要介绍的最后一个方法是 removeAttribute() ，这个方法用于彻底删除元素的特性。调用这个方法不仅会清除特性的值，而且也会从元素中完全删除特性，如下所示：

```javascript
div.removeAttribute("class");
```

#### 4.  attributes 属性

Element 类型是使用 attributes 属性的唯一一个 DOM节点类型。 attributes 属性中包含一个NamedNodeMap ，与 NodeList 类似，也是一个“动态”的集合。元素的每一个特性都由一个 Attr 节点表示，每个节点都保存在 NamedNodeMap 对象中。 NamedNodeMap 对象拥有下列方法。

 getNamedItem(name) ：返回 nodeName 属性等于 name 的节点；
 removeNamedItem(name) ：从列表中移除 nodeName 属性等于 name 的节点；
 setNamedItem(node) ：向列表中添加节点，以节点的 nodeName 属性为索引；
 item(pos) ：返回位于数字 pos 位置处的节点。

```javascript
a.attributes.getNamedItem("id").value	//"whh"
a.attributes["id"].value="sss"	//"sss"
a.removeAttribute("class") === a.attributes.removeNamedItem("class")
a	//<h3 id="sss">
```

#### 5. 创建元素

使用 document.createElement() 方法可以创建新元素。这个方法只接受一个参数，即要创建元素的标签名。这个标签名在 HTML 文档中不区分大小写，而在 XML（包括 XHTML）文档中，则是区分大小写的。

在使用 createElement() 方法创建新元素的同时，也为新元素设置了 ownerDocuemnt 属性。此时，还可以操作元素的特性，为它添加更多子节点，以及执行其他操作。

#### 6. 元素的子节点

### 10.1.4  Text 类型

文本节点由 Text 类型表示，包含的是可以照字面解释的纯文本内容。纯文本中可以包含转义后的HTML 字符，但不能包含 HTML 代码。 Text 节点具有以下特征：
 nodeType 的值为 3；
 nodeName 的值为 "#text" ；
 nodeValue 的值为节点所包含的文本；
 parentNode 是一个 Element ；
  不支持（没有）子节点。

可以通过 nodeValue 属性或 data 属性访问 Text 节点中包含的文本，这两个属性中包含的值相同。对 nodeValue 的修改也会通过 data 反映出来，反之亦然。使用下列方法可以操作节点中的文本。

 appendData(text) ：将 text 添加到节点的末尾。
 deleteData(offset, count) ：从 offset 指定的位置开始删除 count 个字符。
 insertData(offset, text) ：在 offset 指定的位置插入 text 。
 replaceData(offset, count, text) ：用 text 替换从 offset 指定的位置开始到 offset+count 为止处的文本。
 splitText(offset) ：从 offset 指定的位置将当前文本节点分成两个文本节点。
 substringData(offset, count) ：提取从 offset 指定的位置开始到 offset+count 为止
处的字符串。

```javascript
c.data	//"hello world"
c.nodeValue	//"hello world"
c.appendData(" wmsj100")	//hello world wmsj100
c.deleteData(6,6)	//hello wmsj100
c.insertData(5,"yes")	//helloyes wmsj100
c.replaceData(5,3,"")	//hello wmsj100
c.splitText(6)	//#text "wmsj100"	从下标6开始把字符串分割为俩部分
b.childNodes
//NodeList [ #text "hello ", #text "wmsj100" ]
c.substringData(2,2)	//"ll" 从2，4提取字符串“ll”
```

除了这些方法之外，文本节点还有一个 length 属性，保存着节点中字符的数目。而且，nodeValue.length 和 data.length 中也保存着同样的值。

```javascript
c	//#text "hello world"
c.data.length	//11
c.nodeValue.length	//11
c.length	//11
```

#### 1. 创建文本节点

可以使用 document.createTextNode() 创建新文本节点，这个方法接受一个参数——要插入节点中的文本。

一般情况下，每个元素只有一个文本子节点。不过，在某些情况下也可能包含多个文本子节点，比如分多次`appendChild` 给元素文本节点，或是使用了`splitText` 函数

```javascript
var q = document.createElement("p")
var w = document.createTextNode("ni hao")
document.body.appendChild(q)
var e = document.createTextNode("another txt")
q.appendChild(e)
q.childNodes
//NodeList [ #text "ni hao", #text "another txt" ]
q.childNodes[0].splitText(3)	//#text "hao"
//NodeList [ #text "ni ", #text "hao", #text "another txt" ]
```

如果两个文本节点是相邻的同胞节点，那么这两个节点中的文本就会连起来显示，中间不会有空格。

#### 2. 规范化文本节点

DOM 文档中存在相邻的同胞文本节点很容易导致混乱，因为分不清哪个文本节点表示哪个字符串。另外，DOM 文档中出现相邻文本节点的情况也不在少数，于是就催生了一个能够将相邻文本节点合并的方法。这个方法是由 Node 类型定义的（因而在所有节点类型中都存在），名叫 normalize() 。如果在一个包含两个或多个文本节点的父元素上调用 normalize() 方法，则会将所有文本节点合并成一个节点，结果节点的 nodeValue 等于将合并前每个文本节点的 nodeValue 值拼接起来的值。

```javascript
q.childNodes
//NodeList [ #text "ni ", #text "hao", #text "another txt" ]
q.normalize()
q.childNodes	//NodeList [ #text "ni haoanother txt" ]
q.childNodes[0].data	//"ni haoanother txt"
```

浏览器在解析文档时永远不会创建相邻的文本节点。这种情况只会作为执行 DOM操作的结果出现。

#### 3. 分割文本节点

Text 类型提供了一个作用与 normalize() 相反的方法： splitText() 。这个方法会将一个文本节点分成两个文本节点，即按照指定的位置分割 nodeValue 值。原来的文本节点将包含从开始到指定位置之前的内容，新文本节点将包含剩下的文本。这个方法会返回一个新文本节点，该节点与原节点的parentNode 相同。

分割文本节点是从文本节点中提取数据的一种常用 DOM解析技术。

### 10.1.5  Comment 类型

注释在 DOM 中是通过 Comment 类型来表示的。 Comment 节点具有下列特征：
 nodeType 的值为 8；
 nodeName 的值为 "#comment" ；
 nodeValue 的值是注释的内容；
 parentNode 可能是 Document 或 Element ；
  不支持（没有）子节点。

创建一个注释节点并插入页面

```javascript
var q = document.createComment("another comment")
q	//<!-- another comment -->
a.insertBefore(q, a.children[0].nextElementSibling)
```

显然，开发人员很少会创建和访问注释节点，因为注释节点对算法鲜有影响。

### 10.1.6  CDATASection 类型

### 10.1.7  DocumentType 类型

DocumentType 类型在 Web 浏览器中并不常用，仅有 Firefox、Safari 和 Opera 支持它

### 10.1.8  DocumentFragment 类型

在所有节点类型中，只有 DocumentFragment 在文档中没有对应的标记。DOM 规定文档片段（document fragment）是一种“轻量级”的文档，可以包含和控制节点，但不会像完整的文档那样占用额外的资源。 DocumentFragment 节点具有下列特征：
 nodeType 的值为 11；
 nodeName 的值为 "#document-fragment" ；
 nodeValue 的值为 null ；
 parentNode 的值为 null ；
  子节点可以是 Element 、 ProcessingInstruction 、 Comment 、 Text 、 CDATASection 或EntityReference 。
虽然不能把文档片段直接添加到文档中，但可以将它作为一个“仓库”来使用，即可以在里面保存将来可能会添加到文档中的节点。要创建文档片段，可以使用 document.createDocumentFragment() 方法，

`<ul id="myList"></ul>` 

假设我们想为这个 <ul> 元素添加 3 个列表项。如果逐个地添加列表项，将会导致浏览器反复渲染（呈现）新信息。为避免这个问题，可以像下面这样使用一个文档片段来保存创建的列表项，然后再一次性将它们添加到文档中。

```javascript
var fragment = document.createDocumentFragment();
var ul = document.getElementById("myList");
var li = null;
for (var i=0; i < 3; i++){
li = document.createElement("li");
li.appendChild(document.createTextNode("Item " + (i+1)));
fragment.appendChild(li);
}
ul.appendChild(fragment);
```

### 10.1.9  Attr 类型

我们并不建议直接访问特性节点。实际上，使用 getAttribute() 、 setAttribute()
和 removeAttribute() 方法远比操作特性节点更为方便。

## 10.2 DOM 操作技术

使用` <script>`  元素可以向页面中插入 JavaScript 代码，一种方式是通过其 src 特性包含外部文件，另一种方式就是用这个元素本身来包含代码。

动态加载的外部 JavaScript 文件能够立即运行，比如下面的 <script> 元素：

```javascript
<script type="text/javascript" src="client.js"></script>
```

#### 10.2.2 动态样式

能够把 CSS 样式包含到 HTML 页面中的元素有两个。其中， <link> 元素用于包含来自外部的文件，而 <style> 元素用于指定嵌入的样式。与动态脚本类似，所谓动态样式是指在页面刚加载时不存在的样式；动态样式是在页面加载完成后动态添加到页面中的。



如果专门针对 IE 编写代码，务必小心使用 styleSheet.cssText 属性。在重用同一个 <style> 元素并再次设置这个属性时，有可能会导致浏览器崩溃。同样，将
cssText 属性设置为空字符串也可能导致浏览器崩溃。

#### 10.2.3 操作表格

为 <table> 元素添加的属性和方法如下。
 caption ：保存着对 <caption> 元素（如果有）的指针。
 tBodies ：是一个 <tbody> 元素的 HTMLCollection 。
 tFoot ：保存着对 <tfoot> 元素（如果有）的指针。
 tHead ：保存着对 <thead> 元素（如果有）的指针。
 rows ：是一个表格中所有行的 HTMLCollection 。
 createTHead() ：创建 <thead> 元素，将其放到表格中，返回引用。
 createTFoot() ：创建 <tfoot> 元素，将其放到表格中，返回引用。
 createCaption() ：创建 <caption> 元素，将其放到表格中，返回引用。
 deleteTHead() ：删除 <thead> 元素。
 deleteTFoot() ：删除 <tfoot> 元素。
 deleteCaption() ：删除 <caption> 元素。
 deleteRow(pos) ：删除指定位置的行。
 insertRow(pos) ：向 rows 集合中的指定位置插入一行。
为 <tbody> 元素添加的属性和方法如下。
 rows ：保存着 <tbody> 元素中行的 HTMLCollection 。
 deleteRow(pos) ：删除指定位置的行。
 insertRow(pos) ：向 rows 集合中的指定位置插入一行，返回对新插入行的引用。
为 <tr> 元素添加的属性和方法如下。
 cells ：保存着 <tr> 元素中单元格的 HTMLCollection 。
 deleteCell(pos) ：删除指定位置的单元格。
 insertCell(pos) ：向 cells 集合中的指定位置插入一个单元格，返回对新插入单元格的引用。
使用这些属性和方法，可以极大地减少创建表格所需的代码数量。

#### 10.2.4 使用 NodeList

这个例子中初始化了第二个变量 len 。由于 len 中保存着对 divs.length 在循环开始时的一个快照，因此就会避免上一个例子中出现的无限循环问题。在本章演示迭代 NodeList 对象的例子中，使用的都是这种更为保险的方式。
一般来说，应该尽量减少访问 NodeList 的次数。因为每次访问 NodeList ，都会行一次基于文档的查询。所以，可以考虑将从 NodeList 中取得的值缓存起来。

## 10.3 小结

DOM 是语言中立的 API，用于访问和操作 HTML 和 XML 文档。DOM1 级将 HTML 和 XML 文档形象地看作一个层次化的节点树，可以使用 JavaScript 来操作这个节点树，进而改变底层文档的外观和结构。
DOM 由各种节点构成，简要总结如下。
  最基本的节点类型是 Node ，用于抽象地表示文档中一个独立的部分；所有其他类型都继承自Node 。
 Document 类型表示整个文档，是一组分层节点的根节点。在 JavaScript 中， document 对象是Document 的一个实例。使用 document 对象，有很多种方式可以查询和取得节点。
 Element 节点表示文档中的所有 HTML 或 XML 元素，可以用来操作这些元素的内容和特性。
  另外还有一些节点类型，分别表示文本内容、注释、文档类型、CDATA 区域和文档片段。

访问 DOM 的操作在多数情况下都很直观，不过在处理 <script> 和 <style> 元素时还是存在一些复杂性。由于这两个元素分别包含脚本和样式信息，因此浏览器通常会将它们与其他元素区别对待。这些区别导致了在针对这些元素使用 innerHTML 时，以及在创建新元素时的一些问题。

理解 DOM 的关键，就是理解 DOM 对性能的影响。DOM 操作往往是 JavaScript程序中开销最大的部分，而因访问 NodeList 导致的问题为最多。 NodeList 对象都是“动态的”，这就意味着每次访问NodeList 对象，都会运行一次查询。有鉴于此，***最好的办法就是尽量减少 DOM 操作***。

