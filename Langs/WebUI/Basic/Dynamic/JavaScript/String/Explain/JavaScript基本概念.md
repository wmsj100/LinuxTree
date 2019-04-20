---
title: JavaScript基本概念
date: 2016-04-28
tags: [JavaScript,Book]
categories: Dynamic
---

## 变量
ECMAScript 的语法大量借鉴了 C 及其他类 C 语言（如 Java 和 Perl）的语法。

ECMAScript 中的一切（变量、函数名和操作符）都区分大小写。这也就意味着，变量名 test 和变量名 Test 分别表示两个不同的变量，而函数名不能使用 typeof ，因为它是一个关键字（3.2 节介绍关键字），但 typeOf 则完全可以是一个有效的函数名。

## 标识符
所谓标识符，就是指变量、函数、属性的名字，或者函数的参数。标识符可以是按照下列格式规则
   组合起来的一或多个字符：
     第一个字符必须是一个字母、下划线（ _ ）或一个美元符号（ $ ）；
     其他字符可以是字母、下划线、美元符号或数字。
   标识符中的字母也可以包含扩展的 ASCII或 Unicode字母字符（如 À和 Æ），但我们不推荐这样做。
   按照惯例，ECMAScript 标识符采用驼峰大小写格式，也就是第一个字母小写，剩下的每个单词的首字母大写，
   虽然没有谁强制要求必须采用这种格式，但为了与 ECMAScript 内置的函数和对象命名格式保持一
   致，可以将其当作一种最佳实践。

## 3.1.3 注释

ECMAScript 使用 C 风格的注释，包括单行注释和块级注释。单行注释以两个斜杠开头，如下所示：
// 单行注释
块级注释以一个斜杠和一个星号（ /* ）开头，以一个星号和一个斜杠（ */ ）结尾，如下所示：
```javascript
/*
* 这是一个多行
* （块级）注释
*/
```
  虽然上面注释中的第二和第三行都以一个星号开头，但这不是必需的。之所以添加那两个星号，纯粹是为了提高注释的可读性（这种格式在企业级应用中用得比较多）。

## 严格模式

ECMAScript 5 引入了严格模式（strict mode）的概念。严格模式是为 JavaScript 定义了一种不同的解析与执行模型。在严格模式下，ECMAScript 3 中的一些不确定的行为将得到处理，而且对某些不安全的操作也会抛出错误。要在整个脚本中启用严格模式，可以在顶部添加如下代码：

```
"use strict";
```

这行代码看起来像是字符串，而且也没有赋值给任何变量，但其实它是一个编译指示（pragma），用于告诉支持的 JavaScript 引擎切换到严格模式。这是为不破坏 ECMAScript 3 语法而特意选定的语法。
在函数内部的上方包含这条编译指示，也可以指定函数在严格模式下执行：严格模式下，JavaScript 的执行结果会有很大不同，

## 语句

虽然语句结尾的分号不是必需的，但我们建议任何时候都不要省略它。因为加上这个分号可以避免很多错误（例如不完整的输入），开发人员也可以放心地通过删除多余的空格来压缩 ECMAScript 代码（代码行结尾处没有分号会导致压缩错误）。另外，加上分号也会在某些情况下增进代码的性能，因为这样解析器就不必再花时间推测应该在哪里插入分号了。

虽然条件控制语句（如 if 语句）只在执行多条语句的情况下才要求使用代码块，但最佳实践是始终在控制语句中使用代码块——即使代码块中只有一条语句，例如：

```javascript
if (test)
alert(test); // 有效但容易出错，不要使用
if (test){ // 推荐使用
alert(test);
}
```

在控制语句中使用代码块可以让编码意图更加清晰，而且也能降低修改代码时出错的几率。

# 关键字和保留字

关键字

```
break	 do		 instanceof		 typeof
case 		else 		new 	var
catch 	finally	 return 	void
continue 	for 	switch 	while
debugger*	function 	this 	with
default 	if 		throw
delete 		in 		try
```

保留字

```
abstract enum int short
boolean export interface static
byte extends long super
char final native synchronized
class float package throws
const goto private transient
debugger implements protected volatile
double import public
```

