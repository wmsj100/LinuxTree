单选题：
1. 如何查看/tmp/test文件的权限  B
A: type /tmp/test B: ls -l /tmp/test C: cat ls /tmp/test D: file ls /tmp/test
2. head命令用途：C
A: 查看文件类型  B: 查看head文件  C: 查看文件头几行  D: 裁剪文件头几行
3. 打印变量的命令: D
A: cat  B: ls  C: tac  D: echo
4. test的用途  A
A: 用于逻辑判断  B: 用于测试文件用途  C: 判断文件用途  D: 打印文件
5. 如何用find在/tmp目录下查找a.txt D
A: find a.txt  B: find a.txt /tmp   C: find /tmp a.txt  D: find /tmp -name a.txt
6. 如何用grep查找/tmp目录下哪些文件包含hello world 	D
A: grep hello world /tmp  B: grep "hello world" /tmp  C: grep -name "Hello world" /tmp  D: grep -r "Hello world" /tmp
7. 如何用sed打印/tmp/a.txt的第2行 D
A: sed 2 /tmp/a.txt  B: sed -line 2 /tmp/a.txt  C: sed "2p" /tmp/a.txt  D: sed -n "2p" /tmp/a.txt
8. 如何把"hello world" 追加到a.txt  C
A: cat "hello wolrd" > a.txt B: echo "hello wolrd" > a.txt C: echo "hello world" >> a.txt D: tac "hello world" >> a.txt
9. 如何查看etho的网卡信息  A
A: ifconfig eth0 B: ifconfig -l eth0 C: route eth0 D: route -l eth0
10. 下面那个是shell写num递增1的正确写法  D
A: num++  B: `num++`  C: `expr num + 1` D: `expr $num + 1`

第二套题目：
1. 如何查看/bin/ls文件的权限  B
A: type /bin/ls B: ls -l /bin/ls C: cat ls /bin/ls D: file ls /bin/ls
2. tail命令用途：C
A: 查看文件类型  B: 查看tail文件  C: 查看文件末尾几行  D: 裁剪文件末尾几行
3. 输出变量PATH的值: D
A: cat PATH B: ls PATH C: echo PATH  D: echo $PATH
4. file的用途  A
A: 查看文件类型  B: 查看可执行文件类型  C: 查看可读文件类型  D: 查看可写文件类型
5. 如何用find在/home目录下查找a.txt D
A: find a.txt  B: find a.txt /home   C: find /home a.txt  D: find /home -name a.txt
6. 如何用grep查找/home目录下哪些文件包含hello world 	D
A: grep hello world /home  B: grep "hello world" /home  C: grep -name "Hello world" /home  D: grep -r "Hello world" /home
7. 如何用sed打印/home/a.txt的第2行 D
A: sed 2 /home/a.txt  B: sed -line 2 /home/a.txt  C: sed "2p" /home/a.txt  D: sed -n "2p" /home/a.txt
8. 如何把"hello world" 追加到/home/a.txt  C
A: cat "hello wolrd" > /home/a.txt B: echo "hello wolrd" > /home/a.txt C: echo "hello world" >> /home/a.txt D: tac "hello world" >> /home/a.txt
9. 如何查看eth1的网卡信息  A
A: ifconfig eth1 B: ifconfig -l eth1 C: route eth1 D: route -l eth1
10. shell写count递增1的正确写法  D
A: count++  B: `count++`  C: `expr count + 1` D: `expr $count + 1`

第三套题目：
1. 如何查看/bin/bash文件的权限  B
A: type /bin/bash B: ls -l /bin/bash C: cat ls /bin/bash D: file ls /bin/bash
2. head命令用途：C
A: 查看文件类型  B: 查看head文件  C: 查看文件头几行  D: 裁剪文件头几行
3. 输出变量USER的值: D
A: cat USER B: ls USER C: echo USER D: echo $USER
4. readelf的用途  A
A: 查看C二进制文件的信息  B: 查看Shell文件信息  C: 查看Python文件信息  D: 查看json文件信息
5. 如何用find在/var目录下查找a.txt D
A: find a.txt  B: find a.txt /var   C: find /var a.txt  D: find /var -name a.txt
6. 如何用grep查找/var目录下哪些文件包含hello world 	D
A: grep hello world /var  B: grep "hello world" /var  C: grep -name "Hello world" /var  D: grep -r "Hello world" /var
7. 如何用sed打印/var/a.txt的第2行 D
A: sed 2 /var/a.txt  B: sed -line 2 /var/a.txt  C: sed "2p" /var/a.txt  D: sed -n "2p" /var/a.txt
8. 如何把"hello world" 追加到/var/a.txt  C
A: cat "hello wolrd" > /var/a.txt B: echo "hello wolrd" > /var/a.txt C: echo "hello world" >> /var/a.txt D: tac "hello world" >> /var/a.txt
9. 查看/var/a.txt的行数  A
A: wc -l /var/a.txt B: wc -c /var/a.txt  C: wc -t /var/a.txt D: wc /var/a.txt
10. shell写sum递增1的正确写法  D
A: sum++  B: `sum++`  C: `expr sum + 1` D: `expr $sum + 1`

