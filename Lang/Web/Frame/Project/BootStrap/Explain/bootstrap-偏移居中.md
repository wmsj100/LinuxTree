---
title: bootstrap 偏移居中
date: 2016-04-27
tags: [框架,BootStrap]
categories: Frame
---

1. 使用`bootstrap` 对`div` 进行偏移是很方便的，直接使用`col-md-offset-3` 这个会是元素的最外边距增加3列。总共是12列。

2. 在`h1` 内部使用`small` 标签可以得到字号更小，颜色更浅的字体

   ```html
   <h1>hello world! <small>hello world!</small></h1>
   ```

3. 引导主题副本--通过添加`class="lead"` 得到字体更粗行高更高的字体

   ```html
   <p class="lead"> hello world</p>
   ```

4. 文本格式

   - `small`-设置字体为父元素的85%；
   - `strong` -设置为更粗的字体
   - `em` -设置为斜体
   - `text-left / right / center` -设置字体的对其方式为左/右/居中对齐
   - `text-muted` - 本行内容是减弱的。
   - `text-primary / success / info / warning / danger ` -分别设置文本为相应级别的颜色。

5. | .lead               | 使段落突出显示                                  | [尝试一下](http://www.runoob.com/try/try2.php?filename=trybs_ref_txt_lead) |
   | ------------------- | ---------------------------------------- | ---------------------------------------- |
   | .small              | 设定小文本 (设置为父文本的 85% 大小)                   | [尝试一下](http://www.runoob.com/try/try2.php?filename=trybs_ref_txt_small) |
   | .text-left          | 设定文本左对齐                                  | [尝试一下](http://www.runoob.com/try/try2.php?filename=trybs_ref_text-left) |
   | .text-center        | 设定文本居中对齐                                 | [尝试一下](http://www.runoob.com/try/try2.php?filename=trybs_ref_text-left) |
   | .text-right         | 设定文本右对齐                                  | [尝试一下](http://www.runoob.com/try/try2.php?filename=trybs_ref_text-left) |
   | .text-justify       | 设定文本对齐,段落中超出屏幕部分文字自动换行                   | [尝试一下](http://www.runoob.com/try/try2.php?filename=trybs_ref_text-left) |
   | .text-nowrap        | 段落中超出屏幕部分不换行                             | [尝试一下](http://www.runoob.com/try/try2.php?filename=trybs_ref_text-left) |
   | .text-lowercase     | 设定文本小写                                   | [尝试一下](http://www.runoob.com/try/try2.php?filename=trybs_ref_text-lowercase) |
   | .text-uppercase     | 设定文本大写                                   | [尝试一下](http://www.runoob.com/try/try2.php?filename=trybs_ref_text-lowercase) |
   | .text-capitalize    | 设定单词首字母大写                                | [尝试一下](http://www.runoob.com/try/try2.php?filename=trybs_ref_text-lowercase) |
   | .initialism         | 显示在 <abbr> 元素中的文本以小号字体展示                 | [尝试一下](http://www.runoob.com/try/try2.php?filename=trybs_ref_txt_abbr2) |
   | .blockquote-reverse | 设定引用右对齐                                  | [尝试一下](http://www.runoob.com/try/try2.php?filename=trybs_ref_txt_blockquote2) |
   | .list-unstyled      | 移除默认的列表样式，列表项中左对齐 ( <ul> 和 <ol> 中)。 这个类仅适用于直接子列表项    (如果需要移除嵌套的列表项，你需要在嵌套的列表中使用该样式) | [尝试一下](http://www.runoob.com/try/try2.php?filename=trybs_ref_txt_list-unstyled) |
   | .list-inline        | 将所有列表项放置同一行                              | [尝试一下](http://www.runoob.com/try/try2.php?filename=trybs_ref_txt_list-inline) |
   | .dl-horizontal      | 该类设置了浮动和偏移，应用于 <dl> 元素和 <dt> 元素中，具体实现可以查看实例 | [尝试一下](http://www.runoob.com/try/try2.php?filename=trybs_ref_txt_dl-horizontal) |
   | .pre-scrollable     | 使 <pre> 元素可滚动 scrollable                 | [尝试一下](http://www.runoob.com/try/try2.php?filename=trybs_ref_txt_pre2) |

   ​

