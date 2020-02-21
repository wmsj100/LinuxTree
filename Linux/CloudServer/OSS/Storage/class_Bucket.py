#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 ubuntu <ubuntu@VM-0-13-ubuntu>
#
# Distributed under terms of the MIT license.

"""
获取ossutil的权限
auth 登录信息
endpoint
bucket
bucket_status 当前bucket是否cunz
"""
import oss2

class Bucket():
    __default_path = '/home/ubuntu/.ossutilconfig'
    def __init__(self, bucket_name='wmsj100-python-test',config_path=''):
        self.__config_path = config_path or self.__default_path
        self.__auth = self.__read_conf()
        self.auth = oss2.Auth(self.__auth['accessKeyID'], self.__auth['accessKeySecret'])
        self.endpoint = self.__auth['endpoint']
        self.bucket = oss2.Bucket(self.auth, self.endpoint, bucket_name)
        self.bucket_status = self.__bucket_exist()

    def __read_conf(self):
        auth = dict()

        with open(self.__config_path) as file:
            for line in file.readlines():
                if line.find('=') > -1:
                    [key, val] = line.split('=')
                    auth[key.strip()] = val.strip()
        return auth

    def __bucket_exist(self):
        try:
            self.bucket.get_bucket_info()
        except oss2.exceptions.NoSuchBucket:
            return False
        except:
            raise
        return True
