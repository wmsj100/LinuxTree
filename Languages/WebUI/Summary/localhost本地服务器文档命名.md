---
title: localhost本地服务器注意事项
date: 2016-04-22
tags: [技巧]
categories: Dynamic
---

在本地搭建的服务器进行文档测试的时候，对于文档或者是文档所在的文件夹都不能使用汉字，必须全部使用英文，不然就会出现文档无法加载，报错说`JSON`和`>`这个符号，尤其是使用ajax加载数据的时候。

本地文件夹名称只能是"字母、数字、下划线"，如果出现汉字或者“—”中横线这种就会出现各种错误，比如我刚刚弄的这个php文件，无论怎么测试都出现错误，无法识别，这就是因为文件夹命名。

还有本地测试的时候不要使用cdn加速，因为有可能现在是翻墙网络，而cdn是被我屏蔽掉的百度资源，这样jQuery文件本身就无法加载，所以js可能是提示错误。