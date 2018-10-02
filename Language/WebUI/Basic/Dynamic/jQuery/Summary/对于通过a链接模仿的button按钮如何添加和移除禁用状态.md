---
title: 对于通过a链接模仿的button按钮如何添加和移除禁用状态
date: 2016-07-18
tags: [jQuery,Summary]
categories: Dynamic
---

我使用`a`链接创建了按钮，但是现在想要禁用按钮，阻止事件的冒泡，如何切换这个状态。

不需要切换状态，只需要通过`if`条件进行判断，如果点击的目标`pagedata`和当前的激活`pagedata`相同，则不做处理，返回`return null`