第 5 版把在非严格模式下运行时的保留字缩减为下列这些：

```
class enum extends super
const export import
```

在严格模式下，第 5 版还对以下保留字施加了限制：

```
implements package public
interface private static
let protected yield
```

一般来说，最好都不要使用关键字和保留字作为标识符和属性名，
以便与将来的 ECMAScript 版本兼容。

ECMA-262 第 5 版对 eval 和 arguments 还施加了限制。在严
格模式下，这两个名字也不能作为标识符或属性名，否则会抛出错误。

## 3.3 变量

`var message` 这样未初始化的值会保存一个特殊值-`undefined` 

```
var message = "hi";
message = 100; //  有效，但不推荐
```

变量 message 一开始保存了一个字符串值 "hi" ，然后该值又被一个数字值 100 取代。虽然我们不建议修改变量所保存值的类型，但这种操作在 ECMAScript 中完全有效。

用 var 操作符定义的变量将成为定义该变量的作用域中的局部变量。也就是说，如果在函数中使用 var 定义一个变量，那么这个变量在函数退出后就会被销毁，

虽然省略 var 操作符可以定义全局变量，但这也不是我们推荐的做法。因为在局部作用域中定义的全局变量很难维护，而且如果有意地忽略了 var 操作符，也会由于相应变量不会马上就有定义而导致不必要的混乱。给未经声明的变量赋值在严格模式下会导致抛出 ReferenceError 错误。

```
var message = "hi",
found = false,
age = 29;
```

这个例子定义并初始化了 3 个变量。同样由于 ECMAScript 是松散类型的，因而使用不同类型初始化变量的操作可以放在一条语句中来完成。虽然代码里的换行和变量缩进不是必需的，但这样做可以提
高可读性。

## 数据类型

ECMAScript 中有 5 种简单数据类型（也称为基本数据类型）： Undefined 、 Null 、 Boolean 、 Number和 String 。还有 1种复杂数据类型—— Object ， Object 本质上是由一组无序的名值对组成的。ECMAScript不支持任何创建自定义类型的机制，而所有值最终都将是上述 6 种数据类型之一。乍一看，好像只有 6种数据类型不足以表示所有数据；但是，由于 ECMAScript 数据类型具有动态性，因此的确没有再定义其他数据类型的必要了。

### typeof操作符

鉴于 ECMAScript 是松散类型的，因此需要有一种手段来检测给定变量的数据类型—— typeof 就
是负责提供这方面信息的操作符。对一个值使用 typeof 操作符可能返回下列某个字符串：
 "undefined" ——如果这个值未定义；
 "boolean" ——如果这个值是布尔值；
 "string" ——如果这个值是字符串；
 "number" ——如果这个值是数值；
 "object" ——如果这个值是对象或 null ；
 "function" ——如果这个值是函数。

从技术角度讲，函数在 ECMAScript中是对象，不是一种数据类型。然而，函数也确实有一些特殊的属性，因此通过 typeof 操作符来区分函数和其他对象是有必要的。

### Undefined 类型

Undefined 类型只有一个值，即特殊的 undefined 。在使用 var 声明变量但未对其加以初始化时，这个变量的值就是 undefined ，例如：

```
var message;
alert(message == undefined); //true
var message = undefined;
alert(message == undefined); //true
```

对于尚未声明过的变量，只能执行一项操作，即使用 typeof 操作符检测其数据类型（对未经声明的变量调用 delete 不会导致错误，但这样做没什么实际意义，而且在严格模式下确实会导致错误）。
然而，令人困惑的是：对未初始化的变量执行 typeof 操作符会返回 undefined 值，而对未声明的变量执行 typeof 操作符同样也会返回 undefined 值。

```
var message; // 这个变量声明之后默认取得了 undefined 值
// 下面这个变量并没有声明
// var age
alert(typeof message); // "undefined"
alert(typeof age); // "undefined"
```

结果表明，对未初始化和未声明的变量执行 typeof 操作符都返回了 undefined 值；这个结果有其逻辑上的合理性。因为虽然这两种变量从技术角度看有本质区别，但实际上无论对哪种变量也不可能执行真正的操作。

