---
title: ASP.NET基础控件
date: 2016-08-24
tags: [.NET]
categories: Language
---

`init` -- 事件在控件初始化时候被调用，这是每个控件生命周期的第一步。

`DateTime.Now.ToString()` -- 获取当前时间并以字符串输出。

---

## font属性

- `Bold` -- 设置文本为粗体，类型为`Boolean`，默认为`false`；
- `Italic` -- 设置文本为斜体 `false`
- `Name` -- 设置字体的名称，
- `Names` -- 字体数组，
- `Strickeout` -- 设置贯穿字体的横线
- `Underline` -- 设置字体的下划线
- `Overline` -- 设置字体的上划线
- `Size` -- 设置字体的尺寸

---

## Label控件

`Label`控件用于显示文本，`Text`属性包含要显示的文本，

---

## TextBox控件

`TextBox`控件用于用户输入或显示只读文本，可以配置为单行多行或接受密码。

- `AutoPostBack` -- 当用户更改控件的内容时候，是否自动回发到服务器，默认为`false`.
- `Columns` -- 文本框以字符为单位的宽度
- `MaxLength` -- 最多允许的字符数
- `ReadOnly` -- 用户不可以更改它的内容，但可以以编程的方式更改。
- `Rows` -- 多行文本框的行数
- `Text` -- 默认显示的内容
- `TextMode` -- 选择文本框的类型，默认为`SingleLine`,还有`MultiLine`, `Password`.
- `validationGroup` -- 指定一个验证组
- `Wrap` -- 是否允许多行文本框换行，默认为true

它依附的事件有： `Init`, `Load`, `PreRender`，当文本框发生变化且失去焦点时候，`TextBox`会触发`TextChange`事件，除非把`AutoPostBack`设置为`true`，否则不会引起回传。

`TextChange`事件由`ONTextChange`属性指定。

---

## HiddenField控件

当`web`开发者处理页面信息，又不想让用户看到信息时候，隐藏字段是一个常用的技巧。

---

## 按钮控件

将表单提交到服务器，从而激活服务器端进程，有3种按钮：
- `Button` -- 标准按钮，
- `LinkButton` -- 介于标准按钮和`HyperLink`之间的按钮，类似超链接，转换为`HTML`就是超链接。
- `ImageButton` -- 按钮可以被图片替换，和标准按钮完成一样的功能，没有`Text`属性，但是包含`AlternateText`用于图片未能正常显示时显示的文本内容。另外，该控件的事件处理程序使用`ImageClickEventArgs`事件参数，该事件参数公开俩个参数，分别表示用户点击图片的`X`座标和`Y`座标，可以实现地图功能。

- `tooltip` -- 这个属性值是给按钮控件添加`title`值，提示。

```aspx
<asp:Button Text="click" ToolTip="link" OnClick="btnLink_Click" runat="server" />
<asp:ImageButton ImageUrl="./img_btn_storeInfo.png" ToolTip="image button" OnClick="imgLink_Click" runat="server" />
<asp:LinkButton Text="LinkBtn" ToolTip="link btn" OnClick="btnLink_Click" runat="server" />
```

---

## 文件位置

对于文件的引用位置，肯定是使用相对位置，而`ASP.NET`使用应用程序相对位置，使用`~`运算符，指示应用程序根目录。
`"~/img_btn_storeInfo.png"` 表示应用程序的根目录下面的图片。

---

## HyperLink控件

类似`LinkButton`,但是有本质区别，`HyperLink`不进行回发，而直接导航到目标`URL`，而`LinkButton`则提交表单。它有四个属性，如下：

- `ImageUrl` -- 这个和`ImageButton`极为类似，区别在于这个仅仅是导航，不提交表单。
- `NavigateUrl` -- 要链接到的目标URL。
- `Text` -- 显示在浏览器中的链接文本，如果同时设置了`Text`和`ImageUrl`，则优先使用图片，文本只在图片无效时候显示。
- `Target` -- 打开链接的方式

`<asp:HyperLink NavigateUrl="navigateurl" Text="hello" Target="_blank" ToolTip="just link" ForeColor="Yellow" Font-Names="MS" Font-Size="20px" runat="server" />`

其实这个我完全没必要使用你，直接使用`HTML`的`a`就可以呀。