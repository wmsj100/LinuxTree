---
title: splice方法操作数组
date: 2016-06-18
tags: [Array]
categories: Dynamic
---

通过`splice`可以操作数组，传入俩个参数就是删除数组，传入
- a.splice(1,2) -- 从数组的第二位开始删除俩项；
- a.splice(1,0,2) -- 在数组第二位前面插入一个数字`2`；
- a.splice(1,1,3,4) -- 把数组的第二项替换为`3,4`;

splice会返回删除的数组，如果是添加数组，则返回一个空数组，splice会修改原数组。

