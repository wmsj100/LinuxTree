---
title: 处理文件
date: Sat 30 Dec 2017 10:18:39 PM CST
tag: [python]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

- open() 使用'open'函数打开文件，需要俩个参数，第一个参数时文件的的路径或文件名，第二个时文件的打开模式，
    - r 以只读模式打开，只能读取文件，不能编辑或删除文件内容
    - w 以写入模式打开，如果文件存在，将会删除里面的所有内容，然后打开这个文件进行写入
    - a 以追加模式打开，写入到文件的任何数据都将自动添加到文件的末尾
- 默认的模式为只读模式，

- `close()` 文件打开后我们应该总是关闭文件
- 始终确保显示关闭每个打开的文件，一旦他的工作完成就及时关闭文件，因为程序能打开的文件数量是有限制的，如果超出了这个限制，没有任何可靠的方法恢复，因此程序可能会崩溃。
- 每个打开的文件关联的数据结构（文件描述符/句柄/文件锁。。）都要消耗资源。

- `read()` 一次性读取整个文件，这个方法只能调去一次，因为第二次调用会返回空字符串，之前它以及读取完成整个文件。

- readline() 每次读取文件的一行，可以执行多次来完成文件的读取，如果读取完成，也会返回空字符串
    - 可以循环遍历文件对象来读取文件中的每一行
    ```python
    file = open("String.txt")
    for x in file:
        print(x)
    file.close()
    ```
    - 上面会把文件读取完成

- `write()` 打开一个文件，然后写入文本
    ```python
    file = open("String.txt", 'w')
    file.write('hello\n')
    file.write('world\n')
    file.close()
    file.open('String.txt')
    file.read()
    file.close()
    ```

- `with` 实际情况下我们应该尝试使`with`语句处理文件对象，它会在文件用完后自动关闭，就算发生异常也没有关系，它时`tru-finally`的简写
    ```python
    with open("String.txt") as file:
        for line in file:
            print(line)
    ```
