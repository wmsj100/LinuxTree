---
title: PHP入门学习
date: 2016-4-3 15:23:26
tags: [PHP]
categories: Dynamic
---
- php脚本以`<?php`开始`?>`结束：	
- PHP的文件扩展名是`.php`

  <!-- more -->
- `echo`和`print`可以在浏览器中输出文本；
- `//`是单行注释，`/*......*/`这是多行注释；
- 变量是用于存储信息的“容器”；
---

- 变量名以`$`开头；
- 变量名只能以字母或者下划线开始；
- 变量名只能包含字母数字下划线，
- 变量名不能包含空格；
- 变量名是区分大小写的。

---

- PHP没有申明变量的命令，在第一次赋值的时候被创建。
- PHP是弱类型语言；

---

- PHP有四种不同的变量作用域：`local , global , static , parameter `;


- 在函数外部申明的变量拥有全局作用域，除了函数外，全局变量可以被脚本中的任何部分访问；

- 要再函数中访问全局作用域，需要使用关键字`global`

- 你可以在不同函数中使用相同的变量名称，因为这些函数内定义的变量名是局部变量，只作用于该函数内。

- 在函数内调用函数外定义的全局变量，我们需要在函数中的变量前加上 global 关键字：

- PHP 将所有全局变量存储在一个名为 $GLOBALS[*index*] 的数组中。 *index* 保存变量的名称。这个数组可以在函数内部访问，也可以直接用来更新全局变量。

- **php的使用比较不方便，需要把全部申明的变量注释，否则如果只是注释`<?php ...?>`这样内部的变量还是可以被访问的，或者说是被占用的。**

- 当一个函数完成时，它的所有变量通常都会被删除。然而，有时候您希望某个局部变量不要被删除。要做到这一点，请在您第一次声明变量时使用 **static** 关键字：

  ```php
  <?php 
  function test(){
  static $x=0;
  // $x++;
  echo $x++;
  }
  test();
  test();
  test();
   ?>//012
  ```

  ```php
  <?php 
  function test(){
  $x=0;
  // $x++;
  echo $x++;
  }
  test();
  test();
  test();
   ?>
  ```

  然后，每次调用该函数时，该变量将会保留着函数前一次被调用时的值。

  **注释：**该变量仍然是函数的局部变量。


- 参数是通过调用代码将值传递给函数的局部变量；
- 数组是用`array( )`形式写成的。

---

`echo` and `print`

echo可以输出一个或多个字符串；

print只允许输出一个字符串，返回值总为1；

echo输出的速度比print快，echo没有返回值，print有返回值1；

---

-  PHP var_dump() 函数返回变量的数据类型和值：

-  NULL 值表示变量没有值。NULL 是数据类型为 NULL 的值。

   NULL 值指明一个变量是否为空值。 同样可用于数据空值和NULL值的区别。

---

- 常量——是全局变量，可以在函数内部访问到，使用关键词`define(name,value,boolean)`默认是false，即区分大小写，如果为`true`即表示不区分大小写；

```php
 define("HELLO", "wmsj100",true);
  echo HELLO;	// "wmsj100"
  echo "<br>";
  echo hello;	// "wmsj100"
  function test(){
echo hello;	// "wmsj100"
```

- `str1.str2.——用于连接字符串；
- `strlen(string)`——用于计算字符串长度；
- `strpos($s1 , "wmsj")——查找字符串中的指定字符，如果查找到就返回下标，如果没有，就是空白。

---

PHP的switch和js是不同的，PHP会进行类型转换，即

```php
$a="1";
switch($a){
  case 1;
  echo "duile";
  break;
  default:
  echo "cuole";
}
//duile;
```

它进行了类型转换，把”1“=》1；

---

```php
$cars=array("Volvo","BMW","Toyota");
echo $cars[0]." ".$cars[1]." ".$cars[2]."<br>";
echo count($cars);
for($i=0;$i<count($cars);$i++)
{
	echo $cars[$i]."<br>";
}
//Volvo BMW Toyota
//3Volvo
//BMW
//Toyota
```

`for($i=0;$i<count($cars);$i++)`——通过它可以遍历数组，而且`i`不需要使用`var`来进行申明，直接使用`$`使用就行。	

---

php的`foreach`循环：

```javascript
$age=array("peter"=>"35","ben"=>"37","joe"=>"43");
foreach ($age as $key => $value) {
	echo $key." :age = ".$value."<br>";
}
//peter :age = 35
//ben :age = 37
//joe :age = 43
```

---

数组排序：PHP的排序会改变原数组，这和js是不一样的。同样的，通过`foreach`来遍历数组，因为要比`for`循环要简单。

`sort` and `rsort`——根据数组内容进行升序/降序

```php
$cars=array("Volvo","BMW","Toyota");
foreach ($cars as $value) {
	echo $value."<br>";
}
//Volvo
//BMW
//Toyota
sort($cars);	//升序排法
foreach ($cars as $value) {
	echo $value."<br>";
}
//BMW
//Toyota
//Volvo
rsort($cars);	//降序排法
foreach ($cars as $value) {
	echo $value."<br>";
}
//Volvo
//Toyota
//BMW
```

`asort` and `arsort` ——根据数组的值进行升序/降序

