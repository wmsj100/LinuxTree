---
title: git-系列-远程--本地-clone操作
date: 2016-03-24 12:18:58
tags: [Git]
categories: Frame
---
> ###上面的操作是从本地到远程的push操作，我比较认可这种方式，但是，这种方式只适合自己创建并且管理项目的情况。如果是遇到协同办公的场景，就只能是从远程pull项目到本地，而这就是此次要讨论的内容。
<!-- more -->
1. 在github上面创建一个空白项目，基本操作和前边的一样，唯一的区别就是创建时候要记得勾选`readme`选项框。
![Paste_Image.png](http://upload-images.jianshu.io/upload_images/1606281-206ff21eeefefec2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![Paste_Image.png](http://upload-images.jianshu.io/upload_images/1606281-40e36365b2dd0aa7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![Paste_Image.png](http://upload-images.jianshu.io/upload_images/1606281-fb96d4aee4a20aec.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
2. 在本地git bush命令面板中进行克隆操作，首先需要创建一个克隆的文件夹
![Paste_Image.png](http://upload-images.jianshu.io/upload_images/1606281-8f9ea9d59bbb7e15.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
> 我发现克隆文件夹不是必须的，可以跳过这一步直接进行第三步，这样文件夹反倒还挺清爽的，因为少了一层自己创建的克隆文件夹嘛！
3. 输入克隆命令`git clone git@github.com:wmsj100/test-4.git`
![Paste_Image.png](http://upload-images.jianshu.io/upload_images/1606281-2b647e650ba19b1a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
> ###当然了，我的github用户名是 wmsj100,我创建的项目名称是 test-4，所以我输入的是`git@github.com:wmsj100/test-4.git`你输入的时候就需要改成自己的账号名和项目名称！

> ### 还有因为我的本地git文件夹以及绑定了 user.name 和 user.email 还有我的密钥已经绑定过了，所以这次 clone 时候不需要验证身份。
