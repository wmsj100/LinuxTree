---
title: RadioButtonList对象
date: 2016-08-26
tags: [ASP, .NET, c#]
categories: Language
---

它和`CheckBoxList`基本相同，只是它只能选中一个项，当然了也可以通过改变勾选的按钮来触发`SelectedIndexChanged`事件。

这个控件有俩个专有的属性：
- `SelectedIndex` -- 列表的所有选定项中最小的索引，如果为`-1`表示没有选中任何项
- `SelectedItem` -- 具有最低索引的选定项。

可以通过`rblSize.SelectedItem.Value`来获取最低索引的选定项的值，但这个值是以字符串的形式呈现的。

```aspx
<asp:Label ID="lblTime" OnInit="lblTime_Init" runat="server" />
<asp:RadioButtonList ID="rblSize" CellPadding="5" CellSpacing="10" RepeatDirection="Horizontal" RepeatLayout="Table" AutoPostBack="true" OnSelectedIndexChanged="rblSize_Change" runat="server">
    <asp:ListItem Text="10px" Value="10" />
    <asp:ListItem Text="20px" Value="20" Selected="True" />
    <asp:ListItem Text="30px" Value="30" />
</asp:RadioButtonList>
```

```cs
protected void lblTime_Init(object sender, EventArgs e)
    {
        lblTime.Font.Name = "MS";
        lblTime.Font.Size = 20;
        lblTime.Font.Italic = true;
        lblTime.Font.Bold = true;
        lblTime.Text = DateTime.Now.ToString();
    }

    protected void rblSize_Change(object sender, EventArgs e)
    {
        int size = 0;
        if (rblSize.SelectedIndex != -1)
        {
            size = Convert.ToInt32(rblSize.SelectedItem.Value);
        }
        else
        {
            size = 10;
        }
        lblTime.Font.Size = size;
    }
```

