---
title: git-系列-远程--本地-clone操作
date: 2016-03-24 12:18:58
modify: 2018-07-14 16:45:32	
tags: [Git]
categories: Frame
auth: wmsj100
email: wmsj100@hotmail.com
---

## 概述
- git push origin dev:develop 推送本地分支`dev`到远程`origin`的`develop`分支
- `git push --set-upstream origin master` 设置默认提交路径

## 推送多分支
- 假如现在有俩个推送源`github`,`gitlab`;如何通过一个命令来实现同时推送到多个
- ` git remote set-url --add origin git@gitlab.com:wmsj100/HelloWorld.git`
- 上面这个命令会把`gitlab`的源地址添加到配置文件`.git/config`的`origin`地址
- 如果使用`git push`会同时推送到`github`,`gitlab`,但是拉取代码使用的是`git fetch`地址`github`

## git push and git pull false
1. 首先，可以试图用`git push origin wmsj100`推送自己的修改；
2. 如果推送失败，则因为远程分支比你本地更新，需要先用`git pull`试图合并；
3. 如果合并有冲突，则解决冲突，并在本地提交；
4. 没有冲突或者是解决掉冲突后，再用`git push origin wmsj100`推送就能成功！
> 如果`git pull`提示“no tracking information",则说明本地分支和远程分支的链接没有创建，用命令`git branch --set-upstream branch-name origin/branch-name`。

如果是在当前分支又通过`git checkout -b dev` 创建了新的分支`dev` 那么分支`dev` 会继承之前分支上面所以的提交信息，通过`git log` 查看提交历史的时候，并不是空白，而是包含了之前的所有信息，

所以为了查看的额方便，最好在项目开始的时候就创建好3个分支，或者还是像自己之前的那样，对于每个模块进行单独的git备份，因为方便回溯版本，但是这样就碎片化太严重了，还是统一管理的好。这个项目就这样吧，下一次切记。

## 强制推送
- git push -f

## 总结
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
