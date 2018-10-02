---
title: Mock_random生成各种随机数
date: 2016-07-13
tags: [Mock,Models,Frame]
categories: Frame
---

"boolean1": "@boolean(1,5,true)",
"natural": "@natural(0,10)"
占位符可以通过使用`@`来使用。

```javascript
var Random = Mock.Random;
Random.boolean();
// 标识true出现的概率是 min/(min+max);
Random.boolean(min, max, true);
Random.boolean(1,9,true);   // 标识true出现的概率是1/10

// 生成一个随机的自然数，不包含负数，
// 最小值为min(0)，最大值为max( 9007199254740992。)。
Random.natural(min, max);   
Random.natrual(1,10);   // 生成1-10的随机数

// 生成随机整数，包含负整数，
Random.integer(min, max);   
Random.integer(-10,10);  // 生成范围在-10--10之间的随机整数

// 生成随机的浮点数，整数部分最小值为-min， 最大值为-max，
// 小数位数最小值为-dmin， 最大值为-dmax
Random.float(min, max, dmin, dmax);
Random.float(1,10,2,4); // 生成整数最小值为1，最大值为10，小数最小位数为2，最大为4的随机浮点数

// 生成随机字符，包括`lower`小写字母，`upper`,`number`,`symbol`特殊字符
// 如果未传入参数，则从所有字符中随机取一个字符返回。
Random.character(pool); 

// 生成随机字符串，
// pool-表示生成的字符类型，内置的字符类型有`lower, upper, number, symbol`.
// 也可以输入自定义字符，
// min 表示生成字符的最小长度，
// max 表示生成字符串的最大长度，如果省略则生成固定长度字符。
Random.string(pool,min,max);
Random.string("number", 5);    // 16375 生成固定长度数字
Random.string(5);   //6LD9& 表示从所以内置字符类型中随机取出5个字符拼接。
// 伍肆捌 从自定义的字符串中随机挑选3-5个字符
Random.string("壹贰叁肆伍陆柒捌玖拾",3, 5);   

// 生成一个整型数组，start表示数组的起始值，
// stop表示数组的终止值，不包含
// step表示数组递增值，默认为1
Random.range(start, stop, step);
Random.range(10);   // [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Random.range(3, 7); // [3, 4, 5, 6]
Random.range(1, 10, 2); // [1, 3, 5, 7, 9]
Random.range(1, 10, 3); // [1, 4, 7]

// 生成随机日期
Random.date(yyyy-MM-dd);    // 1972-10-01
Random.date();  // 1976-01-15 和上面是等效的

Random.time(); // 17:31:20

Random.datetime("yyyy-MM-dd A HH:mm:ss");   // 1990-04-04 PM 22:40:10
Random.now();   // 2016-07-13 17:29:28
```

---

### 生成图片的方式有以下俩中

```javascript
var Random = Mock.Random;
Random.image(); // http://dummyimage.com/234x60，生成的是一个图片的网址，
Random.dataImage(); // 这个生成base64编码的图片。默认是png格式。

// 随机生成一个16进制颜色
Random.color(); // #79f292
Random.hex(); // #79f292
Random.rgb(); // rgb(147, 242, 121)
Random.rgba();  // rgba(129, 242, 121, 0.74);
Random.hsl();   //hsl(302, 82, 71)
```

---

### text

```javascript
var Random = Mock.Random;
// 随机生成段落，默认为3-7个句子，
Random.paragraph(min, max);
Random.paragraph();
Random.paragraph(1);  // 随机生成1个句子
Random.paragraph(1,3);  // 随机生成1-3个句子

Random.cparagraph(1,3); // 随机生成一段中文文本。
// 随机生成一个句子，默认的句子含有的单词个数是12-18之间
Random.sentence(min, max);
Random.sentence(5); // 生成一个句子，含有5个单词
Random.sentence(3,5); // 生成一个句子，随机生成由3或者5个单词组成的句子
Random.csentence(3,5);  // 随机生成一个有3-5个汉字组成的句子。

// 随机生成一个单词，
Random.word(min, max);
Random.word(3); // 随机生成一个单词，由3个字母组成
Random.word(3,6);   // 随机生成一个单词，有3-6个字母组成

// 随机生成一个汉字
Random.cword(pool, min, max);
Random.cword(); // 机
Random.cword(3);    // 随机生成3个汉字， ==> Random.csentence(3);
Random.cword('零一二三四五六七八九十');    // 随机从字符池中取一个汉字
Random.cword('零一二三四五六七八九十', 3);    // 四十七 随机从字符池中取3个汉字
Random.cword('零一二三四五六七八九十', 3, 5);    // 四八十六 随机生成3-5个汉字

// 随机生成一个标题，每个单词首字母大写。单词个数是3-7个随机单词
Random.title();
Random.title(3);    // 生成3个单词的标题
Random.title(3,5);  // Usoxtd Jrnqk Xpn Fkaouqjy
```

--- 

### name

```javascript
var Random = Mock.Random;
Random.first(); // Brenda 随机生成一个常见的英文名
Random.last(); // Brenda 随机生成一个常见的英文姓
Random.name();  // 随机生成一个常见的英文姓名 Scott Johnson
Random.name(true);  // Scott Dorothy Lewis 是否生成中间名

Random.cfirst();    // 邱 随机生成一个中文姓
Random.clast();    // 敏 随机生成一个中文名
Random.cname();    // 汤丽 随机生成一个中文姓名
```

---

### web

```javascript
var Random = Mock.Random;
// 随机生成一个域名，protocol表示协议， host表示域名
Random.url(protocol, host);
Random.url();   // cid://oigg.bm/kciwc
Random.url("http"); // http://pesgkclfs.cz/qzxvld
Random.url("http", "wmsj.com"); // http://wmsj.com/yhbgf

Random.protocol();  // 随机生成一个协议 news
Random.domain();    // hcfiueofx.id 随机生成一个域名
Random.tld();   // cn 随机生成一个顶级域名

Random.email(); // n.fltrv@dfyle.pn 随机生成一个邮箱地址
Random.email("hotmail.com"); // n.lbyyfsm@hotmail.com 随机生成一个邮箱地址

Random.ip();    // 41.127.244.103 随机生成一个ip地址
```

---

### 地址

```javascript
var Random = Mock.Random;
Random.region();    // 华中 随机生成一个中国大区
Random.province();  // 浙江省 随机生成一个省份
Random.city();  // 佳木斯市 随机生成一个市
Random.city(true);  // 湖南省 永州市 随机生成的市前面附属省份
Random.county();    // 米易县 随机生成一个县城
Random.county(true);    // 河南省 洛阳市 西工区 随机生成一个县城，包含省市
Random.zip();   // 420843 随机生成一个区号
Random.id();    // 随机生成一个18位号码的身份证号
```


```javascript
// 打乱数组的顺序并返回新数组
Random.shuffle(['a', 'e', 'i', 'o', 'u']);  // ["e", "u", "i", "a", "o"]

```


`num: "@increment()" ` -- 这是一个自增，默认是加1，每次刷新页面都会增加1，
还有一个自增
`"num|+1": 1` -- 这个刷新页面不会自增