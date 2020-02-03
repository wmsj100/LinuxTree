---
title: shutil
date: 2020-02-03 13:13:49
modify: 
tags: [Notes]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# shutil

## 概要

- 主要作用与拷贝文件

## shutil.copyfileobj(file1, file2)

- 将文件file1拷贝到文件file2
- 使用之前，俩个文件必须都是open状态
- 结束之后也需要各自close
```python
f1=open('test.txt',encoding='utf-8')
f2=open('t1.txt', 'w', encoding='utf-8')
shutil.copyfileobj(f1, f2)
f1.close()
f2.close()
```

## shutil.copyfile(file1, file2)

- 拷贝文件到file2
- 该方法不需要专门使用`open`打开俩个文件
```python
shutil.copyfile('test.txt', 't2.txt')
```

## shutil.copy(file1, file2)

- 直接拷贝文件
- `shutil.copy('test.txt', 't3.txt')`

## shutil.copytree(dir1, dir2)

- 递归拷贝目录dir1到目录dir2
- `shutil.copytree('dir1', 'dir2')`

## shutil.rmtree(dir)

- 递归删除目录
- `shutil.rmtree('dir2')

## shutil.make_active('zipname', 'zip', 'dir')

- 创建压缩包并返回文件路径
- shutil.copyfile('test.txt', 't2.txt')
- 压缩包类型：zip/tar/bztar/gztar
- shutil对压缩包的处理是调用来`ZipFile``TarFile`俩个模块来处理。


## 参考

- [shutil](https://www.cnblogs.com/xiangsikai/p/7787101.html)
