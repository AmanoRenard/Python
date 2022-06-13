from typing import Text


text = 'I am a student.'
text.lower() #转为小写
text.upper() #转为大写
text.islower() #如果是小写返回True否则False
text.isprintable() #当所有字符都是可以打印的时候返回True否则False
text.isnumeric() #所有字符都是数字时返回True否则False
text.isspace() #当所有字符都是空格时返回True否则False
text.endswith('am',1,10) #检测是否以am结尾，开始位置1结束位置10，开始和结尾位置可以省略
text.startswith('I',1,10) #检测是否以I开头，开始位置1结束位置10，开始和结尾位置可以省略
text.split('a') #以括号内的为分隔符分成列表

text.count('a',1,10) #返回范围出现a的次数
text.replace('a','b',3) #把a替换成b，替换3次，次数省略为替换所有
text.center(30,'*') #居中显示text至30长度，用*填充
text.strip('a','b') #去掉text两边的a和b，如果未填则为去除两边的空格

text='123'
print(text.zfill(20))