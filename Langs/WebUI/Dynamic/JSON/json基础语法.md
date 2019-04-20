---
title: json基础语法
date: 2016-06-28
tags: [JSON,JavaScript,DOM]
categories: Dynamic
---

`ECMA5`中定义的原生`JSON`对象,没有兼容性考虑,ie8以上都支持

- json规定了3种数据类型
- 简单值: number, string, Boolean, null. 没有JS中的-undefined
- 对象: 是无序的键值对,无序是因为通过`for-in`遍历时候读取的值可能是通过默认的字符顺序排列的.
- 数组: 有序的值列表,如果对键值对有排序要求,那么可以放入数组中.

- json是JS的一个严格子集,所以表现形式很类似,但有以下区别

```javascript
var person = {
    name: "wmsj",
    age: 10
};
```

```json
{
    "name": "wmsj",
    "age": 10
}
```

- json没有变量的概念,
- json的属性必须用双引号包围,
- json末尾没有`;`分号.

- json通过俩个方法来与JS进行交互
- `JSON.parse` -- 把json对象转换为JS对象
- `JSON.stringify` -- 把JS对象转换为json对象

- 对于`JSON.stringigy(json,arr,num)`可以传入3个参数,
- json -- 要json字符串化的JS对象
- arr -- 表示要过滤出来的对象
- num -- 表示要格式化的空格数,也可以传入字符分隔符,增强可读性

```javascript
var json = {
    "name": {
        "name": "ct1",
        "height": "100",
        "bgcolor": "#DE4A4A"
    },
    "age": {
        "name": "ct2",
        "height": "200",
        "bgcolor": "#900D0D"
    },
    "male": {
        "name": "ct3",
        "height": "380",
        "bgcolor": "#E14399"
    }
};

JSON.stringify(json, ["name", "age"]);
"{"name":{"name":"ct1"},"age":{"name":"ct2"}}"
JSON.stringify(json, ["male", "age"]);
"{"male":{},"age":{}}"
JSON.stringify(json, ["name"]);
"{"name":{"name":"ct1"}}"
JSON.stringify(json, ["name", "height"]);
"{"name":{"name":"ct1","height":"100"}}"
JSON.stringify(json, ["height", "name"]);
"{"name":{"height":"100","name":"ct1"}}"
JSON.stringify(json, ["name", "age", "height", "bgcolor"]);
"{"name":{"name":"ct1","height":"100","bgcolor":"#DE4A4A"},"age":{"name":"ct2","height":"200","bgcolor":"#900D0D"}}"
JSON.stringify(json, ["name", "age"], 4);
"{
    "name": {
        "name": "ct1"
    },
    "age": {
        "name": "ct2"
    }
}"
JSON.stringify(json, ["name", "age"], "-");
"{
-"name": {
--"name": "ct1"
-},
-"age": {
--"name": "ct2"
-}
}"
```

- Date有一个`toJSON`方法

```javascript
new Date().toJSON()
"2016-06-28T10:35:59.681Z"
```


