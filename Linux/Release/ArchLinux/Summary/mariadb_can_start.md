---
title: mariadb_can_start
date: 2020-03-11 13:11:27
modify: 
tags: [Summary]
categories: ArchLinux
author: wmsj100
email: wmsj100@hotmail.com
---

# mariadb_can_start

## 概要

- 使用`sudo pacman -S mariadb`安装了mariadb数据库后无法启动
```
Mar 11 13:00:28 ArchOS systemd[1]: mariadb.service: Main process exited, code=exited, status=1/FAILURE
-- Subject: Unit process exited
-- Defined-By: systemd
-- Support: https://lists.freedesktop.org/mailman/listinfo/systemd-devel
--
-- An ExecStart= process belonging to unit mariadb.service has exited.
--
-- The process' exit code is 'exited' and its exit status is 1.
Mar 11 13:00:28 ArchOS systemd[1]: mariadb.service: Failed with result 'exit-code'.
-- Subject: Unit failed
-- Defined-By: systemd
-- Support: https://lists.freedesktop.org/mailman/listinfo/systemd-devel
--
-- The unit mariadb.service has entered the 'failed' state with result 'exit-code'.
Mar 11 13:00:28 ArchOS systemd[1]: Failed to start MariaDB 10.4.12 database server.
-- Subject: A start job for unit mariadb.service has failed
-- Defined-By: systemd
-- Support: https://lists.freedesktop.org/mailman/listinfo/systemd-devel
--
-- A start job for unit mariadb.service has finished with a failure.
--
-- The job identifier is 433 and the job result is failed.
```
---
- 查看`systemctl status mariadb.service`
```
~ >>> systemctl status mariadb.service                                                                                             [1]
● mariadb.service - MariaDB 10.4.7 database server
   Loaded: loaded (/usr/lib/systemd/system/mariadb.service; disabled; vendor preset: disabled)
   Active: failed (Result: exit-code) since Sat 2019-07-06 00:54:07 CST; 9s ago
     Docs: man:mysqld(8)
           https://mariadb.com/kb/en/library/systemd/
  Process: 1195 ExecStartPre=/bin/sh -c systemctl unset-environment _WSREP_START_POSITION (code=exited, status=0/SUCCESS)
  Process: 1196 ExecStartPre=/bin/sh -c [ ! -e /usr/bin/galera_recovery ] && VAR= ||   VAR=`/usr/bin/galera_recovery`; [ $? -eq 0 ]   >
  Process: 1204 ExecStart=/usr/bin/mysqld $MYSQLD_OPTS $_WSREP_NEW_CLUSTER $_WSREP_START_POSITION (code=exited, status=1/FAILURE)
 Main PID: 1204 (code=exited, status=1/FAILURE)
   Status: "MariaDB server is down"

7月 06 00:54:03 manjaro mysqld[1204]: 2019-07-06  0:54:03 0 [Note] InnoDB: Waiting for purge to start
7月 06 00:54:03 manjaro mysqld[1204]: 2019-07-06  0:54:03 0 [Note] InnoDB: 10.4.7 started; log sequence number 0; transaction id 7
7月 06 00:54:03 manjaro mysqld[1204]: 2019-07-06  0:54:03 0 [ERROR] Could not open mysql.plugin table. Some plugins may be not loaded
7月 06 00:54:03 manjaro mysqld[1204]: 2019-07-06  0:54:03 0 [ERROR] Can't open and lock privilege tables: Table 'mysql.servers' doesn'>
7月 06 00:54:03 manjaro mysqld[1204]: 2019-07-06  0:54:03 0 [Note] Server socket created on IP: '::'.
7月 06 00:54:03 manjaro mysqld[1204]: 2019-07-06  0:54:03 0 [ERROR] Fatal error: Can't open and lock privilege tables: Table 'mysql.db>
7月 06 00:54:03 manjaro mysqld[1204]: 2019-07-06  0:54:03 0 [ERROR] Aborting
7月 06 00:54:07 manjaro systemd[1]: mariadb.service: Main process exited, code=exited, status=1/FAILURE
7月 06 00:54:07 manjaro systemd[1]: mariadb.service: Failed with result 'exit-code'.
7月 06 00:54:07 manjaro systemd[1]: Failed to start MariaDB 10.4.7 database server.
```

## 解决

- 是因为Arch的pacman的打包机制导致的问题,
- 它把mariadb需要的lib装在了/usr/lib/mysql,而应该在/var/lib/mysql
- `sudo mysql_install_db --user=mysql --basedir=/usr/ --ldata=/var/lib/mysql/`
- `sudo systemctl restart mariadb.service`
- `sudo systemctl status mariadb.service`
```
wmsj100@ArchOS:~$ sudo systemctl status mariadb.service
● mariadb.service - MariaDB 10.4.12 database server
     Loaded: loaded (/usr/lib/systemd/system/mariadb.service; enabled; vendor preset: disabled)
     Active: active (running) since Wed 2020-03-11 13:10:03 CST; 9min ago
       Docs: man:mysqld(8)
             https://mariadb.com/kb/en/library/systemd/
   Main PID: 2481 (mysqld)
     Status: "Taking your SQL requests now..."
      Tasks: 30 (limit: 2276)
     Memory: 62.3M
     CGroup: /system.slice/mariadb.service
             └─2481 /usr/bin/mysqld

Mar 11 13:10:02 ArchOS mysqld[2481]: 2020-03-11 13:10:02 0 [Note] InnoDB: Waiting for purge to start
Mar 11 13:10:02 ArchOS mysqld[2481]: 2020-03-11 13:10:02 0 [Note] InnoDB: 10.4.12 started; log sequence number 60772; transaction id 23
Mar 11 13:10:02 ArchOS mysqld[2481]: 2020-03-11 13:10:02 0 [Note] InnoDB: Loading buffer pool(s) from /var/lib/mysql/ib_buffer_pool
Mar 11 13:10:02 ArchOS mysqld[2481]: 2020-03-11 13:10:02 0 [Note] InnoDB: Buffer pool(s) load completed at 200311 13:10:02
Mar 11 13:10:02 ArchOS mysqld[2481]: 2020-03-11 13:10:02 0 [Note] Server socket created on IP: '::'.
Mar 11 13:10:02 ArchOS mysqld[2481]: 2020-03-11 13:10:02 0 [Note] Reading of all Master_info entries succeeded
Mar 11 13:10:02 ArchOS mysqld[2481]: 2020-03-11 13:10:02 0 [Note] Added new Master_info '' to hash table
Mar 11 13:10:02 ArchOS mysqld[2481]: 2020-03-11 13:10:02 0 [Note] /usr/bin/mysqld: ready for connections.
Mar 11 13:10:02 ArchOS mysqld[2481]: Version: '10.4.12-MariaDB'  socket: '/run/mysqld/mysqld.sock'  port: 3306  ArchLinux Linux
Mar 11 13:10:03 ArchOS systemd[1]: Started MariaDB 10.4.12 database server.
```

## 参考

- [archLinux mariadb无法启动](https://blog.csdn.net/qq_39574633/article/details/94789438)
- [https://bbs.archlinux.org/viewtopic.php?id=240842](https://bbs.archlinux.org/viewtopic.php?id=240842)
