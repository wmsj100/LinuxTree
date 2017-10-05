#查看文件

- cat -n file 查看文件，并显示行号，

- tac 逆序显示文件

- head/tail 只显示头/尾10行
- tail -n 1 /etc/passwd 显示最后一行文件

- tail -f 这个参数可以实现不停的读取某个文件的内容并显示，这可以让我们动态查看日志，达到实时监视的目的。

- file finename/directoryname 查看文件类型，可以是文件/目录/链接/可执行文件

- linux不是通过后缀来识别文件类型的，文件类型是通过“file”来查看的。
