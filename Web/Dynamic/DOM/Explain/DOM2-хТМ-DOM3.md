---
title: DOM2 和 DOM3元素宽度元素高度原生javascript
date: 2016-05-07
tags: [DOM,Book]
categories: Dynamic
---

### 12.2.1 访问元素的样式

任何支持 style 特性的 HTML 元素在 JavaScript 中都有一个对应的 style 属性。这个 style 对象是 CSSStyleDeclaration 的实例，包含着通过 HTML 的 style 特性指定的所有样式信息，但不包含与外部样式表或嵌入样式表经层叠而来的样式。在 style 特性中指定的任何 CSS 属性都将表现为这个style 对象的相应属性。对于使用短划线（分隔不同的词汇，例如 background-image ）的 CSS 属性名，必须将其转换成驼峰大小写形式，才能通过 JavaScript 来访问。

其中一个不能直接转换的 CSS 属性就是 float 。由于 float 是 JavaScript 中的保留字，因此不能用作属性名。“DOM2 级样式”规范规定样式对象上相应的属性名应该是 cssFloat ；Firefox、Safari、Opera 和 Chrome 都支持这个属性，而 IE支持的则是 styleFloat 。

#### 1. DOM 样式属性和方法

DOM2级样式”规范还为 style 对象定义了一些属性和方法。这些属性和方法在提供元素的 style特性值的同时，也可以修改样式。下面列出了这些属性和方法。
 cssText ：如前所述，通过它能够访问到 style 特性中的 CSS 代码。
 length ：应用给元素的 CSS 属性的数量。
 parentRule ：表示 CSS 信息的 CSSRule 对象。本节后面将讨论 CSSRule 类型。
 getPropertyCSSValue(propertyName) ：返回包含给定属性值的 CSSValue 对象。
 getPropertyPriority(propertyName) ：如果给定的属性使用了 !important 设置，则返回"important" ；否则，返回空字符串。
 getPropertyValue(propertyName) ：返回给定属性的字符串值。
 item(index) ：返回给定位置的 CSS 属性的名称。
 removeProperty(propertyName) ：从样式中删除给定属性。
 setProperty(propertyName,value,priority) ：将给定属性设置为相应的值，并加上优先权标志（ "important" 或者一个空字符串）。
通过 cssText 属性可以访问style特性中的CSS代码。在读取模式下， cssText 返回浏览器对 style特性中 CSS 代码的内部表示。在写入模式下，赋给 cssText 的值会重写整个 style 特性的值；也就是说，以前通过 style 特性指定的样式信息都将丢失。例如，如果通过 style 特性为元素设置了边框，然后再以不包含边框的规则重写 cssText ，那么就会抹去元素上的边框。

```javascript
myDiv.style.cssText = "width: 25px; height: 100px; background-color: green";
alert(myDiv.style.cssText);
```

设置 cssText 是为元素应用多项变化最快捷的方式，因为可以一次性地应用所有变化。

```javascript
var a = document.querySelector("p");
a.style.cssText = "color: #fff; background: #DE4444;"
var styleName = [],
	styleValue = [],
	styleObj = {};
for (var i = 0, len = a.style.length; i < len; i++) {
	styleName.push(a.style[i]);
	styleValue.push(a.style.getPropertyValue(a.style[i]));
	styleObj[a.style[i]] = a.style.getPropertyValue(a.style[i]);
}
a.style.removeProperty("color")	//移除color属性；
```

#### 2. 计算的样式

虽然 style 对象能够提供支持 style 特性的任何元素的样式信息，但它不包含那些从其他样式表层叠而来并影响到当前元素的样式信息。“DOM2 级样式”增强了 document.defaultView ，提供了getComputedStyle() 方法。这个方法接受两个参数：要取得计算样式的元素和一个伪元素字符串（例如 ":after" ）。如果不需要伪元素信息，第二个参数可以是 null 。 getComputedStyle() 方法返回一个 CSSStyleDeclaration 对象（与 style 属性的类型相同），其中包含当前元素的所有计算的样式。

```javascript
var myDiv = document.getElementById("myDiv");
var computedStyle = document.defaultView.getComputedStyle(myDiv, null);
alert(computedStyle.backgroundColor); // "red"
alert(computedStyle.width); // "100px"
alert(computedStyle.height); // "200px"
alert(computedStyle.border); // 在某些浏览器中是"1px solid black"
```

