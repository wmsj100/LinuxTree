---
title: Page对象
date: 2016-08-19
tags: [ASP, .NET, c#]
categories: Language
---

## page对象

常用的`page`属性和方法如下：
- `IsPostBack` -- 判断是否首次加载
- `Controls` -- 服务器控件集合
- `Request` -- 客户端在`web`请求期间发送的`HTTP`值
- `Response` -- 来自`.NET`操作的`HTTP`响应信息
- `IsValid` -- 页面验证是否成功
- `DataBinding` -- 当服务器绑定到数据源时发生
- `Disposed` -- 当从内存中释放服务器控件时发生，
- `Error` -- 当引发未处理的异常时发生

创建一个`ASP.NET`页面其实就是创建一个`System.Web.UI.Page`类的一个实例。`Page`类成员驻留在`System.web.UI`命名空间中，它提供给了`ASP.NET`页面许多有效的属性和方法。

每个页面都派生自`Page`类，并继承这个类所有公开的属性和方法，

`Page`对象充当页面中所有服务器控件命名容器，

`Page`类与`.aspx`页面相关联，这些文件在运行时被编译为`Page`对象。