"""
__author__ = 'hogwarts_xixi'
__time__ = '2021/6/17 8:26 下午'
"""
import decimal

# 被测代码 计算器
class Calculator:
    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return round(a * b,5)

    def div(self, a, b):
        if b == 0:
            return "除数不能为0"
        return a / b
