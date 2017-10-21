# 创建文件/文件夹

- mkdir -p father/son/grandson 这样可以创建一个多层级的目录结构。这在安装软件和配置安装路径时非常有用。

- cp -r directory 复制目录需要使用“-r/-R”表示递归复制。

- rm -r directory 删除目录也需要进行递归操作。

- 对于只读文件删除时候需要使用“rm -f file”

- rename f F f*.c 对于批量重命名操作，这是c的语法，如果是prel版本的rename，还支持正则。


