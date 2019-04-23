---
title: 给项目添加文件夹
date: 2016-03-24 12:18:58
tags: [Git]
categories: Frame
---
> 这其实就是饥人谷的任务3,做这个任务的时候，首先要创建一个文件夹作为自己的远程git库接受文件夹，具体操作如下：
<!-- more -->
1. 在本地新建接受远程目录文件夹 bbb
![Paste_Image.png](http://upload-images.jianshu.io/upload_images/1606281-e03956ba678032f6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
2. 初始化文件夹`bbb`的git设置，分别设置用户名和邮箱
`git config --global user.name "wmsj100"
git config --global user.email "wmsj100@hotmail.com"`
![Paste_Image.png](http://upload-images.jianshu.io/upload_images/1606281-26a6999f802a48b9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
3. 克隆github项目组中的文件`此时要注意该文件的路径一定要是根目录，不能是子目录，否则就会出现文件路径不存在的警告`
![Paste_Image.png](http://upload-images.jianshu.io/upload_images/1606281-3ee97aa4587787d7.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![Paste_Image.png](http://upload-images.jianshu.io/upload_images/1606281-da51a52108cf0d2d.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
点击进去后会看到.git版本库文件，readme.md项目说明文件，homework项目文件夹
![Paste_Image.png](http://upload-images.jianshu.io/upload_images/1606281-337469591dcab71a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
进入homework文件夹直接创建自己的工作目录wang_hao
![Paste_Image.png](http://upload-images.jianshu.io/upload_images/1606281-9a2987575b9dfc6b.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
在文件夹里面创建一个readme.md的项目说明文件，当然了readme的后缀可以是任何文本格式，.txt/.html/.htm/.css/.js/……
![Paste_Image.png](http://upload-images.jianshu.io/upload_images/1606281-4fefcdbee26d2b9a.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
用文本编辑器打开readme文件，输入说明文字，对了，最好不要用记事本打开，好像是微软的记事本会在文件头部添加一个代码，有时候可能会出现乱码，推荐使用notepad++、sublime text……
![Paste_Image.png](http://upload-images.jianshu.io/upload_images/1606281-3d7b16537e57e75f.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
此时查看git库的状态`git status`然后添加wang_hao文件夹到git库
![Paste_Image.png](http://upload-images.jianshu.io/upload_images/1606281-c2b952055115657e.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![Paste_Image.png](http://upload-images.jianshu.io/upload_images/1606281-3725f3114d57f907.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
提交到本地git库
![Paste_Image.png](http://upload-images.jianshu.io/upload_images/1606281-68facd0888b425e0.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
推送到项目组文件夹，首先查看提交项目的名称，默认为`origin`
![Paste_Image.png](http://upload-images.jianshu.io/upload_images/1606281-5ff93e02e971b667.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
推送到远程git`git push origin`
![Paste_Image.png](http://upload-images.jianshu.io/upload_images/1606281-14d1d874bdd403f8.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
虽然有警告提示，但是看到底部的文件数量和大小信息就知道是提交成功了。可以去github看看刚刚这次的提交
![Paste_Image.png](http://upload-images.jianshu.io/upload_images/1606281-5a83cc954fea39a5.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
> ### 成功啦！说实话，我是真的没有看懂老师的视频，或者说连看完都没有，这几天网络有问题，视频老是看一半就停止了，而且这个视频不能拖动，只能点击，网络不稳定的时候，这样点击很容易停止播放。总之就是，我没有看完整视频，所以走了很久的弯路，只不过在自赎的过程中找到了一位大神的教程[廖雪峰的git教程](http://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000#0)这个我看了一半，但是基本操作也够了，推荐给像我一样有困惑的人。
