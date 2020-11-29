# 数据 + 算法
# 输入 + 算法 + 输出

import os


class MyInt(object):
    def __init__(self, v):
        self.val = v

    def xxx(self, other):
        return MyInt(self.val + other)

    def __add__(self, other):
        return MyInt(self.val + other)

    def __str__(self):
        return "MyInt => %s" % self.val

    def __len__(self):
        return 1

    __repr__ = __str__


class Bank(object):
    def __init__(self):
        self.balances = {}

    def dep(self, name, amount):
        print("bank")
        if name in self.balances:
            self.balances[name] += amount
        else:
            self.balances[name] = amount

    def bal(self, name):
        if name not in self.balances:
            return 0
        return self.balances[name]


class FakeBank(Bank):
    def dep(self, name, amount):
        print("fake bank")
        return
