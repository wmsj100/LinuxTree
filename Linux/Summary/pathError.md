# path错误设置

- 由于错误设置导致PATH值为空，然后所有的命令都无法调用，此时可以直接使用完整路径进行调用命令。

- 因为之前有保存PATH的路径值，所以可以通过“grep”命令过滤出值，然后重新赋值给PATH。

PATH=$PATH:{cat search.md | grep /usr};
