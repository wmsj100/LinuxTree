---
title: jq
date: 2020-02-18 19:19:30
modify: 2020-03-21 18:35:50 
tags: [Notes]
categories: Linux
author: wmsj100
email: wmsj100@hotmail.com
---

# jq

## 概要

- 一款用来格式化json的工具
- 也是一个可以用来处理json数据的工具

## 使用

- `cat a.json | jq` 直接再控制台输出
- `cat a.json | jq . >a.json` 把输出内容重定向到`a.json`
- `jq . test1.json` 直接输出全部内容并且默认执行可是和和颜色打印
- `jq .Type test1.json` 只输出json中的Type内容
- `jq .Items[] test1.json` 只输出json中的列表Items
- `jq .Items[].OutCommondityCode test1.json` 只输出Items列表中的OutCommondityCode内容
- `jq .Items[1].OutCommondityCode test1.json` 只输出第一个列表的对象

## 练习代码

```test1.json
{
  "Type": "online_confirm_order_bill",
  "Source": "MEITUAN",
  "AreaCode": 2,
  "OutCode": "14769782825369498",
  "OutStoreCode": "586",
  "OnlineChannelCode": 2,
  "OrderCreateDate": "2018-12-18 17:50:08",
  "Items": [
    {
      "OutCommodityCode": "2035253",
      "CommodityQty": 1,
      "CommodityName": "品胜1A充电器",
      "CommodityPrice": 3800,
      "AvailableNum": 6
    },
    {
      "OutCommodityCode": "2040664",
      "CommodityQty": 1,
      "CommodityName": "Z品胜双面USB苹果充电线",
      "CommodityPrice": 3600,
      "AvailableNum": 3
    }
  ]
}
```

## 参考

- [linux json格式化](http://www.openskill.cn/article/357)
- [linux jq](https://www.cnblogs.com/wangxusummer/p/10168576.html)
