---
title: MultiView和View控件
date: 2016-09-08
tags: [ASP, .NET, c#]
categories: Language
---

块是页面中某区域的内容，`ASP.NET`提供了`View`控件对块进行管理。每个块对应一个`View`控件。所有的`View`对象包含在`MultiView`对象中。`MultiView`中每次只显示一个`View`对象。这个对象称为活动视图。

- `ActiveViewIndex` -- 该属性可以获取或设置以`0`开始的当前活动视图的索引，如果没有视图是活动的，则值为`-1`。

- `MultiView`控件的4个`CommandName`字段，为按钮的`CommandName`属性赋值，能够实现视图的导航

- `NextViewCommandName` -- `NextView` 导航到下一个视图，如果是最后一个视图，则不做处理
- `PreviousViewVommandName` -- `PrevView` 导航到上一个视图
- `SwitchViewByIDCommandName` -- 导航到指定视图
- `SwitchViewByIndexCommandName` -- 导航到指定索引的视图

例如，将`Button, ImageButton或LinkButton`控件的`CommandName`属性设置为`NextView`,单击这些按钮后将自动导航到下一个视图，而不需要额外的代码。

- `SetActiveView` 设置活动视图
- `GetActiveView` 获取活动视图

每次视图发生变化时，页面都会被提交到服务器，同时`MultiView`控件和`View`控件将触发多个事件。

活动视图发生变化时，`MultiView`控件将触发`ActiveViewChanged`事件，于此同时，新的活动视图将触发`Activate`事件，原活动视图则触发`Deactiveat`事件。

所有的事件都包含一个`EventArgs`类型的参数，该参数只是一个占位符，它没有提供与事件相关的附加信息。然而，与所有的事件处理程序一样，对事件源的引用将传递给事件处理程序。