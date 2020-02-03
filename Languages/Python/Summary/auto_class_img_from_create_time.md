---
title: 按照图片的创建时间自动分类
date: 2020-02-03 17:47:01
modify: 
tags: [Summary]
categories: Python
author: wmsj100
email: wmsj100@hotmail.com
---

# 按照图片的创建时间自动分类

## 概要

- 现在有很多图片，我现在想要自动分类，按照图片的创建时间
- 图片都是手机拍摄自动起的名字
- 诺基亚的名字有固定前缀，然后是时间

## 脚本规划

- 通过`os.walk`来循环和遍历目录，获取所有的文件，
- 解析文件的头，是否以`IMG_`开头，如果是就按照诺基亚的命名规则解析
- 固定头部
	- `IMG_20130113_094300.jpg`: 诺基亚照片
	- `2013-02-16 12.34.05.jpg_966656.png`
	- `360壁纸_5002165.jpg`: 360壁纸
	- `C360_2013-01-29-11-46-14-069.jpg`: 360
	- `20111120887.jpg`: 固定日期时间戳
	- `Camera_20130415_093958.3gp`: 视频
	- `VID_20130120_205743.3gp`: 视频
	- `_DSC6534.JPG`: 王平婚礼
- 文件有一些是诺基亚手机的缓存，所以得判断文件是不是图片格式结尾'.jpg/.JPG/.png'

## 做法

- 先收集所有文件的信息
- 

## 代码
```python
import sys
import os
import json

BaseDir = r'E:\old\云相册\2011\寒假'

def isExistsDir(dirName, createDir=False):
    dirPath = os.path.join(path, dirName)
    if not os.path.exists(dirPath):
        if not createDir:
            return False
        else:
            os.makedirs(dirPath)
    return True

def forEachDir(targetDir=None):
    suffix_set = {'jpg', 'png', 'bmp', '3gp'}
    target_files = []
    all_files = []
    abandon_files = []

    if not targetDir:
        return False

    for path, dirs, files in os.walk(targetDir):
        if files:
            for file in files:
                file_path = os.path.join(path, file)
                all_files.append(file_path)
                suffix = file.split('.').pop().lower()
                if suffix in suffix_set:
                    print(file_path)
                    target_files.append(file_path)
                else:
                    abandon_files.append(file_path)
            else:
                continue
    save_data = {'target_files': target_files, 'abandon_files': abandon_files}
    save_to_database(BaseDir, save_data)

def save_to_database(BaseDir, save_data):
    with open(os.path.join(BaseDir, 'database'), 'w') as file:
        file.write(json.dumps(save_data))
        print(save_data)

def init():
    forEachDir(BaseDir)

if __name__ == '__main__':
    init()
```

## 参考

