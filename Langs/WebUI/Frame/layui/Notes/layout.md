---
title: layout
date: 2018-05-05 16:28:42 Sat
modify: 2018-05-05 16:28:42 Sat
tag: [layui]
categories: Web
author: wmsj100
mail: wmsj100@hotmail.com
---

# 页面布局

## 概述
- layui-container 是一个固定宽度且水平居中的内容框
- layui-fluid 铺满页面的一个流式内容框，对于后台内容多的页面多使用这个class
- 栅格系统： layui的栅格使用12等分规则
- layui-row 定义行
- layui-col-md3 定义列，当前dom占用3列的宽度
- 不同屏幕分辨率：
    - xs: 超小屏幕；<768px
    - sm: 小屏幕  >=768px
    - md: 中等屏幕 >=992px
    - lg: 大屏幕  >=1200px
- layui-col-space10 列间距为10px
- layui-col-md-offset3 中型屏幕下，当前列向有偏移3列
- 在`layui-col-md3`中插入一个行元素`layui-row`即可完成嵌套

## 范例
```html
<div class="layui-container">
    <div class="layui-row layui-col-space10">
        <div class="layui-col-md4">
            <div class="layui-row">
                <div class="layui-col-md6 iconWrap">
                    <i class="layui-inline layui-icon overIcon">&#xe61c;</i>
                </div>
                <div class="layui-col-md6">
                    <div class="layui-row">
                        <div class="layui-col-md12">
                            <span class="layui-inline layui-elip countStyle">22</span>
                        </div>
                        <div class="layui-col-md12">
                            <span class="layui-inline layui-elip countName">统计0</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="layui-col-md4">
            <div class="layui-row">
                <div class="layui-col-md6 iconWrap">
                    <i class="layui-inline layui-icon overIcon">&#xe609;</i>
                </div>
                <div class="layui-col-md6">
                    <div class="layui-row">
                        <div class="layui-col-md12">
                            <span class="layui-inline layui-elip countStyle">22</span>
                        </div>
                        <div class="layui-col-md12">
                            <span class="layui-inline layui-elip countName">统计1</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="layui-col-md4">
            <div class="layui-row">
                <div class="layui-col-md6 iconWrap">
                    <i class="layui-inline layui-icon overIcon">&#xe62e;</i>
                </div>
                <div class="layui-col-md6">
                    <div class="layui-row">
                        <div class="layui-col-md12">
                            <span class="layui-inline layui-elip countStyle">22</span>
                        </div>
                        <div class="layui-col-md12">
                            <span class="layui-inline layui-elip countName">统计2</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>
```
