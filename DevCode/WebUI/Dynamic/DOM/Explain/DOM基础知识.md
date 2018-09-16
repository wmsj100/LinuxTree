---
title: DOM基础知识
date: 2016-06-23
tags: [DOM]
categories: Dynamic
---

- 使用`children`替代`childNodes`,这样可以过滤文本节点。

- 使用`firstElementChild`替代`firstChild`.

- 使用`nextElementSibling`替代`nextSibling`;

- `parentElement` === `parentNode`;

- `nodes.firstChild.previousElementSibling` => `null`;

- `nodes.lastChild.nextElementSibling` => `null`;

- `nodes.insertBefore(node,nodes.firstChild)` -- 可以在第一项之前插入节点

- `nodes.previousElementSibling === null` => `nodes`是第一项。

- `nodes.nextElementSibling === null` => `nodes`是最后一项。

- 如果列表中只有一个节点，那么这个节点的`nextSibling`和`priviousSibling`都是`null`；

- `nodes.firstElementChild === nodes.children[0]`;

- `nodes.lastElementChild === nodes.children[nodes.children.length-1]`;

- `nodes.firstChild === null || nodes.lastChild === null`表示没有子节点。

- `var c = a.appendChild(b)` => `c === a.lastChild && c === b`;

- `var d = a.insertBefore(b, a.firstChild)` => `d === a.firstChild && c === b`;

- 如果`appendChild / insertBefore`的是一个已经存在于文档中的对象，那么会把对象从之前位置删除，然后重新添加到新位置。

- 任何`DOM`节点不能同时出现在文档中的多个位置。

- `insertBefore(node, null)` === `appendChild(node)`

- `a.replaceChild(b,para)`其中`a`作为父元素，`b`作为替换元素，`para`作为被替换元素，会被从`DOM`树删除，然后由`b`占用其位置。这个方法会返回删除的`para`标签。

- `a.removeChild(b)`把`b`节点从`DOM`树删除；

- 被替换或删除的节点依然存在，只不过是从`DOM`树上删除了，还存在于内存中，但是不属于任何元素节点，其`parentNode` => `node`;

- `appendChild, insertBefore, replaceChild, removeChild`都需要先获取父节点。

- `cloneNode(true)`会执行深度复制，但是不会复制绑定到节点上面的事件，

- `removeEventListener("click",show,false)`只能用来移除使用`addEventListener`添加的事件，而且必须是使用独立函数(函数声明或者函数表达式),如果是`addEventListener`内部的匿名函数，则没有办法移除，因为没有指向的引用指针。

- 元素节点属性`a.nodeType` =>1 / `a.nodeName` => `DIV`/ `a.nodeValue` =>`null`

- `document.nodeType` => 9 / `document.nodeName` => `"#document"`
- `document.childNodes` => `[[<!DOCTYPE HTML>],[<html len="en">]]` 

- `document instanceof HTMLDocument` => `true`;

- `document instanceof Document` => `true`;

- `document.documentElement`执行`html`页面

- `document.documentElement === (document.lastChild || document.childNodes[1])`

- 所有浏览器都支持`document.documentElement`和`document.body`;

- 通过`document.documentElement.clientWidht`可以获取不包含滚动条`17px`的页面宽度。

- `window.innerWidth`可以获取包含滚动条的页面宽度。

- 因为`document`作为`HTMLDocument`的实例，所以拥有`body`属性。

- `document.doctype`可以访问页面的声明。`<!DOCTYPE HTML>`

- 对于位于`<html>`标签外部的注释，`firefox`会获取不管是位于`<html>`前面的注释，还是位于`</html>`后面的注释；但是其它浏览器只会获取`<html>`前面的一条注释，直接忽略后一条注释。

- `document.title`--可以获取页面的标题。

- `document.URL === location.href` -- 获取页面的完整链接

- `document.domain` -- 获取页面的主域名。没有在JS中设置默认为空字符串。可以写入，但是只能写入当前域名的主域名。`a.com`如果设置为当前域名中不包含的字符串则会报错。如果开始把值设置为紧绷的，就不能再设置为松散的，比如刚开始设置为`a.com`，就不能再设置为`child.a.com`.

- `document.referrer` -- 获取链接到当前页面的那个链接。如果没有则默认空字符串。

- `document.getElementsByName("para")` 可以获取页面标签`name="para"`的数组集合。

- `Document`的俩个元素查找方法为`getElementById`和`getElementsByTagName`,这俩个方法会返回`HTMLCollection`对象，是一个动态集合，伪数组。

- `HTMLDocument`类型拥有的查找方法`getElementsByName`;常用于获取所有的单选按钮。

- 如果页面有多个`id`相同的标签，那么只会获取第一个。

- `document.links` -- 获取所有的链接

- `document.images` -- 获取所有的图片标签

- `document.write('<script src="01.js"><\/script>')`可以动态的向页面添加`JS`文件，到目前未知，记得转义`/`

- `a.tagName === a.nodeName` => `"p"`;获取元素的标签名，在`HTML`中，标签名始终都是以全部大小的形式表现。

- 所有的`HTML`元素都由`HTMLElement`子类型表示，而它也是继承自`Element`并且添加了一些属性。`a.id, a.className, a.title`

