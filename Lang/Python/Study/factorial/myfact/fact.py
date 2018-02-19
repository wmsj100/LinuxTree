"myfact module"

def factorial(num):
    """
    返回给定数字的阶乘
    :arg num: 将计算的阶乘值
    :return: 阶乘值，若传递的参数为负数，则为-1
    """
    if num >= 0:
        if num == 0:
            return 1
        return num * factorial(num - 1)
    else:
        return -1
