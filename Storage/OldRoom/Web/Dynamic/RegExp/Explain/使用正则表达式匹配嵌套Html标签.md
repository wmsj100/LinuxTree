---
title: 使用正则表达式匹配嵌套Html标签
date: 2016-3-30 22:54:08
tags: [正则,JavaScript]
categories: Dynamic
---

## 概述

正则表达式是做文本解析工作必不可少的技能。如Web服务器日志分析，网页前端开发等。很多高级文本编辑器都支持正则表达式的一个子集，熟练掌握正则表达式，经常能够使你的一些工作事半功倍。例如[统计代码行数](http://www.54kevinyang.cn/2009/05/visual-studio%e7%bb%9f%e8%ae%a1%e6%9c%89%e6%95%88%e4%bb%a3%e7%a0%81%e8%a1%8c%e6%95%b0.html)，只需一个正则就搞定。嵌套Html标签的匹配是正则表达式应用中一个比较难的话题，因为它涉及到的正则语法比较多，也比较难。因此也就更有研究的价值。
<!-- more -->
## 思路

任何复杂的正则表达式都是由简单的子表达式组成的，要想写出复杂的正则来，一方面需要有化繁为简的功底，另外一方面，我们需要从正则引擎的角度去思考问题。关于正则引擎的原理，推荐《Mastering Regular Expression》中文名叫《精通正则表达式》。挺不错的一本书。

OK，先确定我们要解决的问题——**从一段Html文本中找出特定id的标签的innerHTML**。

这里面最大的难点就是，Html标签是支持嵌套的，怎么能够找到指定标签相对应的闭合标签呢？

我们可以这样想，**先匹配最前面的起始标签，假设是div吧（。

我之所以能够这样去思考，是因为我了解过正则的特性，我知道正则中的平衡组能够实现我刚才说的“堆栈”操作。所以，如果我们要编写复杂正则表达式，需要对正则的一些高级特性至少有所了解，这样我们思考问题才有个方向。

## 实现

这里假设我们要匹配的文本是一段合法的Html文本。下面这段Html代码是从我的博客上拷贝下来的，作为我们的测试文本。我们要匹配的就是footer这个div的innerHTML，同时把标签名也捕获下来。

```
<div style="background-color:gray;" id="footer">
    <a id="gotop" href="#" onclick="MGJS.goTop();return false;">Top</a>
    <a id="powered" href="http://wordpress.org/">WordPress</a>
    <div id="copyright">
        Copyright &copy; 2009 简单生活 —— Kevin Yang的博客 
    </div>
    <div id="themeinfo">
        Theme by <a href="http://www.neoease.com/">mg12</a>. Valid <a href="http://validator.w3.org/check?uri=referer">XHTML 1.1</a>
        and <a href="http://jigsaw.w3.org/css-validator/">CSS 3</a>. 
    </div>
</div>

```

这里我们需要借助[Expresso](http://www.54kevinyang.cn/2009/07/%e3%80%90%e6%8e%a8%e8%8d%90%e3%80%91%e4%bd%bf%e7%94%a8ultrapico-expresso%e5%ad%a6%e4%b9%a0%e6%ad%a3%e5%88%99%e8%a1%a8%e8%be%be%e5%bc%8f.html)工具来构建和测试编写的正则表达式。

## 匹配起始标签

起始标签特征很好提取，以尖括号打头，然后跟着一连串英文字母，然后一大串属性中（非尖括号字符）匹配id（不区分大小写）=footer。需要注意的是，footer可以被双引号或者单引号包裹，也可以什么都不加。正则如下：

```
<(?<HtmlTag>[\w]+)[^>]*\s[iI][dD]=(?<Quote>["']?)footer(?(Quote)\k<Quote>)["']?[^>]*>

```

上面的正则表达式需要做几点说明：

\1. <尖括号在正则中算是一个特殊字符，在显式捕获分组中用它将分组名括起来。但是因为开头的尖括号在此上下文下并不会出现解析歧义，因此加不加转义符效果是一样的。

\2. (?<GroupName>RegEx)格式定义一个命名分组，我们在上面定义了一个HtmlTag的标签分组，用来存放匹配到的Html标签名。Quote分组是用来给后面的匹配使用的。

\3. (?(GroupName)Then|Else)是条件语句，表示当捕获到GroupName分组时执行Then匹配，否则执行Else匹配。上面的正则中，我们先尝试匹配footer字符串左边的引号，并将其存入LeftQuote分组中，然后在footer右侧进行条件解析，如果之前匹配到LeftQuote分组，那么右侧也应该批评LeftQuote分组。这样一来，我们就能精确匹配id的各种情况了。

## 匹配闭合标签

```
((?<Nested><\k<HtmlTag>[^>]*>)|</\k<HtmlTag>>(?<-Nested>)|.*?)*</\k<HtmlTag>>

```

在成功匹配到起始标签之后，后面的Html文本可以分为三种情况：

A. 匹配到嵌套div起始标签<div，这个时候，需要将其捕获到Nested分组。

B. 匹配到嵌套div起始标签的闭合标签，这个时候，需要将之前的Nested分组释放

C. 其他任意文本。注意，需要使用.*?方式关闭贪婪匹配，否则最后的闭合标签可能会过度匹配

使用(RegEx1|RegEx2|RegEx3)*这种方式，可以将几个条件以或的形式组合起来，然后再取若干次匹配结果，最终再匹配闭合标签。其中(?<-Nested>)是表示释放之前捕获的Nested分组。确切的语法是(?<N-M>)即使用N分组替换掉M分组，如果N分组没有指定或不存在，则释放M分组。

