#4.5.1回文判断：12321，啊哈哈哈啊。
'''
import math
text = input('请输入一段话：')
lenbc = math.ceil(len(text)/2)-1
i=0
while i < lenbc:
    if text[i] != text[-i-1]:
        print(text,'不是回文。');break
    i+=1
else:
    print(text,'是回文。')
'''

#4.5.2字符串循环左移
'''
text=input('输入文本')
for i in range(eval(input('输入移动次数'))):
    text=text[1:]+text[0]
print('移动后的字符串：',text)
'''

#4.5.3将Excel的列名转为十进制数
'''
#机器解法
a=input('输入列名：').upper();number=0
for i in a:
    number=number*26+(ord(i)-64)
print(a,'在第',number,'列',sep='')
'''

'''
#人类解法
a=input('输入列名：').upper();sum=0;v=1
for i in a:
    sum+=(ord(i)-64)*(26**(len(a)-v));v+=1
print('%s在第%d列'%(a,sum))
'''