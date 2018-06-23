---
title: Function 函数类型
date: 2016-04-30
tags: [函数,JavaScript]
categories: Dynamic
---

在使用函数表达式定义函数时，没有必要使用函数名——通过变量 sum 即可以引用函数。另外，还要注意函数末尾有一个分号，就像声明其他变量时一样。

由于函数名仅仅是指向函数的指针，因此函数名与包含对象指针的其他变量没有什么不同。换句话说，一个函数可能会有多个名字，

```javascript
function sum(num1, num2){
return num1 + num2;
}
alert(sum(10,10)); //20
var anotherSum = sum;
alert(anotherSum(10,10)); //20
sum = null;
alert(anotherSum(10,10)); //20
```

以上代码首先定义了一个名为 sum() 的函数，用于求两个值的和。然后，又声明了变量 anotherSum ，并将其设置为与 sum 相等（将 sum 的值赋给 anotherSum ）。注意，使用不带圆括号的函数名是访问函数指针，而非调用函数。此时， anotherSum 和 sum 就都指向了同一个函数，因此 anotherSum() 也可以被调用并返回结果。即使将 sum 设置为 null ，让它与函数“断绝关系”，但仍然可以正常调用anotherSum() 。

## 函数声明与函数表达式

而实际上，解析器在向执行环境中加载数据时，对函数声明和函数表达式并非一视同仁。解析器会率先读取函数声明，并使其在执行任何代码之前可用（可以访问）；至于函数表达式，则必须等到解析器执行到它所在的代码行，才会真正被解释执行。

```javascript
alert(sum(10,10));
var sum = function(num1, num2){
return num1 + num2;
};
```

以上代码之所以会在运行期间产生错误，原因在于函数位于一个初始化语句中，而不是一个函数声明。换句话说，在执行到函数所在的语句之前，变量 sum 中不会保存有对函数的引用；而且，由于第一行代码就会导致“unexpected identifier”（意外标识符）错误，实际上也不会执行到下一行。
除了什么时候可以通过变量访问函数这一点区别之外，函数声明与函数表达式的语法其实是等价的。

*也可以同时使用函数声明和函数表达式，例如 `var sum = function sum(){} ` 。不过，这种语法在 Safari 中会导致错误。* 

## 作为值的函数

因为 ECMAScript 中的函数名本身就是变量，所以函数也可以作为值来使用。也就是说，不仅可以像传递参数一样把一个函数传递给另一个函数，而且可以将一个函数作为另一个函数的结果返回。来看一看下面的函数。

```javascript
function callSomeFunction(someFunction, someArgument){
return someFunction(someArgument);
}function add10(num){
return num + 10;
}
var result1 = callSomeFunction(add10, 10);
alert(result1); //20
function getGreeting(name){
return "Hello, " + name;
}
var result2 = callSomeFunction(getGreeting, "Nicholas");
alert(result2); //"Hello, Nicholas"
```

当然，可以从一个函数中返回另一个函数，而且这也是极为有用的一种技术。例如，假设有一个对象数组，我们想要根据某个对象属性对数组进行排序。而传递给数组 sort() 方法的比较函数要接收两个参数，即要比较的值。可是，我们需要一种方式来指明按照哪个属性来排序。要解决这个问题，可以定义一个函数，它接收一个属性名，然后根据这个属性名来创建一个比较函数，下面就是这个函数的定义。

```javascript
function createComparisonFunction(propertyName) {
return function(object1, object2){
var value1 = object1[propertyName];
var value2 = object2[propertyName];
if (value1 < value2){
	return -1;
} else if (value1 > value2){
	return 1;
} else {
	return 0;
}
};
}
```

这个函数定义看起来有点复杂，但实际上无非就是在一个函数中嵌套了另一个函数，而且内部函数前面加了一个 return 操作符。在内部函数接收到 propertyName 参数后，它会使用方括号表示法来取得给定属性的值。取得了想要的属性值之后，定义比较函数就非常简单了。上面这个函数可以像在下面例子中这样使用。

```
var data = [{name: "Zachary", age: 28}, {name: "Nicholas", age: 29}];
data.sort(createComparisonFunction("name"));
alert(data[0].name); //Nicholas
data.sort(createComparisonFunction("age"));
alert(data[0].name); //Zachary
```

这里，我们创建了一个包含两个对象的数组 data 。其中，每个对象都包含一个 name 属性和一个age 属性。在默认情况下， sort() 方法会调用每个对象的 toString() 方法以确定它们的次序；但得到的结果往往并不符合人类的思维习惯。因此，我们调用 createComparisonFunction("name") 方法创建了一个比较函数，以便按照每个对象的 name 属性值进行排序。而结果排在前面的第一项是 name为 "Nicholas" ， age 是 29 的对象。然后，我们又使用了 createComparisonFunction("age") 返回的比较函数，这次是按照对象的 age 属性排序。得到的结果是 name 值为 "Zachary" ， age 值是 28的对象排在了第一位。

## 函数内部属性

