# -*- coding: utf-8 -*-

# 1. dict 字典

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])
# print(d['Thomas']) # key不存在会报错 KeyError: 'Thomas'

# 避免key不存在的错误判断1：
if 'Thomas' in d:
    print(d['Thomas'])
else:
    print('不存在该值')

# 避免key不存在的错误判断2：
print(d.get('Thomas')) # None
print(d.get('Thomas', -1)) # -1  :或者自己指定的value

# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
d.pop('Bob')  # 75

# 请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。

# 和list比较，dict有以下几个特点：

# 查找和插入的速度极快，不会随着key的增加而变慢；
# 需要占用大量的内存，内存浪费多。
# 而list相反：

# 查找和插入的时间随着元素的增加而增加；
# 占用空间小，浪费内存很少。
# 所以，dict是用空间来换取时间的一种方法。

# dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。
# 这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。


# 2. set  
# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。要创建一个set，需要提供一个list作为输入集合：
# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：

s = set([1, 2, 3])
print(s)

# 重复元素在set中自动被过滤：
s = set([1, 1, 2, 2, 3, 3, 4])
print(s)

# set 添加元素方法 s.add(key) 可以重复添加，但不会有效果：
s.add(5)
s.add(5)
print(s) # set([1, 2, 3, 4, 5])

# 通过s.remove(key) 方法删除元素
s.remove(4)
print(s)

# set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。


# str替换  替换后原字符串不变，replace()返回替换后的字符串
a = 'abc'
b =  a.replace('a','A') 
print(a)  # abc 
print(b)  # Abc

# 要始终牢记的是，a是变量，而'abc'才是字符串对象！有些时候，我们经常说，对象a的内容是'abc'，但其实是指，a本身是一个变量，它指向的对象的内容才是'abc'：
# 当我们调用a.replace('a', 'A')时，实际上调用方法replace是作用在字符串对象'abc'上的，而这个方法虽然名字叫replace，但却没有改变字符串'abc'的内容。相反，replace方法创建了一个新字符串'Abc'并返回，如果我们用变量b指向该新字符串，就容易理解了，变量a仍指向原有的字符串'abc'，但变量b却指向新字符串'Abc'了：
# 所以，对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的。



