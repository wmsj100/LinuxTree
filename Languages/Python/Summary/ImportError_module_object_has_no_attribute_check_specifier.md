---
title: ImportError: 'module' object has no attribute 'check_specifier'
date: 2020-04-07 15:42:22
modify: 
tags: [Summary]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# ImportError: 'module' object has no attribute 'check_specifier'

## 概要

- 通过gcc来编译mongodb，开始使用python2的pip来install依赖，有一个依赖报错，
- 更换`python3-pip install -r buildscripts/requirements.txt`报错更多
- 报错如下
```
ERROR: Command errored out with exit status 1:
     command: /usr/bin/python2 -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'/tmp/pip-install-I8svWV/ansible/setup.py'"'"'; __file__='"'"'/tmp/pip-install-I8svWV/ansible/setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base pip-egg-info
         cwd: /tmp/pip-install-I8svWV/ansible/
    Complete output (19 lines):
    Traceback (most recent call last):
      File "<string>", line 1, in <module>
      File "/tmp/pip-install-I8svWV/ansible/setup.py", line 315, in <module>
        main()
      File "/tmp/pip-install-I8svWV/ansible/setup.py", line 310, in main
        setup(**setup_params)
      File "/usr/lib64/python2.7/distutils/core.py", line 112, in setup
        _setup_distribution = dist = klass(attrs)
      File "/usr/lib/python2.7/site-packages/setuptools/dist.py", line 269, in __init__
        _Distribution.__init__(self,attrs)
      File "/usr/lib64/python2.7/distutils/dist.py", line 287, in __init__
        self.finalize_options()
      File "/usr/lib/python2.7/site-packages/setuptools/dist.py", line 302, in finalize_options
        ep.load()(self, ep.name, value)
      File "/usr/lib/python2.7/site-packages/pkg_resources/__init__.py", line 2443, in load
        return self.resolve()
      File "/usr/lib/python2.7/site-packages/pkg_resources/__init__.py", line 2453, in resolve
        raise ImportError(str(exc))
    ImportError: 'module' object has no attribute 'check_specifier'
    ----------------------------------------
ERROR: Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
```

## 解决

- 查找资料说是setuptools版本太低导致的，
- `pip install --upgrade setuptools==30.1.0`
- 重新执行这个命令就好了

## 参考

- [pip 模块报错](https://blog.csdn.net/gs80140/article/details/99730850)
