text = {
    'China' : ['中国','No.1'],
    'America' : ['美国','No.2'],
    'Japan' : ['日本','No.3'],
    'India' : ['印度','No.4']
}

'''

#这三种要用for去遍历

print((text.keys())) #打印键名（带字典名）

print((text.values())) #打印键值（带字典名）

print((text.items())) #打印元素（带字典名）

'''


'''

for i in text.keys(): #打印键名
    print(i)

for i in text.values(): #打印键值
    print(i)

for i in text.items(): #打印元素
    print(i)

'''