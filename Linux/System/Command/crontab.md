# Linux任务计划crontab

- crontab 设置周期性执行的指令，这些指令被守护进程激活。crond为其守护进程，crond常常运行在后台，每一分钟会检查一次是否有预订的作业需要执行。

- crontab 可以在固定的时间间隔执行指定的系统指令或shell。时间间隔可以时分/时/日/月/周

- ***** touch /home/wmsj100/Documents/test/$(date +\%Y\%m\%d\%H\%M\%S)

- crontab -e 添加任务
- crontab -l 查看任务列表
- crontab -r 删除任务

- 每个用户使用“crontab -e”添加任务，都会在“/var/spool/cron/crontabs/”中添加一个该用户自己的任务文档，这样目的时为了隔离。

- /etc/crontab 如果时系统级别的定时任务，需要写在这个文件内。

- cron服务监测的最小单位是分钟，所以cron会每分钟去读取一次/etc/crontab与/var/spool/cron/crontabs里面的内容。

- 0 3 * * * cp -a /var/spool/ /var/log/$(date +\%Y-\%m-\%d)
