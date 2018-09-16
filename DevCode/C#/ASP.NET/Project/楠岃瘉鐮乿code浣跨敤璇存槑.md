---
title: 验证码vcode使用说明
date: 2016-08-25
tags: [ASP, .NET, c#, Projct]
categories: Language
---

```aspx
<p style="position: relative;">
    <input name="vcode" id="login_yzm" runat="server" class="bg_login_txt" type="text" placeholder="验证码" autocomplete="off" />
    <img src="/ashx/vcode.ashx?id=1" title="看不清,换一个" style="cursor: pointer; cursor: pointer; position: absolute; right: 81px; top: 7px; width: 92px;"
        onclick="this.src=this.src+1" />
</p>
```

```cs
protected void ImageButton1_Click(object sender, ImageClickEventArgs e)
    {
        string UserName = txt_UserName.Text.Trim();
        string BackPsWd = txt_BackPsWd.Text.Trim();
        string yzm = login_yzm.Value.Trim().ToLower();    // 获取输入的验证码字符并且去掉首位空格且转换为小写
        string num = Session["ValidateCode"].ToString().ToLower();  // 获取存储在Session中的验证码字符
        int len = yzm.Length;   // 获取验证码字符长度
        if (UserName != "")
        {
            if (BackPsWd != "")
            {
                // 先判断不为空，然后判断长度为4，最后判断是否匹配
                if (yzm != "" && len == 4 && num == yzm)
                {
                    string MD5Pwd = CommonTools.EncryptByMD5(BackPsWd);
                    login_SJ(UserName, MD5Pwd);
                }
                else
                {
                    CommonTools.showMessage("请正确输入验证码！");
                    return;
                }
            }
            else
            {
                CommonTools.showMessage("请输入密码！");
                return;
            }
        }
        else
        {
            CommonTools.showMessage("请输入用户名！");
            return;
        }
    }
```