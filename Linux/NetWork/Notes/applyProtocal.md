# 应用层协议

## DNS协议
- 协议基于UDP，使用端口号53
- IP和域名是对应的，这种对应关系保存在DNS服务器
- 在浏览器输入地址会有DNS服务器解析为对应的IP地址。

### DNS服务器
- 根DNS服务器： 全世界共有13台根域名服务器，编号A到M，大部分在美国
- 顶级DNS服务器： 负责如com/ org/ edu等顶级域名和所有国家的域名（cn/uk）
- 权威DNS服务器： 大型组织/大学/企业的域名解析服务器
- 本地DNS服务器： 通常与我们主机最近的DNS服务器
- host github.com 可以查看指定域名和IP
- 当一个DNS服务器收到一个DNS回答后，会将其信息缓存一段时间，当再有一个对相同域名的查询时，便可直接回复。
- 通过DNS缓存，很多查询都只是在本地DNS服务器便可完成。
- hosts文件可以看作时一个小型的DNS服务器  /etc/hosts
- /etc/hosts 这个文件记录的是IP和域名的对应记录

### 查看域名IP
- host google.com 查看google的ip地址	
- netstat -pantu 查看本机端口
- telnet 127.0.0.1 22 测试telnet
