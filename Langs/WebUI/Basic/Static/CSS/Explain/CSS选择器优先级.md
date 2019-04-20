---
title: CSS选择器优先级
date: 2016-03-24 12:18:58
tags: [CSS]
categories: Static
---
### 特指度
特指度表示一个css表达式的重要程度，可以通过一个公式来计算出一个数值，数值越大，越重要。
>这个计算叫做“I-C-E”计算公式
<!-- more -->
1. I——Id；
2. C——class；
3. E——Element；
即针对一个css选择器表达式，遇到一个id就往特指度数值中加100，遇到一个class就往特指度数值中加10，遇到一个element就往特指度数值中加1。下面举几个css表达式的特指度计算结果：

CSS选择器表达式 | 特指度计算结果
 :------- | :------
p | 1
p.large | 1+10=11
p#large | 1+100=101
div p#large | 1+1+100=102
div p#large ul.list | 1+1+100+1+10=113
div p#large ul.list li | 1+1+100+1+10+1=114

还有一个重点要注意：`!important优先级最高`，高于一切。`*选择器最低`，低于一切。
好了，现在可以回到文章一开始提到的特指度的计算公式了，那个计算结果大，浏览器就会以那个为优先。

### 简版规则
如果你嫌上面的规则复杂，有一个简版规则，它只有3个规则，而且这三个规则比较好记，可以覆盖大多数场景。
- 规则一、包含ID的选择器胜过包含Class的选择器，包含Class的选择器胜过包含Element的选择器；下面第一个特指度更高。
```
#div1 li{
            color:blue;
            }
.content .list li{
             color:red;
            }
```
- 规则二、不同选择器的特指度比较是，不区分加载顺序（相同选择器在层叠时，后加载的覆盖前加载的），例如下面代码，虽然后加载，但是特指度低；
```
#div1{
		color:red;
	}
	.content{
		color:blue;
	}
```
- 规则三、设置的样式高于继承的样式，不用考虑特指度。
```
#div1{
		color:red;
	}
	span{
		color:blue;
	}
<div id="div1">
    	<span>span1</span>
    </div>
```
> 文章参考文献[王福朋的博客](http://www.cnblogs.com/wangfupeng1988/p/4285251.html)
