---
title: siblings可以接受参数进行进一步的分类
date: 2016-07-07
tags: [jQuery]
categories: Dynamic
---

`siblings`可以接受参数进行进一步的筛选。

`$("tbody tr:first").siblings(".child_row_01")` -- 表示`tr`的兄弟元素中包含`class=child_row_01`的元素。

我自己的分类是

`$("tbody tr[class^=child_row_01]")`; -- 以`child_roe_`开头的class