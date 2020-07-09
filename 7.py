# -*- coding: utf-8 -*-
import math
# 函数 

# abs(number)求绝对值的函数
print(abs(-100)) #100

# max(2,3,1,-5) 返回最大值函数
print(max(2,3,1,-5)) # 3

# 数据类型转换
int('123')
int(12.34)
float('12.34')
str(1.23)
str(100)
bool(1)     # true
bool('')    # false

# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：
a = abs # 变量a指向abs函数
a(-1) # 所以也可以通过a调用abs函数

# 定义函数
# 在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回。

def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(-99))

# 空函数
# 如果想定义一个什么事也不做的空函数，可以用pass语句：
def nop():
    pass
# pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
age = input('猜一猜闻闻的年龄（1-30之间）')
if age >= 18:
    pass

# 数据类型检查可以用内置函数isinstance()实现
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
# print(my_abs('abc'))

# 练习
print(math.sqrt(2))  # 1.41421356237
def quadratic(a, b, c):
    key=b**2-4*a*c
    if key>0:
        x1=(-b+math.sqrt(key))/2*a
        x2=(-b-math.sqrt(key))/2*a
    if key==0:
        x1=-b/2*a
        x2=x1
    if key<0:
        print('方程无解')
        return(None,None)
    return (x1,x2)
print(quadratic(2, 3, 1))

def add_end(L=[]):
    L.append('END')
    return L
print(add_end())
print(add_end()) # ['END', 'END'] 每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
# 定义默认参数要牢记一点：默认参数必须指向不变对象！

# 修改为
L = [1,2,3]
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
L = [1,2,3]
print(add_end())  # ['END']
print(add_end())  # ['END']

# 练习 关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
print(person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456))

# 命名关键字参数
def person(name, age, *args):
    print(name, age, args)
person('Jack', 24, *(1,2,3))