在函数内部，有两个特殊的对象： arguments 和 this 。其中， arguments 在第 3 章曾经介绍过，它是一个类数组对象，包含着传入函数中的所有参数。虽然 arguments 的主要用途是保存函数参数，但这个对象还有一个名叫 callee 的属性，该属性是一个指针，指向拥有这个 arguments 对象的函数。请看下面这个非常经典的阶乘函数。

```javascript
function factorial(num){
if (num <=1) {
return 1;
} else {
return num * factorial(num-1)
}
}
```

定义阶乘函数一般都要用到递归算法；如上面的代码所示，在函数有名字，而且名字以后也不会变的情况下，这样定义没有问题。但问题是这个函数的执行与函数名 factorial 紧紧耦合在了一起。为了消除这种紧密耦合的现象，可以像下面这样使用 arguments.callee 。

```javascript
function factorial(num){
if (num <=1) {
return 1;
} else {
return num * arguments.callee(num-1)
}
}
```

在这个重写后的 factorial() 函数的函数体内，没有再引用函数名 factorial 。这样，无论引用函数时使用的是什么名字，都可以保证正常完成递归调用。例如：

```
var trueFactorial = factorial;
factorial = function(){
return 0;
};
alert(trueFactorial(5)); //120
alert(factorial(5)); //0
```

在此，变量 trueFactorial 获得了 factorial 的值，实际上是在另一个位置上保存了一个函数的指针。然后，我们又将一个简单地返回 0 的函数赋值给 factorial 变量。如果像原来的 factorial()那样不使用 arguments.callee ，调用 trueFactorial() 就会返回 0。可是，在解除了函数体内的代码与函数名的耦合状态之后， trueFactorial() 仍然能够正常地计算阶乘；至于 factorial() ，它现在只是一个返回 0 的函数。

## 函数属性和方法

ECMAScript 中的函数是对象，因此函数也有属性和方法。每个函数都包含两个属性： length 和 prototype 。其中， length 属性表示函数希望接收的命名参数的个数，

```javascript
function sayName(name){
alert(name);
}
function sum(num1, num2){
return num1 + num2;
}
function sayHi(){
alert("hi");
}
alert(sayName.length); //1
alert(sum.length); //2
alert(sayHi.length); //0
```

在 ECMAScript 核心所定义的全部属性中，最耐人寻味的就要数 prototype 属性了。对于ECMAScript 中的引用类型而言， prototype 是保存它们所有实例方法的真正所在。换句话说，诸如toString() 和 valueOf() 等方法实际上都保存在 prototype 名下，只不过是通过各自对象的实例访问罢了。在创建自定义引用类型以及实现继承时， prototype 属性的作用是极为重要的.在 ECMAScript 5 中， prototype 属性是不可枚举的，因此使用 for-in 无法发现。

每个函数都包含两个非继承而来的方法： apply() 和 call() 。这两个方法的用途都是在特定的作用域中调用函数，实际上等于设置函数体内 this 对象的值。首先， apply() 方法接收两个参数：一个是在其中运行函数的作用域，另一个是参数数组。其中，第二个参数可以是 Array 的实例，也可以是arguments 对象。

call() 方法与 apply() 方法的作用相同，它们的区别仅在于接收参数的方式不同。对于 call()方法而言，第一个参数是 this 值没有变化，变化的是其余参数都直接传递给函数。换句话说，在使用call() 方法时，传递给函数的参数必须逐个列举出来，

```javascript
function sum(num1, num2) {
	return num1 + num2;
}

function callSum1(num1, num2) {
	return sum.apply(this, arguments);
}

function callSum2(num1, num2) {
	return sum.apply(this, [num1, num2]);
}

function callSum3(num1, num2) {
	return sum.call(this, num1, num2);
}
console.log(callSum1(10, 11));
console.log(callSum2(10, 20));
console.log(callSum3(10, 20));
```

事实上，传递参数并非 apply() 和 call() 真正的用武之地；它们真正强大的地方是能够扩充函数赖以运行的作用域。

```javascript
var color = "red";
var o = {
	"color": "blue"
};

function show() {
	return this.color;
}
show();
var b = show.call(this);	//"red";
var c = show.call(window);	//"red";
var d = show.call(o);	//"blue";
```

ECMAScript 5 还定义了一个方法： bind() 。这个方法会创建一个函数的实例，其 this 值会被绑定到传给 bind() 函数的值。

```javascript
var objectSayColor = show.bind(o);
console.log(objectSayColor());	//"blue";
```

## 基本包装类型

引用类型与基本包装类型的主要区别就是对象的生存期。使用 new 操作符创建的引用类型的实例，在执行流离开当前作用域之前都一直保存在内存中。而自动创建的基本包装类型的对象，则只存在于一行代码的执行瞬间，然后立即被销毁。这意味着我们不能在运行时为基本类型值添加属性和方法。

```javascript
a.age = 12;
var b = a.substring(2);
var c = new Object("hello wmsj");
var d = String("hello wmsj100");
c.age = 23;
d.age = 24;
console.log(typeof(a)); //string;
console.log(typeof(c)); //object;
console.log(typeof(d)); //string;
console.log(a.age); //undefined;
console.log(d.age); //undefined;
console.log(c.age); //23
```
