---
title:  查看登陆用户信息
date: Sun 25 Feb 2018 12:41:18 PM CST
tag: [linux]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

# 查看登陆用户信息

## users
- `root wmsj100 wmsj100 wmsj100`

## who
```
wmsj100  :0           2018-02-25 09:31 (:0)
wmsj100  pts/0        2018-02-25 09:34 (:0)
root     tty2         2018-02-25 09:38
wmsj100  pts/1        2018-02-25 11:53 (:0)
```

## w
```
 12:47:02 up  3:18,  4 users,  load average: 0.01, 0.07, 0.12
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
wmsj100  :0       :0               09:31   ?xdm?   8:36   0.56s /usr/libexec/gnome-session-binary --session gnome-classic
wmsj100  pts/0    :0               09:34    6.00s  1.41s  0.01s w
root     tty2                      09:38    7:42   1.50s  1.50s -bash
wmsj100  pts/1    :0               11:53    4:14   0.45s  0.45s bash
```

## finger
- finger 不加参数
```
Login     Name       Tty      Idle  Login Time   Office     Office Phone   Host
root      root       tty2        8  Feb 25 09:38           
wmsj100   wmsj100   *:0             Feb 25 09:31                           (:0)
wmsj100   wmsj100    pts/0          Feb 25 09:34                           (:0)
wmsj100   wmsj100    pts/1          Feb 25 11:53                           (:0)
```

- finger wmsj100
```
Login: wmsj100        			Name: wmsj100
Directory: /home/wmsj100            	Shell: /bin/bash
On since Sun Feb 25 09:31 (CST) on :0 from :0 (messages off)
On since Sun Feb 25 09:34 (CST) on pts/0 from :0
On since Sun Feb 25 11:53 (CST) on pts/1 from :0
   24 seconds idle
No mail.
No Plan.
```