多选题：
1. 下面哪些属于shell数字比较符  ABCD
A: eq 	B: ne	C: ge	D: lt
2. 下面哪些属于shell字符串比较符  AC
A: ==	B: !==	C: !=	D: !!
3. shell中if写法正确的是 BD
A: if/else	B: if/fi  C: if/else if/fi	D: if/elif/fi
4. 打印/tmp/a.txt中所有包含数字的行 ABCD
A: grep "[[:digit:]]" /tmp/a.txt  B: grep "[0-9]" /tmp/a.txt  C: grep "[[:xdigit:]]" /tmp/a.txt D: grep "[0123456789]" /tmp/a.txt
5. 打印/tmp/a.txt中同时包含数字和字母的行  AD
A: grep "[[:alnum:]]" /tmp/a.txt  B: grep "[0-9]" /tmp/a.txt C: grep "[[:alpha:]]" /tmp/a.txt  D: grep "[0-9a-zA-Z]" /tmp/a.txt


第二套题目：
6. 打印/tmp/a.txt文件按照空格分隔的第一列  ABD  
A: awk '{print $1}' /tmp/a.txt  B: awk -F ' ' '{print $1}' /tmp/a.txt C: echo /tmp/a.txt | awk '{print $1}'  D: cat /tmp/a.txt | awk -F ' ' '{print $1}'
7. 输出/tmp/a.txt文件的最后一行 ABCD
A: tail -1 /tmp/a.txt  B: cat /tmp/a.txt | tail -1  C: tac /tmp/a.txt | head -1 D: sed -n "1p" /tmp/a.txt
8. 查找/tmp目录下以"log" 结尾的文件 BCD
A: find /tmp -name "log$"  B: find /tmp -name "*log"   C: find /tmp -type f -name "*log"  D: find /tmp -type f | grep "log$"
9. 如何查看当前文件系统的挂载信息  AB
A: mount B: df  C: du D: cat /etc/fstab
10. 当前角色是root，如何以root角色登录到192.168.1.1  AB
A: ssh 192.168.1.1  B: ssh "root@192.168.1.1"  C: scp 192.168.1.1  D: scp "root@192.168.1.1"

第三套题目：
4. 打印/home/a.txt中所有包含数字的行 ABCD
A: grep "[[:digit:]]" /home/a.txt  B: grep "[0-9]" /home/a.txt  C: grep "[[:xdigit:]]" /home/a.txt D: grep "[0123456789]" /home/a.txt
5. 打印/home/a.txt中同时包含数字和字母的行  AD
A: grep "[[:alnum:]]" /home/a.txt  B: grep "[0-9]" /home/a.txt C: grep "[[:alpha:]]" /home/a.txt  D: grep "[0-9a-zA-Z]" /home/a.txt
6. 打印/home/a.txt文件按照空格分隔的第一列  ABD  
A: awk '{print $1}' /home/a.txt  B: awk -F ' ' '{print $1}' /home/a.txt C: echo /home/a.txt | awk '{print $1}'  D: cat /home/a.txt | awk -F ' ' '{print $1}'
7. 输出/home/a.txt文件的最后一行 ABCD
A: tail -1 /home/a.txt  B: cat /home/a.txt | tail -1  C: tac /home/a.txt | head -1 D: sed -n "1p" /home/a.txt
8. 查找/home目录下以"log" 结尾的文件 BCD
A: find /home -name "log$"  B: find /home -name "*log"   C: find /home -type f -name "*log"  D: find /home -type f | grep "log$"


填空：
1. 清理72877进程： kill 72877 kill -9 72877
2. 打印当前虚拟机所有登录用户:  who
3. 打印/etc/group中pi所在组的信息： cat /etc/group | grep "pi"
4. 查看命令ls所在位置： which ls
5. 查看所有网卡信息： ifconfig

第二套题目：
1. 清理91279进程： kill 91279 kill -9 91279
2. 切换到git用户:  su -git su git
3. 查看当前虚拟机进程资源消耗命令: top
4. 查看命令find所在位置： which find
5. 查看路由信息： route

第三套题目：
1. 清理85631进程： kill 85631 kill -9 85631
2. 切换到mysql用户:  su -mysql su mysql
4. 查看命令grep所在位置： which grep
3. 查看当前文件系统挂载情况 mount
5. 查看mysql服务的运行情况： service mysql status   systemctl status mysql
