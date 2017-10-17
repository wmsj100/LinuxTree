# Git action (Push Pull Clone) 避免输入用户名和密码方法

文地址：http://www.cnblogs.com/ballwql/p/3462104.html

前言

    在大家使用github的过程中，一定会碰到这样一种情况，就是每次要push 和pull时总是要输入github的账号和密码，这样不仅浪费了大量的时间且降低了工作效率。在此背景下，本文在网上找了两种方法来避免这种状况，这些成果也是先人提出来的，在此只是做个总结。

1.方法一

1.1 创建文件存储GIT用户名和密码

在%HOME%目录中，一般为C:\users\Administrator，也可以是你自己创建的系统用户名目录，反正都在C:\users\中。文件名为.git-credentials,由于在Window中不允许直接创建以"."开头的文件，所以需要借助git bash进行，打开git bash客户端，进行%HOME%目录，然后用touch创建文件 .git-credentials, 用vim编辑此文件，输入内容格式：

    touch .git-credentials

    vim .git-credentials

    https://{username}:{password}@github.com
1.方法一

1.1 创建文件存储GIT用户名和密码

在%HOME%目录中，一般为C:\users\Administrator，也可以是你自己创建的系统用户名目录，反正都在C:\users\中。文件名为.git-credentials,由于在Window中不允许直接创建以"."开头的文件，所以需要借助git bash进行，打开git bash客户端，进行%HOME%目录，然后用touch创建文件 .git-credentials, 用vim编辑此文件，输入内容格式：

    touch .git-credentials

    vim .git-credentials

    https://{username}:{password}@github.com

1.2 添加Git Config 内容

进入git bash终端， 输入如下命令：

    git config --global credential.helper store

执行完后查看%HOME%目录下的.gitconfig文件，会多了一项：

    [credential]

        helper = store

重新开启git bash会发现git push时不用再输入用户名和密码
