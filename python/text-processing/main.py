#!D:\DevelopTool\Python35-32\python.exe
# coding=utf-8
# -*- coding: UTF-8 -*-
# 第一行表示执行python 的 python.exe 路径 在命令行使用 ./main.py 的形式会使用 配置的 python 环境
# 两种形式执行python 文件 编码集。

#stra = '第一行表示执行python 的 python.exe 路径 在命令行使用 ./main.py 的形式会使用 配置的 python 环境'
# print(stra[-6:-1])

#tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}
# print(tinydict)

import codecs

"""
#遍历数组
for letter in 'Python':     # 第一个实例
   print('当前字母 :', letter)

fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # 第二个实例
   print('当前水果 :', fruit)

# len返回数组长度， range生成迭代器
for num in range(10, 20):  # 迭代 10 到 20 之间的数字
    for i in range(2, num):  # 根据因子迭代
        if num % i == 0:      # 确定第一个因子
            j = num / i          # 计算第二个因子
            print ('%d 等于 %d * %d' % (num, i, j))
            break            # 跳出当前循环
    else:                  # 循环的 else 部分
        print (num, '是一个质数')


fruits = ['banana', 'apple',  'mango']
for index in range(len(fruits)):
   print ('当前水果 :', fruits[index])

#遍历
sequence = [12, 34, 34, 23, 45, 76, 89]
for i, j in enumerate(sequence):
    print (i, j)
"""
# 文件模式
"""
模式	描述
r	以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
rb	以二进制格式打开一个文件用于只读。文件指针将会放在文件的开头。这是默认模式。
r+	打开一个文件用于读写。文件指针将会放在文件的开头。
rb+	以二进制格式打开一个文件用于读写。文件指针将会放在文件的开头。
w	打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
wb	以二进制格式打开一个文件只用于写入。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
w+	打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
wb+	以二进制格式打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
a	打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
ab	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
a+	打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
ab+	以二进制格式打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。如果该文件不存在，创建新文件用于读写。
"""
# 文件读取
fo = open("../index.py", "r")
print("文件名: ", fo.name)
print("是否已关闭 : ", fo.closed)
print("访问模式 : ", fo.mode)

with codecs.open('../index.py', 'r', 'utf-8') as pyFile:
    for line in pyFile.readlines():
        print(line.strip())  # 把末尾的'\n'删掉

# 文件写入
