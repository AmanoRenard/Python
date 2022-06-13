import time
num=eval(input("请输入参与玩围圆圈数数的游戏人数(至少3人）："))
print('游戏开始！')
time.sleep(1)
peoplenumber=s1=s2=s3=[]
for i in range(0,num):
    peoplenumber.append(i+1)
a=2
while len(peoplenumber)>1:
    print('\n\n[公告]',peoplenumber[a],'号 淘汰！')
    del peoplenumber[a]
    a+=2
    while a+1>len(peoplenumber):
        a-=len(peoplenumber)
    print('剩余',len(peoplenumber),'名玩家:',peoplenumber)
    time.sleep(1)
print('\n\n[通知] 常胜将军是',peoplenumber[0],'号，让我们祝贺他！')