---
title: 编程基础知识
date: 2016-08-15
tags: [C#, Code]
categories: Lang
---

基姆拉尔森公式 -- week = (d + 2 * m + 3 * (m + 1) / 5 + y + y / 4 - y / 100 + y / 400 + 1) % 7;

封装的函数如下：

```c#
static string CalculateWeekDay(int y, int m, int d)
    {
        if (m == 1 || m == 2)
        {
            m += 12;
            y--;
        }
        int weekday = (d + 2 * m + 3 * (m + 1) / 5 + y + y / 4 - y / 100 + y / 400 + 1) % 7;
        string result = "";
        switch (weekday)
        {
            case 1: result = "星期一"; break;
            case 2: result = "星期二"; break;
            case 3: result = "星期三"; break;
            case 4: result = "星期四"; break;
            case 5: result = "星期五"; break;
            case 6: result = "星期六"; break;
            case 0: result = "星期日"; break;
        }
        return result;
    }
```

调用时候，只需要在主函数内部引入函数既可
`string week = CalculateWeekDay(2016, 8, 15);`