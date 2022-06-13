num=int(input())
peoplenumber=[]
for x in range(1,num+1):
    peoplenumber.append(x)
count=1
while len(peoplenumber)>1:
    t=[]
    for i in peoplenumber:
        if count>3:
            count=1
        if count!=3:
            t.append(i)
        count+=1
    peoplenumber=t
print(peoplenumber[0])