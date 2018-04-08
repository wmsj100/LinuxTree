---
title: CSS选择器
date: 2016-03-24 12:18:58
tags: [CSS,名词]
categories: Static
---
### CSS选择器常见的有几种？
- !important选择器——它是所有选择器里面权重最高的。
- *选择器——它是所有选择器里面权重最低的。可以为页面所有的标签添加统一样式，多用于页面整体样式调整，但它会增加浏览器的负荷，因为浏览器需要计算出页面所有的标签然后给这些标签添加样式，增加了页面的渲染时间；
  <!-- more -->
- 标签选择器--可以为选择标签设置统一样式，比如设置`p{color:red;}`页面所有的段落颜色都是红色。
- id选择器——为页面单个标签设置属性，因为该属性只能在页面使用一次，所以只用来为重要的语义标签添加id属性。
- class选择器——为页面属性值为class的标签添加样式，因为可以多次反复的引用，所以使用频率很高。`p.user{font-size:18px;}`意思是为class属性值为‘user’的段落标签p设置样式为文本尺寸18px；
- 属性选择器——通过为标签附加属性值来缩写选择范围，`input[type="text"]{color:blue;}`意思是为属性值type为text的input标签设置文本颜色为蓝色；
- 组合选择器——通过父标签来选择后代标签元素为其添加样式`p span{color:purple;}`意思是选择p标签的所有span子元素并且为其设置颜色为purple。
- 伪类选择器——通过伪类设置选择范围，这种选择对于页面的变动性适应更好。
  div p:first-of-type——选择div的所以子元素p中的第一个p；
  div p:first-child——查找div的第一个子元素是否是p，如果是则匹配成功并为其添加样式，如果匹配不成功，则不起作用。
  常见的这类属性：first-of-type;last-of-type;first-child;last-child;nth-of-type(n);nth-child(n);

### 选择器的优先级是怎样的？
选择器的优先级可以归纳为以下三条规则：
- 规则一、ID选择器的权重大于Class选择器，Class选择器的权重大于Element（元素）选择器；比如下面代码：
```
#div1 li{
            color:blue;
            }
.content .list li{
             color:red;
            }
```
- 规则二、选择器的权重不区分加载先后顺序，如果是同级的权重，则后加载的样式覆盖先加载的；比如下面代码：
```
#div1{
		color:red;
	}
	.content{
		color:blue;
	}
```
虽然.content后加载，但是ID的权重高于Class。
- 规则三、继承的样式低于设置的样式；比如下面代码：
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
虽然ID的权重高于Element的权重，但是ID是继承的样式，而Element（span）是设置的样式。
> 此外！important的优先级是最高的，*的优先级是最低的。

### class和id的使用场景？
> 其实class和id的使用场景在规则中并没有给出规范，只是日常人们总结出来一些经验。

- id适合于页面板块切分时候的命名，因为页面板块的名称在页面中是独一无二的，是权重最高的。
- class适合于页面板块内部细节性的样式名命名，因为一个板块的样式可能是统一的，使用class可以很方便的重复使用。

### 使用class选择器时候为什么要划定适当的命名空间？
因为单纯的class选择器的范围太广泛，影响的标签太多，如果没有指定更具体的使用范围，引用时候就会出现很多意想不到的错误，比如本想修改div的字体大小，结果p因为样式需要引用的class也被修改了样式，如果是指定了这次修改是针对div的修改 `div .style{font-size:16px;}`这样p的文本就不会被影响力。而且在团队协作时候，这种操作就越发的重要了。
```
	/* 选择class属性值为header的标签 */
	.header{

	}
	/* 选择class属性值为header的后代元素中class为logo的标签 */
	.header .logo{

	}
	/* 选择同时具备class值为header和mobile的标签 */
	.header.mobile{

	}
	/* 同时选择class值为header的后代p标签和class值为header的后代h3标签 */
	.header p,.header h3{

	}
	/* 选择id值为header的后代元素中class值为nav的子元素li标签 */
	#header .nav>li{

	}
	/* 选择id值为header的后代元素a的hover状态 */
	#header a:hover{

	}
```

### 列出你所知道的伪类选择器？
- ：hover——鼠标悬停元素时候的样式；
- ：active——鼠标点击元素时候的样式；
- ：link——元素的常态样式；
- ：actived——元素被点击过后的样式；
- ：first-of-type——所选标签元素中的第一个使用样式；
- ：nth-of-type（n）——所选标签元素中的第n个使用样式；
- ：nth-child（n）——所选标签的父元素的第n个子元素使用样式；
- ：last-of-type——所选标签元素中的最后一个使用样式；
- ：first-child——所选标签元素的父元素的第一个子元素使用样式；
- ：last-child——所选标签元素的父元素的最后一个子元素使用样式；
- focus——当元素获取焦点时候使用样式；

### first-of-type和first-child的作用和区别？
俩者都可以选择标签，区别在于first-of-type表示所选标签的全部元素中的第一个，而first-child表示所选标签的父元素中所有子元素的第一个元素；

### text-align：center的作用是什么，作用在什么元素上？能让是什么元素水平居中？
- text-align：center的作用是让行内元素水平居中；
- 作用在块级元素上；
- 能让块级元素的子元素中的行内元素水平居中；

### 如果遇到一个属性想知道兼容性，在哪里查看？
可以在网站[caniuse](http://caniuse.com/)查询。

---
一、写一个 btn 的class， 任何 a，span,div,button 添加此class后后变成如下按钮的样式(鼠标hover背景色#c14d21, 鼠标按下背景色#e25f31)。[task 8-1](http://book.jirengu.com/jirengu-inc/jrg-tehui2/homework/%E7%8E%8B%E6%B5%A9/%E4%BB%BB%E5%8A%A1-8/task 8-1.html)
![task 8-1](http://upload-images.jianshu.io/upload_images/1606281-a051bf4526a7fef0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
二、根据所写的html，实现如下页面；[task 8-2](http://book.jirengu.com/jirengu-inc/jrg-tehui2/homework/%E7%8E%8B%E6%B5%A9/%E4%BB%BB%E5%8A%A1-8/task 8-2.html)

![task 8-2](http://upload-images.jianshu.io/upload_images/1606281-a5aec8db82c9f85a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
