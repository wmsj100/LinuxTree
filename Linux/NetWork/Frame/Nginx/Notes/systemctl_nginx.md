---
title: systemctl_nginx
date: 2020-04-30 15:37:07
modify: 
tags: [Notes]
categories: Nginx
author: wmsj100
email: wmsj100@hotmail.com
---

# systemctl_nginx

## 概要

- 手动安装的nginx如何被systemctl管理

## 配置如下：

- `vi /usr/lib/systemd/system/nginx.service`
```nginx.service
[Unit]                                                  //对服务的说明

Description=nginx - high performance web server              //描述服务
After=network.target remote-fs.target nss-lookup.target   //描述服务类别

[Service]                       //服务的一些具体运行参数的设置
Type=forking                //后台运行的形式
PIDFile=/usr/local/nginx/logs/nginx.pid                               //PID文件的路径
ExecStartPre=/usr/local/nginx/sbin/nginx -t -c /usr/local/nginx/conf/nginx.conf   //启动准备
ExecStart=/usr/local/nginx/sbin/nginx -c /usr/local/nginx/conf/nginx.conf           //启动命令
ExecReload=/usr/local/nginx/sbin/nginx -s reload          //重启命令
ExecStop=/usr/local/nginx/sbin/nginx -s stop                //停止命令
ExecQuit=/usr/local/nginx/sbin/nginx -s quit               //快速停止
PrivateTmp=true               //给服务分配临时空间


[Install]
WantedBy=multi-user.target   //服务用户的模式
```
- `systemctl daemon-reload` 重新加载配置文件
- `systemctl start nginx.service` 启动服务
- `systemctl status nginx.service` 查看服务

- 真正在配置文件中需要把后面的注释删除，否则会在执行时候报错

## 参考

- [nginx systemctl](https://www.cnblogs.com/zhuxiangru/p/9414038.html)
