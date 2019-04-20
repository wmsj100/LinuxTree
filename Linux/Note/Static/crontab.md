---
title: Linux任务计划
date: Tue 20 Feb 2018 10:35:46 PM CST
tag: [linux,config]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

# Linux任务计划

## 周期性执行计划crontab

### 基础概念
- crontab 设置周期性执行的指令，这些指令被守护进程激活。crond为其守护进程，crond常常运行在后台，每一分钟会检查一次是否有预订的作业需要执行。

- crontab 可以在固定的时间间隔执行指定的系统指令或shell。时间间隔可以是 `分/时/日/月/周`
    - * | */1 代表每一时间间隔
    - 分 1～59
    - 时 1～23
    - 日 1～31
    - 月 1～12
    - 星期 0～6 星期日 0
- crontab -e 编辑添加
- crontab -r  删除所有任务

- /etc/cron.deny 添加用户名到该文件，用户就不可以使用周期命令crontab

### 查看用户任务列表
- 每个用户只能查看自己定义的任务列表
- root可以查看每个用户的任务列表
    - crontab -u wmsj100 -l 列出wmsj100的任务列表

### 系统例行任务
- /etc/crontab 查看系统的例行任务
- 这里的任务只有在root端口以邮件的方式查看任务 mail 邮件可以看到执行结果
- */1 * * * * root echo "hello world" 每分钟以root权限执行命令输出“hello world”

### 範例
- * * * * * service httpd restart 每分钟重启http服务
- * 23-3/1 * * * service httpd restart 每天从23点到3点每小时重启一次http服务
- 30 23 * * * service httpd restart 每天23:30分重启http服务
- 30 23 1 * * service httpd restart 每月1日23:30分重启http服务 
- 30 23 1 1 * service httpd restart 每年1月1日23:30 重启服务
- 30 23 * * 0 service httpd restart 每周日23:30分重启服务

- ***** touch /home/wmsj100/Documents/test/$(date +\%Y\%m\%d\%H\%M\%S)

- crontab -e 添加任务
- crontab -l 查看任务列表
- crontab -r 删除任务

- 每个用户使用“crontab -e”添加任务，都会在“/var/spool/cron/crontabs/”中添加一个该用户自己的任务文档，这样目的时为了隔离。

- /etc/crontab 如果时系统级别的定时任务，需要写在这个文件内。

- cron服务监测的最小单位是分钟，所以cron会每分钟去读取一次/etc/crontab与/var/spool/cron/crontabs里面的内容。

- 0 3 * * * cp -a /var/spool/ /var/log/$(date +\%Y-\%m-\%d)

## 只执行一次的计划at
- at 单一时刻执行一次任务
    ```at
    at now + 30 minutes
    /sbin/shutdown -h now
    <EOT> // ctrl+d的意思
    ```
- 在某一天午夜关机
    ```at 
    at 00:00 2018-02-25
    /sbin/shutdown -h now
    <EOT>
    ```
- atq 查看at列表任务,第一列是任务编号，
- atrm 1 删除任务编号是1的at任务
- at中的任务列表执行一次就从at列表移除了。

### at.deny列表
- 默认情况下所有用户都可以使用at，
- 可以通过把用户名添加到`/etc/at.deny`中来禁用at
- sudo echo "test1" >> /etc/at.deny 这样test1用户就不允许使用at命令
