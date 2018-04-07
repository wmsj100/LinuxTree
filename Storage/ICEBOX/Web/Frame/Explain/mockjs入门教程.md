---
title: mockjs入门教程
date: 2016-07-13
tags: [Models,Frame]
categories: Frame
---

这是我第一个完整看完的官方文档。
https://github.com/nuysoft/Mock/wiki/Syntax-Specification


`mockjs`加载方式有很多，因为我不了解`node`，所以我现在使用的是通过`require`方式来加载这个模块。具体如下

```javascript
require.config({
    paths: {
        mock: "mock-min"
    }
});

define(["jquery", "mock"], function($, Mock){
    var data = Mock.mock({
        "list|1-10": [{
            "id|+1": 1
        }]
    });
    $("<pre/>").text(JSON.stringify(data, null, 4)).appendTo("body");
    console.log(data);
});
```

这样就可以在页面和控制面板查看生成的随机数据了。

语法规范：
- 数据模板规范    `'name|rule': value`
    + 属性名
    + 生成规则  有七种
        * `"name|min-max": value`
        * `"name|count": value`
        * `"name|min-max.dmin-dmax": value`
        * `"name|min-max.dcount": value`
        * `name|count.dmin-dmax": value`
        * `name|count.dcount": value`
        * `name|+step": value`
    + 属性值
- 数据占位符规范

生成规则和示例
- 属性值是字符串
    - `"name|min-max": value` 属性值是字符串 通过重复字符串，重复次数大于等于`min`，小于等于`max`；
    + `"list|1-5": "wmsj100"`;  // "wmsj100wmsj100wmsj100wmsj100wmsj100"
    - `"name|count": value` 重复string，生成一个重复次数为`count`的字符串

- 属性值是number
```javascript
    var data = Mock.mock({
    // "list|1-5": "wmsj100"
    "num1|1-100.1": 1,  // 生成的浮点数中整数部分 1<=num<=100, 小数位数等于1
    "num2|123.1-3": 1,  // 整数部分为123， 小数位数为随机的1-3为
    "num3|123.3": 1,    // 整数部分为123， 小数位数为3
    "num4|123.10": 1.123 // 整数部分为123， 小数位数为10
});
```

- 属性值是布尔值

```javascript
var data = Mock.mock({
        "num1|1": true, // 值为true的概率是1/2，
        "num2|1-3": 2   // 值为2的概率是1/3
    });
```

- 属性值是对象，从对象中随机选取`count`个属性，或者是在`min-max`中随机抽取属性

```javascript
    var data = Mock.mock({
        "obj|1-3": {
            name: "wmsj",
            age: 12,
            male: "female"
        }
    })
```

- 属性是数组，

```javascript
    var data = Mock.mock({
        // 从数组中随机抽取一个值
        "arr1|1": [12,34,"wmsj",true, null, undefined], 
        // 把数组随机重复1-3次
        "arr2|1-3": [12,34,"wmsj",true, null, undefined],
        // 按顺序依次遍历数组
        "arr3|+1": [12,34,"wmsj",true, null, undefined],
        // 把数组重复3次
        "arr4|3": [12,34,"wmsj",true, null, undefined]
    })
```

- 属性是函数,fn的值为函数的返回值。

```javascript
    var data = Mock.mock({
        "fn": function(){
            return Math.round(Math.random()*10 + 1);
        }
    })
```

- 属性是正则表达式，根据正则表达式反向生成可以匹配的字符串

```javascript
    var data = Mock.mock({
        "str1": /[a-z][a-z][0-9]/,      //"au4"
        "str2": /\w\W\s\S\d\D/,     // "l?o6]"
        "str3": /\d{5,10}/      // "89925429"
    });
```

- 数据占位符模板，@后跟占位符

```javascript
    var data = Mock.mock({
    name: {
        first: '@FIRST',
        middle: '@FIRST',
        last: '@LAST',
        full: '@first @middle @last'
    },

    age: {
        first: "@first",
        middle: "@first",
        last: "@last",
        full: "@first @middle @last"
    }
})
```

---

### 综合练习

```javascript
    var template = {
        "title": "synamic Demo",
        "string|1-10": "&",
        "string|3": "value",

        "num1|1": 12,
        "num2|+1": 1,
        "num3|1-100": 1,
        "num4|123.1-10": 1,
        "num5|123.3": 1,
        "num6|123.10": 123.123,
        "num7|1-100.1-10": 1,

        "boolean1|1": true,
        "boolean2|1-2": true,

        "obj1|2-4": {
            "11011": "山西省",
            "12342": "陕西省",
            "123567": "黑龙江省",
            "09123": "江苏省"
        },

        'object2|2': {
            '310000': '上海市',
            '320000': '江苏省',
            '330000': '浙江省',
            '340000': '安徽省'
        },

        "arr1|1": ["amd", "cmd", "umd"],
        "arr2|+1": ["amd", "cmd", "umd"],
        "arr3|1-10": ["amd", "cmd", "umd"],
        "arr4|3": ["amd", "cmd", "umd"],

        "fn1": function(){
            return this.title;
        }
    }

    var data = Mock.mock(template);
    $("<pre>").text(JSON.stringify(data, null, 4)).appendTo("body");
    console.log(data);
```

-Mock.mock( rurl, template ) 当拦截到匹配`rurl`的ajax请求时，将根据数据模板生成数据。



- Mock.mock(rurl, function(){}) 当拦截到匹配`rurl`的ajax请求时，将根据函数的返回值生成数据。

```javascript
Mock.mock(/\.json/, function(opt){
    return opt;
});

$.ajax({
    url: "wmsj.json",
    dataType: "json",
    data: {
        name: "wmsj",
        age: 12
    }
}).done(function(data){
    $("<pre>").text(JSON.stringify(data, null, 4)).appendTo("body");
});

$.ajax({
    url: "json.json",
    dataType: "json",
}).done(function(data){
    $("<pre>").text(JSON.stringify(data, null, 4)).appendTo("body");
});

$.ajax({
    url: "baidu.json",
    type: "post",
    dataType: "json",
    data: {
        name: "wmsj",
        age: 12
    }
}).done(function(data){
    $("<pre>").text(JSON.stringify(data, null, 4)).appendTo("body");
})
```

- Mock.mock(rurl, rtype, template) 先匹配`ajax`地址，然后匹配请求类型，最后返回`template`数据,必须地址和请求类型都匹配才会拦截请求。

```javascript
Mock.mock(/\.json/, "post", {
    "type": "post"
});

$.ajax({
    url: "wmsj.json",
    type: "post",
}).done(function(data){
    console.log(data);
})
```

- Mock.mock(rurl, rtype, function(opt){}) -- 根据类型和地址匹配，然后返回函数的返回值。

```javascript
Mock.mock(/\.json/, "post", function(opt){
    return opt.type;
});

$.ajax({
    url: "wmsj.json",
    type: "post",
}).done(function(data){
    console.log(data);  // "POST"
})
```


Mock.setup -- 只有一个参数`timeout`，用来设置延迟多久返回数据，默认值为`10-100`，标识延时范围为`10-100ms`.

```javascript
    Mock.setup({
        timeout: "400-1000" // 延时范围为400ms-1000ms;
    })
```









