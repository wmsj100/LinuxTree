---
title: locale 语系
date: Tue 20 Feb 2018 11:52:53 AM CST
tag: [linux]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

- locale 设置环境的语系，
- centos只有tty1可以显示中文，tty2-tty7不能显示中文，即便设置语系为中文语系也只是显示乱码，因为在linux主机终端接口环境下无法显示像中文这么复杂的编码文字。
- 所以必须要安装一些中文接口化的软件，才能够看到中文。
- locale 没有参数，显示当前环境的语系配置信息，其中重要的参数时`LANG`其它参数都是在这个参数的基础上动态变更的。
- 如果要修改语系，只需要修改`LANG`这个值就可以。
- LANG=zh_CN.utf8 这样就把语系修改为中文语系了。
- 
