---
title: locale 语系
date: Tue 20 Feb 2018 11:52:53 AM CST
modify: 2020-04-29 19:44:58 
tag: [linux]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

# locale

## 概述

- locale用来设置语系
- locale 设置环境的语系，
- centos只有tty1可以显示中文，tty2-tty7不能显示中文，即便设置语系为中文语系也只是显示乱码，因为在linux主机终端接口环境下无法显示像中文这么复杂的编码文字。
- 所以必须要安装一些中文接口化的软件，才能够看到中文。
- locale 没有参数，显示当前环境的语系配置信息，其中重要的参数时`LANG`其它参数都是在这个参数的基础上动态变更的。
- 如果要修改语系，只需要修改`LANG`这个值就可以。
- LANG=zh_CN.utf8 这样就把语系修改为中文语系了。
- 

## 问题

- cannot change locale (en_US.UTF-8): No such file or director
```
[root@ecs0004 ~]# docker container exec -it kunpen bash
bash: warning: setlocale: LC_CTYPE: cannot change locale (en_US.UTF-8): No such file or directory
bash: warning: setlocale: LC_COLLATE: cannot change locale (en_US.UTF-8): No such file or directory
bash: warning: setlocale: LC_MESSAGES: cannot change locale (en_US.UTF-8): No such file or directory
bash: warning: setlocale: LC_NUMERIC: cannot change locale (en_US.UTF-8): No such file or directory
bash: warning: setlocale: LC_TIME: cannot change locale (en_US.UTF-8): No such file or directory
[root@kunpen /]# more /etc/sysconfig/i18n
/etc/sysconfig/i18n: No such file or directory
```
- 上面这个报错是因为没有设置本地语系
- 执行locale会有报错
```
[root@kunpen /]# locale
locale: Cannot set LC_CTYPE to default locale: No such file or directory
locale: Cannot set LC_MESSAGES to default locale: No such file or directory
locale: Cannot set LC_ALL to default locale: No such file or directory
LANG=en_US.UTF-8
LC_CTYPE="en_US.UTF-8"
LC_NUMERIC="en_US.UTF-8"
LC_TIME="en_US.UTF-8"
LC_COLLATE="en_US.UTF-8"
LC_MONETARY="en_US.UTF-8"
LC_MESSAGES="en_US.UTF-8"
LC_PAPER="en_US.UTF-8"
LC_NAME="en_US.UTF-8"
LC_ADDRESS="en_US.UTF-8"
LC_TELEPHONE="en_US.UTF-8"
LC_MEASUREMENT="en_US.UTF-8"
LC_IDENTIFICATION="en_US.UTF-8"
LC_ALL=
```
- `vi /etc/sysconfig/i18n`
``` 
LC_ALL=C
export LC_ALL
```
- source /etc/sysconfig/i18n
