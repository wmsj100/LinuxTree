---
title: join和split的用法.txt
date: 2016-08-08
tags: [C#]
categories: Language
---

首先说一下这段代码的最终效果，它就是把用户输入的`no`转换为`yes`，因为实现这个效果的过程中分别使用`split`分割字符串，`join`连接字符串。
但是`split`和`join`的用法还是有区别的。
// 只能使用数组初始值给数组赋值。而且空格不能使用双引号包裹，
`myChar` -- char[] myChar = {' '}; 
`split` -- str.split(myChar);
// 调用`string`的`join`方法，连接符号是字符串符号，所以使用双引号包裹空格， 要连接的对象是数组`myArr`。
`join` -- string.join(" ", myArr);

```c#
Console.WriteLine("input no");
            string str1 = Console.ReadLine();
            char[] myChar = {' '};
            string[] myArr = str1.Split(myChar);
            int i;
            for (i = 0; i < myArr.Length; i++)
            {
                if (myArr[i] == "no")
                {
                    myArr[i] = "yes";
                }
            }
            str1 = string.Join(" ", myArr);
            Console.WriteLine(str1);
            Console.ReadKey();
```