边框属性可能会也可能不会返回样式表中实际的 border 规则（Opera 会返回，但其他浏览器不会）。存在这个差别的原因是不同浏览器解释综合（rollup）属性（如 border ）的方式不同，因为设置这种属性实际上会涉及很多其他属性。在设置 border 时，实际上是设置了四个边的边框宽度、颜色、样式属性（ border-left-width 、 border-top-color 、 border-bottom-style ， 等 等 ）。 因 此 ， 即 使computedStyle.border 不会在所有浏览器中都返回值，但computedStyle.borderLeftWidth 会返回值。

IE 不支持 getComputedStyle() 方法，但它有一种类似的概念。在 IE 中，每个具有 style 属性
的元素还有一个 currentStyle 属性。

```javascript
var myDiv = document.getElementById("myDiv");
var computedStyle = myDiv.currentStyle;
alert(computedStyle.backgroundColor); //"red"
alert(computedStyle.width); //"100px"
alert(computedStyle.height); //"200px"
alert(computedStyle.border); //undefined
```

无论在哪个浏览器中，最重要的一条是要记住所有计算的样式都是只读的；不能修改计算后样式对象中的 CSS 属性。此外，计算后的样式也包含属于浏览器内部样式表的样式信息，因此任何具有默认值的 CSS 属性都会表现在计算后的样式中。换句话说，不能指望某个 CSS 属性的默认值在不同浏览器中是相同的。如果你需要元素具有某个特定的默认值，应该手工在样式表中指定该值。

### 12.2.2 操作样式表

### 12.2.3 元素大

#### 1. 偏移量

首先要介绍的属性涉及偏移量（offset dimension），包括元素在屏幕上占用的所有可见的空间。元素的可见大小由其高度、宽度决定，包括所有内边距、滚动条和边框大小（注意，不包括外边距）。通过下列 4 个属性可以取得元素的偏移量。
 offsetHeight ：元素在垂直方向上占用的空间大小，以像素计。包括元素的高度、（可见的）水平滚动条的高度、上边框高度和下边框高度。
 offsetWidth ：元素在水平方向上占用的空间大小，以像素计。包括元素的宽度、（可见的）垂直滚动条的宽度、左边框宽度和右边框宽度。
 offsetLeft ：元素的左外边框至包含元素的左内边框之间的像素距离。
 offsetTop ：元素的上外边框至包含元素的上内边框之间的像素距离。

其中， offsetLeft 和 offsetTop 属性与包含元素有关，包含元素的引用保存在 offsetParent属性中。 offsetParent 属性不一定与 parentNode 的值相等。例如， <td> 元素的 offsetParent 是作为其祖先元素的 <table> 元素，因为 <table> 是在 DOM层次中距 <td> 最近的一个具有大小的元素。图 12-1 形象地展示了上面几个属性表示的不同大小。

要想知道某个元素在页面上的偏移量，将这个元素的 offsetLeft 和 offsetTop 与其 offsetParent的相同属性相加，如此循环直至根元素，就可以得到一个基本准确的值。

```javascript
function getElementLeft(element){
var actualLeft = element.offsetLeft;
var current = element.offsetParent;
while (current !== null){
actualLeft += current.offsetLeft;
current = current.offsetParent;
}
return actualLeft;
}
function getElementTop(element){
var actualTop = element.offsetTop;
var current = element.offsetParent;
while (current !== null){
actualTop += current. offsetTop;
current = current.offsetParent;
}
return actualTop;
}
```

这两个函数利用 offsetParent 属性在 DOM 层次中逐级向上回溯，将每个层次中的偏移量属性合计到一块。对于简单的 CSS 布局的页面，这两函数可以得到非常精确的结果。对于使用表格和内嵌框架布局的页面，由于不同浏览器实现这些元素的方式不同，因此得到的值就不太精确了。一般来说，页面中的所有元素都会被包含在几个 <div> 元素中，而这些 <div> 元素的 offsetParent 又是<body> 元素，所以 getElementLeft() 与 getElementTop() 会返回与 offsetLeft 和 offsetTop相同的值。

*所有这些偏移量属性都是只读的，而且每次访问它们都需要重新计算。因此，应该尽量避免重复访问这些属性；如果需要重复使用其中某些属性的值，可以将它们保存在局部变量中，以提高性能.*  

#### 2. 客户区大小 

`a.clientHeight` --height+padding;

`a.clientWidth` = width+padding;

与偏移量相似，客户区大小也是只读的，也是每次访问都要重新计算的。

#### 3. 滚动大小

`window.onscroll = function(e){ console.log(1) }` 

#### 4.获取屏幕大小

`window.innerHeight` --获取屏幕高度

`window.innerWidth` --获取屏幕宽度