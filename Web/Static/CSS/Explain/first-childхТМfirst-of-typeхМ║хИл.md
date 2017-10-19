---
title: first-child和first-of-type区别
date: 2016-03-24 12:18:58
tags: [CSS]
categories: Static
---
- first-child是CSS2中定义的选择器，从字面意思也可以理解，就是第一个子元素。不如有段代码：
<!-- more -->
```
<div>
    	<p>第一个子元素</p>
    	<h1>第二个子元素</h1>
    	<span>第三个子元素</span>
    	<span>第四个子元素</span>
</div>
```
p:first-child 匹配到的是p元素，因为p元素是div的第一个子元素；
h1:first-child 匹配不到任何元素，因为在这里h1是div的第二个子元素，而不是第一个；
span:first-child 匹配不到任何元素，因为span和h1一样，都不是div的第一个子元素；
- first-of-type：是CSS3中定义的，这个和first-child有什么区别呢？还是这段代码：
```
<div>
    	<p>第一个子元素</p>
    	<h1>第二个子元素</h1>
    	<span>第三个子元素</span>
    	<span>第四个子元素</span>
</div>
```
p:first-of-type：匹配到的是p元素，因为p是div所以类型为p的子元素中的第一个；
h1:first-of-type：匹配到的是h1元素，因为h1是div所以类型为h1的子元素中的第一个；
span:first-of-type：匹配到的是第一个span元素，这里div有俩个span子元素，匹配到第一个；
---
- 所以，通过以上俩个例子可以得出结论：
：first-child：匹配的是某父元素的第一个子元素，可以说是结构上的第一个子元素。
：first-of-type：匹配的是某父元素相同类型子元素中的第一个，比如span：first-of-type，就是所以类型为span的子元素中的第一个。这里不再限制是第一个子元素了，只要是该类型元素的第一个就行了。

> 同样类型的选择器还有：last-child 和 last-of-type；nth-child（n）和：nth-of-type（n）也可以这样去理解。参考文献--[无双博客](http://www.cnblogs.com/2050/p/3569509.html)
