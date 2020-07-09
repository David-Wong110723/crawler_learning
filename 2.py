# -*- coding: utf-8 -*-
import random

# 编程练习 print()函数
age = 414/23
number = input('猜一猜闻闻的年龄（1-30之间）')
if number > age:
  print('(⊙﹏⊙) 拜托，女孩子永远是18岁的！')
elif number < age:
  print('哈哈，你猜小了，女孩子的年龄永远猜不透~')
else:
  print('ヾ(≧▽≦*)o 恭喜你猜中了！')

# 解决“午饭吃什么”这个问题困扰
menu = ['鸭血粉丝', '黄焖鸡米饭', '虾饺', '秦镇米皮', '麻辣烫', '盖浇饭']
print(random.choice(menu))

print('观音：孙悟空，你根本不想去取西经，也不能原谅你欺师灭祖的行为')
print('唐三藏：姐姐，这是你的不对了')
print('观音：😱😱😱')
print('唐三藏：悟空🐒他要吃我，只不过是一个构思，还没有成为事实')
print('唐三藏：你又没有证据，他又何罪之有呢')
print('唐三藏：不如等他吃了我之后，你有凭有据，再定他的罪也不迟啊😀')
print('观音：😡，唐三藏，你啰嗦我早就知道，不过没想到你居然这么啰嗦')

print('我的意中人是一个盖世英雄')
print('上天既然安排他拔出我的紫青宝剑，他一定是个不平凡的人，错不了')
print('我知道有一天他会在一个万众瞩目的情况下出现')
print('身披金甲圣衣，脚踏七彩祥云来娶我')

# 转义符号 \ \n \\ 
print('当当当')
print('Only you can make all this change in me.')
print('For it\'s true you are my destiny.')
print('When you hold my hand, I understand.')
print('The magic that you do.')
print('You\'re my dream come true.')
print('My one and only you.')

print('For\nit\'s\ntrue\nyou\nare\nmy\ndestiny.')

print('Only you can make all this change in me.')
print('For it\'s true you are my destiny.')
print('When you hold my hand, I understand.')
print('The magic that you do.')
print('You\'re my dream come true.')
print('My one and only you.')


print('曾经有一段真挚的爱情摆在我眼前，\n我没有去珍惜等到失去了才后悔莫及。\n尘世间最痛苦的事莫过于此，\n如果上天能给我一个再来一次的机会，\n我希望能对那个女孩说我爱你，\n如果非要给这份爱加一个期限的话，\n我希望是一万年。\n')

print('  *****    *****')
print(' *******  *******')
print('******************')
print(' ****************')
print('   ************')
print('     ********')
print('        **')

print('张昭：听闻先生高卧隆中，自比管仲、乐毅。但自从刘备有了先生，弃新野，走樊城，败当阳，奔夏口，无容身之地，为何反不如当初了呢？')
print('孔明：我军虽历遭惨败，仍浴血奋战。而今江东兵精粮足，又有长江天堑，却有人劝说其主屈膝投降，不顾天下耻笑？')

# 数据类型 int  str  float  bool
# 查看数据类型 type(name)

name = 7
age = '33'
degree = 36.5
print(type(name))   #<class 'int'>
print(type(age))    #<class 'str'>
print(type(degree)) #<class 'float'>

# Python没有字符串模板？
name = '周瑜'
wife = '小乔'
print(name + '的夫人是' + wife)

num = 100
# print('杖责黄盖' + num + '军棍') #TypeError: cannot concatenate 'str' and 'int' objects
#不同类型数据不可拼接，需进行类型转换，上面一行代码修改为
print('杖责黄盖' + str(num) + '军棍') 
print('黄盖昏迷，众将士求情')
num = num - 60
print('算了，减60军棍，杖责黄盖' + str(num) + '军棍')

# 数据类型转换 str() int() float() 
# print(int('abc')) #报错了，因为 'abc' 并不能转换成整数

# 阿甘的选择  注意if...else...后边是冒号
score = int(input('输入智商值：'))
if score < 80:
  print('智力低下')
  print('呜呜呜~~')
elif score >= 80 and score < 110:
  print('普通智力')
elif score >= 110 and score < 140:
  print('智力较高')
else:
  print('天才或接近天才')

birth = input('birth: ')
if birth < 2000:
    print('00前')
else:
    print('00后')

# 以下为错误语法  
# skill = '跑'
# if skill == '跑':
# print('升入大学，成为橄榄球队主力！')
# else:
# print('无法升入大学，过着不为人知的生活')

# 缩进---Python 的代码块是通过缩进来定义代码块范围的。
# 代码行的缩进决定了代码的缩进层级，相同缩进层级的代码具有相同的缩进，比如下面的两行代码是一个层级，第二行错误地使用了缩进将导致运行报错：
# i = 1
#   b = 1
# 报错：IndentationError: unexpected indent

# 缩进一般使用两个空格或者四个空格，但是一定要记住要保持一致，不能一会用两个空格，一会用四个空格。

# 缩进错误示例1
# skill = '跑'
# if skill == '跑':
#     print('升入大学，成为橄榄球队主力！')
#   print('尽管他是个智障，但所有人都为他惊人的跑步速度欢呼！')
# else:
#   print('无法升入大学，过着不为人知的生活')

# 缩进错误示例2 
# skill = '跑'
# if skill == '跑':
#   print('升入大学，成为橄榄球队主力！')
# print('尽管他是个智障，但所有人都为他惊人的跑步速度欢呼！')
# else:
#     print('无法升入大学，过着不为人知的生活')

# 缩进错误示例3  
# skill = '跑'
#   if skill == '跑':
#   print('升入大学，成为橄榄球队主力！')
#   print('尽管他是个智障，但所有人都为他惊人的跑步速度欢呼！')
# else:
#   print('无法升入大学，过着不为人知的生活')

# 要求严格的代码缩进是 Python 语法的一大特色。代码本身的缩进，使得 Python 不需要标明额外的符号来标识代码块开始和结束。对比其他编程语言，比如 Java 语言，代码没有要求严格的缩进，所以需要额外的花括号来表示代码块的开始和结束。
# Python 使用回车来分割语句，冒号和缩进来分割代码块；C++ 和 Java 等语言使用分号来分割语句，花括号来分割代码块。

# Python使用缩进来组织代码块，请务必遵守约定俗成的习惯，坚持使用4个空格的缩进。

# 注释 以#号开头的语句


print(type(False))

a = 'ABC'
b = a
a = 'XYZ'
print(b)  # ABC
print(a)  # XYZ

# 常量
# 在Python中，通常用全部大写的变量名表示常量：
PI = 3.14159265359

# 在Python中，有两种除法，一种除法是 / 结果为浮点数； 一种是 // 称为地板除，只取结果的整数部分。
# 余数运算  10 % 3 

n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,Lisa!'''

print(n)
print(f)
print(s1)
print(s2)
print(s3)
print(s4)

# 小结
# Python支持多种数据类型，在计算机内部，可以把任何数据都看成一个“对象”，而变量就是在程序中用来指向这些数据对象的，对变量赋值就是把数据和变量给关联起来。

# 对变量赋值x = y是把变量x指向真正的对象，该对象是变量y所指向的。随后对变量y的赋值不影响变量x的指向。

# 注意：Python的整数没有大小限制，而某些语言的整数根据其存储长度是有大小限制的，例如Java对32位整数的范围限制在-2147483648-2147483647。

# Python的浮点数也没有大小限制，但是超出一定范围就直接表示为inf（无限大）。