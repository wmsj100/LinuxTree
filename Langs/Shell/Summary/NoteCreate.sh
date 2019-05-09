#! /bin/sh
#
# module.sh
# Copyright (C) 2019 pi <pi@raspberrypi>
#
# Distributed under terms of the MIT license.
# My note module sh
#

note_name=$1
date_str=`date +"%Y-%m-%d %H:%M:%S %A"`
touch "$note_name"
echo "---
title: $1
date: $date_str
modify:
tag: [$1]
categories: `dirname ${PWD#/*/}}`
author: wmsj100
mail: wmsj100@hotmail.com
---

# $1

## 概述

## 用法

## 范例

## 参考
- []()
" > $note_name

