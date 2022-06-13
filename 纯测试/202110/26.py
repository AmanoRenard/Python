'''
s = input('输入数字')
if s.isnumeric():
    s=eval(s)
    print('{:.2f}'.format(s))
else:
    print('不是数字！')
'''

'''
s='wowf'
print(s.endswith('ow',0,3))
'''

'''
s='awfafcawowafwafwo awfawfwaofawwaf oawfawf'
print(s.split('o'))
'''

'''
s = 'asdfasdasfasfasfsaf'
print(s.count('a',0,-2))
'''

'''
s = 'fawsaf me fwafwaf me awfawfaf me awfwafa'
print(s.replace('me','wow',2))
'''

'''
s = 'aaaww'
print(s.center(20,' ')) # =s.center(20)
'''

'''
s= 'awwwwwb'
print(s.strip('a')) #strip里面没填就是去掉两边空格
'''

'''
a=['1','2','3','4','0']
s='.'
print(s.join(a))
'''

'''
s='零一二三四五'
print(s.find('四'))
'''
