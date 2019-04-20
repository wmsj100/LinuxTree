---
title: 关于HiddenField的范例
date: 2016-08-24
tags: [ASP.NET]
categories: Language
---

这个页面的效果就是，在输入框中输入一个 值，然后把这个值保存到`hiddenfiled`控件中，然后通过一个`asp`的按钮来回传服务器，但是这个按钮没有绑定事件，只是为了回传服务器，然后将`hidden`隐藏的值显示在`label`控件中，具体如下：

```aspx
<asp:HiddenField ID="hdnVal" runat="server" OnValueChanged="ValueChange" /> 
<asp:TextBox runat="server" ID="input" />
<input type="button" name="name" value="ChangeValue" onclick="change()" />
<asp:Button Text="post" runat="server" />
<asp:Label Text="" ID="message" runat="server" />
<script>
    function change() {
        var hdn = document.getElementById("hdnVal");
        var userInfo = document.getElementById("input");
        hdn.value = userInfo.value;
    }
</script>
```

```cs
protected void ValueChange(object sender, EventArgs e)
    {
        HiddenField hdn = (HiddenField)sender;
        message.Text = hdn.Value;
    }
```

