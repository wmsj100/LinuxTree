---
title: 程序员必须知道的几个Git代码托管平台
date: 2016-3-30 23:04:54
tags: [Git,转载]
categories: Frame
---

上一篇博客中[2015继续任性——不会Git命令，照样玩转Git](http://www.cnblogs.com/yunfeifei/p/4207093.html)我们简单的介绍了在VS2013中使用Git，和github客户端的使用。那么使用Git到底有什么好处呢？最为明显的是支持Git代码托管的平台比较多，而且都是免费的。今天就为大家推荐几款比较火的Git代码托管平台，欢迎大家补充。不过，这里首先来对上一篇的问题进行一些说明。如果大家还有喜欢用SVN的，请参考[淘宝code—— 最给力的国内免费SVN(不限语言)，异地团队开发、打造个人开源项目不再是梦](http://www.cnblogs.com/yunfeifei/p/4055439.html)这篇文章。
<!-- more -->
 

** 一、VS2013中克隆远程Git仓库和SSH的配置**

**1、VS2013中克隆远程项目 **

　　首先感谢园友的评论和补充，今日又仔细看了一下，VS2013中是可以克隆项目的，只是我一直用的github来克隆的，所以没有注意到。我们打开VS2013，切换到团队资源管理器，如图：

![](/file/img/tool/march/0330/201.png)

点击连接到团队项目...,会看到如下图界面：

![](/file/img/tool/march/0330/202.png)

点击克隆，输入远程Git地址，然后点击克隆按钮，就会将远程仓库的项目克隆到本地，路径为下面文本框中的地址，我们也可以点击后面的...按钮进行修改或者手动输入。

 

**2、SSH的配置**

　　如果安装了github客户端，github客户端会自动的配置SSH。下面我们来说一下自己配置SSH，首先单击鼠标右键，打开Git Bash here,打开Git命令窗口，如图：输入命令：

```
ssh-keygen -t rsa -C "your_email@youremail.com"
```

点击回车，出现如下提示：

![](/file/img/tool/march/0330/203.png)

这个时候我们看到询问我们保存key的路径，使用默认即可，直接敲回车继续，这里我已经生成过了，所以我输入了新的路径和文件名，回车后会让输入两次密码(passphrase),输入一个大于4位的密码即可。然后会看到SSH生成成功，如图：

![](/file/img/tool/march/0330/204.png)

这里可以看到，我们的公钥保存到了yunfeifei_rsa.pub文件中，大家用的是默认路径的话，就打开路径C:\Users\Admin\.ssh，会看到如图所示文件：

![](/file/img/tool/march/0330/205.png)

用文本编辑工具如记事本打开id_rsa.pub,复制里面的内容，先保存起来，到后面使用。

 

** 二、推荐几个常用的Git代码托管平台**

 　　说到Git代码托管平台，首先推荐的是github，好多好的开源项目都来自github，但是github只能新建公开的Git仓库，私有仓库要收费，如果你做的是一个开源项目，可以首选github。下面推荐几个比较好的Git代码托管平台，这里我不做过多的说明和评价，也好让大家多看看，比较一下，找到自己的"真爱"。

**1、github**

关于github相信大家都有耳闻，我就不详细介绍了。github地址：https://github.com/，其首页如图：

![](/file/img/tool/march/0330/206.png)

 

**2、Gitlab**

　　对于有些人，提到github就会自然的想到Gitlab,Gitlab支持无限的公有项目和私有项目。Gitlab地址：https://about.gitlab.com/，其首页截图如图：

![](/file/img/tool/march/0330/207.png)

 

**3、Bitbucket**

　　bitbucket**免费支持5个开发成员的团队创建无限私有代码托管库**。bitbucket地址：https://bitbucket.org/，首页如图：

![](/file/img/tool/march/0330/208.png)

 

**4、(推荐)开源中国代码托管**

　　前面说的都是国外的，下面来说几个国内的。开源中国一个账号最多可以创建1000个项目，包含公有和私有，开源中国代码托管地址：http://git.oschina.net/，其首页如图：

![](/file/img/tool/march/0330/209.png)

开源中国在几个月前又发布了团队协作开发平台，和代码托管平台一起，打造了一个十分好的团队开发平台，开源中国团队协作平台地址：http://team.oschina.net/，团队协作平台支持任务的创建、讨论、便签等，如图：

![](/file/img/tool/march/0330/210.png)

 

**5、(推荐)coding.net**

　　谈到coding.net,首先必须提的是速度快，功能与开源中国相似，同样一个账号最多可以创建1000个项目，也支持任务的创建等。coding.net地址：https://coding.net/home.html，其首页如图：

![](/file/img/tool/march/0330/211.png)

 

**6、CSDN代码托管**

 CSDN代码托管地址：https://code.csdn.net/，首页如图：

![](/file/img/tool/march/0330/212.png)

 

**7、京东代码托管平台**

　　京东代码托管平台地址：https://code.jd.com/，首页如图：

![](/file/img/tool/march/0330/213.png)

 说到这里，也差不多了，虽然我不想影响大家的选择，但是还是想表达一下我的看法，我个人比较喜欢github、开源中国、Coding.net这个三个。

 

** 三、使用SSH**

 　　在上面我们使用Git bash生成了SSH的公钥和私钥，下面以coding.net为例介绍一下如何将公钥部署到远程Git仓库，打开设置中心，如图：

![](/file/img/tool/march/0330/214.png)

选择SSH公钥，填写公钥名称(可以随意起名字)，然后把我们刚刚从id_rsa.pub里面复制出来的东西粘贴到**SSH-RSA公钥key**这个文本框中即可。如图：

![](/file/img/tool/march/0330/215.png)

添加完成后，我们打开Git命令窗口测试，输入如下命令：

```
ssh -T git@coding.net
```

这个时候会提示你是否继续连接,如图：

![](/file/img/tool/march/0330/216.png)

输入yes,回车继续，会出现如下提示,如图:

![](/file/img/tool/march/0330/207.png)

如果是开源中国，会提示如下信息：

**Welcome to Git@OSC, your name!**

 

好了，到这里也说的差不多了。如果大家在使用过程中有什么问题，欢迎加入下面的QQ群进行讨论~~

