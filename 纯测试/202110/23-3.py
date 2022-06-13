import random
num = eval(input('请输入参与评分的评委人数：'))
allscore = []
for i in range(num):
    allscore.append(round(random.randrange(700,1000)/10,1))
allscore.sort(reverse=True)
print('评委打分为：{}'.format(allscore))
allscore=allscore[1:-1]
print('去掉最高分与最低分：{}'.format(allscore))
sum=0
for i in allscore:
    sum+=i
print('该选手的分数为',round(sum/len(allscore),1))