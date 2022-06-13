import re
try:
    b=str(input("请输入2个字母"))
    result=re.match('[A,a][B,b]',b)
    while len(b) != 2:
        b=str(input('字数不对哦，请重新输入!'))
    a = result.group()
except AttributeError:
    print('格式不对哦！')
else:
    print(a)