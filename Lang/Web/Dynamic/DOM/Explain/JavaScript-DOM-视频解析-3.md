---
title: JavaScript-DOM-视频解析-3
date: 2016-3-31 09:57:11
tags: [JavaScript,DOM]
categories: Dynamic
---

#### firstChild/firstElementChild

```javascript
$("#p2").firstChild
//"我是段落2"	获取的是第一个换行和文本
$("#p2").firstElementChild
//<a class="link" href="#">hhahaha</a> </p>
//获取的是第一个标签a
```
<!-- more -->
#### createElement/appendChild

```javascript
img1=document.createElement('img')
//<img>	首先创建img标签，并且把标签赋值给img1变量
img1
//<img>	查看img1，输出图片标签
img1.id="myimg1"
//"myimg1"	给标签添加id；
img1.src="https://avatars0.githubusercontent.com/u/17332748?v=3&s=460"
//"https://avatars0.githubusercontent.com/u/17332748?v=3&s=460"	给标签添加图片链接
img1.width=100
100
img1.height=100
100
//分别设置图片的宽高
img1
//<img id="myimg1" src="https://avatars0.githubusercontent.com/u/17332748?v=3&amp;s=460" width="100" height="100">
//再查看创建的img标签
$("#p2").appendChild(img1)
//把img1添加到p2的子元素中，
```

#### createTextNode

```javascript
var text1=document.createTextNode("hello world")
text1	//查看text1
//"hello world"	创建文本内容，
p1.appendChild(text1)
p1	//查看p1
//<p>hello world</p>
document.body.appendChild(p1)
//把p1添加到页面
```

#### insertBefore

```javascript
var myimg1=$(".myimg1")
//获取要添加元素的参考元素img1
var p1=$("#p2")
//获取要添加元素的父元素
var p2=document.cerateElement('p');
//创建元素
var text1=document.createTextNode("hello world");
p2.appendChild(text1);
p1.insertBefore(p1,myimg1)
//在父元素p1的子元素myimg1前面添加元素p1;
```

> insertBefore可以结合firstChild来给页面标签添加元素，如果页面标签没有子元素，那么添加的元素默认添加到第一位,
>
> 如果要添加的元素p2已经存在页面中，那么这个添加过程就是把p2原来的位置删除，添加到新位置。

```javascript
var p4=$(".p3").firstChild
//class=p3的p没有子元素
$(".p3").insertBefore(p2,p4)
//把p2添加到p4元素的前面，
//但是p4为空标签，所以这个添加过程就是给.p3下面添加
//一个子元素，p2
```

#### replaceChild

这个属性也是针对标签的子元素进行操作的

```javascript
var p3=p2.firstChild
//设置p3为p2的第一个子元素
var p4=document.createElement("a")
//创建链接a元素p4
p4.appendChild(document.createTextNode("Hello wmsj100"))
//给a元素添加内容“hello wmsj100”
p4.href="#"
//添加链接
p2.replaceChild(p4,p3)
//进行内容替换
```

#### removeChild

```javascript
var q2=p2.childNodes[1]
//通过childNodes可以获取到p2的所有子节点，
//包括换行符(#text)，
//本来p2只有俩个a链接，但是加上换行符就是3个了，
//数组的下标是从零开始的。
p2.removeChild(q2)
//删除p2的第二个链接a
```

#### cloneChild

默认的复制方式是`false`,即只复制标签，不复制标签的内容，如果设置值为`true`，那么就会把所有的子节点也复制上。

```javascript
p2.cloneNode()
//<p id="p2"></p>	只是复制了p标签的属性，但是值为空；
p2.cloneNode(true)
//<p id="p2"> 
    我是段落2 
    <a class="link" href="#">hhahaha</a> 
 </p>
//复制了p标签的所有属性和值；
document.body.appendChild(p3)
//就会再页面的底部添加一个p标签，和p2是一样的。
```

给标签添加属性

```javascript
p3.className="wmsj"
//<p class="wmsj">...</p>
```

---

### 属性

#### createAttribute / nodeValue / getAttribute / setAttribute

先通过createAttribute，创建属性，然后通过nodeValue给属性名赋值，然后通过setAttribute把属性名添加给标签，最后通过getAttribute查看标签的属性；

```javascript
var q1=document.createAttribute("name")
name=""	//创建属性
q1.nodeValue="wmsj"
name="value"	//为属性赋值
p2.setAttributeNode(q1)	//把属性q1添加给p2
p2.getAttribute("name")
//"wmsj"	查看添加的属性
```

添加class属性有俩种方法：

```javascript
script.className="wmsj";
script.setAttribute("class","wmsj");
//这俩个的效果是一样的。
```

- 因为属性是要依附于标签的，所以要先创建标签，


- 然后给标签设置属性和值，通过setAttribute方法；
- 然后添加onload函数来添加监听事件：

```javascript
script.onload=function(){console.log("complete")}
//当script添加完成就会再控制台打印“complete“
```

