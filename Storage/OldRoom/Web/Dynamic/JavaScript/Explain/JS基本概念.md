---
title: JS基本概念
date: 2016-03-24 12:18:58
tags: [JavaScript]
categories: Dynamic
---
### 问答
1. CSS和JS在网页中的放置顺序是怎样的？
- CSS放在前端是保证页面渲染时候所有的HTML下载完成构建好DOM，所有的CSS下载完成构建CSSOM，然后浏览器整合俩个OM生成渲染树，如果CSS放在后面页面可能会出现闪烁或者白屏。
  <!-- more -->
- JS是阻塞加载，如果在head里有javascript文件，那么必须是先要把这些文件全部下载、解析，然后执行，它是下载完成之后就会立刻执行。执行完成之后程序才会继续往下走。如果放置在页面前端，势必会影响速度。如果JS文件比较大，算法也比较复杂的话，影响更大。
- 但是JS也有非阻塞解决方案，常用的方式就是用defer或者async属性，这个属性的用途是表明脚本在执行时候不会影响页面构造。也就是说，脚本会延长到整个页面都解析完成后再执行。如果是这样的操作，JS的文件放置位置就不是很重要了，放在head里面也是可以的。
- 但是使用defer或者async有一个缺陷，在有的浏览器里面并不会按照自己文件的顺序来执行。并且有的浏览器会忽略这个属性。所以考虑到兼容性和稳定性，还是将引入的文件放置到后面，如果是要使用html标签的js，也最好放置在后面，防止页面加载时候正文标签还没有加载而出现错误。
- 由于现在浏览器的性能提升如此之强，可能在加载一个页面时候它会提前把后续页面的JS和CSS提前下载（只是下载，但不执行)，这样就和JS、CSS的位置无关了。
- 但是综合考虑包括兼容性已经稳定性，还是建议把CSS放置在顶部，把JS放置到底部。
> 参考文献——[知乎](http://www.zhihu.com/question/23250329)
1. 解释白屏和FOUC？
2. 白屏——是针对IE浏览器来说的，在某些场景下（新窗口打开或者是页面刷新）页面会出现白屏而不是逐步展现，如果使用@import标签，即使使用link标签把CSS放置在顶部，也可能会出现白屏。
3. FOUC——无样式内容闪烁——这个还是针对的IE浏览器，指页面会以无样式显示页面然后再恢复正常页面，就是页面出现无样式和样式加载的页面切换闪烁。
   原因大致为：
   - 使用@import方法导入样式表；
   - 将样式表放置在页面的底部；
   - 有几个样式表，放置在html页面的不同位置。
- 其实原理很清楚：当样式表晚于html加载时，页面会使用无样式加载方式，但当css样式表开始加载时，页面便开始切换到有样式表的渲染方式展现页面。
- 解决方式也很简单，就是使用link标签将样式表放置在head标签中。
1. async和defer的作用是什么？有什么区别？
   当浏览器遇到script脚本的时候：
2. ` <script src="script.js"></script>`
   浏览器读到该script标签的时候会立即加载并执行指定的脚本， 在加载时该标签后面的文档元素就停止加载，知道js脚本文件加载并且执行完成之后才会继续加载html文档；
3. `<script  async  src="script.js"></script>`
   有async，浏览器加载到该script标签的时候，后续的文档元素不会停止等待，而是和js的加载执行并行进行（异步）；
4. `<script  defer  src="script.js"></script>`
   有defer，加载后续文档元素和js脚本是并行进行的（异步），但是script.js的执行要等到所有元素解析完成之后，DOMContentLoaded事件触发之前完成。
   ![js脚本加载解析图](http://upload-images.jianshu.io/upload_images/1606281-7f813cc953f15246.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
     从这张图可以看出async和defer在脚本的加载时候都是异步的,但区别在于;
    --- async加载完脚本就会立即执行脚本，会忽略对于脚本加载的顺序声明。在实际应用中使用率极低，最典型的例子就是：Google Analytics；
    --- defer是在异步加载完成之后等待所有的页面元素都加载完成了才开始执行脚本，这个属性的使用率很高，因为比较符合我们对于脚本执行时间的要求。
> 参考文献——[defer 和 async的区别](https://segmentfault.com/q/1010000000640869)
1. 简述网页的渲染机制
   ![浏览器渲染机制](http://upload-images.jianshu.io/upload_images/1606281-50764bd36ee82bff.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
   ![饥人谷图片](http://upload-images.jianshu.io/upload_images/1606281-f261cb62a9c59179.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 第一副图片概括性的介绍了浏览器从页面内容加载到渲染显示页面的过程，第二副图片介绍的就比较具体了。
- 浏览器的大致渲染过程是：
  - 用户发送访问请求并且经过IP解析给对应的服务器发送请求并且等待服务器的反馈；
  - 当服务器查找到用户的请求数据，然后就会给浏览器发送对应的数据。
  - 浏览器接受数据然后分别根据HTML和CSS构建对应的DOM Tree和CSSOM Tree；
  - 在解析到一个script标签时候会立即解析执行该脚本，并阻塞文档的解析直到脚本执行完成。如果脚本是外引的，则网络必须先请求到这个资源——这个过程也是同步的，阻塞文档解析直到资源被请求到。不过可以给script添加defer属性以使其不阻塞文档的正常解析，并在文档解析完成之后执行。
  - 当DOM Tree构建完成之后就开始构建渲染树，渲染树由元素序列中的可见元素组成，是文档的可视化表示，构建这棵树是为了文档以正确的顺序绘制文档内容；
  - 渲染树和DOM元素是相对应的，但这种关系不是一对一的，不可见的渲染元素不会被插入到DOM树中。
  - 创建渲染树需要计算每个渲染对象的可视属性，可以通过计算每个元素的样式属性得到。样式包括各种来源的样式表。
  - 当渲染树绘制完成之后就会开始绘制阶段，遍历渲染树并调用渲染对象的paint方法将它们的内容显示在屏幕中，此时浏览器的渲染过程就告一段落了。
> 参考文献——[浏览器详谈及其内部工作机制](http://aijuans.iteye.com/blog/1894854)
1. JavaScript定义了几种数据类型？哪些是简单类型，哪些是复杂类型？
- JavaScript定义了6种数据类型；
- 其中有五种原始类型，分别是：Undefined、Null、Number、String、Boolean；
- 字符串（String）、数字（Number）、布尔（Boolean）这三个属于简单类型；
- 数组（Array）、对象（Object）这俩种属于复合数据类型；其中数组包含于对象；
- 空对象（Null）、未定义（Undefined）属于特殊数据类型；
1. NaN、Undefined、Null分别代表什么？
- NaN——是一种特殊的数据类型；它与任何值都不相等，包括自己；
- Undefined——一个未初始化的变量的值、一个没有传入实参的行参变量的值，如果一个函数什么都没有返回，则默认的返回结果是undefined；
- Null——是一种特殊的object（空对象，没有任何属性和方法）；当为变量赋值为Null时候，就会从内存中销毁该变量，包括它占用的空间；
```
var a1;
var a2 = null;
var a3 = undefinde;
var a4 = NaN;
console.log(typeof a1);
 undefined
console.log(typeof a2);
 object
console.log(typeof a3);
VM680:2 undefined
undefined
console.log(typeof a4);
undefined
console.log(typeof a5);
undefined
console.log(typeof NaN);
 number
console.log(typeof undefined);
undefined
```
参考文献——[null、NaN和undefined的区别总结](http://www.jb51.net/article/35404.htm)
1. typeof和instanceof的作用和区别？
- typeof——此运算符可以返回一个字符串，用于说明元素的类型，它的返回值有如下可能：number、Boolean、String、function、object、undefined；
- instanceof——此运算符可以一个变量是否是某个对象的实例，返回值是布尔型的。
```
var st="hello wrold",
    sr=new String("hello world");
undefined
console.log(typeof st)
 string
console.log(typeof sr)
 object
console.log(st instanceof String)
 false
console.log(sr instanceof String);
 true
```
- 一般来说只有使用构造函数创建的对象进行instanceof判断才会返回true，否则返回false，不过数组是个例外，都会返回true；
- 一般来说使用typeof的操作是直接量形式的话能够返回准确的结果，如果是使用构造函数创建的对象则会返回object，不过数组是个例外，无论是否是直接量都会返回‘object’；
> 参考文献——[instanceof和typeof运算符的区别](http://www.jb51.net/article/45247.htm)

### 代码
1. 完成如下代码判断一个变量是否是数字、字符串、布尔、函数
```
function isNumber(e1){
	if(typeof e1 === "number"){
		return true;
	}
}
function isString(e1){
	if(typeof e1 === "string"){
		return true;
	}
}
function isBoolean(e1){
	if(typeof e1 === "boolean"){
		return true;
	}
}
function isFunction(e1){
	if(typeof e1 === "function"){
		return true;
	}
}
var a = 2,
	b = "jirengu",
	c = false;
alert( isNumber(a));
alert(isString(a));
alert(isString(b));
alert( isBoolean(c) );
alert( isFunction(a) );
alert( isFunction( isNumber));
```
1. 以下代码的输出结果是？
```
console.log(1+1) = 2;
console.log("2"+"4") = "24";
console.log(2+"4") = "24";
console.log(+new Date()) = 1457717756319;
console.log(+"4") = 4;
```
1. 一下代码的输出结果是？
   var a = 1;
   a+++a = (a++) + a;
   因为后置递增的优先级高于加法，
   a++ = a = 1;
   a = 1+1 = 2;
   1 + 2 = 3;
   a+++a = 3;
   typeof a+2
   typeof的优先级高于加法，所以
   typeof a+2 = (typeof 2) + 2 = "number" + 2 = "number" + "2" = "number2"; 
2. 遍历数组，把数组里的打印数组每一项的平方；
```
var arr = [3,4,5];
var sum;
for(var i=0;i<arr.length;i++){
  sum+=arr[i]*arr[i]+","; 
}
console.log(sum);
 undefined9,16,25,
```
1. 遍历JSON，打印里面的值；
```
var obj={
	name: "hunger",
	sex: "male",
	age: 28
}
for(var a in obj){	
	console.log(a+": "+obj[a]+"; ");
}
name: hunger; 
sex: male; 
age: 28;
```
 > 对于obj对象，可以创建变量a，然后通过——in——的方式来遍历obj的属性，然后通过——obj[a]——的方式来遍历obj的值；
1. 下面代码的输出是？为什么？
```
console.log(a);  /* 值为 undefined ；因为变量的申明会被前置，所以变量a已经申明，但是赋值的操作不会提前，所以此时a的值为undefined，这个就等价于 console.log(undefined) = undefined; */
var a = 1;  //此时a=1；
console.log(a);  // 等价于console.log(1) = 1;
console.log(b);  //报错！ 因为b是未定义的变量，所以会报错！
```
