# 进程管理
- 程序： 不太精确地说，程序就是执行一系列有逻辑/有顺序结构的指令。
- 进程： 是程序在一个数据集合上的一次执行过程。
- 程序是为了完成某种任务而设计的软件，而进程是运行中的程序。

- jobs 查看被停止并放置在后台的工作。
- fg %2 把后台运行的number号尾2的提取到前台
- ctrl z 把工作停止放置在后台，
- bg %2 可以让后台的进程继续运行
- kill 1% 删除进程
- top 实时查看进程的状态
- ps 静态查看当前进程的状态信息
- nice 静态优先级，是用户空间的一个优先级值，去值范围是-20～19，值越小，表示优先级越高，-20优先级最高，19优先级最低。
- 进入top界面后，
	- i 忽略闲置和僵死的进程，一个开关式命令。

## ps 查看进程
- ps aux 查看详细进程，罗列所有的进程信息
- ps axjf 查看进程时连同进程树显示出来
- ps -l 显示当前bash相关的进程
- pstree 查看进程的相关性
	- pstree -up 同时逻辑出进程的账户名称和PID