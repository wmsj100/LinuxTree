#! /bin/sh
#
# module.sh
# Copyright (C) 2019 pi <pi@raspberrypi>
#
# Distributed under terms of the MIT license.
# My note module sh
#

note_name=$1
note_name=${note_name%.md}
date_str=`date +"%Y-%m-%d %H:%M:%S %A"`
cate=`dirname ${PWD#*/}`
echo "---
title: $note_name
date: $date_str
modify:
tag: [$note_name]
categories: "${cate##*/}"
author: wmsj100
mail: wmsj100@hotmail.com
---

# $note_name

## 概述

## 用法

## 范例

## 参考
- []()
" > ${note_name}.md

