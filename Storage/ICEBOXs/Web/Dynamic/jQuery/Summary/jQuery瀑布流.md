---
title: jQuery瀑布流
date: 2016-04-25
tags: [jQuery,瀑布流]
categories: Dynamic
---

1. 瀑布流布局的原理是什么
   - 计算元素的宽度`itemWidth`和父元素宽度，计算出一行排列的元素个数`count`；
   - 添加一个空数组`array`，数组长度为`count`，数组内部每个值初始值为零；
   - 使用`each`方式遍历要添加的元素，在`each`函数内部对数组`array`进行`for`循环；
   - 遍历数组`array`,`找到最小值`value`的最小下标`index`；
   - 通过绝对定位的方式把元素添加到页面，其中`top = value left = index*itemWidth`

[task 30](http://www.erheizi.com/jirengu/task 30/) 

[index.html](https://github.com/wmsj100/GrowUp/blob/gh-pages/html/jirengu/task30/index.html) 

[get.php](https://github.com/wmsj100/GrowUp/blob/gh-pages/html/jirengu/task30/get.php)