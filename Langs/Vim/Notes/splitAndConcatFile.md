# 切换和拼接大文件

- 对于要进行存储的文件在切割之前要先压缩，当然了压缩格式推荐“bz2”。

'tar -jcv -f HeadfirstJava.pdf.tar.bz2 HeadfirstJava.pdf'

- 经过上面的操作就把文件压缩好了，然后在通过“split”命令进行文件切割

'split -b 30m HeadfirstJava.pdf.tar.bz2 HeadfirstJava.pdf.tar.bz2_'

- 这样就安装大小“30M”把文件切割好了，然后就可以把文件上传了。

- 最后下载好文件之后要先通过“cat”命令进行拼接。

'cat HeadfirstJava.pdf.tar.bz2_* > HeadfirstJava.pdf.tar.bz2'

- 然后再进行解压缩命令

'tar -jxv -f HeadfirstJava.tar.bz2'

- 这样就在当前目录下解压缩好了文件，这样就可以使用。


