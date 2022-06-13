'''
def minus(a):
    if a[0]=='0':
        return a[-1]
    else:
        return a


id = str(input('输入18位身份证号码：'))
print('{}年{}月{}日出生'.format(id[6:10],minus(id[10:12]),minus(id[12:14])))
'''


