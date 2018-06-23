---
title: 关于Checkbox的范例
date: 2016-08-24
tags: [.NET]
categories: Language
---

这个范例效果如下，就是通过勾选多选框，通过`OnCheckedChange`来触发相应的事件。对于事件，首先需要判断多选框是否被选择，这个判断是通过`id.Checked`，返回布尔值。

```aspx
<asp:Label ID="lblTime" OnInit="lblTime_Init" runat="server" /><br />
<br />

<asp:CheckBox Text="Underline" ID="chkUnderLine" AutoPostBack="true" TextAlign="Left" OnCheckedChanged="chkUnderLine_CheckedChange" runat="server" />
<asp:CheckBox Text="Overline" ID="chkOverLine" AutoPostBack="true" OnCheckedChanged="chkOverLine_CheckedChange" runat="server" />
<asp:CheckBox Text="Strikeout" ID="chkStrikeout" AutoPostBack="true" OnCheckedChanged="chkStrikeout_CheckedChange" runat="server" />
```

```cs
protected void lblTime_Init(object sender, EventArgs e)
    {
        lblTime.Font.Name = "MS";
        lblTime.Font.Size = 20;
        lblTime.Font.Bold = true;
        lblTime.Font.Italic = true;
        lblTime.Text = DateTime.Now.ToString();
    }

protected void chkUnderLine_CheckedChange(object sender, EventArgs e)
{
    if (chkUnderLine.Checked)
    {
        lblTime.Font.Underline = true;
    }
    else
    {
        lblTime.Font.Underline = false;
    }
}

protected void chkOverLine_CheckedChange(object sender, EventArgs e)
{
    if (chkOverLine.Checked)
    {
        lblTime.Font.Overline = true;
    }
    else
    {
        lblTime.Font.Overline = false;
    }
}

protected void chkStrikeout_CheckedChange(object sender, EventArgs e)
{
    if (chkStrikeout.Checked)
    {
        lblTime.Font.Strikeout = true;
    }
    else
    {
        lblTime.Font.Strikeout = false;
    }
}
```

