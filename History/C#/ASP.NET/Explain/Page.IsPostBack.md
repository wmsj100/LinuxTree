---
title: Page.IsPostBack
date: 2016-08-19
tags: [ASP, .NET, c#]
categories: Language
---

它是一个布尔值，当该值为真时，则页面为回传，否则就是首次加载。

```c#
if(!Page.IsPostBack)
{
    txtLoginId.Text = "请输入用户名";
    txtLoginPwd.Text = "请输入密码";
}
```

