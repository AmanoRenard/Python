from random import randint


def generatedbc():
    allnum = []
    while True:
        gen = randint(1,10)
        if not gen in allnum:
            allnum.append(gen)
        if len(allnum) == 4:
            allnum.sort()
        if len(allnum) == 5:
            print('黑色球：%d %d %d %d， 白色球：%d'%(allnum[0],allnum[1],allnum[2],allnum[3],allnum[4]))
            return allnum

print('此次开出的中奖号码为：')
lotterynum=generatedbc()
print('你机选投注号码为：')
mynum=generatedbc()

a=0

for i in mynum[:4]:
    if i in lotterynum[:4]:
        a += 1

if mynum[4] == lotterynum[4]:
    b=1
else:
    b=0
    
print('黑中%d  白中%d'%(a,b))


if a==3 or b==1:
    print('恭喜中奖！你什么也没得到！')
else:
    print('重开吧，这都没中！')