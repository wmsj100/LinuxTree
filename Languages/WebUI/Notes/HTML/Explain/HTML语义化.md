---
title: HTML语义化
date: 2016-03-24 12:18:58
tags: [HTML]
categories: Static
---
### 什么是HTML语义化？
- 基本上都是围绕几个重要的标签，像标题（H1～H6）、列表（li）、强调（strong、em）……
<!-- more -->
- 根据内容的结构化（内容语义化），选择合适的标签（代码语义化）便于开发者阅读和写出更优雅的代码的同时让浏览器的爬虫和机器更好的解析。
### 为什么要语义化？
- 为了在没有CSS的情况下，页面也能呈现出很好的内容结构、代码结构，为了更好看；
- 用户体验：例如title、alt用于解释名词和解释图片信息、label标签的活用；
- 有利于SEO：和搜索引擎建立良好的沟通，有助于爬虫抓取更多的有效信息，爬虫依赖于标签来确定上下文和各个关键字的权重；
- 方便其他设备解析（如屏幕阅读器、盲人阅读器、移动设备）以有意义的方式来渲染页面；
- 便于团队开发和维护，语义化更具可读性，是下一步网页发展的重要动向，遵循W3C标准的团队都遵循这个标准，可以坚持差异化。
### 写HTML代码是应注意什么？
- 尽可能少的使用无语义的标签div和span；
- 在语义不明显是，既可以使用div或者p是，尽量用p，因为p在默认情况下有默认间距，对兼容特殊终端有利；
- 不要使用纯样式标签，如：b、font、u等，改用CSS设置
- 需要强调的文本，可以包含在strong或者em标签中（浏览器预设样式，能用CSS指定就不用他们），strong默认样式是加粗（不要用b），em是斜体（不用i）；
- 使用表格时，标题要用caption，表头用thead，主体部分用tbody包围，尾部用tfoot包围，表头和一般单元格要区分开，表头用th，单元格用td；
- 表单域要用fieldset标签包起来，并用legend标签说明表单的用途；
- 每个input标签对应的说明文本都需要使用label标签，并且通过input设置id属性，在label中设置for=someid来让说明文本和相对应的input关联起来。
> 参考文献[freeyiyi1993](http://www.cnblogs.com/freeyiyi1993/p/3615179.html)
