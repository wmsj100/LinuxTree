# java对象的基础知识

---

- 在设计类的时候要知道，对象是靠类的模型塑造出来的。 
- 在一个“java”文件内定义了俩个类，那么通过“javac”编译的时候就会生成俩个'class'文件。
- 一个“java”文件只创建一个主类和一个测试用的类。

- "main"的用途：1/ 测试真正的类，2/启动java程序

- 真正的java程序只会让对象与对象交互，即相互调用方法。

- 创建对象时，它会被存放到称为堆的内存区域中。此区域的堆是可以回收的堆。java是自动执行垃圾回收管理。

- 任何变量只要加上“public/ static, final”，基本上都会变成全局变量取用的常数。

- java中的任何事物都必须呆在类中。

## 变量

- 变量必须有名称“name”和类型“type”，变量就像是杯子或者容器，承载某些事物。

- “primitive“主数据类型，包含”字符串“==》”char“； ”布尔值“==》”true，false“； ”数值“==》”byte, short, int, long“；浮点数==》“float, double”；

- 不能把大尺寸的变量存入小尺寸的变量。如“int x = 24; byte y = x;”这样的赋值操作是非法的，因为存在溢出的可能性，所以编译器会报错。

- 变量名称必须用“字母/ 下划线/ $”字符开头，后面可以跟随数字。

### 对象

- 没有对象变量存在，只有引用到对象的变量，对象引用变量保存的是存取对象的方法；它并不是对象的容器，而是类似指向对象的指针。

- 对象只会存在于可回收垃圾的堆上。

- 引用变量代表取得“Dog”对象的方法以字节形式放进变量中。 '对象本身并没有放进变量。'

- 所有对象的引用都具有相同的大小，而不管它实际上所引用的对象大小。

## 对象的行为

- 对象有状态和行为俩种属性。分别用实例的方法来表示。

- 对于方法可以传值。

- java是通过值传递的，也就是说通过拷贝传递。

- 没有赋值的“String”初始化为“null”， 没有赋值的“int”初始化为“0”。

- 使用“==”比对“primitive”主数据类型时候相等或者说俩个引用类型是否指向同一对象。

- 我猜测“java”的多态是通过判断传入的参数个数以及参数类型来决定到底执行哪个方法。

## 编写程序

- 编写程序的流程： 写伪代码/ 写测试用例/ 写真实代码；

- 先编写测试用例，如果之前不写，那么以后也不会写，测试用例是一边写一边编码。
