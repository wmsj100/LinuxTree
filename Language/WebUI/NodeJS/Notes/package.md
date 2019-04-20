# 包

- 包用于管理多个模块以及依赖，可以对多个模块进行封装，包的根目录必须包含"package.json",它是commonJS用于描述包的文件，
- package.json内容
	- name: 包名，是唯一的，只能包含小写字母/数值/下划线
	- version: 版本号
	- description: 说明
	- keywords: 关键字数组，用于搜索
	- homepage: 项目主页
	- bugs: 提交bug地址
	- license: 许可证
	- maintainers: 维护者数组
	- contributors: 贡献者数组
	- repositories: 项目仓库托管地址数组
	- dependencies: 包依赖
- package.json文件可以手动编辑，但是可以通过“npm init”命令生成

## npm
- npm search express 搜索express
- npm install express	本地安装express
- npm update express	升级
- npm uninstall express	卸载
