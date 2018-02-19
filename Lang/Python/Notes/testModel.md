---
title: 测试用例
date: Wed 03 Jan 2018 10:44:23 PM CST
tag: [python]
categories: Linux
author: wmsj100
mail: wmsj100@hotmail.com
---

## 基础概念
- 编写测试 检验应用程序所有的不同功能。
- 每一个测试用例集中在一个关注点上验证结果。
- 定期执行测试用例确保应用程序按预期的工作。
- 当测试覆盖很大的时候，通过运行测试就由自信确保修改点和新增点不会影响应用程序。

- 单元测试： 在计算机编程中，单元测试又称为模块测试，是针对程序模块（软件设计的最小单元）来进行正确性检验的测试工作。程序单元是应用的最小可测试部件。
- 在过程化编程中，一个单元就是一个程序/ 函数/ 过程等；
- 在面向对象编程中，一个单元就是一个方法， 包括基类（超类）/ 抽象类/ 派生类的方法。

## 实例
    ```python
    import unittest
    from factorial import fact

    class TestFactorial(unittest.TestCase):
        def test_fact(self):
            res = fact(5)
            self.assertEqual(res, 121)

    if __name__ == '__main__':
        unittest.main()
    ```

- 首先导入`unittest`模块，然后测试我们需要测试的函数
