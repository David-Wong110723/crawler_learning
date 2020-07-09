# -*- coding: utf-8 -*-
# 在最新的Python 3版本中，字符串是以Unicode编码

# ord 函数获取字符的整数表示
print(ord('A'))  # 65

# chr() 函数把编码转换为对应的字符
print(chr(66))  # 'B'

# 数组操作 list

classmates = ['Michael', 'Bob', 'Tracy']

# 获取长度 len(list)
print(len(classmates)) 

# list末尾追加  list.append()
classmates.append('Adam')   
print(classmates)

# list插入制定索引位置，list.insert(index,'jack')
classmates.insert(1,'jack')
print(classmates)

# 删除list末尾的元素，用pop()方法：
print(classmates.pop())  # Adam
print(classmates)

# 删除list制定索引位置的元素，用pop()方法：
print(classmates.pop(1))  # jack
print(classmates)

# 把某个元素替换成别的元素，直接赋值给对应的索引位置：
classmates[1] = 'Sarah'
print(classmates)

# list排序
a = ['c', 'b', 'a']
a.sort()
a = [1, 4, 3]
a.sort()
print(a)

# list 切片(Slice)：取指定索引范围的操作
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0:3])  # 从索引0开始取，直到索引3为止，但不包括索引3
print(L[1:3]) 
print(L[-2:]) # 倒数第2个索引到末尾

# 练习
L = list(range(100))
L[:10:2] # 前10个数，每两个取一个：
L[::5] # 所有数，每5个取一个：

# 练习  去除字符串首尾的空格
def trim(s):
      if s[:1] !=' ' and s[-1:] !=' ':
          return s
      elif s[:1] ==' ':
          return trim(s[1:])
      else:
          return trim(s[:-1])
print(trim('  hello,word  '))

# 字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串：
print('ABCDEFG'[:3]) # ABC

# tuple 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改
# 不可变的tuple有什么意义？因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。
# tuple的陷阱：当你定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来

classmates = ('Michael', 'Bob', 'Tracy')

# 如果要定义一个空的tuple，可以写成()：
t = ()
# 但是，要定义一个只有1个元素的tuple，定义时必须加一个逗号来消除歧义,否则会认为是公式中的小括号: 
t = (1,)

# tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！

t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)  # ('a', 'b', ['X', 'Y'])



# 练习
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print(L[0][0])
print(L[1][1])
print(L[2][2])

