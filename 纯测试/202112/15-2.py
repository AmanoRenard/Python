a=[];
n1=int(input())
for i in range(n1):
    a.append([int(x) for x in reversed(input().split())])
a=dict(a)
d={}
c=[x for x in a.items()]
n2=int(input())
for i in range(n2):
    temp = [int(x) for x in reversed(input().split())]
    for o in c:
        temp2=temp[:]
        temp2[0] += o[0]
        temp2[1] *= o[1]
        try:
            d[temp2[0]]+=temp2[1]
        except:
            d[temp2[0]]=temp2[1]
input()
b=sorted(list(d))
for i in b:
    if d[i] != 0:
        print("{}x^{}".format(d[i],i),end=' ')