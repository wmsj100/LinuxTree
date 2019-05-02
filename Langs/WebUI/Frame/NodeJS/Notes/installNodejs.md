# 安装nodejs

- wget https://npm.taobao.org/mirrors/node/v8.9.0/node-v8.9.0-linux-x64.tar.gz
- mv ~/Downloads/node-v8.9.0-linux-x64.tar.gz /usr/local
- sudo tar zxvf node-v8.9.0-linux-x64.tar.gz
- mv node-v8.9.0-linux-x64.tar.gz node
- 配置环境变量
- vim /etc/profile 再最后面添加：
	- # set for nodejs
	- export NODE_HOME=/usr/local/node
	- export PATH=$NODE_HOME/bin:$PATH
- 保存退出后执行更改生效 source /etc/profile
- node -v 查看node的版本号
[centos7 安装nodejs](http://blog.csdn.net/jonatha_n/article/details/75271050)
