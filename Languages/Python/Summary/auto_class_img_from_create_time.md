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
	- `2019-02-05_15-10-28_028.jpg` 坚果云备份照片
- 文件有一些是诺基亚手机的缓存，所以得判断文件是不是图片格式结尾'.jpg/.JPG/.png'

## 做法

- 先收集所有文件的信息
- 现在整理好了，要怎么调用，重复生成时候要去重
- 数据存储到mysql
- 

## 优化

- 之前是用list存储数据，现在改为set
- 使用字典存储
- 使用正则替换对于字符串的匹配
- 之前就有意识到图片总数没有对上，但是想当然的以为是没问题，今天统计后缀才发现就是有些照片没有统计到，但是数量应该不大，大概100张左右
- 就像今天发现的其实还有5张左右的jpeg，
- 之前的照片太分散了，现在想统一管理，都放在一个目录，就是360云，文档也要统一管理，
- 我主要还是通过目录来查看的，没有在浏览器查看的习惯，
- 后面我会在家里搭建一个图片服务器，然后通过浏览器来查看图片。
- 之前分割只是到年，现在分割到了月份，而且这样更方便查看。

## 代码
```python
import sys
import os
import json
import shutil
import time
import re

BaseDir = r'E:\360云盘\云相册'
TargetDir = r'E:\Code\python\360yunpan'
Separator = '-'

def confirm_dir_exist(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


def forEachDir(targetDir=None):
    '''# 识别有效文件'''
    suffix_set = {'jpg', 'png', 'bmp', 'gif', 'jpeg', '3gp', 'mp4'}
    target_files = set()
    all_files = set()
    abandon_files = set()
    DataObj = {}
    hou_zhui = set()

    if not targetDir:
        return False

    for path, __, files in os.walk(targetDir):
        if files:
            for file in files:
                file_path = os.path.join(path, file)
                all_files.add(file_path)
                suffix = file.split('.').pop().lower()
                hou_zhui.add(suffix)
                if suffix in suffix_set:
                    analysis_file(file_path, DataObj, target_files)
                else:
                    abandon_files.add(file_path)
            else:
                continue
    save_to_database(BaseDir, DataObj)
    print('hou zhui is', hou_zhui)
    print("image total is %d" % len(DataObj))
    print("all file is %d" % len(target_files))


def analysis_file(file_path, DataObj, target_files):
    '''# 分析并解析文件的时间'''
    if os.path.isfile(file_path):
        file_name = os.path.basename(file_path)
        date_str = ''
        target_files.add(file_name)
        # 过滤前缀
        if re.match(r'^20[012]\d-[01]\d-[0123]\d', file_name):
            date_str = analysis_time_str(file_path, "time_reg")
        elif file_name.startswith('IMG_'):
            date_str = analysis_time_str(file_path, 'IMG_')
        elif file_name.startswith('C360_'):
            date_str = Separator.join(file_name[5:15].split("-"))
        elif file_name.startswith('Camera_'):
            date_str = analysis_time_str(file_path, 'Camera_')
        elif file_name.startswith('VID_'):
            date_str = analysis_time_str(file_path, 'VID_')
        elif file_name.startswith('20'):
            date_str = analysis_20(file_path)
        else:
            date_str = analysis_default(file_path)

        # 有时间戳才解析
        if date_str:
            struct_date_dir(file_path, file_name, date_str, DataObj, target_files)

def analysis_time_str(file_path, type=''):
    '''解析图片的字符串时间戳，例如IMG_20130113_094300.jpg'''
    start=0
    date_str = ''
    file_name = os.path.basename(file_path)

    if type:
        if 'IMG_' == type or 'VID_' == type:
            start = 4
        elif 'Camera_' == type:
            start = 7
        elif '20jpg' == type:
            start = 0
        elif 'time_reg' == type:
            date_str = re.match(r'^20[012]\d-[01]\d-[0123]\d', file_name).group()
            date_str = date_str.replace('-', Separator)
    else:
        start = 0

    # 判断时间戳必须全部为数字
    if not date_str:
        if file_name[start:start+8].isdigit():
            year = file_name[start:start+4]
            month = file_name[start+4:start+6]
            day = file_name[start+6:start+8]
            # 月份不大于12，day不大于31
            if int(month) <= 12 and int(day) <= 31:
                date_str = Separator.join([year, month, day])
            else:
                date_str = analysis_default(file_path)
        else:
            date_str = analysis_default(file_path)

    return date_str

def analysis_20(file_path):
    '''解析20开头的时间戳，有俩种格式,jpg/png'''
    date_str = ''
    file_name = os.path.basename(file_path)

    if file_name.lower().endswith('.jpg'):
        date_str = analysis_time_str(file_path, '20jpg')
    elif file_name.lower().endswith('.png'):
        date_str = Separator.join(file_name[:10].split('-'))

    return date_str

def analysis_default(file_path):
    ''' 默认的处理方式'''
    file_meta = os.stat(file_path)
    date_str = time.strftime("%Y{sep}%m{sep}%d".format(sep=Separator), (time.localtime(file_meta.st_mtime)))

    return date_str

def struct_date_dir(file_path, file_name, date_str, DataObj, target_files):
    '''获取到时间字符串后创建目录并且复制图片'''
    print(file_name)
    dir_path = os.path.join(TargetDir, date_str[:4],date_str[:7], date_str)
    new_file_path = os.path.join(dir_path, file_name)
    DataObj[file_name] = {'old': file_path, 'new': new_file_path}
    confirm_dir_exist(dir_path)
    if not os.path.isfile(new_file_path):
        shutil.copy2(file_path, new_file_path)
    else:
        print("{file} is already exist!".format(file=new_file_path))

def save_to_database(BaseDir, save_data):
    '''存储数据到文件'''
    with open(os.path.join(TargetDir, 'database.json'), 'w') as file:
        file.write(json.dumps(save_data))


def init():
    # if os.path.exists(TargetDir):
    #     shutil.rmtree(TargetDir)
    forEachDir(BaseDir)


if __name__ == '__main__':
    init()
```
