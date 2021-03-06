---
title: 文件打包与解压缩
date: Sun 18 Feb 2018 05:02:50 PM CST
modify: 2020-11-17 10:16:15 
tag: [linux]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

# 文件打包与解压缩 

## tar包

- tar -cf test1.tar test1 
	- -c 表示打包tar包，
	- -f 表示要输出的文件名，文件名前面
- tar -xf test1.tar -C test2
	- -x 解压缩tar包
	- -C 解压缩到目标文件夹，目标文件夹必须存在
- tar -tf test1.tar
	- -t 只查看不解压
- tar -cphf test4.tar test1
	- -p 打包时候保留文件的属性，并且去除根路径'/'
	- -h 备份链接指向的源文件而不是链接本身
- tar -jvcp -f test.tar.bz --exclude=test/etc test  表示打包当前目录下的test文件夹，但是排除文件内的etc目录。
- tar -jtv -f test.tar.bz | grep 'yum.conf'  查看打包文件内的某个文件
- tar -jxvp -f test.tar.bz test/yum.conf  只解压打包文件的test/yum.conf文件。
- tar -cvf - /etc | tar -xvf - 一边打包文件，同时在另一个目录解打包目录

## tar 打包压缩包

- tar -czf test1.tar.gz test1
	- -z 打包gzip压缩包
	- -j 打包bz2压缩包
	- -J 打包xz压缩包
- tar -xzf test1.tar.gz test1
	- -x 解压缩gzip包
- `tar -Jcf bak.tar.xz bak.log --remove-files` 打包压缩包并且删除源文件
- `tar --concatenate --file a.tar b.tar` 合并b.tar到a.tar包

## tar 打指定大小的压缩包

- `tar -jzvf aa.tar.bz2 aa` 打压缩包
- `split -b 30M -d -a 1 aa.tar.bz2 aa.tar.bz2.` 分割压缩包为指定大小,最后指定分割后的包名称
- `tar -jzvf aa.tar.bz2 aa | aplit -b 30M -d -a 1 - aa.tar.bz2.`
- `cat aa.tar.bz2.* | tar -jxv -C /opt` 把分割的包解压到指定目录

### tar 打包不包含指定路径

- `tar -zcvf /tmp/downloadFile.tar.gz -C /usr/local downloadFile` 打包downloadFile, 会先进入/usr/local, 然后执行tar的打包操作
- 对于解包的时候不需要进行目录调整，因为如果有需要在打包的时候就已经调整了。

## 安装tar.gz软件包

- tar -xzvf *.tar.gz -C ./filepath
- cd git
- ./configure 为编译做准备
- make 进行软件编译
- make install 编译完成后进行安装
- make clean 删除安装时生成的临时文件


## rpm软件包安装

- rpm需要自己手动安装时候，建议还是使用“yum install ./*.rpm"这样软件安装时候需要的依赖会自动被下载。
