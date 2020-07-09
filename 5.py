# -*- coding: utf-8 -*-
from collections import Iterable

# for x in 循环  for x in list: ...

names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

# range()函数，可以生成一个整数序列  比如range(5)生成的序列是从0开始小于5的整数
numbers = range(5)
print(numbers)  # [0, 1, 2, 3, 4]

sum = 0
for x in range(101):
    sum = sum + x
print(sum)

# while 循环
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

# 练习
L = ['Bart', 'Lisa', 'Adam']
for x in L:
    print('Hello,' + x)


# break 退出循环
n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')

# continue 退出当前的这次循环
n = 0 
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)

# 慎用break和continue语句，有些时候，如果代码写得有问题，会让程序陷入“死循环”，也就是永远循环下去。这时可以用Ctrl+C退出程序，或者强制结束Python进程。

# 迭代dict中的key和value
d = {'a': 1, 'b': 2, 'c': 3}
for key,value in d.items():
    print(key,value)

print(isinstance('abc', Iterable)) #True  str是否可迭代
print(isinstance([1,2,3], Iterable)) #True list是否可迭代
print(isinstance(123, Iterable)) #False 整数是否可迭代

# Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
names = ['Michael', 'Bob', 'Tracy']
for index,name in enumerate(names):
    print(index,name)

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

# 练习 使用迭代查找一个list中最小和最大值
def findMinAndMax(L):
    if L==[]:
        return(None, None)
    else:
        min=L[0]
        max=L[0]
        for num in L:
            if num<min:
                min=num
        for num in L:
            if num>max:
                max=num
        return (min,max)
print(findMinAndMax([1,2,3,4,5,6]))

# 列表生成式
print([x * x for x in range(1, 11)])
print([x * x for x in range(1, 11) if x % 2 == 0])
print([m + n for m in 'ABC' for n in 'XYZ'])