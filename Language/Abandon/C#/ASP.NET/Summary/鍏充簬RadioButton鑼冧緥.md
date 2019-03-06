---
title: 关于RadioButton范例
date: 2016-08-24
tags: [ASP.NET]
categories: Language
---

这个效果还是基于`Checkbox`进行的，但是区别在于，在初始化过程中就触发方法。具体代码如下：

```aspx
<asp:Label ID="lblTime" OnInit="lblTime_Init" runat="server" /><br />
<br />

<asp:CheckBox Text="Underline" Checked="true" ID="chkUnderLine" AutoPostBack="true" TextAlign="Left" OnCheckedChanged="chkUnderLine_CheckedChange" runat="server" />
<asp:CheckBox Text="Overline" Checked="false" ID="chkOverLine" AutoPostBack="true" OnCheckedChanged="chkOverLine_CheckedChange" runat="server" />
<asp:CheckBox Text="Strikeout" ID="chkStrikeout" AutoPostBack="true" OnCheckedChanged="chkStrikeout_CheckedChange" runat="server" />
<asp:RadioButton Text="22px" ID="Radio_22" OnCheckedChanged="grpSize_CheckedChange" GroupName="grpSize" AutoPostBack="true" runat="server" />
<asp:RadioButton Text="32px" ID="Radio_32" OnCheckedChanged="grpSize_CheckedChange" GroupName="grpSize" AutoPostBack="true" runat="server" />
<asp:RadioButton Text="12px" ID="Radio_12" Checked="true" OnCheckedChanged="grpSize_CheckedChange" GroupName="grpSize" AutoPostBack="true" runat="server" />
```

```cs
protected void lblTime_Init(object sender, EventArgs e)
    {
        lblTime.Font.Name = "MS";
        lblTime.Font.Size = 20;
        lblTime.Font.Bold = true;
        lblTime.Font.Italic = true;
        lblTime.Text = DateTime.Now.ToString();
        this.chkUnderLine_CheckedChange(chkUnderLine, e);
        this.chkOverLine_CheckedChange(chkOverLine, e);
        this.chkStrikeout_CheckedChange(chkStrikeout, e);
        this.grpSize_CheckedChange(Radio_22, e);
        this.grpSize_CheckedChange(Radio_12, e);
        this.grpSize_CheckedChange(Radio_32, e);
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

protected void grpSize_CheckedChange(object sender, EventArgs e)
{
    if (Radio_12.Checked)
    {
        lblTime.Font.Size = 12;
    }
    else if (Radio_22.Checked)
    {
        lblTime.Font.Size = 22;
    }
    else
    {
        lblTime.Font.Size = 32;
    }
}
```