即便未初始化的变量会自动被赋予 undefined 值，但显式地初始化变量依然是明智的选择。如果能够做到这一点，那么当 typeof 操作符返回 "undefined" 值时，我们就知道被检测的变量还没有被声明，而不是尚未初始化。

```
var a = "";		//string	
var a = 0;		//number
var a = true;	//boolean
```

### Null 类型

Null 类型是第二个只有一个值的数据类型，这个特殊的值是 null 。从逻辑角度来看， null 值表示一个空对象指针，而这也正是使用 typeof 操作符检测 null 值时会返回 "object" 的原因，如下面的例子所示：

如果定义的变量准备在将来用于保存对象，那么最好将该变量初始化为 null 而不是其他值。这样一来，只要直接检查 null 值就可以知道相应的变量是否已经保存了一个对象的引用，如下面的例子所示：

```
if (car != null){
// 对 car 对象执行某些操作
}
```

实际上， undefined 值是派生自 null 值

尽管 null 和 undefined 有这样的关系，但它们的用途完全不同。如前所述，无论在什么情况下都没有必要把一个变量的值显式地设置为 undefined ，可是同样的规则对 null 却不适用。换句话说，只要意在保存对象的变量还没有真正保存对象，就应该明确地让该变量保存 null 值。这样做不仅可以体现 null 作为空对象指针的惯例，而且也有助于进一步区分 null 和 undefined 。

### Boolean 类型

Boolean 类型是 ECMAScript 中使用得最多的一种类型，该类型只有两个字面值： true 和 false 。这两个值与数字值不是一回事，因此 true 不一定等于 1，而 false 也不一定等于 0。

需要注意的是， Boolean 类型的字面值 true 和 false 是区分大小写的。也就是说， True 和 False（以及其他的混合大小写形式）都不是 Boolean 值，只是标识符。
虽然 Boolean 类型的字面值只有两个，但 ECMAScript 中所有类型的值都有与这两个 Boolean 值等价的值。要将一个值转换为其对应的 Boolean 值，可以调用转型函数 Boolean() ，如下例所示：

```
var message = "Hello world!";
var messageAsBoolean = Boolean(message);
```

|   数据类型    |    转换未true     | 转换未false  |
| :-------: | :------------: | :-------: |
|  Boolean  |      true      |   false   |
|  String   |    任何非空字符串     | " "(空字符串) |
|  Number   | 任何非零数字值(包括无穷大) |   0和NaN   |
|  Object   |      任何对象      |   null    |
| Undefined |                | undefined |

### Number 类型

除了以十进制表示外，整数还可以通过八进制（以 8 为基数）或十六进制（以 16 为基数）的字面值来表示。其中，八进制字面值的第一位必须是零（0），然后是八进制数字序列（0～7）。如果字面值中的数值超出了范围，那么前导零将被忽略，后面的数值将被当作十进制数值解析。请看下面的例子：

在进行算术计算时，所有以八进制和十六进制表示的数值最终都将被转换成十进制数值。

#### 浮点数值

所谓浮点数值，就是该数值中必须包含一个小数点，并且小数点后面必须至少有一位数字。虽然小数点前面可以没有整数，但我们不推荐这种写法。

由于保存浮点数值需要的内存空间是保存整数值的两倍，因此 ECMAScript会不失时机地将浮点数值
转换为整数值。显然，如果小数点后面没有跟任何数字，那么这个数值就可以作为整数值来保存。同样地，如果浮点数值本身表示的就是一个整数（如 1.0），那么该值也会被转换为整数，

在默认情况下，ECMASctipt 会将那些小数点后面带有 6 个零以上的浮点数值转换为以 e 表示法表示的数值（例如，0.0000003 会被转换成 3e-7）。

浮点数值的最高精度是 17 位小数，但在进行算术计算时其精确度远远不如整数。例如，0.1 加 0.2的结果不是 0.3，而是 0.30000000000000004。这个小小的舍入误差会导致无法测试特定的浮点数值。例如：

```javascript
if (a + b == 0.3){ // 不要做这样的测试！
alert("You got 0.3.");
}
```

