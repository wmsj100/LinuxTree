# rpm

- rpm -ivh *.rpm 可视化安装过程
- rpm -e *.rpm 卸载
- 如果可以的话就尽可能使用'yum install *.rpm'这样也是可以的，这样出现依赖的情况会自动进行下载。
- 如果实在是无法解决依赖，那么就果断进行无依赖安装
- rpm -ivh --nodeps *.rpm 
