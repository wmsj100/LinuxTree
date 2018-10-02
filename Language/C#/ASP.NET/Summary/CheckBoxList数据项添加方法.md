---
title: CheckBoxList数据项添加方法
date: 2016-08-24
tags: [.NET]
categories: Language
---

对于`CheckBoxList`的内容项目可以通过编程进行添加，这个添加过程可以添加在`init`初始化过程中。

```aspx
<asp:CheckBoxList ID="cblGener" AutoPostBack="true" CellPadding="5" CellSpacing="10" RepeatColumns="3" OnInit="cblGener_Init" runat="server">
    <asp:ListItem Value="1" Text="text1" />
    <asp:ListItem Text="text2" />
    <asp:ListItem Text="text3" Value="3" />
</asp:CheckBoxList>
```

```cs
protected void cblGener_Init(object sender, EventArgs e)
    {
        string[] gener = {"one", "two", "three", "four"};
        for (int i = 0; i < gener.Length; i++)
        {
            cblGener.Items.Add(new ListItem(gener[i]));
        }
    }
```

对于列表，如果缺少`value`则显示`text`的值，如果缺少`text`则显示`value`，对于缺少`value`值的情况，从服务器把动态页面转换为静态页面发送给客户端之后，会自动补充很多信息，比如项目会有`id`值，而且默认的`value`和`text`值相同。

上面是通过先定义一个数组，然后通过`for`遍历数组，但是还有更高效的方法，就是从数据库获取数据，其方法如下，其他代码都一样，区别在于不用`for`

```cs
protected void cblGener_Init(object sender, EventArgs e)
    {
        string[] gener = {"one", "two", "three", "four"};
        cblGener.DataSource = gener;    // 指定数据源
        cblGener.DataBind();    // 绑定数据
    }
```

