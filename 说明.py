import time
import pyperclip
print("———————————————必看———————————————\n使用前需安装：\n1. PyInstaller\n2. Auto-py-to-exe")
a = int(input("———————————————选项———————————————\n1：复制PyInstaller安装教程链接\n2：复制Pip安装教程链接\n3：复制Auto-py-to-exe安装指令\n4：退出\n————————————————————————————————\n请输入你的选项>"))
for i in range(1,50):
  if(a == 1):
    print("已复制到剪贴板\n")
    pyperclip.copy('http://c.biancheng.net/view/2690.html')
    spam = pyperclip.paste()
  elif(a == 2):
    pyperclip.copy('https://www.cnblogs.com/baiyuer/p/9606773.html')
    spam = pyperclip.paste()
    print("已复制到剪贴板\n")
  elif(a == 3):
    pyperclip.copy('pip install auto-py-to-exe')
    spam = pyperclip.paste()
    print("已复制到剪贴板\n")
  elif(a == 4):
    test = input("Bye!")
    break
  else:
    print("[错误] 无效选项！")
  if(i >= 10 and i < 45):
    print('亲，输入不要太频繁哦，容易引起程序崩溃！')
  if(i > 45):
    print('\\(-w-)/')
  if(i == 45):
    print('恭喜您发现了彩蛋!\n链接：pan.baidu.com/s/1-6PDwtsc5Adfi5aHsrstRw\n神秘代码：2333\n个人制作的MC指令包，供参考。')
  a = int(input("请输入你的选项>"))
i = 50
time.sleep(3)
# 可恶，竟敢偷看源码！0A0