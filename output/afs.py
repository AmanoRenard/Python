def is_number(num): #自定义函数
    if type(num) is not str: #判断num是否为字符串，如果不是：报错。
        raise ValueError('传入的参数必须是字符串！')
    if len(num) > 2 and num.count('.',1,-1) == 1: #判断字符串的长度是否大于2，大于2的话才接着判断有无小数点。
        num=num.replace('.','',1) #替换掉小数点.（如果有的话。最多替换一次）
    if num.isnumeric(): #判断num是否由数字组成，如果是，返回True；如果不是，返回False。
        return True
    else:
        return False

# 演示完毕。

a= is_number() 
#TypeError: is_number() missing 1 required positional argument: 'num'

print(a)

'''
放到VSCode里面试一下。

Python 检测一个字符串是否能转换为整数/浮点数
一个比较简单的方法，
只支持十进制以内的数据。

使用例：

is_number('123') #True

is_number('123a') #False

is_number('12.3') #True

is_number('.123') #False

is_number('1.2.3') #False

is_number('') #False

is_number(123) #ValueError: 传入的参数必须是字符串！

is_number() #TypeError: is_number() missing 1 required positional argument: 'num'

我是新手，有错误请指正！

'''