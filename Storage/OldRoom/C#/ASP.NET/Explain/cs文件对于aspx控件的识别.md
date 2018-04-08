---
title: cs文件对于aspx控件的识别
date: 2016-08-18
tags: [ASP, .NET, c#]
categories: Language
---

在`.aspx`文件添加控件时候，比如添加了一个输入框控件，如果此时要获取用户的输入并通过控件后面的按钮`button`控件来提交，
那么问题来了，后置文件`.cs`文件如何识别并获取输入框的内容，这个时候需要在添加控件时候并且添加`ID`属性，`.cs`文件可以通过控件的`ID`属性来获取控件。整个代码如下：

`.aspx`文件
```c#
<asp:button ID="click" runat="server" text="Click Me" OnClick="Unnamed1_Click" />
<asp:TextBox ID="input1" runat="server" Text="input word" OnTextChanged="Unnamed2_TextChanged"></asp:TextBox>
```

`.cs`文件
```c#
protected void Unnamed1_Click(object sender, EventArgs e)
        {
            string input = input1.Text;
            Response.Write(input);
        }
```