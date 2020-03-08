---
title: journal
date: 2020-03-03 08:40:12
modify: 
tags: [Notes]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# journal

## 概要

- 这是Linux系统自带的日志管理软件，通常位于`/var/log/journal`目录
- 通常会记录一些异常日志
```
-rw-r-----+ 1 root systemd-journal  83886080 Feb 10 13:29 'system@00000000000000000000000000000000-0000000000002772-00059dd5af287eca.journal'
-rw-r-----+ 1 root systemd-journal  83886080 Feb 12 05:52 'system@00000000000000000000000000000000-00000000000170ec-00059e32044d2785.journal'
-rw-r-----+ 1 root systemd-journal  83886080 Feb 15 03:43 'system@00000000000000000000000000000000-000000000002bcf6-00059e53de7b451e.journal'
-rw-r-----+ 1 root systemd-journal  92274688 Feb 17 14:32 'system@00000000000000000000000000000000-0000000000040573-00059e8e6be26a51.journal'
-rw-r-----+ 1 root systemd-journal  83886080 Feb 20 07:09 'system@00000000000000000000000000000000-00000000000554aa-00059ebfb73cfd28.journal'
-rw-r-----+ 1 root systemd-journal  92274688 Feb 22 01:49 'system@00000000000000000000000000000000-0000000000069b82-00059ef5e08024ca.journal'
-rw-r-----+ 1 root systemd-journal 100663296 Feb 23 21:45 'system@00000000000000000000000000000000-000000000007ed91-00059f19a5be29a5.journal'
-rw-r-----+ 1 root systemd-journal 100663296 Feb 25 08:45 'system@00000000000000000000000000000000-0000000000094972-00059f3e76157060.journal'
-rw-r-----+ 1 root systemd-journal  92274688 Feb 25 22:38 'system@00000000000000000000000000000000-00000000000aac70-00059f5bcc47d6ed.journal'
-rw-r-----+ 1 root systemd-journal 100663296 Feb 26 18:04 'system@00000000000000000000000000000000-00000000000bffdb-00059f67727ca499.journal'
-rw-r-----+ 1 root systemd-journal 100663296 Feb 27 11:48 'system@00000000000000000000000000000000-00000000000d7038-00059f77bbf08c2c.journal'
-rw-r-----+ 1 root systemd-journal 100663296 Feb 28 03:44 'system@00000000000000000000000000000000-00000000000edfc8-00059f8697869041.journal'
-rw-r-----+ 1 root systemd-journal 100663296 Feb 28 23:04 'system@00000000000000000000000000000000-0000000000103b64-00059f93f403a892.journal'
-rw-r-----+ 1 root systemd-journal 100663296 Feb 29 15:58 'system@00000000000000000000000000000000-000000000011a4de-00059fa42901e077.journal'
-rw-r-----+ 1 root systemd-journal 109051904 Mar  1 07:30 'system@00000000000000000000000000000000-00000000001308bc-00059fb252dc7535.journal'
-rw-r-----+ 1 root systemd-journal 109051904 Mar  2 02:38 'system@00000000000000000000000000000000-0000000000147e80-00059fbf5564869c.journal'
-rw-r-----+ 1 root systemd-journal 100663296 Mar  2 16:58 'system@00000000000000000000000000000000-000000000015ee3e-00059fcf6188e2c4.journal'
-rw-r-----+ 1 root systemd-journal  50331648 Mar  2 23:10 'system@00059fe095ea72db-9322be3b191a55f2.journal~'
-rw-r-----+ 1 root systemd-journal  83886080 Mar  3 08:28  system.journal
```
- 类似上面这样，会占用大量空间
```
root@VM-0-13-ubuntu:/var/log/journal/4211ff3f594041f3966d836585a11a05# du -sh *
81M     system@00000000000000000000000000000000-0000000000002772-00059dd5af287eca.journal
81M     system@00000000000000000000000000000000-00000000000170ec-00059e32044d2785.journal
81M     system@00000000000000000000000000000000-000000000002bcf6-00059e53de7b451e.journal
89M     system@00000000000000000000000000000000-0000000000040573-00059e8e6be26a51.journal
81M     system@00000000000000000000000000000000-00000000000554aa-00059ebfb73cfd28.journal
89M     system@00000000000000000000000000000000-0000000000069b82-00059ef5e08024ca.journal
97M     system@00000000000000000000000000000000-000000000007ed91-00059f19a5be29a5.journal
97M     system@00000000000000000000000000000000-0000000000094972-00059f3e76157060.journal
89M     system@00000000000000000000000000000000-00000000000aac70-00059f5bcc47d6ed.journal
97M     system@00000000000000000000000000000000-00000000000bffdb-00059f67727ca499.journal
97M     system@00000000000000000000000000000000-00000000000d7038-00059f77bbf08c2c.journal
97M     system@00000000000000000000000000000000-00000000000edfc8-00059f8697869041.journal
97M     system@00000000000000000000000000000000-0000000000103b64-00059f93f403a892.journal
97M     system@00000000000000000000000000000000-000000000011a4de-00059fa42901e077.journal
105M    system@00000000000000000000000000000000-00000000001308bc-00059fb252dc7535.journal
105M    system@00000000000000000000000000000000-0000000000147e80-00059fbf5564869c.journal
97M     system@00000000000000000000000000000000-000000000015ee3e-00059fcf6188e2c4.journal
49M     system@00059fe095ea72db-9322be3b191a55f2.journal~
81M     system.journal
```
- 轻轻松松占用2G空间，这些文件查看和删除也需要通过jourca命令来执行

## 命令

- `journalctl --vacuum-size=10M` 清理空间
- `journalctl --vacuum-time=1w` 只保留一周的日志
- `journalctl --vacuum-size=500M` 只保留500M的日志

## 参考

- [linux journal日志](https://blog.csdn.net/ithomer/article/details/89530790)