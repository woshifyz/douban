### 数据

#### 基础
* int / long
* float / double
* string / byte(char)
* bool 

#### 高级
* list 
* dict

### 常用函数都要知道

```
def data

def function 

return 
```

#### 赋值
a = 2.3

b = a + 2

#### 控制流

##### if elif else

##### for / while (break, continue)

##### 函数
逻辑的抽象 input + logic + output

##### 类
```
class MyInt(object):
    def __init__(self, v):
        self.val = v

    def add(self, other):
        return MyInt(self.val + other)

    def __add__(self, other):
        return MyInt(self.val + other)

    def __str__(self):
        return "%s" % self.val

    __repr__ = __str__


class Bank(object):
    def __init__(self):
        self.balances = {}

    def deposit(self, name, amount):
        if name in self.balances:
            self.balances[name] += amount
        else:
            self.balances[name] = amount

    def balance(self, name):
        if name not in self.balances:
            return 0
        return self.balances[name]

```

