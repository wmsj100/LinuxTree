---
title: defer async 属性
date: 2016-04-28
tags: [异步,JavaScript,DOM]
categories: Dynamic
---

`defer` 标签只能用在引入的外部脚本文件，它表示在页面内容全部加载完成之后再执行脚本，

```javascript
var para = document.querySelector("h1");
para.innerText = "hello world";
```

```javascript
<script src="02.js"></script>
<h1>hahaha</h1>
// hahaha
```

```javascript
<script defer src="02.js"></script>
<h1>hahaha</h1>
//hello world
```

在这个例子中，虽然我们把 <script> 元素放在了文档的 <head> 元素中，但其中包含的脚本将延迟到浏览器遇到 </html> 标签后再执行。HTML5 规范要求脚本按照它们出现的先后顺序执行，因此第一
个延迟脚本会先于第二个延迟脚本执行，而这两个脚本会先于 DOMContentLoaded 事件（详见第 13 章）执行。在现实当中，延迟脚本并不一定会按照顺序执行，也不一定会DOMContentLoaded 事件触发前执行，因此最好只包含一个延迟脚本。

1. HTML5 为 <script> 元素定义了 async 属性。这个属性与 defer 属性类似，都用于改变处理脚本的行为。同样与 defer 类似， async 只适用于外部脚本文件，并告诉浏览器立即下载文件。但与 defer不同的是，标记为 async 的脚本并不保证按照指定它们的先后顺序执行。例如：

   <!DOCTYPE html>
   <html>
   <head>
   <title>Example HTML Page</title>
   <script type="text/javascript" async src="example1.js"></script>
   <script type="text/javascript" async src="example2.js"></script>
   </head>
   <body>
   <!-- 这里放内容 -->
   </body>
   </html>
   在以上代码中，第二个脚本文件可能会在第一个脚本文件之前执行。因此，确保两者之间互不依赖非常重要。指定 async 属性的目的是不让页面等待两个脚本下载和执行，从而异步加载页面其他内容。为此，建议异步脚本不要在加载期间修改 DOM。
   异步脚本一定会在页面的 load 事件前执行，但可能会在 DOMContentLoaded 事件触发之前或之后执行。支持异步脚本的浏览器有 Firefox 3.6、Safari 5 和 Chrome。

   ​