```php
$age=array("Peter"=>"35","Ben"=>"37","Joe"=>"43");
foreach ($age as $key=> $value) {
	echo $key." value ".$value."<br>";
}
//Peter value 35
//Ben value 37
//Joe value 43
echo "<br>";
asort($age);
foreach ($age as $key => $value) {
	echo $key." value ".$value."<br>";
}
//Peter value 35
//Ben value 37
//Joe value 43
echo "<br>";
arsort($age);
foreach ($age as $key=>$value) {
	echo $key." value ".$value."<br>";
}
//Joe value 43
//Ben value 37
//Peter value 35
```

`ksort` and `krsort`——根据数组的键名称进行升序/降序

```php
$age=array("Peter"=>"35","Ben"=>"37","Joe"=>"43");
foreach ($age as $key=> $value) {
	echo $key." value ".$value."<br>";
}
//Peter value 35
//Ben value 37
//Joe value 43
echo "<br>";
ksort($age);
foreach ($age as $key => $value) {
	echo $key." value ".$value."<br>";
}
//Ben value 37
//Joe value 43
//Peter value 35
echo "<br>";
krsort($age);
foreach ($age as $key=>$value) {
	echo $key." value ".$value."<br>";
}
//Peter value 35
//Joe value 43
//Ben value 37
```

---

### php超级全局变量

- $GLOBALS——是一个包含了全部变量的全局组合数组，变量的名字就是数组的键。

```php
$x=75;
$y=25;
function addition(){
	$GLOBALS['z']=$GLOBALS['x']+$GLOBALS['y'];
}
addition();
echo $z;	//100
```

### PHP $_SERVER

`_SERVER`是一个读取服务器信息的命令，比如获取路径、浏览器信息，这个使用的比较少；

## PHP $_REQUEST

PHP $_REQUEST 用于收集HTML表单提交的数据。

```html
<?php
$name=$_REQUEST['fname'];
echo $name;
?>
<form method="post" action="<?php echo $_SERVER['PHP_SELF']; ?>">
	Name: <input type="test" name="fname">
	<input type="submit">
</form>
```

---

### 循环

- `while`循环

```php
$i=0;
while($i<=5){
	echo $i."<br>";
	$i++;
}	//012345
```

- `do....while`循环至少会被执行一次

```php
$i=0;
do{
	$i++;
	echo $i."<br>";
	
}
while($i<=5);	//123456
```

- `foreach`循环用于遍历数组，

```
foreach ($array as $value)
{
要执行代码;
}
```

每进行一次循环，当前数组元素的值就会被赋值给`$value`变量，（数组指针会逐一地移动），在进行下一次循环时，将看到数组中的下一个值。

---

# PHP 函数

PHP 的真正威力源自于它的函数。

在 PHP 中，提供了超过 1000 个内建的函数。

在PHP中定义了函数的变量，但是如果调用函数的时候没有传入参数，那么就会报错，有几个参数就会弹出一个报错。

```php
function funName($name,$age){
	echo __FUNCTION__;
}
funName();
```

![](/file/img/tool/April/0403/001.png)

但是如果传入了参数，就不会报错了。

---

# PHP 魔术变量

`__LINE__`这个变量可以得到目前所在的行号。

```php
echo '这是第'.__LINE__."行";	//257
```

`__FILE__`获得目前文件的绝对路径

```php
echo __FILE__;
//E:\wamp\www\wmsj100\php\0403\test.php
```

`__DIR__`获得文件所在的目录，也是觉得路径

```php
echo __DIR__;
//E:\wamp\www\wmsj100\php\0403
```

`__FUNCTION__`获取函数的名称；

```php
function funName($name,$age){
	echo __FUNCTION__;
}
funName(12,12);
```

# PHP 表单和用户输入

PHP 中的 $_GET 和 $_POST 变量用于检索表单中的信息，比如用户输入。


有一点很重要的事情值得注意，当处理 HTML 表单时，PHP 能把来自 HTML 页面中的表单元素**自动**变成可供 PHP 脚本使用。


`$_POST`变量用于收集来自`method="post"`的表单的值；从带有POST方法的表单发送的信息，不会在任务栏中显示，并且对于发送的信息量也是没有限制的。然后默认情况下，POST发送的信息量最大值为8MB；

```html
<form action="01.php" method="post">
	name:<input type="text" name="name">
	age:<input type="text" name="age">
	<input type="submit">
</form>
```

```php
<html>
<body>
welcom <?php echo $_POST['name']; ?>come here;<br>
you age is <?php echo $_POST['age'] ?>;
</body>
</html>
```

---

### 表单验证

涉及到的函数有：

```
htmlspecialchars()	//把特殊字符转换为实体字符;
trim()	//去除空格、换行、tab;
stripslashes()	//去除反斜杠(\);
$_SERVER['REQUSET_METHOD']=='POST'	//表单的提交是'post'；
$_SERVER['PHP_SELF']	//在当前页面进行验证；
$_POST['name']	//提交表单中`name`为name的项目
empty()	//验证输入框是否为空
```

- 文件名称最好不要用中文，服务器不识别；

- 如果在应该有提示文字出现的地方却没有文字，那么很可能是因为忘记写`echo`; .

- PHP文件最好放到文档的头部，就像CSS文件一样，因为再HTML中引用PHP代码时候，而PHP代码在HTML文档的后面，此时就会报错。

![](/file/img/tool/April/0403/003.png)