---
title: 在字符串中查找字符"e"出现的次数并获取下标 if switch for while循环条件大杂烩
date: 2016-05-01
tags: [字符串,函数,封装]
categories: Dynamic
---

有一个字符串，想要知道字符串中字母`e` 出现的次数，并且获取出现位置的下标，代码如下：

`while()` 循环

```javascript
var stringValue = "Lorem ipsum dolor sit amet, consectetur adipisicing elit";

function findLetter(str, letter) {
	var num = [];
	var pop = str.indexOf(letter);
	while (pop > -1) {
		num.push(pop);
		pop = str.indexOf(letter, pop + 1);
	}
	return num;
}
var b = findLetter(stringValue, "e");
console.log(b);	//Array [ 3, 24, 32, 35, 52 ]
```

`for()` 循环，效率最高的方法，代码最少-`new`
```javascript
var stringValue = "Lorem ipsum dolor sit amet, consectetur adipisicing elit";
function findLetter(str, letter) {
	var arr = [];
	for (var i = 0; i < str.length; i++) {
		i = str.indexOf(letter, i);
		if (i === -1) {
			return arr;
		}
		arr.push(i);
	}
}
var b = findLetter(stringValue, "e");
console.log(b);	// Array [ 3, 24, 32, 35, 52 ]
```
`for()`循环，冗余代码-`old`

```javascript
var stringValue = "Lorem ipsum dolor sit amet, consectetur adipisicing elit";
function findLetter(str, letter) {
	var num = 0,
		arr = [];
	for (var i = 0; i < str.length; i++) {
		num = str.indexOf(letter, i);
		if (num > -1 && num <= str.length) {
			arr.push(num);
			i = num + 1;
		} else {
			return arr;
		}
	}
}
var b = findLetter(stringValue, "e");
console.log(b);
```

`switch()`循环-精简版本
```javascript
var stringValue = "Lorem ipsum dolor sit amet, consectetur adipisicing elit";

function findLetter(str, letter) {
	var arr = [];
	var checkLetter = function(num) {
		var num = str.indexOf(letter, num);
		switch (true) {
			case num === -1 || num > str.length:
				return;
			default:
				arr.push(num);
				checkLetter(num + 1);
		}
	}
	checkLetter(0);
	return arr;
}
var b = findLetter(stringValue, "o");
```

在函数内部使用函数表达式并且进行`switch()` 循环 --代码冗余版本

```javascript
var stringValue = "Lorem ipsum dolor sit amet, consectetur adipisicing elit";

function findLetter(str, letter) {
	var num = 0,
		arr = [];
	var checkLetter = function(num) {
		num = str.indexOf(letter, num);
		switch (true) {
			case num === -1:
				return;
				break;
			case num > str.length:
				return;
				break;
			default:
				arr.push(num);
				checkLetter(num + 1);
		}
	}
	checkLetter(0);
	return arr;
}
var b = findLetter(stringValue, "e");
```

依旧使用函数表达式，但是使用`if()` 循环

```javascript
var stringValue = "Lorem ipsum dolor sit amet, consectetur adipisicing elit";
function findLetter(str, letter) {
	var num1 = [],
		num2 = 0;
	var check = function(num) {
		num2 = str.indexOf(letter, num);
		console.log(num2)
		if (num2 <= str.length && num2 > -1) {
			num1.push(num2);
			check(num2 + 1);
		} 
		else {
			return;
		}	
	}
	check(0);
	return num1;
}
var b = findLetter(stringValue, "e");
console.log(b);
```

## 出现的问题：

1. 我不想函数在最开始就执行，如果使用函数声明的方式就没办法控制，因为函数会前置，所以只能使用函数表达式
2. 在进行条件判断的时候，判断的范围一定是从小到大的，小范围的在前面，因为如果大范围的在前面，后面小范围的条件永远都不会被执行；
3. 对于js脚本要学会调试，而调试的方法就是添加断点， 或者是直接禁止脚本， 一步一步的监督脚本的执行情况， 即便是出现了死循环也可以知道是哪里出现了问题， 及时进行改正。
4. 实现效果的方法不止一个，挑一个最简单的使用。
5. 注意`if`条件的判断，在调试面板仔细查看；
6. 如果在循环内部出现了函数(包括函数声明和函数表达式)，那么函数的执行是在所有的循环结束之后在进行函数计算的，所以性能方面会有缺陷。