在这个例子中，我们测试的是两个数的和是不是等于 0.3。如果这两个数是 0.05 和 0.25，或者是 0.15和 0.15 都不会有问题。而如前所述，如果这两个数是 0.1 和 0.2，那么测试将无法通过。因此，永远不要测试某个特定的浮点数值。

关于浮点数值计算会产生舍入误差的问题，有一点需要明确：这是使用基于IEEE754 数值的浮点计算的通病，ECMAScript 并非独此一家；其他使用相同数值格式的语言也存在这个问题。

#### 数值范围

由于内存的限制，ECMAScript 并不能保存世界上所有的数值。ECMAScript 能够表示的最小数值保存在 Number.MIN_VALUE 中——在大多数浏览器中，这个值是 5e-324；能够表示的最大数值保存在Number.MAX_VALUE 中——在大多数浏览器中，这个值是 1.7976931348623157e+308。如果某次计算的结果得到了一个超出 JavaScript 数值范围的值，那么这个数值将被自动转换成特殊的 Infinity 值。具体来说，如果这个数值是负数，则会被转换成 -Infinity （负无穷），如果这个数值是正数，则会被转换成 Infinity （正无穷）。

如果某次计算返回了正或负的 Infinity 值，那么该值将无法继续参与下一次的计算，因为 Infinity 不是能够参与计算的数值。要想确定一个数值是不是有穷的（换句话说，是不是位于最小和最大的数值之间），可以使用 isFinite() 函数。这个函数在参数位于最小与最大数值之间时会返回 true ，如下面的例子所示：

```javascript
var result = Number.MAX_VALUE + Number.MAX_VALUE;
alert(isFinite(result)); //false
```

访问 Number.NEGATIVE_INFINITY 和Number.POSITIVE_INFINITY 也可以得到负和正 Infinity 的值。可以想见，这两个属性中分别保存着 -Infinity 和Infinity 。

#### NaN

NaN ，即非数值（Not a Number）是一个特殊的数值，这个数值用于表示一个本来要返回数值的操作数未返回数值的情况（这样就不会抛出错误了）。例如，在其他编程语言中，任何数值除以 0都会导致错误，从而停止代码执行。但在 ECMAScript中，但实际上只有 0除以 0 才会返回 NaN，正数除以 0 返回 Infinity，负数除以 0返回-Infinity。因此不会影响其他代码的执行。

NaN 本身有两个非同寻常的特点。首先，任何涉及 NaN 的操作（例如 NaN /10）都会返回 NaN ，这
个特点在多步计算中有可能导致问题。其次， NaN 与任何值都不相等，包括 NaN 本身。例如，下面的代
码会返回 false ：

```javascript
alert(NaN == NaN); //false
```

针对 NaN 的这两个特点，ECMAScript 定义了 isNaN() 函数。这个函数接受一个参数，该参数可以是任何类型，而函数会帮我们确定这个参数是否“不是数值”。 isNaN() 在接收到一个值之后，会尝试将这个值转换为数值。某些不是数值的值会直接转换为数值，例如字符串 "10" 或 Boolean 值。而任何不能被转换为数值的值都会导致这个函数返回 true 。请看下面的例子：
```javascript
alert(isNaN(NaN)); //true
alert(isNaN(10)); //false（10 是一个数值）
alert(isNaN("10")); //false（可以被转换成数值 10）
alert(isNaN("blue")); //true（不能转换成数值）
alert(isNaN(true)); //false（可以被转换成数值 1）
```

尽管有点儿不可思议，但 isNaN() 确实也适用于对象。在基于对象调用 isNaN()函数时，会首先调用对象的 valueOf() 方法，然后确定该方法返回的值是否可以转换为数值。如果不能，则基于这个返回值再调用 toString() 方法，再测试返回值。而这个过程也是 ECMAScript中内置函数和操作符的一般执行流程，

```javascript
[true].valueOf().toString()
"true"
["10","20"].valueOf()
Array [ "10", "20" ]
["10","20"].valueOf().toString()
"10,20"
isNaN("10,20")
true
```




















































