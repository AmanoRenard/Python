n=input()
mylist=[int(x) for x in input().split()]
myset=set(mylist)
result=[]
for i in myset:
    result.append([i,mylist.count(i)])
result.sort(key=lambda x:x[1])
print(result[-1][0])