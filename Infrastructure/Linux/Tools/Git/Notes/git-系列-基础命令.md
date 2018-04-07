---
title: git基本命令
date: 2016-03-24 12:18:58
tags: [Git]
categories: Frame
---
## git基本命令 
- git config --global user.name 查看git使用者的name
- git config --global user.email  查看git使用者的email
- git config --global user.name "wmsj100"  设置name；
- git config --global user.email "wmsj100@hotmail.com"`  设置git使用者的邮箱地址；
- git --version  查看git版本信息
- mkdir learngit  创建learngit文件夹
- rmdir learngit  删除learngit文件夹
  <!-- more -->
- cd learngit  切换工作目录到learngit
- git init  初始化learngit为git版本库
- touch readme.md  创建readme.md文件
- rm readme.md  删除readme.md文件
- git add readme.md     把工作目录中的readme.md文件添加到git暂存区index
- git diff readme.md  查看readme.md文件的修改详情
- git status  查看文件状态，包括了本地工作目录和git暂存区中文件的变动
- git commit -m "版本描述信息"  提交git暂存区中的文件到git版本库，并且给该次提交添加描述，方便以后的版本回滚。
- git checkout -- readme.md  撤销本地工作目录的修改
- git reset HEAD readme.md  把暂存区的文件readme.md退回到本地工作目录中
- git log 查看git版本库中所有的提交次数，并且附有提交信息
- git reset --hard HEAD^  回滚git版本到上一次提交时候的状态
- git reset --hard HEAD^^  回滚git版本到上上次提交时候的状态
- git reset --hard HEAD~20  回滚git版本到上20次提交时候的状态
- git reflog  查看git版本库变化情况，包括查看提交版本时候的id和版本描述

> ###当在本地删除了文件myss.txt时候，此时输入命令 git status 就会看到这样的提示
> `
> Changes not staged for commit:
>   (use "git add/rm <file>..." to update what will be committed)
>   (use "git checkout -- <file>..." to discard changes in working directory)  
        deleted:    listen.md
`
![Uploading Paste_Image_810373.png . . .]
> ###此时如果输入 git add myss.txt  表示要提交本次删除操作，这样会把git版本库中的myss.txt文件也删除，
> ###而如果输入  git checkout -- myss.txt  表示不要提交本次删除，而是恢复工作目录中的myss.txt,这种情况用于误操作的时候。

##git创建ssh通道
1. 在git中输入
   `ssh-keygen -t rsa -C "youremail@example.com"`
   当然此处要替换成自己的git邮箱帐号。
   然后一路回车，就会在administration文件夹中生成一个` .ssh` 文件夹，里面一共有3个文件，其中`id_rsa`是私钥，`id_rsa.pub`是公钥。
2. 登录自己的github账号，点击账号图标的‘setting’，在setting面板中点击 SSH keys ，然后点击创建新的` SSH key`
   ![Paste_Image.png](http://upload-images.jianshu.io/upload_images/1606281-33de98d87585b1af.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
   在title中输入项目的标题，然后在key中输入公钥，即可设置完成。

![Paste_Image.png](http://upload-images.jianshu.io/upload_images/1606281-6fe484893e544ff9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
