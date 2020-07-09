# -*- coding: utf-8 -*-
# Python环境：
# pip 是 Python 包管理工具
# 1、下载载安装脚本 get-pip.py 可能会失败多试几次
# curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
# 2、运行安装脚本
# sudo python get-pip.py
# sudo python3 get-pip.py 用哪个版本的 Python 运行安装脚本，pip 就被关联到哪个版本
# 3、查看pip 版本 
# pip --version
# 4、升级pip
# pip install -U pip || sudo easy_install --upgrade pip
# 5、列出已安装的包
# pip list
# 6、安装requests
# pip install requests


# 练习 抓取豆瓣电影 Top 250
# pip install requests
# pip3 install beautifulsoup4
import requests
from bs4 import BeautifulSoup

headers = { 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36' }
res = requests.get('https://movie.douban.com/top250', headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')
items = soup.find_all('div', class_='hd')
for i in items:
  tag = i.find('a')
  name = tag.find(class_='title').text
  link = tag['href']
  print(name, link)

# 问题：已经安装requests 执行python 3.py 仍然报错 ...ImportError: No module named requests
# 可能是因为在本地安装了多个版本的python导致的，安装了python2和python3版本，运行时使用版本3即可：python3 3.py

r = requests.get('https://www.douban.com/') # 豆瓣首页
print(r.status_code)
print(r.text)


