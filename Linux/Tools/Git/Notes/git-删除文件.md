---
title: git-删除文件
date: 2016-03-24 12:18:58
tags: [Git]
categories: Frame
---
> ### git删除文件包括以下几种情况

1. 删除本地文件，但是未添加到暂存区；
2. 删除本地文件，并且把删除操作添加到了暂存区；
3. 把暂存区的操作提交到了本地git库；
<!-- more -->
4. 把本地git库的删除记录推送到了远程服务器github。

> git对于删除操作有极大的撤销空间，下面分别针对上面4种情况进行恢复操作。

### 一、删除了本地文件，但未添加到暂存区；
![选择要删除的文件12.md](http://upload-images.jianshu.io/upload_images/1606281-3260df21882fdf94.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![删除本地文件12.md](http://upload-images.jianshu.io/upload_images/1606281-8e26479a22bda8f6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
> 此时发现删除错误了要进行恢复操作

![恢复文件](http://upload-images.jianshu.io/upload_images/1606281-505c42bd31234a97.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
### 二、删除了本地文件，并且已经把删除操作添加到了暂存区
![删除本地文件](http://upload-images.jianshu.io/upload_images/1606281-3c84b57c65ca32f0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
通过git status查看状态
![查看删除状态](http://upload-images.jianshu.io/upload_images/1606281-3c16f83b565c6da0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
看提示可以知道，此时如果操作 git checkout 12.md 可以恢复删除文件
如果操作 git add/rm 12.md 可以把删除状态添加到暂存区
我们进行添加操作
![添加到暂存区](http://upload-images.jianshu.io/upload_images/1606281-7095d2e295407ae4.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
查看状态，可以知道删除操作已经被添加到了暂存区，
![查看添加状态](http://upload-images.jianshu.io/upload_images/1606281-fc388ea8363e4d51.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
此时如果要撤销操作，从提示可以知道，进行 git reset HEAD 12.md可以把删除操作退回到本地删除状态，然后按照上面1的操作就可以恢复文件
![从暂存区回滚](http://upload-images.jianshu.io/upload_images/1606281-5fd5546554a84787.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![恢复文件](http://upload-images.jianshu.io/upload_images/1606281-49b10d7c984ed899.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### 三、从暂存区把删除操作提交到了本地git库

![提交删除操作](http://upload-images.jianshu.io/upload_images/1606281-3f72ca0ebac8e4de.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
查看状态 git status

![查看删除状态](http://upload-images.jianshu.io/upload_images/1606281-72387f2c69c17e5d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

可以看到有一个提交改动，此时如果要撤销，就必须对git进行版本回滚操作
通过 git log 命令查看git库的所有版本信息

![查看git库版本](http://upload-images.jianshu.io/upload_images/1606281-276eb2b68df6c4fa.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

如果感觉信息太多，可以查看简洁log版本 输入 git log --pretty=oneline

![简洁版log信息](http://upload-images.jianshu.io/upload_images/1606281-e3df5afb4f5cf32d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

看到一大串类似 6aef622c4……8445f2429f的用16进制表示的字符串是每次 commit 的ID版本号，此时我们进行版本回滚操作
选择ID的前几位字符串就足够表示版本的唯一性，输入命令 git reset --hard 6aef62

![版本回滚](http://upload-images.jianshu.io/upload_images/1606281-83617ca88a3f8a46.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![查看本地文件恢复情况](http://upload-images.jianshu.io/upload_images/1606281-2815b7acbf08563d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### 四、如果删除操作已经推送到了远程github服务器中，可以通过 git push 操作来进行推送

![推送到远程服务器](http://upload-images.jianshu.io/upload_images/1606281-f0f8a7b12e7370b5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

服务器刷新前的状态

![服务器刷新前的状态](http://upload-images.jianshu.io/upload_images/1606281-23fcb3a121b702eb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

刷新服务器

![刷新服务器后的状态](http://upload-images.jianshu.io/upload_images/1606281-856a0a9841c74248.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

可以看到文件被从服务器中删除了，如果此时进行文件恢复操作就需要像上面第三步那样进行版本回滚操作
当然了，这个版本回滚是在本地进行的，然后把回滚后的版本提交

![git版本回滚](http://upload-images.jianshu.io/upload_images/1606281-bbe2b8a7e39eddc9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

把回滚后的版本提交到远程服务器 git push

![版本提交出错](http://upload-images.jianshu.io/upload_images/1606281-6fcdfb0232b937cb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

可以看到提交出错，因为git默认是高版本覆盖低版本，但不能反过来操作，因为回滚的版本比服务器此时的版本低，所以此时常规手段是无效的，但可以进行版本的暴力提交——force
通过git的提示 git push -h 可以查看到 force的说明

![查看force的解释](http://upload-images.jianshu.io/upload_images/1606281-1a92c7f207c35829.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

进行暴力提交 git push -f

![暴力提交](http://upload-images.jianshu.io/upload_images/1606281-227d07aa1bbe0bb6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

刷新github远程服务器刷新操作

![文件失而复得](http://upload-images.jianshu.io/upload_images/1606281-96f1062db9d43086.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

> 如果要在服务器中回到删除文件的高级git版本版本该怎么操作呢？

1. 当然了，最简单的办法就是把费了老劲恢复的文件再次删除就可以，这样效果上是可以的，但是之前的那个git版本号其实是丢失了。
2. git中有一个命令 reflog 可以查看每次提交的信息，包括 commit ID和名称，可以通过提交信息找到之前的版本好，然后重新回滚就可以了。

![查找commit ID](http://upload-images.jianshu.io/upload_images/1606281-4ec14840add3b7c9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

进行回滚操作

![版本回滚成功](http://upload-images.jianshu.io/upload_images/1606281-d56ac0aecd226c23.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

然后再进行暴力提交

![暴力提交](http://upload-images.jianshu.io/upload_images/1606281-b994f966b9afd3eb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

刷新github服务器

![刷新服务器](http://upload-images.jianshu.io/upload_images/1606281-225fc3e81ef6ff53.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
