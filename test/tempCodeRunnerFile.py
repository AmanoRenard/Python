import re
try:
    b=input("请输入2个字母")
    result=re.match('[A,a][B,b]',b)
    while len(result) != 2:
        result=input('字数不对哦，请重新输入!')
    a = result.group()
except AttributeError:
    print('格式不对哦！')
else:
    print(a)