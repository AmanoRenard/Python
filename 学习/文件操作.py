f = open('filename', 'w') #读写模式打开文件 w:读写模式，没有txt会自动生成 r：只读模式，没有txt会报错 a：在末尾添加内容


f.write('hello\n123\n123') #写入字符串


a = f.read(5) #向后读5个字

a = f.readline() #读一行，无法读多行

a = f.readlines() #读所有，保存为列表


f.close() #关闭文件

import os
os.rename('重命名前.txt', '重命名后.txt') #重命名
os.remove('我被删除了.txt') #删除文件