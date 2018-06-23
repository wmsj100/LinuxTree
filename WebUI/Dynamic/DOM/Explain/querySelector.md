---
title: querySelector
date: 2016-4-1 16:26:02
tags: [知识,事件,DOM]
categories: Dynamic
---

`<span class="wrap" id="name" name="hello">hello world</span>`
<!-- more -->
```javascript
document.querySelector(".wrap")	
//选中第一个class="wrap"元素
document.querySelectorAll(".wrap")	
//选中全部class="wrap"元素
document.querySelector("#name")	
//选择第一个id="name"的元素
document.querySelectorALL("#name")	
//选择全部id="name"的元素
document.querySelector("span")	
//选择第一个span元素
document.querySelectorAll("span")	
//选择全部span元素
```

