# git基础知识

- git diff --cached 查看缓冲区哪些文件改变了。
- git remote add origin https://....   添加远程分支
- git brnch test 切换到test分支，
- git checkout -b test 切换到test分支，在重新切换时候需要先把当前分支的修改内容提交。
- git branch -d test 删除分支
- git reset --hard HEAD^  硬撤销一次修改， 工作区的内容也被撤销
- git reset commitID  只是撤销log的记录，即移动HEAD的指针，工作区的内容并没有被撤销
- git log --stat  查看哪些文件被修改。
- git log --pretty=oneline  查看简化版日志
- git diff 只是查看缓冲区和工作区的内容区别，如果使用“git add .”这样在使用git diff就没有差异了，因为把工作区提交到了缓冲区了。
- git diff --cached 查看缓冲区和上次提交之间的区别
- git diff master test 比较master分支和test分支的内容差异
- git diff test 当前分支时master  这样也是比较master和test分支的不同
- git diff test file1 比较不同分支的file1的区别
- git diff test --stat 统计有哪些文件被改动。

## 在本地不同文件开发同一个项目
- 有一个开发项目gitpro
- cd ../ 推出当前项目目录
- git clone gitpro mypro  克隆gitpro到文件夹mypro
- cd mypro 进行git操作，并且提交记录
- cd gitpro 进入到gitpro目录，
- git pull ../mypro  拉mypro中进行的修改
- git status  / git log  查看记录就可以看到修改内容
- cd ../mypro  切换到mypro分支
- git pull  这样会把gitpro中的提交内容同步到当前目录
- git config --get remote.origin.url  查看当前分支的remote地址

---
- git pull ==> git fetch && git merge
- git remote add mypro ../mypro
- git fetch mypro
- git log -p master..mypro/master  查看远程分支所做的修改
- git merge mypro/master  合并远程分支到当前分支

