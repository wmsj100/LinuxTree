---
title: 文件打包与解压缩
date: Sun 18 Feb 2018 05:02:50 PM CST
tag: [linux]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

# 文件打包与解压缩 

## zip打包
- zip -r -q -o img.zip ./img
	- 上面是把img目录打包为img.zip文件
	- -r 表示递归打包
	- -q 表示静默打包，不向屏幕输出信息
	- -o 表示打包文件输入为img.zip文件

- zip -r -9 -q -o notes.zip ./ -x *.zip
	- 打包级别（1-9）1表示最快但压缩体积最大，9压缩体积最小，但耗时最久
	- -x 表示排除的文件

- zip -r -e -o t1.zip notes
	- -e 创建加密压缩包
- zip -r -l -o t2.zip notes
	- -l 因为window和linux的换行符不同，所以通过“-l”参数将LF转换为CR+LF

## unzip 解压缩
- unzip test1.zip 解压缩，会覆盖当前目录的test1文件夹内容
- unzip -l vim.zip 通过“-l”命令只是查看压缩包的内容，而不解压。
- unzip -O GBK vim.zip 通过“-O”大写O 来指定解压缩的文本编码，把字符转换为GBK格式，但是我通过file命令查看解压缩的文本内容还是UTF-8.

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
- 

## 安装tar.gz软件包
- tar -xzvf *.tar.gz -C ./filepath
- cd git
- ./configure 为编译做准备
- make 进行软件编译
- make install 编译完成后进行安装
- make clean 删除安装时生成的临时文件


## rpm软件包安装
- rpm需要自己手动安装时候，建议还是使用“yum install ./*.rpm"这样软件安装时候需要的依赖会自动被下载。
