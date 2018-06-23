---
title: OnSelectedIndexChanged事件
date: 2016-08-26
tags: [ASP, .NET, c#]
categories: Language
---

```aspx
<asp:CheckBoxList ID="cblGener" AutoPostBack="true" CellPadding="5" CellSpacing="10" RepeatDirection="Horizontal" RepeatColumns="3" OnInit="cblGener_Init" OnSelectedIndexChanged="cblGener_Change" runat="server">
<asp:ListItem Value="1" Text="text1" />
<asp:ListItem Value="text2" />
<asp:ListItem Text="text3" Value="3" />
</asp:CheckBoxList>
<asp:Label Text="text" ID="lblGener" runat="server" />
```

```cs
protected void cblGener_Init(object sender, EventArgs e)
    {
        string[] gener = {"one", "two", "three", "four"};
        cblGener.DataSource = gener;
        cblGener.DataBind();
    }

    protected void cblGener_Change(object sender, EventArgs e)
    {
        String sb = "";
        foreach (ListItem li in cblGener.Items)
        {
            if (li.Selected == true)
            {
                sb += "<br/>" + li.Text + "-" + li.Value;
            }
        }
        if (sb.Length == 0)
        {
            lblGener.Text = "Empty";
        }
        else
        {
            lblGener.Text = sb;
        }
    }
```

像上面这种字符串的拼接操作是非常费时且低效的事情，因为它每次修改时创建新的字符串，并注销旧的字符串。