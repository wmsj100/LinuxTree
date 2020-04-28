---
title: zip
date: 2020-04-28 12:30:04
modify: 
tags: [Notes]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# zip

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

- `unzip test1.zip` 解压缩，会覆盖当前目录的test1文件夹内容
- `unzip -l vim.zip` 通过“-l”命令只是查看压缩包的内容，而不解压。
- `unzip -O GBK vim.zip` 通过“-O”大写O 来指定解压缩的文本编码，把字符转换为GBK格式，但是我通过file命令查看解压缩的文本内容还是UTF-8.
- `unzip -oq -d /tmp a.zip` 解压指定解压路径
- `unzip -oq -d /tmp jline-2.14.3.jar *.so 2>/dev/null` 解压jar包，提取jar包中的so动态库文件到目标文件夹tmp中
	- 这个命令超级厉害，因为只解压so后缀的动态库文件，不需要再去遍历多余的无用的文件，减少文件，增加速度

## unzip更新压缩包内容

- `unzip jline-2.14.3.jar META-INF/native/linux32/libjansi.so` 解压指定文件
- `zip -m jline-2.14.3.jar META-INF/native/linux32/libjansi.so` 更新压缩包的指定文件

## 参考