- `HTML`的属性`id, className, title`都是可以读写的，而且改变是实时的。

- `a.setAttribute("data-name","wmsj")`, `a.getAttribute("data-name")` => `wmsj`

- `a.getAttribute("style")` => `"color: red;"`;
- `a.getAttribute("onclick")` => `"console.log('hello')"`;
- 当通过`getAttribute`获取元素的`style`样式和`onclick`事件时候返回的是字符串。

- `a.removeAttribute("onclick")`通过`removeAttribute`可以删除元素的属性，包括样式属性`style`,事件属性`onclick`都可以删除。

- 每个元素都有一个`attributes`列表，里面包含元素的所有属性，可以通过下标或者是字符进行匹配`a.attributes[0]`或者`a.attributes["id"]`，也可以`a.attributes["id"] = "wmsj"`,`a.attributes["id"]` => "wmsj";

- `attributes`是一个类数组，如果想要遍历元素的属性，那么就可以借用`for`循环，其中`name = attributes[i].nodeName`, `value = attribute[i].nodeValue`;

- 通过一个数组来保存名值对，最后再以空格为分隔符，将它们拼接起来，这是序列化从字符串的一种常用技巧。

---

### text

- 文本节点不能再添加子节点，可以通过`txt.data`或者`txt.nodeValue`获取值。
- `txt.length`返回文本的长度。
- `txt.appendData("aaa")` -- 在文本的后面添加字符串`aaa`;
- `txt.deleteData(start,count)` -- 从下标`start`开始删除`count`个字符；
- `txt.insertData(start,"str")` -- 在指定的下标`start`前面插入字符串"str";
- `txt.replaceData(start,count,"str")` -- 从下标`start`开始查找`count`个字符替换为字符串`str`。
- `txt.splitText(start)` -- 在下标`start`开始把文本拆分为俩个文本节点。
- `txt.substringData(start,count)` -- 从下标`start`开始，提取`count`个字符。
- `txt.length === txt.data.length === txt.nodeValue.length`返回字符串长度。

- 默认情况下每个可以包含内容的元素最多只能有一个文本节点。
- `b.nodeValue = "<html>hello</html>"` => `"<html>hello</html>"`;
- 也就是说可以通过这种方式安全的输入标签或者JS代码而不会执行。

- `document.createTextNode("hello world")`可以创建一个文本节点。

```javascript
    var span = document.createElement("span");
    var txt = document.createTextNode("hello world");
    span.appendChild(txt);
    var txt2 = document.createTextNode("happy world");
    span.appendChild(txt2);
    document.body.appendChild(span);
    
    span.childNodes;    ["hello world", "happy world"]
```

- 上面的这个`span`节点内部就有俩个文本节点。
- 通过`txt.splitText(num)`也可以创建多个文本节点。

- 在元素内部出现多个文档节点的情况还是很容易出现的，但是这会扰乱我们的选择，这不是我们希望的，所以就需要在文本节点的父元素上面通过`normalize`方法来合并多个相邻文本节点为一个。

```javascript
span.childNodes;    //["hello world", "happy world"]
span.normalize();
span.childNodes;    //["hello worldhappy world"]
span.childNodes.length; //1
```

- 分割文本节点是从文本节点中提取数据的一种常用的`DOM`解析技术。
- `comment`和`textNode`的唯一区别是没有`splitText`方法。

- `document.createDocumentFragment()`-- 可以创建代码临时仓库，这个作用太犀利了
- 如果节点已经存在，那么把节点`appendChild`/ `insertBefore`到代码片段中，该节点就会从`DOM`树中删除，但是对该节点的引用地址还是可以使用的。

---

- 对于设置属性，最常用的还是`getAttribute, setAttribute, removeAttribute`,但是还是有其它的方法可以直接操作属性节点。`document.createAttribute`;
- 通过`createAttribute`创建的属性节点必须通过`setAttributeNode`把属性节点绑定到元素上面。
- 印象中`jQuery`就是这样设置属性的。

```javascript
    var a = document.querySelector("span");
    var align = document.createAttribute("align");
    align.nodeValue = "right";
    a.setAttributeNode(align);
    var val1 = a.getAttributeNode("align").value; //"right"
    var val2 = a.getAttribute("align"); //"right"
    var val3 = a.attributes["align"].value; //"right"
```

---

- 能够包含样式表的元素有俩个，`link`包含外置样式表，`style`包含指定嵌入样式。
- `ie8`不识别`document.head`，但是识别`document.querySelector("head")`.
- 当动态添加`style`样式时候，`ie`也是存在和`script`类似的问题，把`style`当作特殊对象，不能访问其子对象，所以不能使用`script.innerText`，但是可以通过`style.styleSheet.cssText`可以设置属性。

---

~~- 创建表格可以使用新的`API`，但是这一套`ie9`都不支持，所以就只能用老办法了。~~
- `insertRow(0)` -- 向`rows`集合的指定位置插入一行。
- `insertCell(0)` -- 向`cells`集合的指定位置插入一列。
- `table.createTBody` -- 创建表格主体；不要使用这个，因为`ie9-`不支持
- `table.rows[0].cells[0].innerText` -- 插入列的内容。


